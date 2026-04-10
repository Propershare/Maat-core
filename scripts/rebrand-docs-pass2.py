#!/usr/bin/env python3
"""Pass 2: user-facing docs — mechanical replacements only. Excludes CHANGELOG.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

SKIP_NAMES = frozenset({"CHANGELOG.md"})

SUBSTITUTIONS: list[tuple[str, str]] = [
    ("@mariozechner/pi-coding-agent", "@propershare/maat-coding-agent"),
    ("@mariozechner/pi-agent-core", "@propershare/maat-agent-core"),
    ("@mariozechner/pi-web-ui", "@propershare/maat-web-ui"),
    ("@mariozechner/pi-ai", "@propershare/maat-ai"),
    ("@mariozechner/pi-tui", "@propershare/maat-tui"),
    ("@mariozechner/pi-mom", "@propershare/maat-mom"),
    ("@mariozechner/pi-pods", "@propershare/maat-pods"),
    ("github.com/badlogic/pi-mono", "github.com/Propershare/Maat-core"),
    ("badlogic/pi-mono", "Propershare/Maat-core"),
    ("@mariozechner/pi-agent)", "@propershare/maat-agent-core)"),
    ("package/@mariozechner/pi-agent", "package/@propershare/maat-agent-core"),
]


def process_file(path: Path) -> bool:
    if path.name in SKIP_NAMES:
        return False
    if "node_modules" in path.parts:
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    original = text
    for old, new in SUBSTITUTIONS:
        text = text.replace(old, new)
    text = re.sub(
        r"\[openclaw/openclaw\]\((https://github\.com/openclaw/openclaw[^)]*)\)",
        r"[OpenClaw](\1)",
        text,
    )
    if text == original:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    changed: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        if process_file(path):
            changed.append(path)
    for path in REPO_ROOT.rglob("*.yml"):
        if ".github" not in path.parts:
            continue
        if process_file(path):
            changed.append(path)
    print(f"Updated {len(changed)} files")
    for p in sorted(set(changed)):
        print(f"  {p.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
