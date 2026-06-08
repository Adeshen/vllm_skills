# Feature: MoE

## Mental Model
MoE turns one model step into a routing problem. Tokens choose experts, expert outputs are combined, and communication/custom kernels must agree on shape and activation semantics.

## One-Request Story
The request joins a batch, hidden states are routed to experts, fused MoE kernels or communication layers process those expert inputs, outputs are merged, logits are sampled, and the request continues. Large MoE models often combine this with distributed topology, quantization, FlashComm, MTP, or graph mode.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| expert routing | each forward | per token/batch | no | step end | wrong expert or shape |
| expert weights | model load | no | all requests | process end | missing/incorrect shard |
| fused MoE kernel state | backend init | shape/config | across requests | process end | activation enum or dtype mismatch |
| communication state | distributed init | per forward | process lifetime | shutdown | FlashComm shape mismatch |
| output reference | test setup | no | oracle | no | missing oracle hides wrong output |

## Common Bug Stories
- Qwen3.5 MoE + MTP + FlashComm gives tensor dimension mismatch.
- GPT-OSS MoE output is incorrect because fused MLP activation handling is wrong.
- Expert parallel/rank topology fails only at large scale.
- Quantized MoE combines model mapping and expert routing risks.

## Related Bugs
- [Qwen3.5 MoE MTP FlashComm shape mismatch](../../bug_wiki/bug_capsules/VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE.md)
- [GPT-OSS 120B MoE output correctness](../../bug_wiki/bug_capsules/VA-BUG-8463-GPTOSS-MOE-OUTPUT-CORRECTNESS.md)
- [W8A8 Qwen3 garbled output](../../bug_wiki/bug_capsules/VA-BUG-2318-W8A8-QWEN3-GARBLED.md)

## Fuzzer Strategy
- Seed shape: MoE smoke -> feature-enabled MoE/MTP/FlashComm request -> repeated or batched request -> recovery.
- Mutation axes: batch size, prompt length, MTP/FlashComm, quantization, topology.
- Oracle: no shape traceback, deterministic/reference output, liveness.
- Monitor: logs, response text, status, rank/backend errors.
- Expected failure signals: dimension mismatch, wrong output, engine death, rank failure.

## Verification Strategy
- Preserve exact model family and topology.
- For output correctness, capture a reference response.
- For shape failures, logs and stack traces are primary evidence.
- Separate startup/model-support failure from request-triggered MoE failure.

## Evidence Sources
- [Quant/MoE deep dive](../theory_illustrations/QUANT_MOE_DEEP_DIVE.md)
- [MoE/FlashComm workload pattern](../../bug_wiki/workload_patterns/MOE_FLASHCOMM.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Exact model paths under `/mnt/data2/model_weights`.
- Runtime flags used by #7996 and #8463.
- Reference outputs for MoE correctness cases.

