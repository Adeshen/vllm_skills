# HPC / MLSys Skill References

This directory contains Git submodules for high-performance computing, GPU/kernel profiling, LLM serving, distributed training, and evaluation workflows.

| Source | Path | Best use |
| --- | --- | --- |
| NCU Report Skill | [ncu-report-skill/](ncu-report-skill/) | Nsight Compute report collection, metric interpretation, and kernel optimization reporting. |
| NVIDIA Skills | [nvidia-skills/](nvidia-skills/) | NVIDIA CUDA-X, Dynamo, NeMo, Megatron-Core, Slurm, and platform-specific AI infrastructure skills. |
| FlagOS Skills | [flagos-skills/](flagos-skills/) | Heterogeneous AI stack workflows, Triton/kernel generation, vLLM plugin setup, model migration, and performance testing. |
| AI Research Skills | [ai-research-skills/](ai-research-skills/) | MLSys research skills, especially vLLM, SGLang, TensorRT-LLM, llama.cpp, distributed training, and optimization references. |
| NeMo Evaluator | [nemo-evaluator/](nemo-evaluator/) | Evaluation framework reference for benchmark, quality-gate, distributed eval, and result-format design. |

## High-Value Entrypoints

- [ncu-report-skill/SKILL.md](ncu-report-skill/SKILL.md)
- [flagos-skills/skills/kernelgen-flagos/SKILL.md](flagos-skills/skills/kernelgen-flagos/SKILL.md)
- [flagos-skills/skills/perf-test-flagos/SKILL.md](flagos-skills/skills/perf-test-flagos/SKILL.md)
- [flagos-skills/skills/vllm-plugin-fl-setup-flagos/SKILL.md](flagos-skills/skills/vllm-plugin-fl-setup-flagos/SKILL.md)
- [ai-research-skills/12-inference-serving/vllm/SKILL.md](ai-research-skills/12-inference-serving/vllm/SKILL.md)
- [ai-research-skills/12-inference-serving/tensorrt-llm/SKILL.md](ai-research-skills/12-inference-serving/tensorrt-llm/SKILL.md)
- [nvidia-skills/skills/dynamo-troubleshoot/SKILL.md](nvidia-skills/skills/dynamo-troubleshoot/SKILL.md)
- [nvidia-skills/skills/nemo-evaluator-plugin/SKILL.md](nvidia-skills/skills/nemo-evaluator-plugin/SKILL.md)

## Evidence Rule

These repositories are upstream references. Do not cite them as proof of a local vLLM, vLLM-Ascend, CUDA, or NPU bug unless a local report records the exact command, environment, hardware, profiler artifact, logs, metrics, and source revision.
