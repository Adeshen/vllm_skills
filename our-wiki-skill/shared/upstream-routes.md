# Upstream Skill Routes For Wiki Skills

Use this routing map when the bug wiki or feature wiki needs to connect a theory page, bug capsule, verification route, fuzzer seed, or workload family to the broader skill corpus.

## Evidence Boundary

- Upstream skills are process references unless a local run records evidence.
- KernelWiki is a wiki-construction model, not vLLM fact evidence.
- Generic vLLM skills are verification routes, not proof of Ascend behavior.
- NVIDIA, NCU, FlagOS, and AI Research skills are useful for taxonomy and workflow shape; backend facts must come from local evidence or primary upstream docs/code.
- Supplemental blogs/Zhihu can explain intuition but cannot prove version, compatibility, or reproduction results.

## Feature And Bug Route Map

| Wiki topic | Useful upstream route | Use it for | Do not use it for |
| --- | --- | --- | --- |
| Scheduler / continuous batching | `vllm-skills__vllm-bench-random-synthetic`, `hpc-ai-research__serving-llms-vllm` | Load shape, TTFT/TPOT, queueing vocabulary | Claiming a specific Ascend scheduler bug. |
| KV cache / prefix cache | `vllm-skills__vllm-prefix-cache-bench` | Shared-prefix workload and cache hit/miss seed design | Filling observed cache metrics without local artifacts. |
| Attention / FlashAttention / long context | `hpc-ai-research__optimizing-attention-flash`, `hpc-ai-research__long-context` | Theory narrative and mutation axes | Claiming kernel support on Ascend. |
| Sampling / structured output | `hpc-ai-research__outlines`, `hpc-ai-research__guidance` | Oracle and constrained decoding ideas | Replacing local correctness tests. |
| Speculative decoding | `hpc-ai-research__speculative-decoding` | Draft/target state model and verification axes | Claiming current vLLM-Ascend support. |
| Quantization | `hpc-ai-research__awq-quantization`, `hpc-ai-research__gptq`, `hpc-ai-research__hqq-quantization` | Quantization taxonomy and oracle planning | Backend kernel compatibility claims. |
| MoE / expert parallel | `hpc-nvidia__nemo-mbridge-perf-moe-optimization-workflow` | MoE state axes and communication vocabulary | FlashComm bug evidence. |
| Distributed / PD / Mooncake | `hpc-nvidia__nemo-mbridge-perf-parallelism-strategies`, `hpc-ai-research__serving-llms-vllm` | Topology and matrix design | Local connector behavior without evidence. |
| Kernel/operator bottlenecks | `hpc-ncu__ncu-report-skill`, `hpc-flagos__kernelgen-flagos` | Evidence-backed profiling/report pattern | CUDA metrics as Ascend metrics. |
| Evaluation / regression gate | `hpc-ai-research__nemo-evaluator-sdk`, `hpc-nvidia__nemo-evaluator-plugin` | Evaluation matrix and quality gate wording | Reproduction result without local issue trigger. |

## Citation Form

When adding a wiki note, phrase upstream connections as:

```text
Upstream planning route: <skill>
Reason: <what workflow/theory it contributes>
Evidence status: planning/reference only until local artifacts exist
```
