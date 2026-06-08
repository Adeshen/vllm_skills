# Feature: Streaming

## Mental Model
Streaming keeps a request alive while partial outputs leave the engine. It is a lifecycle feature as much as an output feature: client connection, scheduler state, KV references, and output handler must agree.

## One-Request Story
A streaming request is admitted like a normal request, but each token is emitted as a chunk. If the client disconnects, the HTTP layer must signal cancellation, the scheduler must stop work, the output handler must stop writing, and KV/cache state must be released. A recovery canary proves cleanup worked.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| stream object | API accepts stream | chunk emission | no | finish/cancel | writes after close |
| client connection | HTTP setup | chunks/disconnect | no | disconnect/end | engine keeps generating |
| request status | scheduler admission | running/finished/cancelled | across steps | cleanup | scheduler misses cancel |
| KV refs | prefill/decode | decode extension | across stream | cleanup | cancelled stream leaks blocks |
| output metrics | request start | chunks/errors | scrape | process end | error path double-counts or throws |

## Common Bug Stories
- Disconnect before first token leaves scheduler waiting.
- Cancel after first token leaks KV or output state.
- Proxy stream closes silently while backend still runs.
- Recovery request fails because cancelled stream left global state dirty.

## Related Bugs
- No pure streaming capsule exists yet.
- Adjacent future targets live in [lifecycle/cancel workload pattern](../../bug_wiki/workload_patterns/LIFECYCLE_CANCEL.md).

## Fuzzer Strategy
- Seed shape: streaming control -> disconnect before first token -> disconnect after first token -> cancel long stream -> recovery canary.
- Mutation axes: disconnect timing, max tokens, prompt length, retry delay, concurrency, proxy/PD mode.
- Oracle: no post-cancel tokens, no output-handler 5xx, recovery canary succeeds.
- Monitor: stream chunks, HTTP status, logs, request counters if available.
- Expected failure signals: hung stream, output handler traceback, leaked request state.

## Verification Strategy
- Test both before-first-token and after-first-token disconnect.
- Always send a non-streaming canary afterward.
- If proxy/PD is involved, inspect proxy and backend logs separately.
- Record whether the failure is client-visible or only in logs.

## Evidence Sources
- [Streaming lifecycle deep dive](../theory_illustrations/STREAMING_LIFECYCLE_DEEP_DIVE.md)
- [Lifecycle/cancel workload pattern](../../bug_wiki/workload_patterns/LIFECYCLE_CANCEL.md)
- [GRIEF first smoke report](../../issue_capsule/grief_fuzzer_history/runs/2026-06-02_npu4_first_smoke/report.md)

## Unknowns
- vLLM-Ascend-specific cancel/disconnect bug capsules.
- Current GRIEF support for true disconnect/cancel.
- Request-state metrics exposed by current service.

