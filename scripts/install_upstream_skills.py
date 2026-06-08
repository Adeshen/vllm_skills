#!/usr/bin/env python3
"""Install or index skill folders from local and submodule repositories.

The upstream repositories in officals/ do not share one skill-folder layout.
This script discovers SKILL.md files from known roots and creates a normalized
installation directory made of symlinks or copies.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = REPO_ROOT / "build" / "upstream_skills"


@dataclass(frozen=True)
class SourceSpec:
    source: str
    root: str
    patterns: tuple[str, ...]
    note: str = ""


SOURCES: tuple[SourceSpec, ...] = (
    SourceSpec(
        "local-wiki",
        ".",
        ("our-wiki-skill/*/SKILL.md",),
        "Local wiki-construction skills.",
    ),
    SourceSpec(
        "local-operator",
        ".",
        ("our-operator-skills/*/SKILL.md",),
        "Local vLLM/vLLM-Ascend operation and reproduction skills.",
    ),
    SourceSpec(
        "local-research",
        ".",
        ("our-research-skills/*/SKILL.md",),
        "Local literature search and research synthesis skills.",
    ),
    SourceSpec(
        "vllm-ascend",
        "officals/vllm-ascend",
        (".agents/skills/*/SKILL.md",),
        "Official vLLM-Ascend agent skills.",
    ),
    SourceSpec(
        "vllm-skills",
        "officals/vllm-skills",
        ("plugins/vllm-skills/skills/*/SKILL.md",),
        "Official vLLM skill plugin repository.",
    ),
    SourceSpec(
        "kernelwiki",
        "officals/kernelwiki/KernelWiki",
        ("SKILL.md",),
        "KernelWiki reference skill.",
    ),
    SourceSpec(
        "hpc-ncu",
        "officals/hpc_mlsys/ncu-report-skill",
        ("SKILL.md",),
        "Nsight Compute report and kernel profiling skill.",
    ),
    SourceSpec(
        "hpc-nvidia",
        "officals/hpc_mlsys/nvidia-skills",
        ("skills/*/SKILL.md", "plugins/nvidia-skills/skills/*/SKILL.md"),
        "NVIDIA HPC, CUDA-X, Dynamo, NeMo, and platform skill catalog.",
    ),
    SourceSpec(
        "hpc-flagos",
        "officals/hpc_mlsys/flagos-skills",
        ("skills/*/SKILL.md",),
        "FlagOS heterogeneous AI stack skills.",
    ),
    SourceSpec(
        "hpc-ai-research",
        "officals/hpc_mlsys/ai-research-skills",
        ("**/SKILL.md",),
        "MLSys and AI research skills, including inference serving.",
    ),
    SourceSpec(
        "scientific",
        "officals/scientific/scientific-agent-skills",
        ("skills/*/SKILL.md",),
        "Scientific computing skill catalog.",
    ),
    SourceSpec(
        "huggingface",
        "officals/scientific/huggingface-skills",
        ("skills/*/SKILL.md", "hf-mcp/skills/*/SKILL.md"),
        "Hugging Face ecosystem skill catalog.",
    ),
)


@dataclass
class SkillEntry:
    install_name: str
    source: str
    skill_name: str
    description: str
    skill_dir: Path
    skill_file: Path
    note: str

    def to_json(self, target_dir: Path) -> dict[str, str]:
        return {
            "install_name": self.install_name,
            "source": self.source,
            "skill_name": self.skill_name,
            "description": self.description,
            "skill_dir": str(self.skill_dir.relative_to(REPO_ROOT)),
            "skill_file": str(self.skill_file.relative_to(REPO_ROOT)),
            "install_path": str((target_dir / self.install_name).relative_to(REPO_ROOT))
            if target_dir.is_relative_to(REPO_ROOT)
            else str(target_dir / self.install_name),
            "note": self.note,
        }


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-") or "unnamed"


def read_frontmatter(skill_file: Path) -> dict[str, str]:
    text = skill_file.read_text(encoding="utf-8", errors="replace")
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
        key = key.strip()
        value = value.strip().strip("\"'")
        if key in {"name", "description"}:
            data[key] = value
    return data


def iter_skill_files(spec: SourceSpec) -> Iterable[Path]:
    root = REPO_ROOT / spec.root
    if not root.exists():
        return
    seen: set[Path] = set()
    for pattern in spec.patterns:
        for skill_file in sorted(root.glob(pattern)):
            if skill_file.name != "SKILL.md" or not skill_file.is_file():
                continue
            resolved = skill_file.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            yield skill_file


def discover_skills() -> tuple[list[SkillEntry], list[dict[str, str]]]:
    entries: list[SkillEntry] = []
    skipped: list[dict[str, str]] = []
    install_names: set[str] = set()

    for spec in SOURCES:
        for skill_file in iter_skill_files(spec):
            frontmatter = read_frontmatter(skill_file)
            skill_name = frontmatter.get("name") or skill_file.parent.name
            description = frontmatter.get("description", "")
            base_name = f"{spec.source}__{slugify(skill_name)}"
            install_name = base_name
            if install_name in install_names:
                skipped.append(
                    {
                        "reason": "duplicate install name",
                        "source": spec.source,
                        "skill_file": str(skill_file.relative_to(REPO_ROOT)),
                        "install_name": install_name,
                    }
                )
                continue
            install_names.add(install_name)
            entries.append(
                SkillEntry(
                    install_name=install_name,
                    source=spec.source,
                    skill_name=skill_name,
                    description=description,
                    skill_dir=skill_file.parent,
                    skill_file=skill_file,
                    note=spec.note,
                )
            )

    return entries, skipped


def ensure_target(target_dir: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)


def install_symlink(entry: SkillEntry, target_dir: Path, replace: bool) -> str:
    destination = target_dir / entry.install_name
    if destination.exists() or destination.is_symlink():
        if destination.is_symlink() or replace:
            if destination.is_dir() and not destination.is_symlink():
                shutil.rmtree(destination)
            else:
                destination.unlink()
        else:
            return "kept-existing"

    relative_target = os.path.relpath(entry.skill_dir, start=target_dir)
    destination.symlink_to(relative_target, target_is_directory=True)
    return "linked"


def install_copy(entry: SkillEntry, target_dir: Path, replace: bool) -> str:
    destination = target_dir / entry.install_name
    if destination.exists() or destination.is_symlink():
        if not replace:
            return "kept-existing"
        if destination.is_dir() and not destination.is_symlink():
            shutil.rmtree(destination)
        else:
            destination.unlink()
    shutil.copytree(entry.skill_dir, destination, ignore=shutil.ignore_patterns(".git"))
    return "copied"


def write_manifests(
    target_dir: Path,
    entries: list[SkillEntry],
    skipped: list[dict[str, str]],
    statuses: dict[str, str],
) -> None:
    payload = {
        "schema": "vllm-skills-normalized-install-v1",
        "repo_root": str(REPO_ROOT),
        "target_dir": str(target_dir),
        "skill_count": len(entries),
        "skipped_count": len(skipped),
        "skills": [entry.to_json(target_dir) | {"status": statuses.get(entry.install_name, "indexed")} for entry in entries],
        "skipped": skipped,
    }
    (target_dir / "manifest.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Normalized Skill Install Manifest",
        "",
        f"- Target: `{target_dir}`",
        f"- Skill count: `{len(entries)}`",
        f"- Skipped count: `{len(skipped)}`",
        "",
        "| Install name | Source | Upstream path | Status |",
        "| --- | --- | --- | --- |",
    ]
    for entry in entries:
        path = entry.skill_dir.relative_to(REPO_ROOT)
        status = statuses.get(entry.install_name, "indexed")
        lines.append(f"| `{entry.install_name}` | `{entry.source}` | `{path}` | `{status}` |")
    if skipped:
        lines.extend(["", "## Skipped", ""])
        for item in skipped:
            lines.append(f"- `{item['skill_file']}`: {item['reason']} as `{item['install_name']}`")
    (target_dir / "manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def list_entries(entries: list[SkillEntry]) -> None:
    for entry in entries:
        print(f"{entry.install_name}\t{entry.skill_dir.relative_to(REPO_ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--mode", choices=("symlink", "copy", "manifest"), default="symlink")
    parser.add_argument("--replace", action="store_true", help="replace existing non-symlink install directories")
    parser.add_argument("--list", action="store_true", help="print discovered skills without writing an install tree")
    args = parser.parse_args()

    target_dir = args.target
    if not target_dir.is_absolute():
        target_dir = REPO_ROOT / target_dir
    target_dir = target_dir.resolve()

    entries, skipped = discover_skills()
    if args.list:
        list_entries(entries)
        if skipped:
            print(f"# skipped: {len(skipped)}")
        return 0

    ensure_target(target_dir)
    statuses: dict[str, str] = {}
    if args.mode == "manifest":
        statuses = {entry.install_name: "indexed" for entry in entries}
    else:
        for entry in entries:
            if args.mode == "symlink":
                statuses[entry.install_name] = install_symlink(entry, target_dir, args.replace)
            else:
                statuses[entry.install_name] = install_copy(entry, target_dir, args.replace)

    write_manifests(target_dir, entries, skipped, statuses)
    print(f"Discovered {len(entries)} skills; skipped {len(skipped)} duplicates.")
    print(f"Wrote {target_dir / 'manifest.md'}")
    if args.mode != "manifest":
        print(f"Installed with mode={args.mode} into {target_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
