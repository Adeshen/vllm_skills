# vLLM Bug Wiki Primer

Use this file when a request is broad or when you need to decide which evidence source to inspect.

## Target

```text
llm_state_based/vllm_ascend/bug_wiki/
```

## Evidence Map

| Evidence | Local path | Use |
| --- | --- | --- |
| Issue capsule root | `llm_state_based/vllm_ascend/issue_capsule/` | Main local evidence tree. |
| GitHub issue cache | `issue_capsule/workloads/github_bug_issue_html_cache_vllm_search_20260519/` | Cached issue/search HTML. |
| PR-centric bugfix corpus | `issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/` | PR metadata, diffs, issue-to-fix evidence. |
| Release/image mapping | `issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md` | Image/version/bugfix mapping. |
| Bug pattern findability | `issue_capsule/project_docs/VLLM_BUG_PATTERN_TO_FUZZER_FINDABILITY.md` | GRIEF discoverability assumptions. |
| Container startup | `issue_capsule/project_docs/NPU4_ASCEND_CONTAINER_STARTUP_METHOD.md` | NPU4 environment rules. |
| Fuzzer history | `issue_capsule/grief_fuzzer_history/` | Seeds, logs, smoke corpus. |
| Feature wiki | `llm_state_based/vllm_ascend/vllm_engine_feature_wiki/` | Feature-state interpretation of bugs. |
| Official vLLM skills | `https://github.com/vllm-project/vllm-skills` | Companion deploy/benchmark workflows for verification planning. Not bug evidence by itself. |

## Failure Domains

| Domain | Start with |
| --- | --- |
| KV cache / prefix cache | `workload_patterns/KV_CACHE.md`, `workload_patterns/PREFIX_CACHE.md` |
| scheduler / liveness | `workload_patterns/SCHEDULER.md` |
| distributed / PD / Mooncake | `workload_patterns/DISTRIBUTED_PD.md` |
| MoE / FlashComm | `workload_patterns/MOE_FLASHCOMM.md` |
| quantization | `workload_patterns/QUANTIZATION.md` |
| sampling / output correctness | `workload_patterns/SAMPLING_CORRECTNESS.md` |
| lifecycle / cancel / disconnect | `workload_patterns/LIFECYCLE_CANCEL.md` |
| CPU/mock CI | `ci_and_environment/README.md` |

## Verification Skill Routes

| Bug verification need | Official vLLM skill to reference |
| --- | --- |
| Start a generic local service | `vllm-deploy-simple` |
| Docker service plan | `vllm-deploy-docker` |
| Kubernetes service plan | `vllm-deploy-k8s` |
| Prefix-cache performance or cache-hit workload | `vllm-prefix-cache-bench` |
| Throughput/latency synthetic workload | `vllm-bench-random-synthetic` |
| OpenAI-compatible endpoint benchmark | `vllm-bench-serve` |

## Capsule ID Style

Prefer:

```text
VA-BUG-<issue-or-domain>-<SHORT-SLUG>.md
```

Examples:

- `VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md`
- `VA-BUG-CPUCI-BLOCKSTORED-PARENT-HASH.md`

## Output Contract

Report:

- files created or updated
- capsule count changed
- strongest evidence
- missing evidence
- recommended next verification experiments
