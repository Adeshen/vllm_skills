# Release Matrix

Primary source: [VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Local Summary

- Usable release count in source mapping: 35.
- Usable image count in source mapping: 35 likely or known npu4-compatible release/branch images.
- Best verification candidates from source mapping: `v0.18.0rc1`, `v0.18.0`, `v0.19.1rc1`, `releases-v0.13.0` / `v0.13.0rc3`.
- Known npu4-smoked image: `quay.io/ascend/vllm-ascend:v0.18.0rc1`.
- Quay tags lack fully trusted source-label evidence from manifest-only inspection; do not infer source commit from tag name if labels later disagree.

## Capsule Patch Bases

| PR | Issue | Patch base image | Derived image | Notes |
| --- | --- | --- | --- | --- |
| #8959 | #7871 | `v0.18.0` | `local/vllm-ascend:0.18.0-pr8959` | KV load failure metrics |
| #7683 | #7996 | `v0.17.0rc1` | `local/vllm-ascend:0.17.0rc1-pr7683` | Qwen3.5 MoE FlashComm |
| #5655 | #2865 | `v0.13.0rc1` | `local/vllm-ascend:0.13.0rc1-pr5655` | lm-eval dependency |
| #7266 | #6992 | `v0.16.0rc1` | `local/vllm-ascend:0.16.0rc1-pr7266` | CPU binding locale |
| #7274 | #6992 | `v0.16.0rc1` | `local/vllm-ascend:0.16.0rc1-pr7274` | CPU binding locale |
| #7808 | #7807 | `v0.18.0rc1` | `local/vllm-ascend:0.18.0rc1-pr7808` | rejection sampling |
| #8251 | #6992 | `v0.18.0rc1` | `local/vllm-ascend:0.18.0rc1-pr8251` | CPU binding locale |
| #5444 | #5445 | `v0.13.0rc1` | `local/vllm-ascend:0.13.0rc1-pr5444` | chunk prefill |
| #6151 | #5524 | `v0.13.0rc1` | `local/vllm-ascend:0.13.0rc1-pr6151` | xgrammar dependency |
| #3187 | #3024 | `v0.10.2rc1` | `local/vllm-ascend:0.10.2rc1-pr3187` | EAGLE attention mask |
| #5046 | #4986 | `v0.12.0rc1` | `local/vllm-ascend:0.12.0rc1-pr5046` | MTP ACL graph hang |
| #7427 | #7308 | `v0.17.0rc1` | `local/vllm-ascend:0.17.0rc1-pr7427` | multi-instance HBM |
| #8465 | #8463 | `v0.18.0rc1` | `local/vllm-ascend:0.18.0rc1-pr8465` | GPT-OSS MoE correctness |

Derived PR images are synthetic verification artifacts. They are not official Quay release images.

## Dependency Context

The GRIEF smoke report observed on the running `v0.18.0rc1` container:

- `/version`: `0.18.0`
- `vllm=0.18.0+empty`
- `vllm-ascend=0.18.0rc1`
- `torch=2.9.0+cpu`
- `torch-npu=2.9.0.post1+gitee7ba04`

CANN compatibility is not enumerated in the current capsule evidence and should remain `unknown` until extracted from container logs or image metadata.

