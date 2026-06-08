# Official And Upstream Skill Submodules

This directory keeps upstream repositories as Git submodules, not vendored copies.

## Sources

| Source | Submodule path | GitHub URL | Commit |
| --- | --- | --- | --- |
| vLLM-Ascend | [vllm-ascend/](vllm-ascend/) | `https://github.com/vllm-project/vllm-ascend.git` | `f5c97749fa36f80648a56198e60800f3a0dac3ff` |
| vLLM Skills | [vllm-skills/](vllm-skills/) | `https://github.com/vllm-project/vllm-skills.git` | `c99623410c1531148ff9b39fe1dcb27efbf4bf23` |
| KernelWiki | [kernelwiki/KernelWiki/](kernelwiki/KernelWiki/) | `https://github.com/mit-han-lab/KernelWiki.git` | `76d27b56f804e7e7295d4c570e1e5d7eef4b0a75` |
| NCU Report Skill | [hpc_mlsys/ncu-report-skill/](hpc_mlsys/ncu-report-skill/) | `https://github.com/mit-han-lab/ncu-report-skill.git` | `1cf238d6b41c79bd35041192506c4d45e765a3f1` |
| NVIDIA Skills | [hpc_mlsys/nvidia-skills/](hpc_mlsys/nvidia-skills/) | `https://github.com/NVIDIA/skills.git` | `e29b3c65dd0292e3f9f851b15eefe5a7c2023dd7` |
| FlagOS Skills | [hpc_mlsys/flagos-skills/](hpc_mlsys/flagos-skills/) | `https://github.com/flagos-ai/skills.git` | `d9eb2bbbf976faef4ce1e14c8c7c668aec9b1620` |
| AI Research Skills | [hpc_mlsys/ai-research-skills/](hpc_mlsys/ai-research-skills/) | `https://github.com/Orchestra-Research/AI-research-SKILLs.git` | `28f2d29236f2bade2eb92cadb2585189589a5828` |
| NeMo Evaluator | [hpc_mlsys/nemo-evaluator/](hpc_mlsys/nemo-evaluator/) | `https://github.com/NVIDIA-NeMo/Evaluator.git` | `d4ceac0112769300c15b54fdde5237a12e094c61` |
| Scientific Agent Skills | [scientific/scientific-agent-skills/](scientific/scientific-agent-skills/) | `https://github.com/K-Dense-AI/scientific-agent-skills.git` | `4457f17a29e55c2190c71fca0df156761ac5400c` |
| Hugging Face Skills | [scientific/huggingface-skills/](scientific/huggingface-skills/) | `https://github.com/huggingface/skills.git` | `504191c59a67888cae225ea54fe03aa502ef0319` |
| Skills Vote | [skill_discovery/skills-vote/](skill_discovery/skills-vote/) | `https://github.com/MemTensor/skills-vote.git` | `86fd73915e9ea4b594ca0edbd8c3267109a8f976` |

## Skill Inventory

### vLLM-Ascend

- [vllm-ascend-model-adapter](vllm-ascend/.agents/skills/vllm-ascend-model-adapter/SKILL.md)
- [vllm-ascend-release](vllm-ascend/.agents/skills/vllm-ascend-release/SKILL.md)

### vLLM Skills

- [vllm-bench-random-synthetic](vllm-skills/plugins/vllm-skills/skills/vllm-bench-random-synthetic/SKILL.md)
- [vllm-bench-serve](vllm-skills/plugins/vllm-skills/skills/vllm-bench-serve/SKILL.md)
- [vllm-deploy-docker](vllm-skills/plugins/vllm-skills/skills/vllm-deploy-docker/SKILL.md)
- [vllm-deploy-k8s](vllm-skills/plugins/vllm-skills/skills/vllm-deploy-k8s/SKILL.md)
- [vllm-deploy-simple](vllm-skills/plugins/vllm-skills/skills/vllm-deploy-simple/SKILL.md)
- [vllm-prefix-cache-bench](vllm-skills/plugins/vllm-skills/skills/vllm-prefix-cache-bench/SKILL.md)

### KernelWiki

- [KernelWiki root skill](kernelwiki/KernelWiki/SKILL.md)
- [KernelWiki README](kernelwiki/KernelWiki/README.md)
- [KernelWiki wiki index](kernelwiki/KernelWiki/index.md)

### HPC / MLSys

