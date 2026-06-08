#!/usr/bin/env python3
"""Lightweight validator for the vLLM engine feature wiki."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_FEATURE_SECTIONS = [
    "## Mental Model",
    "## One-Request Story",
    "## State Ledger",
    "## Common Bug Stories",
    "## Fuzzer Strategy",
    "## Verification Strategy",
    "## Evidence Sources",
    "## Unknowns",
]

FEATURE_DIRS = [
    "engine_lifecycle",
    "scheduler",
    "kv_cache",
    "prefix_cache",
    "attention",
    "sampling",
    "streaming",
    "speculative_decoding",
    "lora",
    "quantization",
    "moe",
    "distributed",
    "prefill_decode_disaggregation",
    "metrics_tracing",
    "ascend_backend",
]

DEEP_DIVES = [
    "SCHEDULER_DEEP_DIVE.md",
    "ATTENTION_DEEP_DIVE.md",
    "SAMPLING_AND_SPEC_DEEP_DIVE.md",
    "STREAMING_LIFECYCLE_DEEP_DIVE.md",
    "QUANT_MOE_DEEP_DIVE.md",
    "ASCEND_BACKEND_DEEP_DIVE.md",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_wiki.py <vllm_engine_feature_wiki_dir>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1])
    errors: list[str] = []

    if not root.is_dir():
        errors.append(f"missing wiki directory: {root}")
    else:
        for name in ["README.md", "INDEX.md", "FEATURE_TEMPLATE.md"]:
            if not (root / name).is_file():
                errors.append(f"missing top-level file: {name}")

        for feature_dir in FEATURE_DIRS:
            page = root / feature_dir / "README.md"
            if not page.is_file():
                errors.append(f"missing feature README: {feature_dir}/README.md")
                continue
            text = page.read_text(encoding="utf-8")
            for section in REQUIRED_FEATURE_SECTIONS:
                if section not in text:
                    errors.append(f"{feature_dir}/README.md missing section: {section}")

        theory = root / "theory_illustrations"
        for deep_dive in DEEP_DIVES:
            if not (theory / deep_dive).is_file():
                errors.append(f"missing deep dive: theory_illustrations/{deep_dive}")

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
