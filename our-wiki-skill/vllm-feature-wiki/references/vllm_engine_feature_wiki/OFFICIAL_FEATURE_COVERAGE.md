# Official Feature Coverage

Source page: [vLLM-Ascend Feature Tutorials](https://docs.vllm.ai/projects/ascend/en/latest/tutorials/features/index.html). The page lists feature tutorials and links the broader official feature guide navigation.

The official docs page is the latest developer preview. It also links to the latest stable release docs, so release-specific verification should still be checked against the local [release matrix](../bug_wiki/release_matrix/README.md).

## Official Feature Tutorials

| Official tutorial | Local feature page | Engine state focus | Local bug/fuzzer connection |
| --- | --- | --- | --- |
| PD-Colocated with Mooncake Multi-Instance | [distributed](distributed/README.md), [prefill/decode disaggregation](prefill_decode_disaggregation/README.md), [KV cache](kv_cache/README.md) | KV transfer, Mooncake, multi-instance, cross-node cache reuse | [#7871](../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md), [#6273](../bug_wiki/bug_capsules/VA-BUG-6273-KVPOOL-LAYERWISE-POOLING.md) |
| Prefill-Decode Disaggregation (Qwen2.5-VL) | [prefill/decode disaggregation](prefill_decode_disaggregation/README.md), [distributed](distributed/README.md) | P/D roles, proxy, KV transfer, multimodal/VL serving | PD transfer and proxy failure seeds |
| Prefill-Decode Disaggregation (DeepSeek) | [prefill/decode disaggregation](prefill_decode_disaggregation/README.md), [distributed](distributed/README.md), [moe](moe/README.md) | multi-node P/D, DeepSeek, MTP, Mooncake, expert parallel | [#4986](../bug_wiki/bug_capsules/VA-BUG-4986-MTP-FULL-DECODE-HANG.md), [#7871](../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md) |
| Long-Sequence Context Parallel (Qwen3-235B-A22B) | [attention](attention/README.md), [scheduler](scheduler/README.md), [distributed](distributed/README.md) | context parallelism, long context, large MoE model | long-context and attention-mask fuzz seeds |
| Long-Sequence Context Parallel (DeepSeek) | [attention](attention/README.md), [prefill/decode disaggregation](prefill_decode_disaggregation/README.md), [distributed](distributed/README.md) | context parallel P/D, long sequence, DeepSeek W8A8/MTP | [#4986](../bug_wiki/bug_capsules/VA-BUG-4986-MTP-FULL-DECODE-HANG.md) adjacent |
| Dynamic Chunked Pipeline Parallel (DeepSeek-V3.1) | [scheduler](scheduler/README.md), [distributed](distributed/README.md), [prefill/decode disaggregation](prefill_decode_disaggregation/README.md) | pipeline chunks, scheduling, DeepSeek long decode | [#5445](../bug_wiki/bug_capsules/VA-BUG-5445-CHUNK-PREFILL-LONG-SEQUENCE.md) adjacent |
| Suffix Speculative Decoding | [speculative decoding](speculative_decoding/README.md), [sampling](sampling/README.md) | draft/proposal state, suffix matching, token verification | [#7807](../bug_wiki/bug_capsules/VA-BUG-7807-BLOCK-VERIFY-REJECTION-SAMPLING.md) |
| Ray Distributed (Qwen3-235B-A22B) | [distributed](distributed/README.md), [moe](moe/README.md) | Ray executor, large-model distribution, MoE topology | distributed startup/liveness seeds |

## Official Feature Guide Topics

| Official feature-guide topic | Local page | Current local status |
| --- | --- | --- |
| Graph Mode Guide | [ascend backend](ascend_backend/README.md), [engine lifecycle](engine_lifecycle/README.md) | represented as backend graph/shape state |
| CPU Binding | [distributed](distributed/README.md), [ascend backend](ascend_backend/README.md) | linked to [#6992](../bug_wiki/bug_capsules/VA-BUG-6992-CPU-BINDING-LOCALE.md) |
| AI QoS Feature | [scheduler](scheduler/README.md), [engine lifecycle](engine_lifecycle/README.md) | coverage placeholder; local bug evidence unknown |
| Quantization Guide | [quantization](quantization/README.md) | linked to [#2318](../bug_wiki/bug_capsules/VA-BUG-2318-W8A8-QWEN3-GARBLED.md) |
| Sleep Mode Guide | [engine lifecycle](engine_lifecycle/README.md) | coverage placeholder; local bug evidence unknown |
| Structured Output Guide | [sampling](sampling/README.md) | linked to [#5524](../bug_wiki/bug_capsules/VA-BUG-5524-XGRAMMAR-TYPE-MISMATCH.md) |
| LoRA Adapters Guide | [lora](lora/README.md) | page added; local bug evidence not yet curated |
| Expert Load Balance (EPLB) | [moe](moe/README.md), [distributed](distributed/README.md) | coverage noted; local bug capsule missing |
| Netloader Guide | [engine lifecycle](engine_lifecycle/README.md), [ascend backend](ascend_backend/README.md) | coverage placeholder; local bug evidence unknown |
| RFork Guide | [engine lifecycle](engine_lifecycle/README.md), [ascend backend](ascend_backend/README.md) | coverage placeholder; local bug evidence unknown |
| Multi Token Prediction (MTP) | [speculative decoding](speculative_decoding/README.md), [sampling](sampling/README.md) | linked to [#4986](../bug_wiki/bug_capsules/VA-BUG-4986-MTP-FULL-DECODE-HANG.md) and [#7807](../bug_wiki/bug_capsules/VA-BUG-7807-BLOCK-VERIFY-REJECTION-SAMPLING.md) |
| Dynamic Batch | [scheduler](scheduler/README.md) | coverage noted; local bug capsule missing |
| Disaggregated-encoder | [prefill/decode disaggregation](prefill_decode_disaggregation/README.md), [distributed](distributed/README.md) | coverage noted; local bug evidence unknown |
| Ascend Store Deployment Guide | [kv cache](kv_cache/README.md), [distributed](distributed/README.md) | linked to CPU CI `BlockStored` capsule |
| KV Cache CPU Offload Guide | [kv cache](kv_cache/README.md) | coverage noted; local bug evidence unknown |
| External DP | [distributed](distributed/README.md) | coverage noted; local bug evidence unknown |
| Distributed DP Server With Large-Scale Expert Parallelism | [distributed](distributed/README.md), [moe](moe/README.md) | coverage noted; local bug evidence unknown |
| UCM Store Deployment Guide | [kv cache](kv_cache/README.md), [distributed](distributed/README.md) | coverage noted; local bug evidence unknown |
| Fine-Grained Tensor Parallelism | [distributed](distributed/README.md), [attention](attention/README.md) | coverage noted; local bug evidence unknown |
| Layer Sharding Linear Guide | [distributed](distributed/README.md), [moe](moe/README.md) | coverage noted; local bug evidence unknown |
| Speculative Decoding Guide | [speculative decoding](speculative_decoding/README.md) | page added |
| Context Parallel Guide | [attention](attention/README.md), [distributed](distributed/README.md) | tied to official long-sequence tutorials |
| Weight Prefetch Guide | [engine lifecycle](engine_lifecycle/README.md), [ascend backend](ascend_backend/README.md) | coverage placeholder; local bug evidence unknown |
| Sequence Parallelism | [attention](attention/README.md), [distributed](distributed/README.md) | coverage noted; local bug evidence unknown |
| Batch Invariance | [sampling](sampling/README.md), [scheduler](scheduler/README.md) | useful correctness oracle category |
| LMCache-Ascend Deployment Guide | [kv cache](kv_cache/README.md), [distributed](distributed/README.md) | coverage noted; local bug evidence unknown |
| Dynamic Chunked Pipeline Parallel | [scheduler](scheduler/README.md), [distributed](distributed/README.md) | tied to official tutorial |
| Flash Attention 3 | [attention](attention/README.md), [ascend backend](ascend_backend/README.md) | coverage noted; local bug evidence unknown |

