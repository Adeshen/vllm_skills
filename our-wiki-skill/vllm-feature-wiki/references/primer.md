# vLLM Feature Wiki Primer

Use this file when a request is broad or when you need to decide which feature page to touch.

## Target

```text
llm_state_based/vllm_ascend/vllm_engine_feature_wiki/
```

## Source Layers

| Layer | Local path | Purpose |
| --- | --- | --- |
| Raw evidence | `llm_state_based/vllm_ascend/issue_capsule/` | Issues, PR caches, project docs, fuzzer history, logs. Do not edit during feature-wiki work. |
| Bug synthesis | `llm_state_based/vllm_ascend/bug_wiki/` | Bug capsules, workload patterns, release/fuzzer/CI summaries. |
| Feature synthesis | `llm_state_based/vllm_ascend/vllm_engine_feature_wiki/` | Feature state-machine pages, theory deep dives, feature-to-bug map. |
| Official docs | vLLM and vLLM-Ascend docs | Current feature surface and design details. Browse when freshness matters. |
| Official vLLM skills | `https://github.com/vllm-project/vllm-skills` | Companion operational skills for deploy and benchmark workflows. Use for verification planning, not as local bug evidence. |
| Supplemental intuition | blogs/Zhihu/general web | Teaching analogies only; label clearly. |

## Feature Routes

| User asks about | Open first | Then open |
| --- | --- | --- |
| continuous batching, request admission, liveness | `scheduler/README.md` | `theory_illustrations/SCHEDULER_DEEP_DIVE.md` |
| KV blocks, parent hash, invalid blocks, PD transfer | `kv_cache/README.md` | `theory_illustrations/KV_CACHE_DEEP_DIVE.md` |
| shared prompts, APC, cache hit/miss | `prefix_cache/README.md` | `theory_illustrations/KV_CACHE_DEEP_DIVE.md` |
| masks, positions, context parallel, shape errors | `attention/README.md` | `theory_illustrations/ATTENTION_DEEP_DIVE.md` |
| logits, xgrammar, output correctness | `sampling/README.md` | `theory_illustrations/SAMPLING_AND_SPEC_DEEP_DIVE.md` |
| MTP, EAGLE, suffix speculative decoding | `speculative_decoding/README.md` | `theory_illustrations/SAMPLING_AND_SPEC_DEEP_DIVE.md` |
| stream disconnect/cancel | `streaming/README.md` | `theory_illustrations/STREAMING_LIFECYCLE_DEEP_DIVE.md` |
| LoRA adapter state | `lora/README.md` | `kv_cache/README.md`, `sampling/README.md` |
| W8A8/FP8/quantized output | `quantization/README.md` | `theory_illustrations/QUANT_MOE_DEEP_DIVE.md` |
| experts, FlashComm, fused MoE | `moe/README.md` | `theory_illustrations/QUANT_MOE_DEEP_DIVE.md` |
| TP/PP/DP/PD/Mooncake | `distributed/README.md` | `theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md` |
| prefill/decode split | `prefill_decode_disaggregation/README.md` | `theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md` |
| metrics, tracing, failure observability | `metrics_tracing/README.md` | `feature_to_bug_map/README.md` |
| NPU device, CANN, torch-npu, graph, HBM | `ascend_backend/README.md` | `theory_illustrations/ASCEND_BACKEND_DEEP_DIVE.md` |

## Update Routes

- Theory improvement: update subsystem page plus matching deep dive.
- New feature: create folder `feature_name/README.md`, add `INDEX.md` row, add map entries if bugs exist.
- New bug linkage: update subsystem `Related Bugs`, `feature_to_bug_map/README.md`, and optionally fuzzer playbook.
- New official doc coverage: update `OFFICIAL_FEATURE_COVERAGE.md` and source notes.
- New verification route: update the feature page's `Verification Strategy` and consult `references/vllm_skills.md` for the closest official deploy/benchmark skill.

## Output Contract

Report:

- files changed
- features documented
- strongest feature-to-bug connections
- missing evidence
- validation result
