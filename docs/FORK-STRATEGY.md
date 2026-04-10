# Fork strategy (propershare/maat-core)

## Goals

1. Keep **MAAT** product language and Tehuti Lab governance in docs and contributor experience.
2. Stay **mergeable** with upstream for security and feature fixes where possible.
3. Apply **renames in passes** ([`RENAME-MAP.md`](RENAME-MAP.md)) so installs and CI keep working.

## Upstream

- **Source:** Pi monorepo lineage (historically `badlogic/pi-mono`).
- **This fork:** [`propershare/maat-core`](https://github.com/propershare/maat-core).

## Workflow

1. Prefer **small, reviewable** commits: docs-only, then tooling, then package renames.
2. Before large rebases or renames, run **`npm run build`**, **`npm run check`**, and **`./test.sh`** on a branch.
3. Record **breaking rename** steps in [`RENAME-MAP.md`](RENAME-MAP.md) so downstreams (Tehuti Lab, OpenClaw, agents) know what shifted.

## GitHub metadata

Set the repository **description** and **About** section to reflect MAAT (e.g. “MAAT Core — MAAT Runtime monorepo (fork)”). Topics might include: `maat`, `ai`, `agent`, `terminal`, `llm`. Local git metadata cannot set GitHub About text; update it in the GitHub UI or API.
