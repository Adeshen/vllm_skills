# vLLM Skills Repository

This repository collects Codex skills and upstream references for vLLM knowledge work. It is not only for vLLM-Ascend: it includes general vLLM operational skills, vLLM-Ascend backend workflows, local wiki-construction skills, and KernelWiki-style knowledge-base references.

| Skill | Purpose |
| --- | --- |
| [vllm-feature-wiki](our-wiki-skill/vllm-feature-wiki/SKILL.md) | Maintain vLLM engine feature wikis as state-machine documentation. |
| [vllm-bug-wiki](our-wiki-skill/vllm-bug-wiki/SKILL.md) | Maintain evidence-driven bug wikis as issue-to-fix capsules. |
| [paper-skill](our-research-skills/paper-skill/SKILL.md) | Search, triage, and synthesize related papers from seed literature. |

## Scope

- General vLLM deployment and benchmark skills are imported from the official vLLM skills repository.
- vLLM-Ascend skills and local operator skills support Ascend-specific release, deployment, reproduction, benchmark, and trace workflows.
- Local wiki skills describe how to build feature and bug knowledge bases. The current local bug corpus is vLLM-Ascend heavy because that is the available evidence set, but the schema is reusable for other vLLM backends when matching evidence roots are added.
- KernelWiki is included as a reference for wiki structure, source layering, provenance discipline, query pages, and validation design.

## Our Wiki Skills

Our documentation-maintenance skills are grouped under [our-wiki-skill/](our-wiki-skill/):

| Skill | Scope |
| --- | --- |
| [vllm-feature-wiki](our-wiki-skill/vllm-feature-wiki/SKILL.md) | vLLM feature-state wiki construction, theory pages, feature-to-bug maps, and feature-wiki validation. |
| [vllm-bug-wiki](our-wiki-skill/vllm-bug-wiki/SKILL.md) | Evidence capsule construction for vLLM/vLLM-Ascend bug wikis, workload patterns, release/fuzzer/CI summaries, and bug-wiki validation. |

## Our Research Skills

Research-support skills are grouped under [our-research-skills/](our-research-skills/):

| Skill | Scope |
| --- | --- |
| [paper-skill](our-research-skills/paper-skill/SKILL.md) | Related-paper search, seed-paper expansion, literature clustering, and local wiki/action mapping for vLLM, LLM serving, fuzzing, incidents, CI/security, and MLSys topics. |

## Official And Upstream Skills

Upstream and official-reference repositories are linked as Git submodules under [officals/](officals/):

| Source | Count | Submodule path |
| --- | ---: | --- |
| vLLM-Ascend `.agents/skills` | 2 | [officals/vllm-ascend/](officals/vllm-ascend/) |
| vLLM Skills plugin | 6 | [officals/vllm-skills/](officals/vllm-skills/) |
| KernelWiki | 1 wiki/skill project | [officals/kernelwiki/KernelWiki/](officals/kernelwiki/KernelWiki/) |
| HPC / MLSys skill references | 5 repositories | [officals/hpc_mlsys/](officals/hpc_mlsys/) |
| Scientific / HF skill references | 2 repositories | [officals/scientific/](officals/scientific/) |
| Skill discovery reference | 1 repository | [officals/skill_discovery/](officals/skill_discovery/) |

## External Skill Reference

The local wiki skills intentionally reference the official [vllm-project/vllm-skills](https://github.com/vllm-project/vllm-skills) repository as an operational companion:

- `vllm-deploy-simple`
- `vllm-deploy-docker`
- `vllm-deploy-k8s`
- `vllm-prefix-cache-bench`
- `vllm-bench-random-synthetic`
- `vllm-bench-serve`

Those skills help plan deployment and benchmark verification. They are not backend-specific bug evidence unless a local run records commands, logs, metrics, and environment context.

The local wiki skills also reference [KernelWiki](https://github.com/mit-han-lab/KernelWiki) as a knowledge-base construction model for source layering, schema discipline, provenance, query pages, and validation. KernelWiki is not used as factual evidence for vLLM or vLLM-Ascend bugs unless a specific local page explicitly says so.

Note: the KernelWiki snapshot under [officals/kernelwiki/KernelWiki/](officals/kernelwiki/KernelWiki/) is kept verbatim at the requested commit. Its upstream `SKILL.md` has a frontmatter field that is outside the current local validator schema.

## Normalized Skill Install

The upstream repositories do not all expose skills from the same folder depth. Use the local installer to discover every `SKILL.md` from known submodule layouts and create a normalized install tree:

```bash
make install
```

By default this writes symlinks and manifests under `build/upstream_skills/`, which is ignored by git. To create only the manifest:

```bash
make manifest
```

To inspect discovered skills:

```bash
make list
```

To install into another skill directory, pass `TARGET` and optionally `MODE=copy`:

```bash
make install TARGET="$CODEX_HOME/skills" MODE=symlink
make install TARGET="/tmp/vllm-skills-install" MODE=copy
```

The installer does not modify submodules. It writes:

- `manifest.json`
- `manifest.md`
- one normalized entry per discovered skill, named as `<source>__<skill-name>`

## Local Skill Audit

Run the local audit after changing `our-wiki-skill/` or `our-operator-skills/`:

```bash
python3 scripts/audit_local_skills.py
```

The audit checks that each local skill has frontmatter, a `Use when` trigger, references, UI metadata, evidence rules, validation/output guidance, and upstream-route awareness.

## Clone With Submodules

After cloning this repository:

```bash
git submodule update --init --recursive
```