- [NCU Report Skill](hpc_mlsys/ncu-report-skill/SKILL.md): Nsight Compute report collection and diagnosis workflow.
- [NVIDIA Skills catalog](hpc_mlsys/nvidia-skills/README.md): NVIDIA CUDA-X, Dynamo, NeMo, Megatron-Core, Omniverse, and related platform skills.
- Selected NVIDIA entries:
  - [dynamo-interconnect-check](hpc_mlsys/nvidia-skills/skills/dynamo-interconnect-check/SKILL.md)
  - [dynamo-router-starter](hpc_mlsys/nvidia-skills/skills/dynamo-router-starter/SKILL.md)
  - [dynamo-troubleshoot](hpc_mlsys/nvidia-skills/skills/dynamo-troubleshoot/SKILL.md)
  - [nemo-evaluator-plugin](hpc_mlsys/nvidia-skills/skills/nemo-evaluator-plugin/SKILL.md)
  - [mcore-run-on-slurm](hpc_mlsys/nvidia-skills/skills/mcore-run-on-slurm/SKILL.md)
  - [nemo-mbridge-perf-parallelism-strategies](hpc_mlsys/nvidia-skills/skills/nemo-mbridge-perf-parallelism-strategies/SKILL.md)
  - [nemo-mbridge-perf-memory-tuning](hpc_mlsys/nvidia-skills/skills/nemo-mbridge-perf-memory-tuning/SKILL.md)
  - [nemo-mbridge-perf-moe-optimization-workflow](hpc_mlsys/nvidia-skills/skills/nemo-mbridge-perf-moe-optimization-workflow/SKILL.md)
- Selected FlagOS entries:
  - [kernelgen-flagos](hpc_mlsys/flagos-skills/skills/kernelgen-flagos/SKILL.md)
  - [perf-test-flagos](hpc_mlsys/flagos-skills/skills/perf-test-flagos/SKILL.md)
  - [vllm-plugin-fl-setup-flagos](hpc_mlsys/flagos-skills/skills/vllm-plugin-fl-setup-flagos/SKILL.md)
  - [model-migrate-flagos](hpc_mlsys/flagos-skills/skills/model-migrate-flagos/SKILL.md)
  - [model-verify-flagos](hpc_mlsys/flagos-skills/skills/model-verify-flagos/SKILL.md)
- Selected AI Research inference-serving entries:
  - [vllm](hpc_mlsys/ai-research-skills/12-inference-serving/vllm/SKILL.md)
  - [sglang](hpc_mlsys/ai-research-skills/12-inference-serving/sglang/SKILL.md)
  - [tensorrt-llm](hpc_mlsys/ai-research-skills/12-inference-serving/tensorrt-llm/SKILL.md)
  - [llama-cpp](hpc_mlsys/ai-research-skills/12-inference-serving/llama-cpp/SKILL.md)
- [NeMo Evaluator](hpc_mlsys/nemo-evaluator/README.md) is an evaluation framework reference rather than a standalone `SKILL.md` repository; keep it linked for benchmark and quality-gate design.

### Scientific / Model Ecosystem

- [Scientific Agent Skills index](scientific/scientific-agent-skills/README.md)
- [optimize-for-gpu](scientific/scientific-agent-skills/skills/optimize-for-gpu/SKILL.md)
- [dask](scientific/scientific-agent-skills/skills/dask/SKILL.md)
- [modal](scientific/scientific-agent-skills/skills/modal/SKILL.md)
- [huggingface-llm-trainer](scientific/huggingface-skills/skills/huggingface-llm-trainer/SKILL.md)
- [huggingface-community-evals](scientific/huggingface-skills/skills/huggingface-community-evals/SKILL.md)
- [huggingface-local-models](scientific/huggingface-skills/skills/huggingface-local-models/SKILL.md)

### Skill Discovery

- [Skills Vote](skill_discovery/skills-vote/README.md): reference system for large-scale skill discovery, evaluation, and recommendation.

## Local Use Policy

- These submodules are upstream operational/reference sources.
- They should not overwrite local wiki-maintenance skills under [../our-wiki-skill/](../our-wiki-skill/).
- Generic vLLM deploy/benchmark skills do not prove backend-specific behavior by themselves.
- KernelWiki is a wiki-construction and GPU-kernel knowledge-base reference; it is not vLLM or vLLM-Ascend bug evidence by itself.
- HPC/MLSys skill repositories are workflow and theory references. They become evidence only after a local experiment captures hardware, commands, profiler outputs, logs, metrics, and source revisions.
- A skill route becomes bug-wiki evidence only after local backend-specific commands, logs, metrics, and environment details are captured.
- New local model paths should use `/mnt/data2/model_weights`.

## Validation Notes

- The imported vLLM / vLLM-Ascend skill directories pass the current local Codex `quick_validate.py` in the original baseline.
- The KernelWiki snapshot is preserved verbatim at the requested commit. Its upstream `SKILL.md` contains `argument-hint`, which the current local validator does not accept; keep the snapshot unchanged unless intentionally creating a local sanitized wrapper.
- Large upstream skill catalogs may contain schemas, frontmatter, or tool assumptions that differ from local Codex validation. Keep them verbatim as submodules and create local wrappers only when needed.

## Clone / Update

After cloning this repository, initialize submodules with:

```bash
git submodule update --init --recursive
```

To refresh upstream submodules intentionally, update each submodule and commit the changed submodule pointer.

## Normalized Install

Many upstream repositories keep skills below different paths, such as `skills/*/SKILL.md`, `plugins/*/skills/*/SKILL.md`, `.agents/skills/*/SKILL.md`, or a repository-root `SKILL.md`.

From the repository root, run:

```bash
make install
```

This calls [../scripts/install_upstream_skills.py](../scripts/install_upstream_skills.py), creates symlinks under `build/upstream_skills/`, and writes `manifest.json` plus `manifest.md`. The generated install tree is ignored by git.
