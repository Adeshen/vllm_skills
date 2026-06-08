# Feature: LoRA Adapters

## Mental Model
LoRA is per-request model personality layered onto a shared base model. The engine must apply the right adapter and keep adapter state from contaminating other requests, caches, or ranks.

## One-Request Story
The service loads a base model and one or more adapters. A request selects an adapter, scheduler batching respects adapter constraints, model layers apply adapter deltas, and output should reflect only that adapter. When the request ends, KV/cache and request state must not be reusable under a different adapter unless the cache identity includes adapter context.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| adapter weights | load time | rarely | across requests | unload/process end | missing on one rank |
| adapter selection | request arrival | no | request lifetime | cleanup | wrong adapter applied |
| adapter-aware batch | scheduler step | per batch | no | step end | incompatible adapters batched |
| KV/prefix identity | prefill | cache growth | across requests | eviction | cache reused across adapters |
| output state | decode | token append | no | response end | cross-adapter contamination |

## Common Bug Stories
- Adapter load fails on one distributed worker.
- Base model response appears when adapter response was expected.
- Adapter A and adapter B contaminate each other's prefix cache.
- Same prompt with adapter A changes after running adapter B.

## Related Bugs
- No curated LoRA bug capsule exists yet.

## Fuzzer Strategy
- Seed shape: base prompt -> adapter A -> adapter B -> adapter A again -> recovery canary.
- Mutation axes: adapter order, concurrency, shared prefix, max tokens, adapter load/unload if supported.
- Oracle: deterministic adapter isolation and output consistency.
- Monitor: response text, adapter load logs, HTTP 5xx.
- Expected failure signals: wrong adapter output, load error, cross-request contamination.

## Verification Strategy
- Use adapters with clearly distinguishable deterministic outputs.
- Test single-request and mixed-adapter batch cases.
- For cache-sensitive tests, reuse exact prefix across adapters.
- Record exact adapter artifacts and load flags; current local evidence leaves them unknown.

## Evidence Sources
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)
- [GRIEF source tree](../../issue_capsule/grief_fuzzer_history/runs/2026-06-02_npu4_first_smoke/src/grief-BA95/)
- [KV cache deep dive](../theory_illustrations/KV_CACHE_DEEP_DIVE.md)

## Unknowns
- Official LoRA command adapted to local npu4.
- Local adapter artifacts.
- Known vLLM-Ascend LoRA issues and fixes.

