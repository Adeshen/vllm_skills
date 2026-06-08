# Upstream Skill Routes For Local Operator Skills

Use this file as a routing map from local vLLM/vLLM-Ascend operations to upstream skill references. These routes are companions, not evidence. A route becomes evidence only after a local run records commands, environment, logs, metrics, artifacts, and source/image revisions.

## Core Rules

- Preserve the current scene before disruptive operations.
- Use the most specific local skill first for npu4 and vLLM-Ascend work.
- Use upstream skills to borrow workflow shape, option vocabulary, profiler/eval structure, or benchmark strategy.
- Do not infer Ascend support from generic CUDA/vLLM/NVIDIA skills.
- New local model-path examples must use `/mnt/data2/model_weights`.

## Route Map

| Local task | Primary local skill | Useful upstream reference | Use it for | Evidence caveat |
| --- | --- | --- | --- | --- |
| Start or repair vLLM-Ascend Docker service | `run-vllm-ascend-docker` | `vllm-skills__vllm-deploy-docker`, `hpc-ai-research__serving-llms-vllm` | Serve flags, health checks, OpenAI API smoke shape | Generic vLLM flags may not be valid on Ascend. |
| Benchmark a running service | `benchmark-vllm-ascend` | `vllm-skills__vllm-bench-serve`, `vllm-skills__vllm-bench-random-synthetic` | TTFT/TPOT, request-rate, result JSON structure | Use local EvalScope/KV recorder when Ascend metrics are needed. |
| Prefix/KV cache workload | `benchmark-vllm-ascend` | `vllm-skills__vllm-prefix-cache-bench` | Shared-prefix seed shape and cache hit workload design | Cache support and metrics must be locally observed. |
| Slow/crash/hang incident | `vllm-ascend-incident-triage` | `hpc-nvidia__dynamo-troubleshoot`, `hpc-nvidia__dynamo-interconnect-check` | Diagnostics checklist and failure-domain thinking | Use only after read-only local baseline is preserved. |
| End-to-end traces | `collect-vllm-ascend-traces` | `hpc-ai-research__phoenix-observability`, `hpc-ai-research__langsmith-observability` | Observability vocabulary and trace/report structure | Local Jaeger/OTEL tunnel evidence is authoritative. |
| Kernel or operator profiling | local report skill plus explicit user request | `hpc-ncu__ncu-report-skill`, `hpc-flagos__kernelgen-flagos` | NCU report discipline, kernel bottleneck taxonomy, Triton/kernel route | NCU is CUDA-specific; Ascend operator evidence needs Ascend profiler/tooling. |
| Distributed/PD/Mooncake issue | `reproduce-vllm-ascend-issue` | `hpc-nvidia__nemo-mbridge-perf-parallelism-strategies`, `hpc-ai-research__serving-llms-vllm` | Distributed vocabulary and test matrix design | PD/Mooncake topology is local evidence only. |
| MoE/FlashComm issue | `reproduce-vllm-ascend-issue` | `hpc-nvidia__nemo-mbridge-perf-moe-optimization-workflow` | MoE axes and expert-parallel failure vocabulary | FlashComm behavior is Ascend-specific. |
| Quantization correctness/perf | `reproduce-vllm-ascend-issue` or `benchmark-vllm-ascend` | `hpc-ai-research__awq-quantization`, `hpc-ai-research__gptq`, `hpc-ai-research__hqq-quantization` | Quantization axes, oracle planning, report fields | Kernel/backend support must be proven locally. |
| Evaluation or quality gate | `record-vllm-ascend-report` | `hpc-ai-research__nemo-evaluator-sdk`, `hpc-nvidia__nemo-evaluator-plugin` | Eval matrix and result-format design | Eval does not prove reproduction unless tied to issue trigger. |

## Output Contract

When a local skill uses an upstream route, mention it as:

```text
Upstream route used for planning: <normalized skill name>
Local evidence collected: <commands/logs/metrics/artifacts>
Evidence boundary: <what remains unknown>
```
