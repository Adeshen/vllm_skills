# Bug Capsule: `prompt_token_ids` keyword mismatch

## Identity
- Issue: [vllm-ascend #2865](https://github.com/vllm-project/vllm-ascend/issues/2865)
- Fixing PR: [vllm-ascend #5655](https://github.com/vllm-project/vllm-ascend/pull/5655)
- Related PRs: [#2871](https://github.com/vllm-project/vllm-ascend/pull/2871) is also linked to #2865 in corpus review.
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for issue/PR linkage; low for runtime root cause because diff is dependency-only

## Failure Summary
- Failure domain: evaluation dependency/API mismatch
- Failure symptom: accuracy test failed due to unexpected keyword argument `prompt_token_ids`.
- Expected behavior: evaluation harness path should call the compatible API without unexpected kwargs.
- Observed behavior: TypeError-like unexpected keyword argument failure.
- User impact: accuracy validation and CI-style eval jobs can fail even when serving path is healthy.

## Triggering Workload
- Model: unknown.
- Request shape: accuracy/eval harness path using `prompt_token_ids`.
- Prefix/cache behavior: unknown.
- Batch/concurrency: unknown.
- Sampling params: unknown.
- Distributed/parallel setting: unknown.
- Quantization: unknown.
- Special runtime flags: unknown.

## Version And Environment
- Affected vLLM-Ascend version: unknown; release mapping uses v0.13.0rc1 as patch base.
- Affected image: `quay.io/ascend/vllm-ascend:v0.13.0rc1` as patch-base candidate.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: `local/vllm-ascend:0.13.0rc1-pr5655` as derived candidate.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: unknown; likely not NPU-specific.
- Container/runtime notes: dependency mismatch may be reproducible in CPU/mock CI if exact package set is known.

## Fix Evidence
- Fixing PR: [#5655](https://github.com/vllm-project/vllm-ascend/pull/5655)
- Code diff summary: commit says `bump lm-eval to v0.49.2`.
- Files changed: `requirements-dev.txt`.
- Suspected root cause: local `lm-eval` version did not match the argument contract expected by the eval path.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives v0.13.0rc1 patch base; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: unexpected keyword argument `prompt_token_ids`.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: none.
- Traces: none.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_05655__accuract_test_failed_due_to_unexpected_keyword_argument_prompt_token_ids/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_05655__accuract_test_failed_due_to_unexpected_keyword_argument_prompt_token_ids/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: no.
- Required seed type: eval harness invocation, not HTTP inference trace.
- Required oracle: CI/eval failure.
- Required monitor: process exit and traceback.
- Mutation axes: dependency version, eval task, prompt-token input path.
- Minimal seed sketch: run the affected accuracy test with the pre-fix `lm-eval` dependency.
- Why this is or is not fuzzable: GRIEF's HTTP request mutation is outside the failing eval dependency path.

## Next Actions
- Immediate next action: identify the exact accuracy test and dependency lockfile from cached issue HTML.
- Missing evidence: exact command, dependency versions, before/after result.
- Owner: unknown

