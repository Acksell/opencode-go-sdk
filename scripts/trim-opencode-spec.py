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


# SDK consumers (clank) never use these schemas — they're sync/replay-layer
# duplicates of domain events, all sharing `type: "sync"`. Dropping them
# from any anyOf they appear in lets us put a real discriminator on the
# remaining variants (otherwise OpenAPI's "each variant must have a unique
# discriminator value" rule is violated by the duplicated "sync" type).
DROP_VARIANT_PREFIXES = ("SyncEvent",)

# Discriminator candidates Fern can dispatch on. We try each field name in
# order on every anyOf variant; the first field for which all variants have a
# single-member enum becomes the discriminator. This keeps the script
# self-maintaining: new union, no config change needed — as long as each
# variant has one of these fields with a single-value enum, Fern gets a
# discriminator.
DISCRIMINATOR_FIELDS = ("type", "role", "status")


def variant_enum_value(variant_schema: dict, field: str):
    """Return the single-member enum value for `field` on a variant schema,
    or None if the variant doesn't pin it."""
    enum = variant_schema.get("properties", {}).get(field, {}).get("enum")
    if not enum or len(enum) != 1:
        return None
    return enum[0]


def transform_anyof_unions(schemas: dict) -> tuple[int, int]:
    """For every `anyOf` (whether on a top-level schema or nested inline):
      1) drop variants whose target schema name starts with a prefix in
         DROP_VARIANT_PREFIXES,
      2) inject `discriminator` if every surviving variant has a single-
         member enum for the same DISCRIMINATOR_FIELDS candidate.

    Returns (dropped_count, patched_count).
    """
    dropped = 0
    patched = 0

    def walk(node):
        nonlocal dropped, patched
        if isinstance(node, dict):
            if isinstance(node.get("anyOf"), list):
                # 1a) Drop SyncEvent-style variants (clank-irrelevant +
                # their shared discriminator value would block uniqueness).
                # 1b) Dedupe by $ref — opencode's spec lists some refs twice
                # under the same anyOf, which would also collide on
                # discriminator uniqueness.
                before = len(node["anyOf"])
                seen_refs = set()
                pruned = []
                for v in node["anyOf"]:
                    if _ref_matches_drop_prefix(v):
                        continue
                    ref = v.get("$ref", "") if isinstance(v, dict) else ""
                    if ref and ref in seen_refs:
                        continue
                    if ref:
                        seen_refs.add(ref)
                    pruned.append(v)
                node["anyOf"] = pruned
                dropped += before - len(node["anyOf"])

                # 2) Inject discriminator if possible.
                if "discriminator" not in node and node["anyOf"]:
                    if _inject_discriminator(node, schemas):
                        patched += 1

            # Recurse into all children regardless of whether this node was
            # itself a union — nested anyOfs are real (see GlobalEvent.payload).
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(schemas)
    return dropped, patched


def _ref_matches_drop_prefix(variant: dict) -> bool:
    ref = variant.get("$ref", "") if isinstance(variant, dict) else ""
    if not ref.startswith("#/components/schemas/"):
        return False
    name = ref.split("/")[-1]
    return any(name.startswith(p) for p in DROP_VARIANT_PREFIXES)


def _inject_discriminator(union: dict, schemas: dict) -> bool:
    """Try each DISCRIMINATOR_FIELDS candidate. Use the first one where all
    surviving variants have a single-member enum AND those values are unique
    (OpenAPI requires uniqueness for discriminator mappings)."""
    variants = union["anyOf"]
    for field in DISCRIMINATOR_FIELDS:
        mapping = {}
        ok = True
        for variant in variants:
            ref = variant.get("$ref", "") if isinstance(variant, dict) else ""
            if not ref.startswith("#/components/schemas/"):
                ok = False
                break
            v_name = ref.split("/")[-1]
            v_schema = schemas.get(v_name, {})
            value = variant_enum_value(v_schema, field)
            if value is None or value in mapping:
                ok = False
                break
            mapping[value] = ref
        if ok and mapping:
            union["discriminator"] = {"propertyName": field, "mapping": mapping}
            return True
    return False


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

    # Walk every anyOf union in the trimmed schemas:
    #   - drop SyncEvent* variants (clank-irrelevant + their shared "sync"
    #     discriminator value would block injecting a real discriminator)
    #   - inject `discriminator` so Fern's generated UnmarshalJSON validates
    #     the wire `type` / `role` / `status` instead of falling back to its
    #     buggy try-each-in-order pattern (every event would end up in the
    #     first variant).
    dropped_variants, n_unions_patched = transform_anyof_unions(kept_schemas)
    # After dropping SyncEvent variants, re-prune so the orphaned schemas
    # don't ship in the SDK.
    seed_refs_after = collect_refs(kept_paths) | collect_refs(spec.get("tags", []))
    needed_after = transitive_schemas(kept_schemas, seed_refs_after)
    kept_schemas = {name: s for name, s in kept_schemas.items() if name in needed_after}

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
    sys.stderr.write(f"paths kept:        {len(kept_paths):>3} / {len(paths_in)}\n")
    sys.stderr.write(f"endpoints kept:    {n_endpoints:>3} / {total_endpoints}\n")
    sys.stderr.write(f"schemas kept:      {len(kept_schemas):>3} / {len(schemas_in)}\n")
    sys.stderr.write(f"unions patched:    {n_unions_patched:>3} (discriminators injected on anyOf unions)\n")
    sys.stderr.write(f"variants dropped:  {dropped_variants:>3} (e.g. SyncEvent* shared `type: sync`)\n")


if __name__ == "__main__":
    main()
