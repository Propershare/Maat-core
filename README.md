<!-- OSS_WEEKEND_START -->
# OSS Weekend

**Issue tracker reopens Monday, April 13, 2026.**

OSS weekend runs Thursday, April 2, 2026 through Monday, April 13, 2026. New issues and PRs from unapproved contributors are auto-closed during this time. Approved contributors can still open issues and PRs if something is genuinely urgent, but please keep that to pressing matters only. For support, join [Discord](https://discord.com/invite/3cU7Bz4UPx).

> _Current focus: at the moment i'm deep in refactoring internals, and need to focus._
<!-- OSS_WEEKEND_END -->

---

<p align="center">

# MAAT Core

**MAAT Runtime** — agent runtime, terminal coding harness, and supporting packages for AI-assisted development.

</p>

<p align="center">
  <a href="https://discord.com/invite/3cU7Bz4UPx"><img alt="Discord" src="https://img.shields.io/badge/discord-community-5865F2?style=flat-square&logo=discord&logoColor=white" /></a>
  <a href="https://github.com/Propershare/Maat-core/actions/workflows/ci.yml"><img alt="Build status" src="https://img.shields.io/github/actions/workflow/status/Propershare/Maat-core/ci.yml?style=flat-square&branch=main" /></a>
</p>

## About this repository

This repo is **[Propershare/Maat-core](https://github.com/Propershare/Maat-core)** — a **MAAT**-aligned fork of the upstream Pi monorepo. It contains the same packages (AI layer, agent core, coding agent CLI, TUI, web UI, Slack bot, pods), rebranded for MAAT product language and Tehuti Lab governance.

- **Docs:** [`docs/RENAME-MAP.md`](docs/RENAME-MAP.md) (migration targets), [`docs/MAAT-RUNTIME-SPEC.md`](docs/MAAT-RUNTIME-SPEC.md) (positioning), [`docs/FORK-STRATEGY.md`](docs/FORK-STRATEGY.md) (upstream sync), [`docs/SYSTEM_ARCHITECTURE.md`](docs/SYSTEM_ARCHITECTURE.md) (layout).
- **Internals:** Package names on disk and npm may still match upstream until a scoped migration; the CLI may still be invoked as `pi` until binaries are renamed. Surfaces and docs use **MAAT** naming first.

## Packages

| Package | Description |
|---------|-------------|
| **[@propershare/maat-ai](packages/ai)** | Unified multi-provider LLM API (OpenAI, Anthropic, Google, etc.) |
| **[@propershare/maat-agent-core](packages/agent)** | Agent runtime with tool calling and state management |
| **[@propershare/maat-coding-agent](packages/coding-agent)** | Interactive coding agent CLI |
| **[@propershare/maat-mom](packages/mom)** | Slack bot that delegates messages to the MAAT Coding Agent |
| **[@propershare/maat-tui](packages/tui)** | Terminal UI library with differential rendering |
| **[@propershare/maat-web-ui](packages/web-ui)** | Web components for AI chat interfaces |
| **[@propershare/maat-pods](packages/pods)** | CLI for managing vLLM deployments on GPU pods |

Published npm scopes may still show upstream names until the migration in [`docs/RENAME-MAP.md`](docs/RENAME-MAP.md) completes.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and [AGENTS.md](AGENTS.md) for project-specific rules (for both humans and agents).

## Development

```bash
npm install          # Install all dependencies
npm run build        # Build all packages
npm run check        # Lint, format, and type check
./test.sh            # Run tests (skips LLM-dependent tests without API keys)
./pi-test.sh         # Run the coding agent from sources (can be run from any directory)
```

> **Note:** `npm run check` requires `npm run build` to be run first. The web-ui package uses `tsc` which needs compiled `.d.ts` files from dependencies.

## License

MIT
