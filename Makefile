SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

# Where to fetch opencode's published OpenAPI from. opencode is maintained by
# anomalyco; the spec lives under packages/sdk/openapi.json on the dev branch.
# (The repo used to live at sst/opencode — that's stale.)
OPENCODE_SPEC_URL ?= https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/sdk/openapi.json

# Alternative: pull from a locally-running opencode-serve instance.
# Use `make pull-local` to switch over.
OPENCODE_SERVER ?= http://127.0.0.1:4096

.PHONY: regen
regen: pull trim generate   ## (default-ish) pull upstream spec → trim → fern generate

.PHONY: pull
pull:   ## fetch opencode's published OpenAPI from upstream (anomalyco/opencode)
	@echo "→ fetching $(OPENCODE_SPEC_URL)"
	@curl -fsSL "$(OPENCODE_SPEC_URL)" >opencode-spec.json
	@echo "  wrote opencode-spec.json ($$(wc -c <opencode-spec.json) bytes)"

.PHONY: pull-local
pull-local:   ## fetch from a running opencode-serve (OPENCODE_SERVER, default :4096)
	@echo "→ fetching $(OPENCODE_SERVER)/doc"
	@curl -fsS "$(OPENCODE_SERVER)/doc" >opencode-spec.json
	@echo "  wrote opencode-spec.json"

.PHONY: trim
trim:   ## filter opencode-spec.json to the allow-list → fern/openapi/trimmed.json
	@mkdir -p fern/openapi
	@python3 scripts/trim-opencode-spec.py opencode-spec.json >fern/openapi/trimmed.json

.PHONY: generate
generate:   ## run fern generate against the trimmed spec
	@cd fern && fern generate --group local

.PHONY: check
check:   ## validate the Fern config + trimmed spec without generating
	@cd fern && fern check

# The fern-generated tests under sdk/<tag>/<tag>_test exercise the SDK against
# a WireMock server preloaded with stub mappings (both generated into
# sdk/wiremock/). We boot that compose stack, point the tests at the
# dynamically-mapped host port via WIREMOCK_URL, and always tear it down.
WIREMOCK_COMPOSE := $(CURDIR)/sdk/wiremock/docker-compose.test.yml

.PHONY: test
test:   ## build + test the generated Go SDK (boots WireMock for the generated tests)
	@cd sdk && go build ./...
	@trap 'docker compose -f $(WIREMOCK_COMPOSE) down' EXIT; \
		docker compose -f $(WIREMOCK_COMPOSE) up -d --wait; \
		port="$$(docker compose -f $(WIREMOCK_COMPOSE) port wiremock 8080 | sed 's/.*://')"; \
		cd sdk && WIREMOCK_URL="http://127.0.0.1:$$port" go test ./...

.PHONY: clean
clean:   ## remove pulled spec + trimmed-spec intermediate
	@rm -f opencode-spec.json fern/openapi/trimmed.json

.PHONY: help
help:   ## list available targets
	@awk -F'##' '/^[a-zA-Z_-]+:.*##/ { sub(/:.*/, "", $$1); printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
