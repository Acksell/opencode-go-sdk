#!/usr/bin/env python3
"""Trim opencode's OpenAPI spec down to the endpoints this SDK exposes.

Reads opencode's full OpenAPI from stdin (or a file arg), drops every path
not in the allow-list, transitively prunes unreferenced components/schemas,
and writes the trimmed spec to stdout. Stats go to stderr.

Allow-list:
  - Prefix rules (any path starting with /<prefix>): /agent, /auth, /permission,
    /project, /provider, /question, /session
  - Exact rules (only these specific routes): /config/providers, /global/event,
    /global/health, /instance/dispose

The prefix rules make this self-maintaining as opencode evolves:
opencode adding new routes under a kept prefix automatically flows through;
routes added under a dropped prefix get filtered out. No per-route allow-list
that has to be hand-edited every regen.

As of opencode 1.15.x: 47 endpoints kept (Fern hobby tier cap: 50).

Usage:
    python3 trim-opencode-spec.py <opencode-spec.json >trimmed-spec.json
    curl http://127.0.0.1:4096/doc | python3 trim-opencode-spec.py >trimmed-spec.json
"""

import json
import re
import sys


# First-path-segment prefixes. Matches a path if it equals "/<prefix>" or
# starts with "/<prefix>/". Use prefixes for whole subtrees you want to
# follow as opencode adds routes within them.
PREFIX_RULES = (
    "/agent",
    "/auth",
    "/permission",
    "/project",
    "/provider",
    "/question",
    "/session",
)

# Exact paths. Use these when a prefix would over-match (e.g. /config/* would
# pull in /config GET/PATCH which we don't want; /global/* would pull in
# /global/upgrade, /global/dispose, /global/config which we don't want).
EXACT_RULES = frozenset((
    "/config/providers",
    "/global/event",
    "/global/health",
    "/instance/dispose",
))


def keep_path(path: str) -> bool:
    if path in EXACT_RULES:
        return True
    for prefix in PREFIX_RULES:
        if path == prefix or path.startswith(prefix + "/"):
            return True
    return False


_REF_RE = re.compile(r'"\$ref"\s*:\s*"#/components/schemas/([^"]+)"')


def collect_refs(node) -> set:
    """Find every #/components/schemas/X reference anywhere in this subtree."""
    return set(_REF_RE.findall(json.dumps(node)))


def transitive_schemas(schemas: dict, seed: set) -> set:
    """Expand `seed` by transitively following $refs through `schemas`."""
    needed = set(seed)
    frontier = set(seed)
    while frontier:
        next_frontier = set()
        for name in frontier:
            schema = schemas.get(name)
            if schema is None:
                continue
            for ref in collect_refs(schema):
                if ref not in needed:
                    next_frontier.add(ref)
                    needed.add(ref)
        frontier = next_frontier
    return needed


def main():
    src = open(sys.argv[1]) if len(sys.argv) >= 2 else sys.stdin
    spec = json.load(src)

    paths_in = spec.get("paths", {})
    kept_paths = {p: ops for p, ops in paths_in.items() if keep_path(p)}

    schemas_in = spec.get("components", {}).get("schemas", {})
    seed_refs = collect_refs(kept_paths)
    # Also seed from tags (in case tag descriptions reference schemas, rare
    # but cheap to include).
    seed_refs |= collect_refs(spec.get("tags", []))
    needed_schemas = transitive_schemas(schemas_in, seed_refs)
    kept_schemas = {name: s for name, s in schemas_in.items() if name in needed_schemas}

    # Build trimmed spec preserving top-level structure.
    trimmed = {k: v for k, v in spec.items() if k != "paths" and k != "components"}
    trimmed["paths"] = kept_paths
    if "components" in spec:
        components = dict(spec["components"])
        components["schemas"] = kept_schemas
        trimmed["components"] = components

    json.dump(trimmed, sys.stdout, indent=2)
    sys.stdout.write("\n")

    # Stats.
    n_endpoints = sum(
        1
        for ops in kept_paths.values()
        for method in ops
        if method in ("get", "post", "put", "delete", "patch")
    )
    total_endpoints = sum(
        1
        for ops in paths_in.values()
        for method in ops
        if method in ("get", "post", "put", "delete", "patch")
    )
    sys.stderr.write(f"paths kept:     {len(kept_paths):>3} / {len(paths_in)}\n")
    sys.stderr.write(f"endpoints kept: {n_endpoints:>3} / {total_endpoints}\n")
    sys.stderr.write(f"schemas kept:   {len(kept_schemas):>3} / {len(schemas_in)}\n")


if __name__ == "__main__":
    main()
