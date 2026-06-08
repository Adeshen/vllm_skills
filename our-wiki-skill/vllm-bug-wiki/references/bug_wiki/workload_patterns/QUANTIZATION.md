# Quantization

## Common Failure Symptoms
- Garbled output with quantized model where reference backend is coherent.
- Startup rejection for unsupported quantization mode.
- Wrong packed module mapping.
- Model family-specific quantization config mismatch.

## Issue/PR Examples
- [VA-BUG-2318](../bug_capsules/VA-BUG-2318-W8A8-QWEN3-GARBLED.md): W8A8 per-token Qwen3 garbled output, PR #7248 open.
- [VA-BUG-8463](../bug_capsules/VA-BUG-8463-GPTOSS-MOE-OUTPUT-CORRECTNESS.md): MoE correctness may overlap quant/model execution path.
- `ENV_CONSTRAINTS.md` marks direct FP8 Qwen3.5-35B-A3B startup on stock v0.18.0rc1 as forbidden in baseline.

## Workload Trigger Axes
- Quantization mode: W4A8, W8A8, FP8.
- Dense versus MoE model mapping.
- Model family, especially Qwen3/GLM/GPT-OSS.
- Deterministic prompt with known reference.

## Useful Fuzzer Seed Shapes
- Temperature-zero factual/copy prompts.
- Same prompt against quantized and unquantized/reference backend.
- Short prompt, long prompt, and repeated-call variants.

## Useful Oracle/Monitor Design
- Reference output comparison.
- Text corruption heuristic as weak oracle.
- Token-level/logprob comparison when available.
- Startup unsupported-quantization detector.

## Evidence Still Missing
- Exact W8A8 Qwen3 model path and reference prompt.
- Before/after output samples for PR #7248.
- Clear official fixed release for open quantization PRs.

