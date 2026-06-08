# Official vLLM Skills Reference

This file connects the local bug-wiki skill to the official `vllm-project/vllm-skills` repository.

Source: https://github.com/vllm-project/vllm-skills

For broader upstream routes including NCU, NVIDIA, FlagOS, AI Research, and evaluation skills, also read `../shared/upstream-routes.md` from the `our-wiki-skill/` directory.

## Available Official Skill Routes

| Official skill | Bug-wiki use |
| --- | --- |
| `vllm-deploy-simple` | Plan a simple generic vLLM service smoke. |
| `vllm-deploy-docker` | Plan Docker-based service verification. |
| `vllm-deploy-k8s` | Plan Kubernetes deployment verification. |
| `vllm-prefix-cache-bench` | Plan prefix-cache/KV reuse benchmarks. |
| `vllm-bench-random-synthetic` | Plan synthetic throughput/latency stress for scheduler or batching symptoms. |
| `vllm-bench-serve` | Plan OpenAI-compatible endpoint benchmark against a running service. |

## Evidence Boundary

- A planned official skill route is not reproduction evidence.
- A route becomes evidence only after local commands, logs, metrics, artifacts, and environment details are captured.
- Generic vLLM commands must be adapted to vLLM-Ascend with local environment evidence.
- New model-path examples must use the approved `/mnt/data2/model_weights` root.

## Capsule Field Mapping

| Capsule field | How official vLLM skills can help |
| --- | --- |
| Triggering Workload | Name a benchmark/serve route that could generate the workload. |
| Reproduction Evidence | Only fill command/result after a local run exists. Until then, use `unknown` or `planned route`. |
| Fuzzer Discoverability | Use official benchmark routes to think about seed shape, not as a GRIEF replacement. |
| Next Actions | Recommend the closest skill route for verification experiments. |

## Bug Domain Mapping

| Bug domain | Best official skill route | Caveat |
| --- | --- | --- |
| KV/prefix cache | `vllm-prefix-cache-bench` | Ascend cache metrics/support must be locally verified. |
| scheduler/liveness | `vllm-bench-random-synthetic`, `vllm-bench-serve` | Need recovery canary and timeout oracle. |
| streaming/cancel | `vllm-bench-serve` plus custom lifecycle seed | Official benchmark may not cover disconnect/cancel. |
| sampling/output correctness | `vllm-bench-serve` | Needs deterministic or reference oracle. |
| quantization | `vllm-deploy-docker`, `vllm-bench-serve` | Generic vLLM support does not prove Ascend kernel support. |
| MoE/FlashComm | `vllm-deploy-docker`, `vllm-bench-serve` | FlashComm is Ascend-specific; keep support unknown unless local evidence exists. |
| distributed/PD | `vllm-deploy-k8s`, `vllm-bench-serve` | PD/Mooncake verification needs local topology and connector evidence. |
| CPU/mock CI | none | CI failures are not endpoint benchmark cases. |
