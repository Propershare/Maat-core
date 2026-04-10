# System architecture (MAAT Core)

High-level layout of the **maat-core** monorepo. Package **folder** names match the upstream layout; **npm names** migrate per [`RENAME-MAP.md`](RENAME-MAP.md).

## Layers

```text
┌─────────────────────────────────────────────────────────────┐
│  apps / CLIs                                                 │
│  packages/coding-agent  ·  packages/mom  ·  packages/pods   │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│  agent + UI                                                    │
│  packages/agent  ·  packages/tui  ·  packages/web-ui         │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│  model / LLM                                                   │
│  packages/ai                                                   │
└──────────────────────────────────────────────────────────────┘
```

## Responsibilities

| Area | Role |
|------|------|
| **packages/ai** | Provider-agnostic streaming LLM API, models, OAuth helpers |
| **packages/agent** | Sessions, tools, agent loop, state |
| **packages/coding-agent** | Terminal CLI, RPC, JSON mode, extensions/skills/themes |
| **packages/tui** | Differential terminal rendering for the interactive UI |
| **packages/web-ui** | Web components for chat-style interfaces |
| **packages/mom** | Slack integration delegating to the coding agent |
| **packages/pods** | GPU pod / vLLM deployment helper CLI |

## Build order

Root `package.json` `build` script orders packages so dependencies compile before dependents (TUI → AI → agent → coding-agent → mom → web-ui → pods). See root [README](../README.md) for day-to-day commands.
