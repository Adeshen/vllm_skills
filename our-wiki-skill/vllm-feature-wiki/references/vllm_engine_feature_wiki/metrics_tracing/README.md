# Feature: Metrics And Tracing

## Mental Model
Metrics and traces are the engine's memory of what happened. They must be safe on the success path and the failure path. A metrics bug can turn a real engine failure into a second, noisier failure.

## One-Request Story
As a request moves through scheduling, prefill, decode, transfer, sampling, streaming, and cleanup, metrics counters and traces are updated. On error paths, labels and counters should describe failure without dereferencing impossible state. After a toxic trace, `/metrics` should still scrape successfully.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| request metrics | request start | latency/status/token updates | scrape | process end | missing or contradictory labels |
| failure labels | error path | once per failure | scrape | process end | refer to invalid object |
| KV/transfer metrics | transfer operation | success/failure | scrape | process end | metrics path sees invalid block |
| trace span | request/operation | annotations/events | trace backend | span end | missing link across roles |
| log correlation | runtime | every event | external analysis | log rotation | wrong root cause hidden |

## Common Bug Stories
- KV load failure path triggers metrics exception.
- Observability hides whether failure came from producer, connector, decoder, or proxy.
- `/metrics` fails after the toxic trace and blocks automated monitoring.
- NPU monitor assumes NVIDIA NVML unless GRIEF uses mock monitor.

## Related Bugs
- [KV load failure metrics exception](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md)

## Fuzzer Strategy
- Seed shape: control canary -> toxic failure-path request -> immediate `/metrics` scrape -> recovery canary.
- Mutation axes: connector failure, long prompt, streaming/proxy path, concurrency.
- Oracle: metrics endpoint succeeds and failure remains client-visible.
- Monitor: `/metrics`, logs, trace backend if configured.
- Expected failure signals: metrics exception, 500, missing recovery, invisible root cause.

## Verification Strategy
- Treat `/metrics` as part of the oracle for failure-path bugs.
- Capture logs around the original error and any metrics error.
- For distributed cases, keep producer/consumer/proxy logs separate.
- Do not infer trace availability unless a trace backend is configured.

## Evidence Sources
- [#7871 capsule](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md)
- [Fuzzer findability](../../bug_wiki/fuzzer_findability/README.md)
- [GRIEF first smoke report](../../issue_capsule/grief_fuzzer_history/runs/2026-06-02_npu4_first_smoke/report.md)
- [PD/Mooncake deep dive](../theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md)

## Unknowns
- Exact metrics names for KV transfer failure.
- Trace configuration for current npu4 service.
- Before/after metrics output for PR #8959.

