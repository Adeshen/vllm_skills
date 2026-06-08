---
name: vllm-feature-wiki
description: Build, audit, and extend the local vLLM/vLLM-Ascend engine feature wiki as an evidence-driven state-machine knowledge base. Use when the user asks to document vLLM engine features, explain scheduler/KV/prefix/attention/sampling/speculative/streaming/LoRA/quantization/MoE/distributed/PD/metrics/Ascend backend state, connect features to bug capsules or fuzzer seeds, improve theory storytelling, update feature-to-bug maps, or validate the feature wiki structure under llm_state_based/vllm_ascend/vllm_engine_feature_wiki.
---

# vLLM Feature Wiki

Use this skill to maintain the local feature wiki:

```text
llm_state_based/vllm_ascend/vllm_engine_feature_wiki/
```

The wiki answers: what feature exists, how it works as engine state, what bugs it tends to enable, and how to fuzz or verify it.

## Working Model

Borrow the knowledge-base discipline from KernelWiki and the lightweight `SKILL.md` style from `vllm-project/vllm-skills`:

- Treat raw evidence, synthesized pages, and cross-reference maps as separate layers.
- Treat official vLLM deploy/benchmark skills as companion execution skills: useful for verification planning, but do not run them during documentation-only wiki work unless the user explicitly asks for experiments.
- Prefer primary sources: local evidence, official vLLM/vLLM-Ascend docs, papers, GitHub issues/PRs/RFCs, and code diffs.
- Use blogs/Zhihu/general web only for intuition, labeled as supplemental.
- Preserve `unknown` instead of inventing version, CANN, command, model, or compatibility facts.
- New local model-path examples must use `/mnt/data2/model_weights`; do not write the legacy model-volume path.

## Core Workflow

1. Locate the workspace root and target wiki. If the user gives no path, use the current workspace and `llm_state_based/vllm_ascend/vllm_engine_feature_wiki/`.
2. Read [references/primer.md](references/primer.md) for navigation and source priorities.
3. Read [references/schema.md](references/schema.md) before editing feature pages, indices, deep dives, or maps.
4. Read [references/vllm_skills.md](references/vllm_skills.md) when the user asks how a feature should be verified, benchmarked, deployed, or connected to existing vLLM skills.
5. Inspect the existing page and nearby evidence before writing. Use `rg` and `sed`; do not modify evidence files.
6. Update the smallest useful set of feature pages and cross-links:
   - subsystem `README.md`
   - `INDEX.md`
   - `theory_illustrations/*`
   - `feature_to_bug_map/README.md`
7. Use the teaching flow on each feature page:
   - mental model
   - one-request story
   - state ledger
   - common bug stories
   - fuzzer strategy
   - verification strategy
   - evidence sources
   - unknowns
8. Validate with:

```bash
python3 llm_state_based/vllm_ascend/codex_skills/our-wiki-skill/vllm-feature-wiki/scripts/validate_wiki.py \
  llm_state_based/vllm_ascend/vllm_engine_feature_wiki
```

9. In the final response, report files changed, feature pages touched, strongest feature-to-bug links, evidence gaps, official-vLLM-skill connections if added, and validation result.

## Source Search Rules

- Start local: feature wiki, bug wiki, issue capsule, project docs, GRIEF fuzzer history, CPU CI reports.
- Browse only when the user asks for internet knowledge, latest docs, official references, or missing theory context.
- For current vLLM/vLLM-Ascend facts, verify with primary sources. Do not rely on memory for latest releases, docs, APIs, or support matrices.
- If citing KernelWiki or vLLM Skills, cite them as process/style references, not as vLLM-Ascend bug evidence.

## Edit Discipline

- Documentation-only unless the user explicitly asks for code or experiments.
- Do not run reproductions, fuzzer campaigns, Docker/NPU jobs, or destructive commands as part of wiki maintenance.
- Do not edit `issue_capsule/`, bug evidence, logs, PR caches, or fuzzer corpora unless explicitly requested.
- Keep page text English unless the user asks otherwise.
- Keep cross-links relative and local where possible.

## Useful References

- [references/primer.md](references/primer.md): subsystem map, source map, and update routes.
- [references/schema.md](references/schema.md): feature page contract, confidence levels, and quality gates.
- [references/examples.md](references/examples.md): worked task patterns.
- [references/vllm_skills.md](references/vllm_skills.md): how official vLLM deploy/benchmark skills connect to this wiki.
