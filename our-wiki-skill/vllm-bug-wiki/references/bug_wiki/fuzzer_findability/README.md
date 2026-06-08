# Fuzzer Findability

Primary source: [VLLM_BUG_PATTERN_TO_FUZZER_FINDABILITY.md](../../issue_capsule/project_docs/VLLM_BUG_PATTERN_TO_FUZZER_FINDABILITY.md). Smoke evidence: [GRIEF first smoke report](../../issue_capsule/grief_fuzzer_history/runs/2026-06-02_npu4_first_smoke/report.md).

## Current GRIEF Baseline

- Target service: `http://127.0.0.1:8000`.
- Served model in smoke: `Qwen3-1.7B-W4A8-V1`.
- Smoke image/container: `quay.io/ascend/vllm-ascend:v0.18.0rc1`.
- Seeds validated: short deterministic, shared-prefix two request, mixed prompt length, streaming.
- Fuzzer command used `--mock-monitor` because the default monitor expects NVIDIA NVML.
- Result: 10 iterations completed with no findings.

## Likely Findable With Current Style

- Scheduler hangs and liveness failures, if the target service mode is already configured.
- Streaming/cancel/disconnect lifecycle bugs after adding cancel/disconnect seeds.
- KV/prefix cache anomalies with shared-prefix traces, especially if KV events or metrics are enabled.
- Crash or HTTP 5xx paths in sampling, structured output, and long-context workloads.

## Seed-Dependent Or Environment-Dependent

- PD/Mooncake/KV transfer bugs require a PD topology and often fault injection.
- MoE/FlashComm/MTP bugs require exact model/backend flags.
- EAGLE repeated-call bugs need EAGLE service setup and enough iterations.
- HBM/multi-instance bugs require lifecycle harness outside plain HTTP trace mutation.

## Oracle-Dependent

- Output correctness regressions such as GPT-OSS wrong answer and Qwen3 quantized garbling need reference outputs or differential comparison.
- Rejection-sampling block verify needs accepted-token or baseline comparison oracle.
- Structured output needs schema validation, not just HTTP success.

## Not Good GRIEF Targets

- CPU binding locale failures.
- Eval dependency mismatch such as `prompt_token_ids`.
- CPU CI fixture/API mismatches.
- Startup/build failures before a healthy server exists.

