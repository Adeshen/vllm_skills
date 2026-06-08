# CI And Environment

Sources:

- [NPU4_ASCEND_CONTAINER_STARTUP_METHOD.md](../../issue_capsule/project_docs/NPU4_ASCEND_CONTAINER_STARTUP_METHOD.md)
- [ENV_CONSTRAINTS.md](../../issue_capsule/ENV_CONSTRAINTS.md)
- [GRIEF first smoke report](../../issue_capsule/grief_fuzzer_history/runs/2026-06-02_npu4_first_smoke/report.md)
- Requested CPU CI report path: `/mnt/data/vllm_observe/vllm_ascend_cpu_ci_check/report_20260603/CPU_CI_FEASIBILITY_REPORT.md`

## npu4 Container Rules

Before debugging vLLM arguments, verify that the container can see Ascend devices. Healthy npu4 startup requires:

- `--ipc=host`
- `--network host`
- `--privileged`
- host-visible `/dev/davinci*` device IDs from `npu-smi info`
- `/dev/davinci_manager`
- `/dev/hisi_hdc`
- `/dev/devmm_svm`
- Ascend driver/tool mounts
- `/mnt/data2` model-weight mount

Observed healthy device IDs on 2026-06-02 were `2`, `3`, `6`, and `7`; do not assume `/dev/davinci0-3`.

## Model Path Rule

Use `/mnt/data2/model_weights` for new runs. Do not copy legacy model-volume paths from historical artifacts into new reproduction commands.

## Known Smoke Context

The GRIEF smoke used:

- Container: `vllm_qwen3`
- Image: `quay.io/ascend/vllm-ascend:v0.18.0rc1`
- Served model: `Qwen3-1.7B-W4A8-V1`
- Runtime versions: `vllm=0.18.0+empty`, `vllm-ascend=0.18.0rc1`, `torch=2.9.0+cpu`, `torch-npu=2.9.0.post1+gitee7ba04`
- Fuzzer monitor: `--mock-monitor`

## NPU Constraints

- Treat startup failures before `/v1/models` as environment/container/startup blockers, not request-triggered fuzzer findings.
- `draft_model` speculative decoding is not a stable default baseline on current Ascend `v0.18.0rc1`.
- Direct FP8 Qwen3.5-35B-A3B on stock `v0.18.0rc1` is forbidden as a baseline because startup fails before serving.
- DeepSeek-V4-Flash is forbidden as a generic baseline on stock `v0.18.0rc1`; use a custom build track if needed.

## CPU CI Feasibility

The prompt referenced `/mnt/data/vllm_observe/vllm_ascend_cpu_ci_check/report_20260603/CPU_CI_FEASIBILITY_REPORT.md`, but that file was not present locally during wiki construction. The CPU CI capsule records the reported failing test and keeps all missing fields unknown until the report is restored.
