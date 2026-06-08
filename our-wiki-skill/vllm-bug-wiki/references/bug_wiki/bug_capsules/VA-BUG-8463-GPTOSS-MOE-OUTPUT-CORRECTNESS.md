# Bug Capsule: GPT-OSS 120B MoE output correctness

## Identity
- Issue: [vllm-ascend #8463](https://github.com/vllm-project/vllm-ascend/issues/8463)
- Fixing PR: [vllm-ascend #8465](https://github.com/vllm-project/vllm-ascend/pull/8465)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for issue/PR linkage; medium for root cause from commit message

## Failure Summary
- Failure domain: MoE MLP, output correctness
- Failure symptom: GPT-OSS 120B inference result is incorrect on vllm-ascend 0.17.0.rc1.
- Expected behavior: output should match expected model behavior or reference implementation.
- Observed behavior: incorrect inference result.
- User impact: service may be healthy but answers incorrectly, which is high severity for production.

## Triggering Workload
- Model: GPT-OSS 120B.
- Request shape: inference request; exact prompt unknown.
- Prefix/cache behavior: unknown.
- Batch/concurrency: unknown.
- Sampling params: unknown.
- Distributed/parallel setting: likely large-model multi-card, but unknown.
- Quantization: MoE path; exact quantization unknown.
- Special runtime flags: unknown.

## Version And Environment
- Affected vLLM-Ascend version: v0.17.0.rc1 in issue title.
- Affected image: unknown; release mapping gives v0.18.0rc1 as patch-base candidate for PR #8465.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: derived `local/vllm-ascend:0.18.0rc1-pr8465`.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend NPU; exact topology unknown.
- Container/runtime notes: large-model verification likely requires multi-card resources and model availability.

## Fix Evidence
- Fixing PR: [#8465](https://github.com/vllm-project/vllm-ascend/pull/8465)
- Code diff summary: commit says `[BugFix] (moe_mlp) handle enum-based MoE activation in unquant_apply_mlp`.
- Files changed: `vllm_ascend/ops/fused_moe/moe_mlp.py`.
- Suspected root cause: MoE activation enum handling in unquantized MLP path led to incorrect computation.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives v0.18.0rc1 patch base; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: incorrect inference result.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: output/reference correctness metric needed.
- Traces: unknown.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_08465__the_inference_result_of_the_gptoss_120b_model_is_incorrect_on_vllm_ascen/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_08465__the_inference_result_of_the_gptoss_120b_model_is_incorrect_on_vllm_ascen/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: deterministic GPT-OSS 120B prompt with known expected output/reference.
- Required oracle: semantic or differential correctness oracle.
- Required monitor: response comparator, optional logits/token diff.
- Mutation axes: prompt family, MoE activation path, quantization, batch size.
- Minimal seed sketch: send a temperature-zero canary prompt with a reference answer from a known-good backend.
- Why this is or is not fuzzable: HTTP trigger is easy but generic crash/hang oracles will miss wrong-answer bugs.

## Next Actions
- Immediate next action: locate exact issue prompt/reference output from cached issue HTML.
- Missing evidence: model availability, prompt, expected output, dependency context.
- Owner: unknown

