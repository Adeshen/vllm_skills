# Feature: Attention

## Mental Model
Attention is where request shape becomes kernel shape. It binds together positions, masks, KV block tables, batch layout, parallel partitions, and backend kernels.

## One-Request Story
The scheduler selects tokens to run. The engine builds positions and masks for those tokens, points attention at the relevant KV blocks, and calls the selected backend kernel. Decode then advances position state and repeats. In long-context, context-parallel, MTP, or MoE/FlashComm cases, the same story crosses more shape and rank boundaries.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| position state | prefill/decode | every token | across decode | cleanup | off-by-one at boundaries |
| attention mask | batch construction | per step/shape | graph capture may reuse | step end | index out of range |
| block table | KV allocation | cache growth | across tokens | cleanup | attention reads wrong KV |
| backend graph/kernel | backend init | capture/config | across requests | process end | dynamic shape unsupported |
| parallel partition | distributed setup | unknown | process lifetime | shutdown | rank shape mismatch |

## Common Bug Stories
- EAGLE repeated calls reuse or mutate mask state incorrectly.
- MoE + MTP + FlashComm gives hidden-state shape to a backend expecting another shape.
- Long context/context parallel exposes partition-specific mask or KV layout errors.
- FlashAttention/custom kernels reject shape combinations that generic paths accepted.

## Related Bugs
- [EAGLE repeated-call attention mask index error](../../bug_wiki/bug_capsules/VA-BUG-3024-EAGLE-ATTN-MASK-REPEATED-CALLS.md)
- [Qwen3.5 MoE MTP FlashComm shape mismatch](../../bug_wiki/bug_capsules/VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE.md)

## Fuzzer Strategy
- Seed shape: short control -> shape sweep -> repeated EAGLE/MTP request -> recovery canary.
- Mutation axes: prompt length, max tokens, batch shape, repeated-call count, MTP/EAGLE/FlashComm/context parallel toggles.
- Oracle: no shape traceback, no 5xx, deterministic output where appropriate.
- Monitor: logs, status codes, recovery canary, optional shape/trace instrumentation.
- Expected failure signals: `attn_mask index out of range`, dimension mismatch, backend kernel error.

## Verification Strategy
- Record exact shape inputs: prompt tokens, batch size, max tokens, topology, backend flags.
- Test one-shot and repeated-call variants.
- For context parallel, preserve rank count and partition settings.
- For shape bugs, logs are often stronger evidence than text output.

## Evidence Sources
- [Attention deep dive](../theory_illustrations/ATTENTION_DEEP_DIVE.md)
- [MoE/FlashComm workload pattern](../../bug_wiki/workload_patterns/MOE_FLASHCOMM.md)
- [Sampling correctness workload pattern](../../bug_wiki/workload_patterns/SAMPLING_CORRECTNESS.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Exact attention backend selected by each release/image.
- Exact runtime flags for #3024 and #7996.
- Kernel-level trace availability on npu4.

