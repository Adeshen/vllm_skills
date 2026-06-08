# Official vLLM Skills Reference

This file connects the local feature-wiki skill to the official `vllm-project/vllm-skills` repository.

Source: https://github.com/vllm-project/vllm-skills

## What To Import Conceptually

Use official vLLM skills as companion execution workflows:

| Official skill | Use in feature wiki |
| --- | --- |
| `vllm-deploy-simple` | Generic local service readiness route for feature smoke tests. |
| `vllm-deploy-docker` | Docker deployment route when a feature needs service-level verification. |
| `vllm-deploy-k8s` | Kubernetes deployment route for production-stack or cluster-oriented feature notes. |
| `vllm-prefix-cache-bench` | Verification route for prefix cache, KV reuse, and shared-prefix performance stories. |
| `vllm-bench-random-synthetic` | Synthetic throughput/latency route for scheduler, batching, and output-token stress. |
| `vllm-bench-serve` | OpenAI-compatible endpoint benchmark route for service-level verification. |

## Boundary

- These skills are generic vLLM operational skills.
- They are not vLLM-Ascend evidence unless the local run, log, report, or capsule proves an Ascend execution.
- Use them to name a verification route, then adapt commands only from local Ascend evidence or explicit user instructions.
- Do not run deploy or benchmark skills during documentation-only wiki updates.

## Feature Mapping

| Local feature | Best official skill route | Notes |
| --- | --- | --- |
| scheduler | `vllm-bench-random-synthetic`, `vllm-bench-serve` | Useful for concurrency, throughput, TTFT/TPOT, and liveness planning. |
| kv_cache | `vllm-prefix-cache-bench`, `vllm-bench-serve` | Use for cache reuse and repeated prompt workloads. |
| prefix_cache | `vllm-prefix-cache-bench` | Closest official route. Keep Ascend-specific cache hash/support unknown unless locally proven. |
| streaming | `vllm-bench-serve` | Endpoint-level streaming/cancel still needs custom lifecycle seeds. |
| quantization | `vllm-deploy-docker`, `vllm-bench-serve` | Official skill can provide serving route; correctness oracle remains local. |
| moe | `vllm-deploy-docker`, `vllm-bench-serve` | Expert/FlashComm behavior is Ascend-specific; do not infer support from generic skill. |
| distributed / PD | `vllm-deploy-k8s`, `vllm-bench-serve` | Official route may help service setup, but PD/Mooncake details need local evidence. |
| ascend_backend | none generic | Use local Ascend skills and environment docs instead of generic CUDA/GPU assumptions. |

## Citation Note

When referencing official vLLM skills in wiki pages, cite this as a verification route or companion workflow, not as proof of a bug, version, or Ascend compatibility claim.
