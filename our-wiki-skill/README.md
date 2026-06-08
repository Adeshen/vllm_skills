# Our Wiki Skills

This directory contains the local wiki-maintenance skills for vLLM and vLLM-Ascend knowledge bases.

| Skill | Purpose |
| --- | --- |
| [vllm-feature-wiki](vllm-feature-wiki/SKILL.md) | Build, audit, and extend the vLLM/vLLM-Ascend engine feature wiki as state-machine documentation. |
| [vllm-bug-wiki](vllm-bug-wiki/SKILL.md) | Build, audit, and extend evidence-driven vLLM/vLLM-Ascend bug wikis as issue-to-fix capsules. |

## Boundaries

- These are our local wiki-construction skills.
- Upstream/reference skills live under [../officials/](../officials/).
- Operational/reproduction skills live under [../our-operator-skills/](../our-operator-skills/).
- The feature-wiki skill is suitable for general vLLM engine state documentation. The current local reference snapshot focuses on vLLM-Ascend because that is the active research corpus.
- The bug-wiki skill currently targets vLLM-Ascend capsules, release mappings, and fuzzer evidence. The same schema can be reused for CUDA, CPU, or other vLLM backend bug corpora when their evidence roots are added.
- Wiki work is documentation-first. Do not run NPU/GPU, Docker, fuzzer, or reproduction campaigns unless the user explicitly asks.

## Validation

Feature wiki:

```bash
python3 llm_state_based/vllm_ascend/codex_skills/our-wiki-skill/vllm-feature-wiki/scripts/validate_wiki.py \
  llm_state_based/vllm_ascend/vllm_engine_feature_wiki
```

Bug wiki:

```bash
python3 llm_state_based/vllm_ascend/codex_skills/our-wiki-skill/vllm-bug-wiki/scripts/validate_wiki.py \
  llm_state_based/vllm_ascend/bug_wiki
```
