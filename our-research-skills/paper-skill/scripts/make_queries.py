#!/usr/bin/env python3
"""Generate related-paper search queries from paper-skill seed papers."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "references" / "seed_papers.md"


def titles() -> list[str]:
    text = SEEDS.read_text(encoding="utf-8")
    results: list[str] = []
    for line in text.splitlines():
        if not line.startswith("| ") or "Primary source" in line or "---" in line:
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 3 and parts[0] and parts[1].startswith("http"):
            results.append(parts[0])
    return results


def slug_query(title: str) -> str:
    return re.sub(r"\s+", " ", title).strip()


def main() -> int:
    for title in titles():
        q = slug_query(title)
        print(f'"{q}"')
        print(f'"{q}" related work')
        print(f'"{q}" artifact OR code OR dataset')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
