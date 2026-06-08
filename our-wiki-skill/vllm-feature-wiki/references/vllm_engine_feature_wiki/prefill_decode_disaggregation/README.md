# Feature: Prefill/Decode Disaggregation

## Mental Model
PD disaggregation separates prompt work from decode work. The prefiller creates KV state; the decoder consumes it. The connector is the contract between those two worlds.

## One-Request Story
The request is routed to a prefill instance, which computes prompt KV blocks. A connector such as Mooncake, TCP, store, or KV pool transfer moves block metadata and KV bytes to the decode instance. The decoder loads those blocks and generates output. If transfer fails, both sides must mark the request and blocks consistently.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| prefill request state | proxy/prefill admission | prompt progress | no | cleanup | producer thinks done too early |
| produced KV blocks | prefill | transfer status | maybe cached | cleanup/eviction | partial or invalid block visible |
| connector metadata | transfer scheduled | success/failure | no | connector cleanup | producer/consumer disagree |
| decode request state | decode admission | token generation | no | cleanup | decode waits for failed transfer |
| proxy response state | client route | status/body | no | response end | silent close instead of explicit error |

## Common Bug Stories
- KV transfer failure causes metrics exception and internal server error.
- Layerwise KV pool mode works differently from normal transfer mode.
- Proxy hides downstream sequence-length or transfer error.
- Decode side keeps waiting after prefill side has failed.

## Related Bugs
- [KV load failure metrics exception](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md)
- [Layerwise KV pool pooling abnormal](../../bug_wiki/bug_capsules/VA-BUG-6273-KVPOOL-LAYERWISE-POOLING.md)

## Fuzzer Strategy
- Seed shape: PD health canary -> normal transfer -> induced/approximated transfer failure -> `/metrics` scrape -> recovery canary.
- Mutation axes: prompt length, connector type, layerwise mode, timeout, streaming/proxy path.
- Oracle: explicit error propagation, metrics endpoint survives, recovery succeeds.
- Monitor: producer logs, consumer logs, proxy logs, `/metrics`, KV event traces.
- Expected failure signals: 500, silent close, invalid block, stale transfer state.

## Verification Strategy
- Test transfer success and failure paths separately.
- Preserve connector type and topology.
- After transfer failure, verify both producer and consumer cleanup.
- Do not call a derived PR image an official fixed image.

## Evidence Sources
- [PD/Mooncake deep dive](../theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md)
- [Distributed/PD workload pattern](../../bug_wiki/workload_patterns/DISTRIBUTED_PD.md)
- [KV cache workload pattern](../../bug_wiki/workload_patterns/KV_CACHE.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Exact PD topology commands.
- Fault-injection method for Mooncake failures.
- Before/after transfer traces.

