# Rename Map

Controlled migration for **propershare/maat-core**. Update this file when a step completes.

## Repo

| From | To |
|------|-----|
| `badlogic/pi-mono` (upstream) | `propershare/maat-core` (this fork) |

## Product language

| From | To |
|------|-----|
| Pi (product) | MAAT Runtime |
| pi coding agent | MAAT Coding Agent |
| Pi monorepo (this fork) | MAAT Core monorepo |

## Packages (target npm scope: `@propershare`)

| Current / upstream-style | Target |
|--------------------------|--------|
| `@mariozechner/pi-coding-agent` | `@propershare/maat-coding-agent` |
| `@mariozechner/pi-ai` | `@propershare/maat-ai` |
| `@mariozechner/pi-agent-core` | `@propershare/maat-agent-core` |
| `@mariozechner/pi-tui` | `@propershare/maat-tui` |
| `@mariozechner/pi-mom` | `@propershare/maat-mom` |
| `@mariozechner/pi-web-ui` | `@propershare/maat-web-ui` |
| `@mariozechner/pi-pods` | `@propershare/maat-pods` |
| `@mariozechner/pi` (pods CLI package name on npm) | `@propershare/maat-pods` |

## CLI

| From | To (planned) |
|------|----------------|
| `pi` | `maat` (optional; may keep `pi` as a compatibility shim during transition) |

## Status

- [x] Pass 1: Top-level README, AGENTS, CONTRIBUTING, this map, fork docs
- [x] Pass 2: Docs and package READMEs (user-facing text; no import rewrites)
- [ ] Pass 3: Binary/package/workspace naming decisions and scripted updates
- [ ] Pass 4: `package.json` names, imports, published binaries, examples/tests
