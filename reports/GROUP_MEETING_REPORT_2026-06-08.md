# Group Meeting Report: vLLM Skill Repository And Knowledge Workflow

Date: 2026-06-08

## 1. One-Sentence Summary

We built a reusable vLLM-oriented skill repository that integrates local vLLM/vLLM-Ascend bug/wiki/operation skills, upstream HPC/MLSys skill references, normalized skill installation, local skill quality audit, and a new paper-search skill for literature-driven bug and feature research.

## 2. Motivation

The current vLLM/vLLM-Ascend research workflow needs more than isolated bug notes. We need a repeatable system that connects:

- bug evidence and issue reproduction
- engine feature theory and state-machine explanations
- fuzzer seed design and discoverability analysis
- NPU/Docker/benchmark/trace operation workflows
- HPC/MLSys references such as NCU, NVIDIA skills, FlagOS, KernelWiki, and vLLM skills
- related papers on LLM inference bugs, serving fuzzing, incidents, CI, workflow security, and disaggregated serving

The main goal is to make future agents and researchers start from structured workflows instead of rediscovering procedures from scattered notes.

## 3. Repository Status

Repository:

```text
llm_state_based/vllm_ascend/codex_skills/
```

Remote:

```text
git@github.com:Adeshen/vllm_skills.git
```

Recent commits:

| Commit | Purpose |
| --- | --- |
| `26cf46a` | Add paper search skill |
| `60978df` | Optimize local skills with upstream routes |
| `2c9988b` | Add normalized skill installer |
| `9682d68` | Add HPC MLSys skill references |
| `91a71a7` | Broaden skills repository scope |
| `0d51909` | Initialize vLLM skills repository |

Current working tree: clean.

## 4. What Was Built

### 4.1 Local Wiki Skills

Two wiki-construction skills are now maintained:

| Skill | Purpose |
| --- | --- |
| `vllm-feature-wiki` | Maintains vLLM/vLLM-Ascend engine feature wiki as state-machine documentation. |
| `vllm-bug-wiki` | Maintains evidence-driven issue-to-fix bug capsules and workload/fuzzer/release summaries. |

Key improvements:

- added explicit golden rules
- added evidence boundaries
- added upstream route awareness
- preserved documentation-only behavior unless experiments are explicitly requested
- connected feature/bug wiki work to vLLM, NCU, NVIDIA, FlagOS, AI Research, and evaluation skill routes

### 4.2 Local Operator Skills

Eight local operation/reproduction skills are maintained:

| Skill | Purpose |
| --- | --- |
| `run-vllm-ascend-docker` | Start, restart, and troubleshoot vLLM-Ascend Docker service on `npu4`. |
| `benchmark-vllm-ascend` | Run EvalScope and KV-cache-aware benchmark workflows. |
| `collect-vllm-ascend-traces` | Collect local Jaeger/OTEL traces for vLLM-Ascend services. |
| `reproduce-vllm-ascend-issue` | Fetch, extract, reproduce, and report GitHub issues. |
| `record-vllm-ascend-report` | Normalize raw logs/notes into Markdown and HTML reports. |
| `update-issue-tracker` | Update issue tracker JSON state and generated HTML report state. |
| `vllm-ascend-incident-triage` | Preserve incident scene, save trigger request, replay, and route to specialist workflow. |
| `workload-feedback-report` | Synthesize multiple runs into workload-family-centered research feedback. |

Key improvements:

- added evidence and validation contracts
- added "inspect before restart" and "baseline before disruption" rules
- added upstream route map for benchmark, NCU/profiling, NVIDIA distributed/MoE, FlagOS kernel, evaluation, and generic vLLM routes
- added missing `openai.yaml` metadata for `update-issue-tracker`

### 4.3 New Research Skill: `paper-skill`

Added:

```text
our-research-skills/paper-skill/
```

Purpose:

- search related papers from seed literature
- build literature maps
- classify papers by local relevance
- connect papers to bug wiki, feature wiki, fuzzer playbooks, incident SOPs, CI matrix, and skill safety

Seed papers added:

| Theme | Seed papers |
| --- | --- |
| LLM inference bugs and fuzzing | `A First Look at Bugs in LLM Inference Engines`; `Continuous Discovery of Vulnerabilities in LLM Serving Systems with Fuzzing` |
| Production incidents and troubleshooting | `Enhancing reliability in AI inference services`; `Agentic Troubleshooting Guide Automation for Incident Management` |
| CI and workflow security | `Argus`; `Demystifying and Detecting Agentic Workflow Injection Vulnerabilities in GitHub Actions`; `Taming the Variants` |
| Agentic optimization | `AVO: Agentic Variation Operators for Autonomous Evolutionary Search` |
| Stage-level and disaggregated serving | `TridentServe`; `vLLM-Omni` |

Also added a query generator:

```bash
python3 our-research-skills/paper-skill/scripts/make_queries.py
```

### 4.4 Upstream Skill References

All imported upstream repositories are Git submodules, not copied files.

| Source | Current pointer / status |
| --- | --- |
| `vllm-project/vllm-ascend` | `f5c97749fa36f80648a56198e60800f3a0dac3ff` |
| `vllm-project/vllm-skills` | `c99623410c1531148ff9b39fe1dcb27efbf4bf23` |
| `mit-han-lab/KernelWiki` | `76d27b56f804e7e7295d4c570e1e5d7eef4b0a75` |
| `mit-han-lab/ncu-report-skill` | `1cf238d6b41c79bd35041192506c4d45e765a3f1` |
| `NVIDIA/skills` | `e29b3c65dd0292e3f9f851b15eefe5a7c2023dd7` |
| `flagos-ai/skills` | `d9eb2bbbf976faef4ce1e14c8c7c668aec9b1620` |
| `Orchestra-Research/AI-research-SKILLs` | `28f2d29236f2bade2eb92cadb2585189589a5828` |
| `NVIDIA-NeMo/Evaluator` | `d4ceac0112769300c15b54fdde5237a12e094c61` |
| `K-Dense-AI/scientific-agent-skills` | `4457f17a29e55c2190c71fca0df156761ac5400c` |
| `huggingface/skills` | `504191c59a67888cae225ea54fe03aa502ef0319` |
| `MemTensor/skills-vote` | `86fd73915e9ea4b594ca0edbd8c3267109a8f976` |

