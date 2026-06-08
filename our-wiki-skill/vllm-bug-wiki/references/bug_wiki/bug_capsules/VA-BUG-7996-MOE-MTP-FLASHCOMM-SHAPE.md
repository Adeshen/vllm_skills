# Bug Capsule: Qwen3.5 MoE MTP FlashComm shape mismatch

## Identity
- Issue: [vllm-ascend #7996](https://github.com/vllm-project/vllm-ascend/issues/7996)
- Fixing PR: [vllm-ascend #7683](https://github.com/vllm-project/vllm-ascend/pull/7683)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for issue/PR linkage; medium for workload details

## Failure Summary
- Failure domain: MoE, MTP/speculative decoding, FlashComm custom op
- Failure symptom: tensor dimension mismatch in Qwen3.5-35B when MoE, MTP, and FLASHCOMM1 are combined.
- Expected behavior: Qwen3.5 MoE with MTP and FlashComm should start and generate without shared expert shape mismatch.
- Observed behavior: tensor dimension mismatch.
- User impact: advanced Qwen3.5 MoE speculative deployments fail or cannot be validated.

## Triggering Workload
- Model: Qwen3.5-35B from issue title.
- Request shape: unknown.
- Prefix/cache behavior: unknown.
- Batch/concurrency: unknown.
- Sampling params: speculative/MTP path implied.
- Distributed/parallel setting: unknown.
- Quantization: unknown.
- Special runtime flags: FLASHCOMM1 and MTP.

## Version And Environment
- Affected vLLM-Ascend version: unknown; release mapping uses v0.17.0rc1 as patch base.
- Affected image: `quay.io/ascend/vllm-ascend:v0.17.0rc1` as patch-base candidate.
- Fixed vLLM-Ascend version: unknown; release mapping suggests comparing to v0.19.1rc1 or derived PR image.
- Fixed image: `local/vllm-ascend:0.17.0rc1-pr7683` as derived candidate; official fixed image unknown.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend NPU; exact issue hardware unknown.
- Container/runtime notes: stock v0.18.0rc1 has speculative decode caveats in `ENV_CONSTRAINTS.md`.

## Fix Evidence
- Fixing PR: [#7683](https://github.com/vllm-project/vllm-ascend/pull/7683)
- Code diff summary: commit says `Fix flash comm v1 problems of Qwen3.5 series on A2`.
- Files changed: `vllm_ascend/ops/register_custom_ops.py`, `vllm_ascend/spec_decode/eagle_proposer.py`.
- Suspected root cause: Qwen3.5 MoE/MTP path supplied a shape not accepted by FlashComm v1/custom op registration or EAGLE proposer state.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives v0.17.0rc1 patch base commit `e20f0b1a0d2f`; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: tensor dimension mismatch from issue title.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: unknown.
- Traces: unknown.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07683__moe_mtp_flashcomm1_causes_tensor_dimension_mismatch_in_qwen3_5_35b/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07683__moe_mtp_flashcomm1_causes_tensor_dimension_mismatch_in_qwen3_5_35b/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: Qwen3.5 MoE + MTP + FlashComm service-mode seed.
- Required oracle: startup/generation crash, tensor shape mismatch log detector.
- Required monitor: server liveness and logs.
- Mutation axes: MTP on/off, FlashComm version, prompt length, batch size, MoE model variant.
- Minimal seed sketch: run one deterministic request against a Qwen3.5 MoE service with MTP and FLASHCOMM1 enabled.
- Why this is or is not fuzzable: trigger is request-expressible only after the special model/backend configuration is live; ordinary HTTP mutation will not discover the required environment.

## Next Actions
- Immediate next action: verify whether Qwen3.5 MoE weights exist under `/mnt/data2/model_weights`, then perform a v0.17.0rc1 or v0.18.0rc1 smoke with MTP/FlashComm isolated.
- Missing evidence: exact startup command, model path, dependency versions, before/after logs.
- Owner: unknown

