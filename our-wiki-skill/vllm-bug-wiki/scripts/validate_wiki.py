#!/usr/bin/env python3
"""Lightweight validator for the vLLM-Ascend bug wiki."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "README.md",
    "INDEX.md",
    "BUG_CAPSULE_TEMPLATE.md",
]

REQUIRED_DIRS = [
    "bug_capsules",
    "workload_patterns",
    "release_matrix",
    "fuzzer_findability",
    "ci_and_environment",
    "raw_source_index",
]

REQUIRED_CAPSULE_SECTIONS = [
    "## Identity",
    "## Failure Summary",
    "## Triggering Workload",
    "## Version And Environment",
    "## Fix Evidence",
    "## Reproduction Evidence",
    "## Fuzzer Discoverability",
    "## Next Actions",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_wiki.py <bug_wiki_dir>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1])
    errors: list[str] = []

    if not root.is_dir():
        errors.append(f"missing wiki directory: {root}")
    else:
        for name in REQUIRED_TOP_LEVEL:
            if not (root / name).is_file():
                errors.append(f"missing top-level file: {name}")

        for name in REQUIRED_DIRS:
            if not (root / name).is_dir():
                errors.append(f"missing directory: {name}")

        capsule_dir = root / "bug_capsules"
        if capsule_dir.is_dir():
            for capsule in sorted(capsule_dir.glob("*.md")):
                text = capsule.read_text(encoding="utf-8")
                for section in REQUIRED_CAPSULE_SECTIONS:
                    if section not in text:
                        errors.append(f"{capsule.relative_to(root)} missing section: {section}")

        forbidden_model_path = "/mnt/data" + "/model_weights"
        for md in root.rglob("*.md"):
            text = md.read_text(encoding="utf-8")
            if forbidden_model_path in text:
                errors.append(f"forbidden model path in {md.relative_to(root)}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
