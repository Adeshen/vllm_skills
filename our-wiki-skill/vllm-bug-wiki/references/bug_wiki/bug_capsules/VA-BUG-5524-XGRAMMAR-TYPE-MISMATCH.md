# Bug Capsule: xgrammar type mismatch in structured output

## Identity
- Issue: [vllm-ascend #5524](https://github.com/vllm-project/vllm-ascend/issues/5524)
- Fixing PR: [vllm-ascend #6151](https://github.com/vllm-project/vllm-ascend/pull/6151)
- Related PRs: unknown; issue #6820 is a weak reference in the same PR-centric case.
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for #5524 linkage; low for #6820 linkage

## Failure Summary
- Failure domain: structured output, xgrammar, token bitmask dependency/API
- Failure symptom: xgrammar type mismatch on `apply_token_bitmask_inplace_cpu`.
- Expected behavior: structured output bitmask application should accept the tensor/argument types supplied by vLLM-Ascend.
- Observed behavior: type mismatch / incompatible function arguments.
- User impact: structured output requests can fail at runtime.

## Triggering Workload
- Model: unknown.
- Request shape: structured output / guided decoding request.
- Prefix/cache behavior: unknown.
- Batch/concurrency: unknown.
- Sampling params: structured output constraints.
- Distributed/parallel setting: unknown.
- Quantization: unknown.
- Special runtime flags: xgrammar structured output path.

## Version And Environment
- Affected vLLM-Ascend version: unknown; weak related issue mentions v0.13.0.
- Affected image: v0.13.0rc1 patch base in release mapping.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: derived `local/vllm-ascend:0.13.0rc1-pr6151`.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: likely not NPU-specific because changed files are dependencies/workflow.
- Container/runtime notes: exact xgrammar version is important.

## Fix Evidence
- Fixing PR: [#6151](https://github.com/vllm-project/vllm-ascend/pull/6151)
- Code diff summary: commit says `Fix xgrammar type mismatching error on apply_token_bitmask_inplace_cpu`.
- Files changed: `.github/workflows/_e2e_test.yaml`, `pyproject.toml`, `requirements.txt`.
- Suspected root cause: dependency version or type contract mismatch between xgrammar and structured output bitmask call.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives v0.13.0rc1 patch base; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: xgrammar type mismatch.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: none.
- Traces: none.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_06151__structured_output_xgrammar_type_mismatching_error_on_apply_token_bitmask/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_06151__structured_output_xgrammar_type_mismatching_error_on_apply_token_bitmask/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: structured output request with schema/grammar constraints.
- Required oracle: HTTP 5xx, structured-output parser failure, schema-validity check.
- Required monitor: response schema validator and server logs.
- Mutation axes: schema shape, batch size, output length, grammar backend, xgrammar dependency.
- Minimal seed sketch: deterministic request requiring JSON object output through structured output/guided decoding.
- Why this is or is not fuzzable: trigger is request-level if structured output is enabled, but dependency-version issues require environment control.

## Next Actions
- Immediate next action: capture exact xgrammar/requirements versions before and after PR #6151.
- Missing evidence: exact request JSON, dependency lock, before/after logs.
- Owner: unknown

