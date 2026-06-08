---
name: vllm-bug-wiki
description: Build, audit, and extend the local vLLM-Ascend bug wiki as an evidence-driven issue-to-fix knowledge base. Use when the user asks to create or update bug capsules, triage vLLM-Ascend GitHub issues/PRs, connect failure symptoms to workloads, versions, images, CANN/vLLM/torch context, fixing PRs, patch applicability, reproduction evidence, fuzzer discoverability, release matrices, workload pattern files, or raw-source indices under llm_state_based/vllm_ascend/bug_wiki.
---

# vLLM Bug Wiki

Use this skill to maintain the local bug wiki:

```text
llm_state_based/vllm_ascend/bug_wiki/
```

The wiki answers: what broke, why it broke, which workload triggered it, which release/image is affected, what fixed it, and whether GRIEF or CI can find it.

## Working Model

Borrow two useful patterns:

- KernelWiki-style evidence layers: raw sources, synthesized capsules, cross-reference indices, and validation.
- vLLM Skills-style task focus: one skill should guide a repeatable workflow with concrete commands and output contracts.
- Official vLLM deploy/benchmark skills as companion execution skills for reproduction planning, not as bug evidence by themselves.

Do not treat KernelWiki or vLLM Skills as factual evidence for vLLM-Ascend bugs. They are style references only.

## Core Workflow

1. Locate the workspace root and target wiki. If the user gives no path, use `llm_state_based/vllm_ascend/bug_wiki/`.
2. Read [references/primer.md](references/primer.md) for evidence locations and triage routes.
3. Read [references/schema.md](references/schema.md) before editing capsules, index tables, workload patterns, or fuzzer summaries.
4. Read [references/vllm_skills.md](references/vllm_skills.md) when the capsule needs a verification plan involving deploy, serve benchmark, random synthetic benchmark, or prefix-cache benchmark skills.
5. Gather evidence from local sources first:
   - issue capsule root
   - GitHub issue HTML/search cache
   - PR-centric bugfix corpus
   - release/image/bugfix mapping
   - fuzzer history
   - CPU CI feasibility reports
   - feature wiki cross-links
6. Create or update the capsule using the issue-to-fix chain:

```text
bug issue
-> failure symptom
-> triggering workload
-> affected version/image
-> dependency context
-> fixing PR/code diff
-> patch applicability
-> before/after evidence
-> fuzzer discoverability
```

7. Preserve `unknown` for missing facts. Do not invent commands, CANN compatibility, release commits, image tags, or reproduction results.
8. Update cross-links where relevant:
   - `INDEX.md`
   - `workload_patterns/*.md`
   - `fuzzer_findability/README.md`
   - `release_matrix/README.md`
   - `raw_source_index/README.md`
   - `../vllm_engine_feature_wiki/feature_to_bug_map/README.md` only if the user allows feature-wiki edits too.
9. Validate with:

```bash
python3 llm_state_based/vllm_ascend/codex_skills/our-wiki-skill/vllm-bug-wiki/scripts/validate_wiki.py \
  llm_state_based/vllm_ascend/bug_wiki
```

10. In the final response, report capsules created/updated, evidence strength, unresolved gaps, official-vLLM-skill connections if added, and recommended verification experiments.

## Evidence Rules

- Local evidence wins over memory.
- Official docs, GitHub issues/PRs/RFCs, release mapping, code diffs, and logs are primary.
- Blogs/Zhihu/general web can explain intuition but cannot prove a bug fact by themselves.
- If asked for latest upstream facts, browse and cite primary sources.
- New model-path examples must use `/mnt/data2/model_weights`; do not write the legacy model-volume path.

## Edit Discipline

- This is knowledge-base construction, not reproduction.
- Do not run NPU/Docker/fuzzer campaigns unless the user explicitly asks.
- Do not modify raw evidence files unless the user explicitly asks.
- Use scoped documentation edits and relative local links.

## Useful References

- [references/primer.md](references/primer.md): evidence map and bug-domain triage.
- [references/schema.md](references/schema.md): capsule contract, confidence levels, and quality gates.
- [references/examples.md](references/examples.md): worked task patterns.
- [references/vllm_skills.md](references/vllm_skills.md): how official vLLM deploy/benchmark skills connect to bug verification.
