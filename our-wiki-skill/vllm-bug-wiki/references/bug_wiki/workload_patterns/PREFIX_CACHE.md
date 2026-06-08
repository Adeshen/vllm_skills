# Prefix Cache

## Common Failure Symptoms
- Wrong cache hit or miss at token/block boundaries.
- Latency regression where shared-prefix requests do not benefit from caching.
- Output drift after warm/probe requests.
- Cache or memory not returning to baseline after workload drain.

## Issue/PR Examples
- No initial capsule is a pure prefix-cache correctness bug, but KV/cache cases such as [VA-BUG-7871](../bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md) and [VA-BUG-5445](../bug_capsules/VA-BUG-5445-CHUNK-PREFILL-LONG-SEQUENCE.md) share cache-adjacent trigger axes.
- `ENV_CONSTRAINTS.md` records Qwen3.5-9B prefix-cache probe/benchmark as feasible with exact token/LCP control.

## Workload Trigger Axes
- Shared prefix length and longest common prefix.
- Token boundary and KV block boundary alignment.
- Chunked prefill on/off.
- Warm/probe/recovery ordering.
- Batch shape with one shared-prefix group and one unrelated canary.

## Useful Fuzzer Seed Shapes
- Two deterministic requests with identical prefix and different suffixes.
- Warm request, repeated probe request, then changed-prefix canary.
- Boundary sweep around 1024-token and KV block multiples.

## Useful Oracle/Monitor Design
- Deterministic output comparison with `temperature=0`.
- Cache-hit proxy from latency or KV events.
- Final KV/cache baseline delta.
- Recovery canary after cache pressure.

## Evidence Still Missing
- Initial bug capsules for specific prefix-cache issues.
- Exact npu4 prefix-cache trace with KV events enabled.
- Strong output-drift oracle beyond text comparison.

