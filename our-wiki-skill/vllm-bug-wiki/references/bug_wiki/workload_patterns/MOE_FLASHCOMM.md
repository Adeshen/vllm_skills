# MoE / FlashComm

## Common Failure Symptoms
- Tensor dimension mismatch.
- Custom op registration/backend mismatch.
- Incorrect MoE output with healthy HTTP status.
- FlashComm/EAGLE/MTP path crashes or refuses startup.

## Issue/PR Examples
- [VA-BUG-7996](../bug_capsules/VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE.md): Qwen3.5 MoE + MTP + FLASHCOMM1 shape mismatch.
- [VA-BUG-8463](../bug_capsules/VA-BUG-8463-GPTOSS-MOE-OUTPUT-CORRECTNESS.md): GPT-OSS 120B MoE output correctness.

## Workload Trigger Axes
- MoE model family.
- FlashComm version.
- EAGLE/MTP/speculative decoding enabled.
- Activation type and fused/unquantized MLP path.
- Model size and distributed topology.

## Useful Fuzzer Seed Shapes
- Single deterministic smoke request after MoE/FlashComm service startup.
- Repeated short requests to exercise proposer state.
- Differential canary against non-FlashComm or reference backend when possible.

## Useful Oracle/Monitor Design
- Shape-mismatch traceback detector.
- HTTP 5xx and service liveness.
- Deterministic output/reference comparator.
- Acceptance-rate monitor for EAGLE/MTP.

## Evidence Still Missing
- Exact model paths for Qwen3.5-35B and GPT-OSS 120B.
- Startup commands and runtime flags.
- Reference outputs for correctness cases.

