# Bug Capsule: Block verify rejection sampling correctness

## Identity
- Issue: [vllm-ascend #7807](https://github.com/vllm-project/vllm-ascend/issues/7807)
- Fixing PR: [vllm-ascend #7808](https://github.com/vllm-project/vllm-ascend/pull/7808)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for issue/PR linkage

## Failure Summary
- Failure domain: rejection sampling, speculative decoding, block verification
- Failure symptom: block verify implementation in rejection sampling is not correct.
- Expected behavior: block verification should compute accepted/rejected draft tokens consistently.
- Observed behavior: incorrect block verify behavior; exact user-visible output not recorded locally.
- User impact: speculative decoding may return incorrect acceptance behavior or degraded output correctness.

## Triggering Workload
- Model: unknown.
- Request shape: speculative decoding / MTP request.
- Prefix/cache behavior: unknown.
- Batch/concurrency: unknown.
- Sampling params: rejection sampling path.
- Distributed/parallel setting: unknown.
- Quantization: unknown.
- Special runtime flags: speculative decoding with block verify.

## Version And Environment
- Affected vLLM-Ascend version: unknown; release mapping uses v0.18.0rc1 as patch base.
- Affected image: `quay.io/ascend/vllm-ascend:v0.18.0rc1` as patch base.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: derived `local/vllm-ascend:0.18.0rc1-pr7808`.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend NPU.
- Container/runtime notes: `ENV_CONSTRAINTS.md` says `draft_model` speculative decoding is not a stable default baseline on v0.18.0rc1.

## Fix Evidence
- Fixing PR: [#7808](https://github.com/vllm-project/vllm-ascend/pull/7808)
- Code diff summary: commit messages mention correct `h_block` computation and `p_i` indexing.
- Files changed: `vllm_ascend/ops/triton/reject_sample.py`, `vllm_ascend/sample/rejection_sampler.py`, `tests/ut/sample/test_rejection_sampler.py`.
- Suspected root cause: block verify indexing/math was wrong in rejection sampler implementation.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives v0.18.0rc1 patch base commit `99e1ea0fe685`; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: incorrect block verify behavior.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: acceptance-rate/accepted-token oracle needed.
- Traces: unknown.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07808__block_verify_feature_implementation_in_rejection_sampling_is_not_correct/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07808__block_verify_feature_implementation_in_rejection_sampling_is_not_correct/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: speculative decoding request with deterministic baseline.
- Required oracle: accepted-token correctness, greedy/draft comparison, output equivalence or unit-test oracle.
- Required monitor: output text, token IDs, acceptance metrics/logs.
- Mutation axes: draft length, block size, repeated-token prompts, max tokens, temperature zero.
- Minimal seed sketch: compare deterministic output with speculative block verify enabled against non-spec baseline for the same prompt.
- Why this is or is not fuzzable: trigger is request-expressible, but a strong correctness oracle is needed; crash/liveness oracles are too weak.

## Next Actions
- Immediate next action: run the PR-added rejection sampler unit tests on patch base and fixed tree.
- Missing evidence: exact runtime reproducer and acceptance/output oracle.
- Owner: unknown

