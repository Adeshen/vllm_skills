# Sampling / Output Correctness

## Common Failure Symptoms
- Wrong speculative decoding/block verification.
- Garbled or semantically wrong output with HTTP 200.
- Structured output parser/type errors.
- Token acceptance or attention mask indexing errors.

## Issue/PR Examples
- [VA-BUG-7807](../bug_capsules/VA-BUG-7807-BLOCK-VERIFY-REJECTION-SAMPLING.md): rejection sampling block verify correctness.
- [VA-BUG-5524](../bug_capsules/VA-BUG-5524-XGRAMMAR-TYPE-MISMATCH.md): xgrammar structured output type mismatch.
- [VA-BUG-3024](../bug_capsules/VA-BUG-3024-EAGLE-ATTN-MASK-REPEATED-CALLS.md): repeated EAGLE attention mask index error.
- [VA-BUG-8463](../bug_capsules/VA-BUG-8463-GPTOSS-MOE-OUTPUT-CORRECTNESS.md): incorrect GPT-OSS output.

## Workload Trigger Axes
- Temperature zero versus stochastic sampling.
- Speculative/EAGLE/MTP enabled.
- Structured output schema.
- Repeated calls and high concurrency.
- Model-specific quantization or MoE path.

## Useful Fuzzer Seed Shapes
- Deterministic baseline request and feature-enabled request.
- Repeated 100+ request loop.
- JSON schema/guided decoding request.
- Output-copy task with strict expected text.

## Useful Oracle/Monitor Design
- Exact output comparison for deterministic prompts.
- Schema validator.
- Acceptance-rate and token-count checks.
- Traceback detector for index/type errors.

## Evidence Still Missing
- Reference outputs for correctness-only bugs.
- Token-level oracle implementation in GRIEF.
- Runtime flags for EAGLE/MTP cases.

