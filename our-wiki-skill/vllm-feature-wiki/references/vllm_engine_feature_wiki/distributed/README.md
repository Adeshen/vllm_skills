# Feature: Distributed

## Mental Model
Distributed serving splits engine state across processes, devices, nodes, or roles. A distributed bug is often a disagreement: one rank thinks work is done, another waits, a connector failed, or a proxy did not translate the failure.

## One-Request Story
A request may enter through a proxy, land on a coordinator, fan out across tensor/pipeline/data/expert-parallel ranks, and possibly cross prefill/decode roles. Each rank mutates local request, KV, and backend state. The response is correct only if all ranks and roles agree on progress, failure, and cleanup.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| process/rank group | startup | health/failure | process lifetime | shutdown | one rank fails silently |
| CPU/NPU placement | startup | no | process lifetime | shutdown | locale/device mapping mismatch |
| connector/proxy state | distributed setup | request routing | across requests | shutdown | proxy closes without useful error |
| distributed KV state | prefill/transfer | success/failure | across roles | cleanup | producer/consumer disagree |
| topology config | launch | no | process lifetime | shutdown | request shape incompatible with topology |

## Common Bug Stories
- CPU binding fails because localized output breaks parsing.
- PD/Mooncake transfer failure reaches one role but not the other.
- Proxy closes an overlength or failed request without a clear client-visible error.
- Multi-node/parallel startup fails before healthy serving.

## Related Bugs
- [CPU binding locale failure](../../bug_wiki/bug_capsules/VA-BUG-6992-CPU-BINDING-LOCALE.md)
- [KV load failure metrics exception](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md)
- [KV pool layerwise pooling abnormal](../../bug_wiki/bug_capsules/VA-BUG-6273-KVPOOL-LAYERWISE-POOLING.md)

## Fuzzer Strategy
- Seed shape: distributed canary -> toxic transfer/proxy request -> per-role health check -> recovery canary.
- Mutation axes: topology, connector type, prompt length, streaming, failure/retry timing.
- Oracle: explicit client-visible error, recovery success, no stuck ranks.
- Monitor: per-role logs, proxy response, `/metrics`, NPU health.
- Expected failure signals: hang, 500, silent close, stale transfer state, rank death.

## Verification Strategy
- Record topology and role mapping with every distributed capsule.
- Inspect producer, consumer, and proxy logs separately.
- Verify both pre-toxic and post-toxic canaries.
- For CPU binding, run locale-controlled unit tests rather than HTTP fuzzing.

## Evidence Sources
- [PD/Mooncake deep dive](../theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md)
- [Distributed/PD workload pattern](../../bug_wiki/workload_patterns/DISTRIBUTED_PD.md)
- [NPU4 startup method](../../issue_capsule/project_docs/NPU4_ASCEND_CONTAINER_STARTUP_METHOD.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Exact distributed commands for initial capsules.
- Stable connector modes on current image.
- Per-rank tracing configuration.

