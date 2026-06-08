# Official And Upstream Skill Submodules

This directory keeps upstream repositories as Git submodules, not vendored copies.

## Sources

| Source | Submodule path | GitHub URL | Commit |
| --- | --- | --- | --- |
| vLLM-Ascend | [vllm-ascend/](vllm-ascend/) | `https://github.com/vllm-project/vllm-ascend.git` | `f5c97749fa36f80648a56198e60800f3a0dac3ff` |
| vLLM Skills | [vllm-skills/](vllm-skills/) | `https://github.com/vllm-project/vllm-skills.git` | `c99623410c1531148ff9b39fe1dcb27efbf4bf23` |
| KernelWiki | [kernelwiki/KernelWiki/](kernelwiki/KernelWiki/) | `https://github.com/mit-han-lab/KernelWiki.git` | `76d27b56f804e7e7295d4c570e1e5d7eef4b0a75` |

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

## Local Use Policy

- These submodules are upstream operational/reference sources.
- They should not overwrite local wiki-maintenance skills under [../our-wiki-skill/](../our-wiki-skill/).
- Generic vLLM deploy/benchmark skills do not prove vLLM-Ascend behavior by themselves.
- KernelWiki is a wiki-construction and GPU-kernel knowledge-base reference; it is not vLLM-Ascend bug evidence by itself.
- A skill route becomes bug-wiki evidence only after local Ascend commands, logs, metrics, and environment details are captured.
- New local model paths should use `/mnt/data2/model_weights`.

## Validation Notes

- The 8 imported vLLM / vLLM-Ascend skill directories pass the current local Codex `quick_validate.py`.
- The KernelWiki snapshot is preserved verbatim at the requested commit. Its upstream `SKILL.md` contains `argument-hint`, which the current local validator does not accept; keep the snapshot unchanged unless intentionally creating a local sanitized wrapper.

## Clone / Update

After cloning this repository, initialize submodules with:

```bash
git submodule update --init --recursive
```

To refresh upstream submodules intentionally, update each submodule and commit the changed submodule pointer.