## 5. Current Skill Inventory

The normalized installer now discovers:

```text
428 installable skills
11 duplicate entries skipped
```

The normalized install command is:

```bash
make install
```

The manifest-only command is:

```bash
make manifest
```

The generated manifest is:

```text
build/upstream_skills/manifest.md
```

The new local research skill appears as:

```text
local-research__paper-skill
```

## 6. Quality Gates And Validation

Validation commands executed:

```bash
python3 scripts/audit_local_skills.py
python3 scripts/install_upstream_skills.py --target build/upstream_skills --mode manifest
python3 our-wiki-skill/vllm-feature-wiki/scripts/validate_wiki.py ../vllm_engine_feature_wiki
python3 our-wiki-skill/vllm-bug-wiki/scripts/validate_wiki.py ../bug_wiki
```

Results:

| Check | Result |
| --- | --- |
| Local skill audit | all local skills `OK` |
| Normalized installer | discovered `428` skills, skipped `11` duplicates |
| Feature wiki validator | `OK` |
| Bug wiki validator | `OK` |
| Forbidden model path check | no legacy model-volume path in local skill docs |
| Git status | clean |

The local audit checks that every local skill has:

- frontmatter
- `Use when` trigger
- references
- UI metadata
- evidence rules
- validation/output guidance
- upstream-route awareness

## 7. Design Principles

### 7.1 Evidence Discipline

The skill system uses this boundary:

```text
upstream skill / paper / blog = planning or theory reference
local command + logs + metrics + artifacts + environment = evidence
```

This prevents generic vLLM, CUDA, or NVIDIA knowledge from being treated as proof of vLLM-Ascend behavior.

### 7.2 Progressive Disclosure

Each `SKILL.md` stays relatively small and points to:

- `references/`
- `scripts/`
- shared route maps

This follows the pattern from high-quality upstream skills: only load details when the task needs them.

### 7.3 Routing Instead Of Duplication

Local skills now route to upstream references explicitly:

- vLLM skills for deployment and benchmark shape
- NCU skill for evidence-backed profiling discipline
- NVIDIA skills for Dynamo, NeMo, Megatron, MoE, distributed, and evaluation vocabulary
- FlagOS skills for kernel generation, heterogeneous stack, vLLM plugin, and model migration routes
- AI Research skills for serving, optimization, evaluation, incidents, and paper-writing routes

## 8. Why This Matters For The Research Project

This skill repository turns the research workflow into a reusable system:

1. Bug reports become structured capsules instead of one-off notes.
2. Feature explanations become state-machine pages instead of vague architecture summaries.
3. Fuzzer seeds can be derived from known failure domains and paper-driven mutation axes.
4. Incident handling has a fixed scene-preservation and replay protocol.
5. Benchmarks and traces have evidence contracts.
6. Literature search now feeds directly into local bug/wiki/fuzzer/CI work.

The immediate research value is that future agents can use the same operational and documentation discipline without re-learning the whole workspace.

## 9. Open Gaps

| Gap | Impact | Proposed next step |
| --- | --- | --- |
| Paper-skill currently stores seed papers but not a generated paper map artifact | Literature workflow is ready, but no reviewed map yet | Run `paper-skill` to produce a first `Paper Map: LLM Serving Reliability And Fuzzing` |
| Upstream skill catalog is large | Some imported skills are only loosely relevant | Add filtering profile for `vLLM/HPC/MLSys only` |
| Installer skips duplicate entries but does not yet explain each duplicate in the meeting report | Fine for installation, less useful for curation | Add duplicate summary table to manifest |
| Local skills are optimized, but not yet benchmarked with independent agent tasks | Skill quality is audited structurally, not behaviorally | Run 3 dry-run prompts and record whether the correct skill triggers |
| Wiki and paper skill are connected conceptually, not via generated cross-links | Manual step remains | Add paper-to-feature and paper-to-bug map files |

## 10. Recommended Next Work

1. Build a paper map from the current seed corpus.
   Suggested topic:

   ```text
   LLM Serving Reliability, Fuzzing, Incidents, And Multi-Architecture Validation
   ```

2. Use the paper map to update:

   ```text
   vllm_engine_feature_wiki/theory_illustrations/
   bug_wiki/fuzzer_findability/
   bug_wiki/workload_patterns/
   ```

3. Add a curated install profile:

   ```text
   make install PROFILE=vllm-mlsys
   ```

   This would install only the most relevant subset instead of all 428 skills.

4. Run behavioral skill tests:

   - issue reproduction prompt
   - paper search prompt
   - feature-wiki theory prompt
   - benchmark planning prompt

5. Convert the current report into slides if needed.

## 11. Suggested Group Meeting Talking Points

1. We now have a GitHub-backed vLLM skills repository.
2. The repo is not only for vLLM-Ascend; it covers general vLLM, Ascend-specific workflows, HPC/MLSys references, and research literature.
3. Upstream repositories are submodules, not vendored copies.
4. The normalized installer discovers 428 installable skills.
5. Local skills now have evidence contracts and validation gates.
6. A new paper-search skill connects the literature to bug wiki, feature wiki, fuzzer, CI, and incident work.
7. Next step is to generate the first paper map and feed it back into the bug/feature wiki.
