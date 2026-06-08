# Feature: KV Cache

## Mental Model
KV cache is the engine's working memory for previous tokens. PagedAttention makes this memory block-based: requests own logical blocks that map to physical KV blocks, and those blocks can be reused, transferred, invalidated, or freed.

## One-Request Story
During prefill, the request allocates or reuses KV blocks. During decode, each accepted token extends the cache. If prefix caching is active, full blocks may become reusable for later requests. If PD disaggregation is active, blocks may cross a connector boundary. When the request ends, references must drop and blocks must either remain safely cached or return to the free pool.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| physical KV block | engine init | ownership/hash/ref count | reused by active/cache refs | eviction/shutdown | premature reuse or leak |
| block table | request allocation | sequence growth | across decode | request cleanup | points to wrong block |
| block hash | full cacheable block | reset on eviction | prefix lookup | eviction | false hit/miss |
| transfer metadata | PD/KV connector | success/failure | no | connector cleanup | producer/consumer disagree |
| metrics labels | failure/success paths | counters update | scrape | process end | metrics exception hides root error |

## Common Bug Stories
- Transfer-failed blocks are not invalidated before scheduler or metrics sees them.
- A fixture or serialized block misses required parent-block metadata.
- Layerwise KV pool transfer behaves differently from normal chat KV flow.
- HBM does not return after request or multi-instance cleanup.

## Related Bugs
- [KV load failure metrics exception](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md)
- [Layerwise KV pool pooling abnormal](../../bug_wiki/bug_capsules/VA-BUG-6273-KVPOOL-LAYERWISE-POOLING.md)
- [CPU CI BlockStored parent hash](../../bug_wiki/bug_capsules/VA-BUG-CPUCI-BLOCKSTORED-PARENT-HASH.md)
- [Single-card multi-service HBM](../../bug_wiki/bug_capsules/VA-BUG-7308-MULTI-INSTANCE-HBM.md)

## Fuzzer Strategy
- Seed shape: shared-prefix warm/probe/recovery or PD transfer-failure trace.
- Mutation axes: prefix length, block boundary, request count, connector type, transfer failure timing.
- Oracle: no 5xx, deterministic output stability, `/metrics` survives, final HBM/cache baseline acceptable.
- Monitor: KV logs, optional KV events, `/metrics`, recovery canary.
- Expected failure signals: invalid block logs, stale transfer state, cache leak, metrics exception.

## Verification Strategy
- For local NPU tests, keep model paths under `/mnt/data2/model_weights`.
- After any failure-path test, scrape `/metrics` and run a recovery canary.
- For cache reuse, compare warm/probe latency and deterministic output.
- For CI fixture failures, record exact class fields and dependency versions.

## Evidence Sources
- [KV cache deep dive](../theory_illustrations/KV_CACHE_DEEP_DIVE.md)
- [KV cache workload pattern](../../bug_wiki/workload_patterns/KV_CACHE.md)
- [PD/Mooncake deep dive](../theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Complete KV event configuration for current npu4 service.
- Release-specific KV block schema.
- Before/after logs for #7871.

