# Feature: Scheduler

## Mental Model
The scheduler is a per-step traffic controller. It decides which requests may spend token budget, KV blocks, backend time, and output-handler attention on each iteration.

## One-Request Story
A request arrives, gets tokenized, waits for admission, pre-fills enough prompt state, then enters the decode loop. On every scheduler step, the request either advances, waits for resources, finishes, fails, or gets cancelled. Cleanup must release scheduler state and KV references exactly once.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| waiting queue entry | request arrival | priority/admission | no | admission/cancel | request waits forever |
| running request | admission | every step | across decode | finish/fail/cancel | marked running without progress |
| prefill/decode budget | scheduler step | selection | no | end of step | long prefill starves decode |
| KV capacity view | cache manager query | allocation/free | across steps | process end | scheduler and cache disagree |
| output progress | first token | each emitted token | across stream | cleanup | output handler waits after request died |

## Common Bug Stories
- Long chunked prefill blocks a short canary.
- MTP full-decode-only mode hangs because proposer/graph state never advances.
- Recovery request fails after a toxic trace because cleanup did not fully run.
- Dynamic batching changes shape and exposes a hidden correctness bug.

## Related Bugs
- [FULL_DECODE_ONLY MTP hang](../../bug_wiki/bug_capsules/VA-BUG-4986-MTP-FULL-DECODE-HANG.md)
- [Chunk prefill long-sequence bug](../../bug_wiki/bug_capsules/VA-BUG-5445-CHUNK-PREFILL-LONG-SEQUENCE.md)
- [KV load failure metrics exception](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md)

## Fuzzer Strategy
- Seed shape: baseline canary -> mixed short/long burst -> toxic long/chunked/MTP request -> strict-timeout recovery canary.
- Mutation axes: prompt length, max tokens, concurrency, chunked prefill, graph mode, MTP/speculative mode.
- Oracle: no hung request, recovery canary succeeds, no scheduler/proposer traceback.
- Monitor: HTTP timeout, logs, latency, `/metrics` if exposed.
- Expected failure signals: timeout, starvation, 500, recovery failure.

## Verification Strategy
- Always compare before-toxic and after-toxic canaries.
- Record concurrency and prompt length, not only model name.
- For graph/dynamic batch issues, test single request versus mixed batch.
- For hang bugs, preserve logs from before shutdown; the lack of response is not enough.

## Evidence Sources
- [Scheduler deep dive](../theory_illustrations/SCHEDULER_DEEP_DIVE.md)
- [Scheduler workload pattern](../../bug_wiki/workload_patterns/SCHEDULER.md)
- [Fuzzer playbooks](../theory_illustrations/FUZZER_PLAYBOOKS.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Exact queue metrics available in current npu4 service.
- Exact reproduction commands for #4986 and #5445.
- Release-specific scheduler internals.

