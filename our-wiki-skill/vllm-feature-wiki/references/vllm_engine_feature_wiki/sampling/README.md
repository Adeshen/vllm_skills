# Feature: Sampling

## Mental Model
Sampling is the boundary where internal logits become user-visible tokens. It is also where structured output, stop conditions, batch invariance, and speculative verification can silently change correctness.

## One-Request Story
After attention/model execution produces logits, sampling applies processors, constraints, grammar masks, and token selection. The chosen token mutates output state and extends future KV state. If structured output is enabled, grammar state also advances. If speculative decoding is enabled, sampling may verify draft tokens before committing them.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| sampling params | request arrival | rarely | no | cleanup | unsupported or conflicting settings |
| logits/bitmask | each decode step | processors/grammar | no | step end | type or shape mismatch |
| output tokens | accepted token | append/finish | stream chunks | response end | wrong token accepted |
| grammar state | structured request | each token | across decode | cleanup | schema state desync |
| batch context | scheduler step | per batch | no | step end | batch invariance failure |

## Common Bug Stories
- xgrammar bitmask function receives an incompatible type.
- Rejection sampling accepts/rejects with wrong index math.
- Same deterministic prompt changes when batched with another request.
- Quantized or MoE backend feeds wrong logits into an otherwise healthy sampler.

## Related Bugs
- [Block verify rejection sampling correctness](../../bug_wiki/bug_capsules/VA-BUG-7807-BLOCK-VERIFY-REJECTION-SAMPLING.md)
- [xgrammar type mismatch](../../bug_wiki/bug_capsules/VA-BUG-5524-XGRAMMAR-TYPE-MISMATCH.md)
- [W8A8 Qwen3 garbled output](../../bug_wiki/bug_capsules/VA-BUG-2318-W8A8-QWEN3-GARBLED.md)

## Fuzzer Strategy
- Seed shape: deterministic baseline -> feature-enabled request -> same request inside mixed batch -> recovery.
- Mutation axes: temperature, max tokens, stop tokens, schema shape, batch shape, speculative on/off.
- Oracle: exact output, schema validation, batch invariance, no 5xx.
- Monitor: response body, logs, token counts, validator result.
- Expected failure signals: wrong output, TypeError, schema violation, output drift.

## Verification Strategy
- Always name the reference for correctness: non-spec baseline, fixed image, Transformers, or expected schema.
- Use `temperature=0` for deterministic checks.
- Validate structured output mechanically.
- Preserve request JSON; sampling bugs are often parameter-sensitive.

## Evidence Sources
- [Sampling and speculative deep dive](../theory_illustrations/SAMPLING_AND_SPEC_DEEP_DIVE.md)
- [Sampling correctness workload pattern](../../bug_wiki/workload_patterns/SAMPLING_CORRECTNESS.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Exact structured-output request bodies from cached issues.
- Token-level oracle availability in GRIEF.
- Active sampler backend in each release/image.

