# vLLM-Ascend Wiki Skills

This directory contains local Codex skills for maintaining the vLLM-Ascend knowledge base.

| Skill | Purpose |
| --- | --- |
| [vllm-feature-wiki](our-wiki-skill/vllm-feature-wiki/SKILL.md) | Maintain the engine feature wiki as state-machine documentation. |
| [vllm-bug-wiki](our-wiki-skill/vllm-bug-wiki/SKILL.md) | Maintain the bug wiki as issue-to-fix evidence capsules. |

## Our Wiki Skills

Our documentation-maintenance skills are grouped under [our-wiki-skill/](our-wiki-skill/):

| Skill | Scope |
| --- | --- |
| [vllm-feature-wiki](our-wiki-skill/vllm-feature-wiki/SKILL.md) | Feature-state wiki construction, theory pages, feature-to-bug maps, and feature-wiki validation. |
| [vllm-bug-wiki](our-wiki-skill/vllm-bug-wiki/SKILL.md) | Bug capsules, workload patterns, release/fuzzer/CI summaries, and bug-wiki validation. |

## Official And Upstream Skills

Upstream and official-reference repositories are linked as Git submodules under [officals/](officals/):

| Source | Count | Submodule path |
| --- | ---: | --- |
| vLLM-Ascend `.agents/skills` | 2 | [officals/vllm-ascend/](officals/vllm-ascend/) |
| vLLM Skills plugin | 6 | [officals/vllm-skills/](officals/vllm-skills/) |
| KernelWiki | 1 wiki/skill project | [officals/kernelwiki/KernelWiki/](officals/kernelwiki/KernelWiki/) |

## External Skill Reference

The local wiki skills intentionally reference the official [vllm-project/vllm-skills](https://github.com/vllm-project/vllm-skills) repository as an operational companion:

- `vllm-deploy-simple`
- `vllm-deploy-docker`
- `vllm-deploy-k8s`
- `vllm-prefix-cache-bench`
- `vllm-bench-random-synthetic`
- `vllm-bench-serve`

Those skills help plan deployment and benchmark verification. They are not vLLM-Ascend bug evidence unless a local Ascend run records commands, logs, metrics, and environment context.

The local wiki skills also reference [KernelWiki](https://github.com/mit-han-lab/KernelWiki) as a knowledge-base construction model for source layering, schema discipline, provenance, query pages, and validation. KernelWiki is not used as factual evidence for vLLM-Ascend bugs unless a specific local page explicitly says so.

Note: the KernelWiki snapshot under [officals/kernelwiki/KernelWiki/](officals/kernelwiki/KernelWiki/) is kept verbatim at the requested commit. Its upstream `SKILL.md` has a frontmatter field that is outside the current local validator schema.

## Clone With Submodules

After cloning this repository:

```bash
git submodule update --init --recursive
```
