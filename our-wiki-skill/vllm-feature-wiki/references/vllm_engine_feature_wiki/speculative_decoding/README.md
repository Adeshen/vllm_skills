# Feature: Speculative Decoding

## Mental Model
Speculative decoding is a promise-and-check loop. A draft path proposes tokens, the target path verifies them, accepted tokens are committed, and rejected tokens must leave no trace.

## One-Request Story
The request starts with normal prompt state. The proposer, such as MTP, EAGLE, or suffix speculative logic, drafts one or more tokens. Target verification scores those tokens, accepts a prefix, rejects the rest, commits accepted KV/output state, rolls back unaccepted state, and repeats until stop conditions.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| proposal tokens | proposer step | verify accepts/rejects | within request | after verification | rejected token persists |
| accepted-token count | verification | every spec step | across decode | cleanup | wrong output length/content |
| proposer state | request/model init | repeated calls | across steps | request/process end | stale EAGLE/MTP state |
| attention mask | verification step | dynamic shape | sometimes graph-captured | step end | index out of range |
| graph/backend state | feature init | shape capture | across requests | process end | full-decode/MTP hang |

## Common Bug Stories
- Block verify uses wrong `h_block` or index and commits incorrect tokens.
- MTP full-decode-only graph path hangs.
- EAGLE repeated calls corrupt attention-mask state.
- MoE/MTP/FlashComm combines speculative and expert state into a shape mismatch.

## Related Bugs
- [Block verify rejection sampling correctness](../../bug_wiki/bug_capsules/VA-BUG-7807-BLOCK-VERIFY-REJECTION-SAMPLING.md)
- [FULL_DECODE_ONLY MTP hang](../../bug_wiki/bug_capsules/VA-BUG-4986-MTP-FULL-DECODE-HANG.md)
- [EAGLE attention mask repeated-call error](../../bug_wiki/bug_capsules/VA-BUG-3024-EAGLE-ATTN-MASK-REPEATED-CALLS.md)
- [Qwen3.5 MoE MTP FlashComm shape mismatch](../../bug_wiki/bug_capsules/VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE.md)

## Fuzzer Strategy
- Seed shape: non-spec deterministic baseline -> spec-enabled same prompt -> repeated spec calls -> recovery canary.
- Mutation axes: draft length, max tokens, prompt length, method, graph mode, FlashComm/MoE on/off.
- Oracle: baseline equivalence where expected, accepted-token accounting, no hang, no shape traceback.
- Monitor: response text, logs, acceptance metrics if available.
- Expected failure signals: wrong output, attention-mask index error, hang, dimension mismatch.

## Verification Strategy
- Do not use `draft_model` as a neutral baseline on current v0.18.0rc1 evidence.
- Compare spec off/on for deterministic prompts.
- Preserve proposer method, graph flags, and model family.
- Use unit tests for rejection sampler math before service-scale reproduction.

## Evidence Sources
- [Sampling and speculative deep dive](../theory_illustrations/SAMPLING_AND_SPEC_DEEP_DIVE.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)
- [Sampling correctness pattern](../../bug_wiki/workload_patterns/SAMPLING_CORRECTNESS.md)

## Unknowns
- Exact suffix speculative command for local npu4.
- Acceptance metrics availability.
- Stable speculative method matrix by release image.

