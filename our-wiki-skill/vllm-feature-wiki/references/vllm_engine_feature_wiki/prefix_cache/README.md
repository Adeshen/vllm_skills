# Feature: Prefix Cache

## Mental Model
Prefix cache is cross-request memory reuse. If two requests share the same token prefix and the same hidden cache context, the second request can borrow full KV blocks from the first instead of recomputing them.

## One-Request Story
Request A fills KV blocks and assigns hashes to complete cacheable blocks. After A releases active references, those blocks may remain in the cache. Request B arrives with a matching prefix, computes the same prefix hashes, touches the cached blocks, increments references, computes only its suffix, and later releases its references.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| prefix hash | full block ready | hash algorithm/version | cache lookup | eviction | omits LoRA/media/salt context |
| parent hash | previous block context | chain growth | hash input | eviction | same tokens but wrong history |
| cached block ref | cache hit | ref count | across requests | release/eviction | leak or premature eviction |
| suffix KV state | probe request | decode | request lifetime | cleanup | suffix reads wrong prefix |
| latency/cache-hit signal | request timing | per request | comparisons | no | noisy proxy for correctness |

## Common Bug Stories
- Same tokens but different adapter/media context accidentally share a block.
- Boundary prompt misses a cache hit or reuses the wrong block.
- Cancellation leaves ref count wrong, causing leak or premature reuse.
- Chunked prefill changes where blocks become hashable.

## Related Bugs
- No pure prefix-cache capsule exists yet.
- Adjacent: [chunk prefill long-sequence bug](../../bug_wiki/bug_capsules/VA-BUG-5445-CHUNK-PREFILL-LONG-SEQUENCE.md)
- Adjacent: [KV load failure metrics exception](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md)

## Fuzzer Strategy
- Seed shape: warm shared prefix -> probe same prefix -> mutated suffix -> changed-prefix canary -> recovery.
- Mutation axes: prefix length, suffix length, token boundary, LoRA/media/cache salt, request ordering.
- Oracle: deterministic output, cache-hit latency proxy, no leak, no 5xx.
- Monitor: response text, latency, KV events if enabled, HBM/cache baseline.
- Expected failure signals: output drift, missed hit, false hit, cache leak.

## Verification Strategy
- Use exact token-length prompts, not approximate character lengths.
- Compare same request alone versus after warmup.
- Include a negative control with one token changed in the prefix.
- Do not claim correctness from latency alone; use it as a cache-hit proxy.

## Evidence Sources
- [KV cache deep dive](../theory_illustrations/KV_CACHE_DEEP_DIVE.md)
- [Prefix cache workload pattern](../../bug_wiki/workload_patterns/PREFIX_CACHE.md)
- vLLM prefix caching design linked from [source notes](../theory_illustrations/SOURCE_NOTES.md)

## Unknowns
- Specific vLLM-Ascend prefix-cache bug capsules.
- Exact prefix-cache flags and metrics for current npu4 baseline.
- Token-boundary repro seeds for known prefix-cache issues.

