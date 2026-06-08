#!/usr/bin/env python3
"""Audit local skills for frontmatter, references, agents metadata, and routing hints."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOTS = [
    ROOT / "our-wiki-skill",
    ROOT / "our-operator-skills",
    ROOT / "our-research-skills",
]


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def main() -> int:
    rows = []
    failed = False
    for root in SKILL_ROOTS:
        for skill_file in sorted(root.glob("*/SKILL.md")):
            text = skill_file.read_text(encoding="utf-8", errors="replace")
            fm = frontmatter(text)
            rel = skill_file.relative_to(ROOT)
            checks = {
                "name": bool(fm.get("name")),
                "description": bool(fm.get("description")) and "Use when" in fm.get("description", ""),
                "references": (skill_file.parent / "references").exists(),
                "agent": (skill_file.parent / "agents" / "openai.yaml").exists(),
                "evidence": bool(re.search(r"evidence|Evidence", text)),
                "validation": bool(re.search(r"validate|Validation|final response|Expected Output", text)),
                "upstream": bool(re.search(r"upstream|official|vLLM Skills|KernelWiki|NCU|FlagOS|NVIDIA", text)),
            }
            missing = [name for name, ok in checks.items() if not ok]
            if missing:
                failed = True
            rows.append((str(rel), missing))

    for rel, missing in rows:
        status = "OK" if not missing else "MISSING " + ",".join(missing)
        print(f"{rel}\t{status}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
