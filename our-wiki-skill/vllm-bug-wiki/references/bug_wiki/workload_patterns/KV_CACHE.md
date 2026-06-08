# KV Cache

## Common Failure Symptoms
- KV transfer failure escalates to HTTP 500 or metrics exception.
- KV pool/layerwise transfer path returns abnormal output or fails.
- KV metadata changes break CPU/mock CI tests.
- Distributed startup can hit KV cache key errors under large topology.

## Issue/PR Examples
- [VA-BUG-7871](../bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md): KV load failure metrics exception, fixed by PR #8959.
- [VA-BUG-6273](../bug_capsules/VA-BUG-6273-KVPOOL-LAYERWISE-POOLING.md): pooling KV transfer abnormal with `use_layerwise=true`, PR #5168.
- [VA-BUG-CPUCI](../bug_capsules/VA-BUG-CPUCI-BLOCKSTORED-PARENT-HASH.md): CPU CI fixture missing `parent_block_hash`.

## Workload Trigger Axes
- PD or disaggregated serving topology.
- Mooncake/KV pool connector mode.
- Transfer failure, timeout, retry, or invalid block.
- Pooling endpoint versus chat/completion endpoint.
- Shared-prefix warm/probe/recovery traces.

## Useful Fuzzer Seed Shapes
- Control request -> induced transfer failure -> recovery canary.
- Shared-prefix two-request seed with deterministic output.
- Pooling request pair with layerwise disabled/enabled.
- Long-running KV pressure seed that measures post-run memory/cache state.

## Useful Oracle/Monitor Design
- HTTP 5xx and timeout.
- `/metrics` scrape must not fail.
- KV transfer log detector for invalid blocks, failed sends, failed loads.
- Optional KV event endpoint for block lifecycle validation.
- Recovery canary after any failed KV transfer.

## Evidence Still Missing
- Exact #7871 before/after command and logs.
- Patch-apply checks for release bases.
- KV event traces for the current npu4 service.
- CPU CI report artifact for `BlockStored.parent_block_hash`.

