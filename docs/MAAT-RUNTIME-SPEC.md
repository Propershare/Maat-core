# MAAT Runtime — product spec (fork)

This document defines **product language** for the **Propershare/Maat-runtime** fork. It does not change runtime behavior by itself; behavior stays aligned with upstream until renamed binaries and packages ship.

## Name

- **MAAT Runtime** — umbrella term for the interactive agent stack (CLI + agent core + AI layer) used in Tehuti Lab.
- **MAAT Coding Agent** — the terminal-oriented coding harness (the `packages/coding-agent` surface).

## Principles

1. **Surfaces first** — README, docs, and contributor flows say MAAT before low-level renames.
2. **Internals second** — workspace wiring and scripts follow a planned migration ([`RENAME-MAP.md`](RENAME-MAP.md)).
3. **Package names last** — `@scope/package` and import graph updates happen in one coordinated pass to avoid broken installs.

## Relationship to upstream

This tree tracks an upstream Pi monorepo. Fork-specific changes should be:

- Documented in [`FORK-STRATEGY.md`](FORK-STRATEGY.md)
- Tested with `npm run build`, `npm run check`, and `./test.sh` after any structural change

## Configuration paths

Until a dedicated migration renames on-disk directories, user config may still live under **`.pi/`** paths used by the upstream implementation. Documentation calls out MAAT naming while remaining accurate about actual paths.
