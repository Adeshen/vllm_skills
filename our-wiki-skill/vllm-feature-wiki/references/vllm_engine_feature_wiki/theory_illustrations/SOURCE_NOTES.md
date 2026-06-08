# Source Notes

This page records external knowledge sources used to enrich the theory illustrations. Official docs, papers, GitHub issues, RFCs, and local evidence are treated as primary grounding. General web and Zhihu material is used only for intuition unless a claim is also supported by primary sources.

## Primary Sources

| Source | Why it matters | Local theory pages |
| --- | --- | --- |
| [PagedAttention paper](https://arxiv.org/abs/2309.06180) | Introduces block/page-style KV cache management and the throughput motivation behind vLLM. | [KV cache](KV_CACHE_DEEP_DIVE.md), [attention](ATTENTION_DEEP_DIVE.md), [scheduler](SCHEDULER_DEEP_DIVE.md) |
| [vLLM prefix caching design](https://docs.vllm.ai/en/latest/design/prefix_caching/) | Defines prefix-cache block hashing, parent hash, extra hashes, ref count, allocation/free/eviction workflow. | [KV cache](KV_CACHE_DEEP_DIVE.md), [state invariants](STATE_INVARIANTS.md) |
| [vLLM hybrid KV cache manager](https://docs.vllm.ai/en/stable/design/hybrid_kv_cache_manager/) | Explains KV grouping for hybrid models, sliding-window attention, Mamba-style layers, and prefix-cache constraints. | [KV cache](KV_CACHE_DEEP_DIVE.md), [attention](ATTENTION_DEEP_DIVE.md) |
| [vLLM disaggregated prefill docs](https://docs.vllm.ai/en/stable/features/disagg_prefill/) | Explains P/D split, TTFT/ITL motivation, connectors, lookup buffer, and scheduler/worker connector split. | [PD/Mooncake](PD_MOONCAKE_DEEP_DIVE.md), [scheduler](SCHEDULER_DEEP_DIVE.md) |
| [vLLM Mooncake RFC](https://github.com/vllm-project/vllm/issues/10727) | Gives Mooncake transfer-engine motivation and a data-transfer view of prefill/decode disaggregation. | [PD/Mooncake](PD_MOONCAKE_DEEP_DIVE.md) |
| [vLLM-Ascend feature tutorials](https://docs.vllm.ai/projects/ascend/en/latest/tutorials/features/index.html) | Official public feature surface for Ascend tutorials. | [official coverage](../OFFICIAL_FEATURE_COVERAGE.md), all subsystem pages |
| [vLLM-Ascend design documents](https://docs.vllm.ai/projects/ascend/en/main/developer_guide/Design_Documents/index.html) | Entry point for Ascend-specific design material. | [Ascend backend](ASCEND_BACKEND_DEEP_DIVE.md) |
| [vLLM-Ascend CPU binding design](https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/Design_Documents/cpu_binding.html) | Grounds CPU binding as an Ascend backend lifecycle feature. | [Ascend backend](ASCEND_BACKEND_DEEP_DIVE.md), [state invariants](STATE_INVARIANTS.md) |
| [Local bug wiki](../../bug_wiki/README.md) | Provides local issue/PR/evidence capsules and avoids inventing reproduction claims. | [feature-to-bug map](../feature_to_bug_map/README.md), all feature pages |
| [Local GRIEF fuzzer history](../../issue_capsule/grief_fuzzer_history/) | Provides local seed shapes and smoke-test evidence for request-level fuzzing. | [fuzzer playbooks](FUZZER_PLAYBOOKS.md), [bug reading workflow](BUG_READING_WORKFLOW.md) |

## Supplemental Sources

| Source | Use |
| --- | --- |
| [RunPod vLLM explainer](https://www.runpod.io/articles/guides/vllm-pagedattention-continuous-batching) | General explanation of PagedAttention and continuous batching; useful for reader intuition. |
| [Zhihu KV cache memory answer](https://www.zhihu.com/en/answer/1896598668137722183) | Supplemental intuition on what happens when KV cache exceeds memory. |
| [Zhihu KV cache sharing answer](https://www.zhihu.com/en/answer/60672621935) | Supplemental intuition on prefix/KV sharing and space-time tradeoffs. |
| [Zhihu PagedAttention intro](https://zhihu.com/en/article/1922304038260696074) | Supplemental analogy for paged KV cache. |
| [Zhihu vLLM KV cache lifecycle/code reading](https://zhuanlan.zhihu.com/p/1931739777427829216) | Supplemental code-reading perspective on KV cache lifecycle. |

## Evidence Discipline

- Use official docs or local evidence for commands, flags, release/image claims, and CANN/vLLM/torch compatibility.
- Use supplemental web sources for intuition only.
- Keep unknown facts as `unknown`.
- Link a bug statement to a local bug capsule when possible.
- New model-path examples must use `/mnt/data2/model_weights`.
