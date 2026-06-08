# Feature: Engine Lifecycle

## Mental Model
Engine lifecycle is the story of how a vLLM-Ascend process becomes a healthy server, stays healthy while features mutate state, and releases resources cleanly when it stops. Request fuzzing only makes sense after this state machine is healthy.

## One-Request Story
Before the first request, the container must see Ascend devices, source CANN runtime, import torch-npu and vLLM-Ascend, load weights from `/mnt/data2/model_weights`, initialize custom ops/graph/HBM, and pass `/v1/models`. A tiny deterministic request then proves the request path can allocate KV, run the backend, sample output, and clean up. Feature campaigns should always return to this canary after toxic traces.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| device mapping | container start | no | process lifetime | container end | container sees wrong NPU IDs |
| runtime env | shell/startup | no | process lifetime | process end | CANN or torch-npu import mismatch |
| model weights | service start | no | all requests | process end | stale or unsupported model path |
| graph/custom op state | backend init | graph capture | across requests | process end | dynamic shape violates captured path |
| HBM/KV memory | model and request init | every request | across requests | cleanup/shutdown | leak or over-allocation |
| readiness state | health endpoint | request failures update confidence | operationally reused | restart | server listens but cannot generate |

## Common Bug Stories
- Device visibility fails before any vLLM argument matters.
- CPU binding parses localized host output incorrectly.
- Graph mode or custom op captures a shape that later requests violate.
- Multi-instance serving leaves HBM allocated after one service exits.
- Unsupported quantization/model family fails during startup rather than request execution.

## Related Bugs
- [CPU binding locale failure](../../bug_wiki/bug_capsules/VA-BUG-6992-CPU-BINDING-LOCALE.md)
- [Single-card multi-service HBM](../../bug_wiki/bug_capsules/VA-BUG-7308-MULTI-INSTANCE-HBM.md)
- [W8A8 Qwen3 garbled output](../../bug_wiki/bug_capsules/VA-BUG-2318-W8A8-QWEN3-GARBLED.md)

## Fuzzer Strategy
- Seed shape: lifecycle harness -> `/v1/models` -> tiny canary -> feature-specific toxic trace -> recovery canary -> HBM check.
- Mutation axes: graph on/off, model family, quantization, visible devices, CPU locale, multi-instance count.
- Oracle: readiness, deterministic generation, no startup traceback, HBM near baseline.
- Monitor: `npu-smi`, server logs, `/metrics`, health endpoints.
- Expected failure signals: device-count failure, import/custom op error, OOM, graph error, recovery canary failure.

## Verification Strategy
- Verify host/container NPU visibility before model arguments.
- Verify `/v1/models` and one tiny generation before feature reproduction.
- Preserve exact image, vLLM/vLLM-Ascend, torch/torch-npu, and CANN context when available.
- After lifecycle tests, check for stale processes and HBM not returning to baseline.

## Evidence Sources
- [Ascend backend deep dive](../theory_illustrations/ASCEND_BACKEND_DEEP_DIVE.md)
- [NPU4 startup method](../../issue_capsule/project_docs/NPU4_ASCEND_CONTAINER_STARTUP_METHOD.md)
- [CI and environment](../../bug_wiki/ci_and_environment/README.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Exact Graph/Sleep/Netloader/RFork commands for local npu4.
- Which lifecycle features exist in each release image.
- Local sleep/wake and graph-mode bug capsules.

