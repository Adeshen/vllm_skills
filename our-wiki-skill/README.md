# Our Wiki Skills

This directory contains the local wiki-maintenance skills for the vLLM-Ascend knowledge base.

| Skill | Purpose |
| --- | --- |
| [vllm-feature-wiki](vllm-feature-wiki/SKILL.md) | Build, audit, and extend the vLLM/vLLM-Ascend engine feature wiki as state-machine documentation. |
| [vllm-bug-wiki](vllm-bug-wiki/SKILL.md) | Build, audit, and extend the vLLM-Ascend bug wiki as issue-to-fix evidence capsules. |

## Boundaries

- These are our local wiki-construction skills.
- Upstream/reference skills live under [../officals/](../officals/).
- Operational/reproduction skills live under [../our-operator-skills/](../our-operator-skills/).
- Wiki work is documentation-first. Do not run NPU, Docker, fuzzer, or reproduction campaigns unless the user explicitly asks.

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
