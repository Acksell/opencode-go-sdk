# opencode-go-sdk

Go SDK for [opencode](https://opencode.ai), generated with [Fern](https://buildwithfern.com/)
from a filtered subset of opencode's OpenAPI.

The committed SDK is regenerated automatically every day from the OpenAPI
spec of the latest tagged
[opencode release](https://github.com/anomalyco/opencode/releases),
so it tracks opencode with no manual work per version bump.

```bash
go get github.com/acksell/opencode-go-sdk/sdk@latest
```

The module lives in the `sdk/` subdirectory, so its tags are prefixed `sdk/`.
SDK tags mirror the upstream release the SDK was generated from (from
`v1.17.x` onward): running opencode `1.17.18` means

```bash
go get github.com/acksell/opencode-go-sdk/sdk@sdk/v1.17.18
```

The version selector is always the full tag — `@sdk/v1.17.18`, not a bare
`@v1.17.18`. The daily sync takes only the latest upstream release, so a
version published and superseded within the same day may have no tag — pin
the closest lower one (the spec rarely changes between adjacent patches).

> [!IMPORTANT]
> opencode has shipped breaking changes even in minor releases. Pin the SDK
> tag matching your installed opencode CLI version, and bump both in lockstep.

opencode's published OpenAPI exposes 131 endpoints — over Fern's 50-endpoint
hobby-tier cap. This repo holds a trim filter that reduces opencode's spec to
the 47 endpoints relevant for SDK consumers, plus the Fern config that
generates the Go SDK from the trimmed spec.

## One-command workflow

```bash
make regen     # pull upstream spec → trim → fern generate
make test      # build + test the regenerated SDK
```

Or step-by-step:

```bash
make pull       # fetch opencode's OpenAPI at the latest release tag
make trim       # filter to allow-list → fern/openapi/trimmed.json
make generate   # fern generate the Go SDK
make help       # list all targets
```

`make pull` resolves the latest GitHub release of `anomalyco/opencode` and
fetches the spec at that tag. To pin a specific release or branch instead:

```bash
make regen OPENCODE_REF=v1.17.18   # a specific release tag
make regen OPENCODE_REF=dev        # the (unstable) dev branch, for testing
```

To regen against a locally-running opencode-serve instead of upstream:

```bash
OPENCODE_SERVER=http://127.0.0.1:4096 make pull-local trim generate
```

## Endpoint surface (47 kept of 131)

| Prefix | Count | Why kept |
|---|---|---|
| `/agent` | 1 | List available agents |
| `/auth/*` | 2 | Per-provider credential set/remove |
| `/config/providers` | 1 | Provider + model catalog |
| `/global/event`, `/global/health` | 2 | SSE event stream + readiness probe |
| `/instance/dispose` | 1 | Tear down a per-directory instance |
| `/permission/*` | 2 | Non-session-scoped permission management |
| `/project/*` | 4 | Project listing, current, patch, git init |
| `/provider/*` | 4 | OAuth flows |
| `/question/*` | 3 | Question/answer interactive flow |
| `/session/*` | 27 | Full session surface (create, message, fork, revert, abort, share, todo, …) |

Whole prefixes dropped: `/api/*` (opencode's experimental v2 API),
`/tui/*`, `/experimental/*`, `/mcp/*`, `/pty/*`, `/vcs/*`, `/find/*`,
`/file/*`, `/sync/*`, and individual routes like `/lsp`, `/formatter`,
`/path`, `/skill`, `/log`, `/command`, plus the demoted root `/event` and
a handful of `/global/*` server-admin routes.

## How the trim works

`scripts/trim-opencode-spec.py` is a single-file script that:

1. Reads opencode's full OpenAPI from a file arg or stdin.
2. Filters paths by the allow-list at the top of the script. Two rule types:
   - **Prefix rules** (whole subtrees): `/agent`, `/auth`, `/permission`,
     `/project`, `/provider`, `/question`, `/session`. Anything opencode adds
     under these auto-flows through.
   - **Exact rules** (single paths only): `/config/providers`, `/global/event`,
     `/global/health`, `/instance/dispose`. Used where a prefix would
     over-match (e.g. `/config/*` would pull in `/config` GET/PATCH which we
     don't want).
3. Transitively walks `$ref` chains through `components/schemas`, keeping
   only schemas reachable from the kept paths. Avoids 78 orphan schemas
   bloating the generated SDK.
4. Writes the trimmed spec to stdout. Stats (kept / dropped counts) go to
   stderr.

The intent is to be self-maintaining: opencode adds an endpoint under a kept
prefix, it auto-flows through; adds under a dropped prefix, it auto-drops.
Allow-list only changes when a consumer needs to opt into a new top-level area.

## Automated regeneration

`.github/workflows/regen.yml` runs daily (03:00 UTC) and on manual
`workflow_dispatch`. It resolves the latest upstream release; if the mirrored
`sdk/v<version>` tag already exists it exits early. Otherwise it runs
`make regen && make test` against that release, and — only if build and tests
pass — commits the regenerated SDK to `main`, tags it `sdk/v<version>`, and
creates a GitHub release.

## Repo layout

```
opencode-go-sdk/
├── README.md
├── Makefile                          one-command regen workflow
├── .github/workflows/regen.yml       daily + on-demand CI regen
├── fern/
│   ├── fern.config.json              Fern org + CLI version
│   ├── generators.yml                Go SDK generator config (api + group + output path)
│   └── openapi/
│       └── trimmed.json              produced by `make trim` (committed)
├── scripts/
│   └── trim-opencode-spec.py         allow-list filter + schema pruner
├── opencode-spec.json                produced by `make pull` (committed)
└── sdk/                              ← the generated Go module
    ├── go.mod                            module github.com/acksell/opencode-go-sdk/sdk
    ├── client/, session/, project/,
    │   provider/, permission/, …         one package per resource
    ├── core/, option/, internal/         shared HTTP + request-option plumbing
    └── *.go                              top-level types, errors, etc.
```

Both `opencode-spec.json` and `fern/openapi/trimmed.json` are checked in so
the SDK output is reproducible from source. Diffs between regens make it easy
to see what changed upstream. The contents of `sdk/` are also checked in so
consumers can `go get` without running Fern themselves.

## Editing the allow-list

If a consumer needs a new endpoint, edit `PREFIX_RULES` or
`EXACT_RULES` at the top of `scripts/trim-opencode-spec.py`. Prefer extending
an existing prefix over adding exact paths — keeps the allow-list short and
forward-compatible. Then `make regen` to rebuild.

Want an endpoint added or something else changed? Open an issue — the SDK aims
to stay fully automated, so changes land in the trim config rather than in
hand-edited output.

## Versions to bump periodically

Two version pins live in `fern/`:

| File | Field | What it tracks | How to bump |
|---|---|---|---|
| `fern.config.json` | `version` | the `fern-api` CLI on npm — Fern auto-installs this when you run any `fern` command | `npm view fern-api version` then edit the file |
| `generators.yml` | `version:` under `fernapi/fern-go-sdk` | the Docker tag of the Go generator | `fern generator upgrade --include-major` — auto-resolves and applies any required migrations |

After bumping either, run `make check` (= `fern check`) to validate the
config + spec against the new versions before generating.

## Consuming the SDK

The generated Go module lives in `./sdk/` to keep it isolated from the build
scaffolding at the repo root. So consumers import via the `/sdk` subpath:

```
require github.com/acksell/opencode-go-sdk/sdk <pseudo-version>
```

```go
import (
    opencodeclient "github.com/acksell/opencode-go-sdk/sdk/client"
    "github.com/acksell/opencode-go-sdk/sdk/session"
    // …
)
```

For a local-checkout dev loop (no GitHub round-trip), add a `replace`
directive in your `go.mod` pointing at this repo's `sdk/` directory:

```
replace github.com/acksell/opencode-go-sdk/sdk => /path/to/opencode-go-sdk/sdk
```

---

_Not affiliated with opencode._
