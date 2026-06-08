# Feature: Quantization

## Mental Model
Quantization changes how weights and activations are represented and which backend kernels/modules execute. The danger is a healthy server returning degraded or garbled text because the wrong low-precision path ran.

## One-Request Story
At startup, the engine reads quantization metadata and maps model layers to quantized modules or kernels. During inference, those modules produce hidden states and logits. Sampling may look normal even if quantized execution is wrong, so verification needs a reference output or invariant.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| quant config | model load | rarely | process lifetime | process end | unsupported mode accepted |
| packed module mapping | model load | rarely | all requests | process end | model family missing |
| quant kernel state | backend init | graph/capture | across requests | process end | dtype/shape mismatch |
| output reference | test setup | no | test oracle | no | missing oracle hides bug |
| HBM capacity | startup | request/cache pressure | across requests | shutdown | quant mode changes capacity assumptions |

## Common Bug Stories
- W8A8 Qwen3 dense model uses wrong packed module mapping and emits garbled text.
- FP8 model fails before serving because the current backend/image does not support it.
- Quantized model works in Transformers but not vLLM-Ascend.
- Batch shape or graph mode changes quantized correctness.

## Related Bugs
- [W8A8 per-token Qwen3 garbled output](../../bug_wiki/bug_capsules/VA-BUG-2318-W8A8-QWEN3-GARBLED.md)
- [GPT-OSS MoE output correctness](../../bug_wiki/bug_capsules/VA-BUG-8463-GPTOSS-MOE-OUTPUT-CORRECTNESS.md)

## Fuzzer Strategy
- Seed shape: reference prompt -> quantized model prompt -> same prompt in mixed batch -> cache-warmed repeat.
- Mutation axes: quantization mode, model family, batch shape, prompt type, max tokens.
- Oracle: reference comparison, exact copy/factual prompt, garbled-text heuristic as weak signal.
- Monitor: response text, startup logs, kernel errors.
- Expected failure signals: garbled output, unsupported quantization error, reference mismatch.

## Verification Strategy
- Define the reference before claiming a correctness bug.
- Record model family, quantization mode, image, and backend flags.
- Treat startup failure separately from request-triggered output failure.
- Use `/mnt/data2/model_weights` for any new local model path.

## Evidence Sources
- [Quant/MoE deep dive](../theory_illustrations/QUANT_MOE_DEEP_DIVE.md)
- [Quantization workload pattern](../../bug_wiki/workload_patterns/QUANTIZATION.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Exact W8A8 Qwen3 artifact and reference prompt.
- Official fixed image for PR #7248.
- CANN/kernel compatibility per quantization mode.

