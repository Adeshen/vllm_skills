# Feature: Ascend Backend

## Mental Model
The Ascend backend is the hardware-and-runtime contract under vLLM. If this state machine is unhealthy, request-level symptoms are misleading.

## One-Request Story
The container exposes NPU devices, CANN environment is sourced, vLLM and torch-npu import, model weights load from `/mnt/data2/model_weights`, custom ops/graph/quantization initialize, `/v1/models` responds, and then a tiny request proves model execution. Every advanced feature sits on top of this ladder.

## State Ledger
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
| device visibility | container start | no | process lifetime | container end | missing `/dev/davinci*` mapping |
| CANN/torch-npu runtime | shell/import | no | process lifetime | process end | incompatible package/env |
| CPU binding | worker startup | placement | process lifetime | shutdown | locale parser failure |
| custom op/graph state | backend init | graph capture | across requests | process end | unsupported dynamic shape |
| HBM allocation | model/KV init | request growth | across requests | cleanup | leak or false OOM |
| quant/model support | model load | no | all requests | process end | unsupported mode or wrong mapping |

## Common Bug Stories
- Container cannot see NPU devices and vLLM errors distract from the real cause.
- CPU binding fails under Chinese OS language.
- Multi-instance service leaves HBM allocated.
- MoE/FlashComm/custom op receives wrong shape.
- Quantized model starts but returns wrong output.

## Related Bugs
- [CPU binding locale failure](../../bug_wiki/bug_capsules/VA-BUG-6992-CPU-BINDING-LOCALE.md)
- [Single-card multi-service HBM](../../bug_wiki/bug_capsules/VA-BUG-7308-MULTI-INSTANCE-HBM.md)
- [Qwen3.5 MoE MTP FlashComm shape mismatch](../../bug_wiki/bug_capsules/VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE.md)
- [W8A8 Qwen3 garbled output](../../bug_wiki/bug_capsules/VA-BUG-2318-W8A8-QWEN3-GARBLED.md)

## Fuzzer Strategy
- Seed shape: backend smoke ladder -> feature trace -> `/metrics`/HBM check -> recovery canary.
- Mutation axes: model family, quantization, graph, visible device IDs, multi-instance count, CPU locale.
- Oracle: health endpoints, tiny generation, HBM baseline, no backend traceback.
- Monitor: `npu-smi`, logs, `/v1/models`, `/metrics`.
- Expected failure signals: device-count error, import/custom op error, OOM, graph error, garbled output.

## Verification Strategy
- Climb the ladder: host `npu-smi`, container `npu-smi`, import smoke, `/v1/models`, tiny generation, feature test.
- Mirror actual NPU IDs; do not assume `/dev/davinci0-3`.
- Use `--mock-monitor` for GRIEF on Ascend unless an NPU-aware monitor is configured.
- Keep startup failures separate from request-triggered bugs.

## Evidence Sources
- [Ascend backend deep dive](../theory_illustrations/ASCEND_BACKEND_DEEP_DIVE.md)
- [CI and environment](../../bug_wiki/ci_and_environment/README.md)
- [NPU4 startup method](../../issue_capsule/project_docs/NPU4_ASCEND_CONTAINER_STARTUP_METHOD.md)
- [Official feature coverage](../OFFICIAL_FEATURE_COVERAGE.md)

## Unknowns
- Full CANN version matrix per release image.
- Source labels for Quay image commits.
- Backend kernel coverage by model family and quantization mode.

