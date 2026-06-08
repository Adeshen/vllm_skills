---
name: benchmark-vllm-ascend
description: Run benchmark and pressure-testing workflows for remote vLLM Ascend services on npu4. Use when Codex needs to sync benchmark scripts to /mnt/data/vllm_observe, prepare prompt or dataset inputs, execute EvalScope pressure tests, record KV cache metrics, and summarize benchmark artifacts or runtime failures.
---

# Benchmark vLLM Ascend

Benchmark remote vLLM services through the existing `vllm_observe` toolchain. Sync assets first, run the benchmark with explicit parameters, and classify failures by startup, runtime, or workload behavior.

## Workflow

1. Verify the target service.
Confirm the service port, served model name, and that `/v1/models` responds before starting a load run.

2. Sync the benchmark assets.
Push the current repo scripts or datasets to `npu4` before assuming the remote copy is up to date.

3. Choose prompt source explicitly.
Use either `PROMPT_FILE`, `PROMPT_TEXT`, or `DATASET_PATH`. For long-context cases, verify token length before load.

4. Run the benchmark through the existing entrypoint.
Prefer `run_evalscope_with_kv_record.sh` over ad hoc hand-written commands.

5. Collect and summarize the artifacts.
Always report the EvalScope log, outputs directory, KV CSV, KV log, and any peak KV summary.

## Standard Checks

- `ssh npu4 'curl -sS http://127.0.0.1:<port>/v1/models'`
- `ssh npu4 'ls -R /mnt/data/vllm_observe/scripts | sed -n "1,80p"'`
- `ssh npu4 'python3 /mnt/data/vllm_observe/scripts/record_kv_cache_usage.py --help >/dev/null'`

## Preferred Execution Path

Use the sync and run patterns in [references/benchmark-workflow.md](references/benchmark-workflow.md).

Prefer these explicit environment variables:

- `BASE_URL`
- `MODEL`
- `PARALLEL`
- `NUMBER`
- `MAX_TOKENS`
- `PROMPT_FILE` or `DATASET_PATH`
- `OUTPUT_ROOT`
- `SCRIPT_ROOT`

If `OUTPUT_ROOT` changes, set `SCRIPT_ROOT` explicitly unless it truly lives under the same root.

## Failure Classification

Classify the result before proposing follow-up work:

- Startup failure: service never reached a healthy `/v1/models`.
- Runtime engine failure: `EngineDeadError`, worker crash, connection reset, or all requests returning `500`.
- Workload failure: timeouts, poor throughput, queueing, or incomplete runs without engine death.
- Benchmark plumbing failure: missing scripts, bad dataset path, or recorder setup problems.

## Reporting

Summaries should include:

- concurrency
- total / success / failed requests
- TTFT and TPOT when present
- peak and final KV cache usage
- exact artifact paths
- whether the run hit a model bug, system bug, or benchmark setup issue
