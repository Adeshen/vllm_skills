# Bug Capsule: Chunk prefill long-sequence bug

## Identity
- Issue: [vllm-ascend #5445](https://github.com/vllm-project/vllm-ascend/issues/5445)
- Fixing PR: [vllm-ascend #5444](https://github.com/vllm-project/vllm-ascend/pull/5444)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for issue/PR linkage; medium for workload details

## Failure Summary
- Failure domain: chunked prefill, long sequence, worker PCP utilities
- Failure symptom: chunk prefill bug for long sequence feature.
- Expected behavior: long-sequence chunked prefill should complete correctly.
- Observed behavior: bug in long-sequence chunk prefill path; exact symptom unknown.
- User impact: long-context workloads may crash, hang, or produce incorrect behavior when chunked prefill is enabled.

## Triggering Workload
- Model: unknown.
- Request shape: long sequence.
- Prefix/cache behavior: chunked prefill.
- Batch/concurrency: multicard e2e test added.
- Sampling params: unknown.
- Distributed/parallel setting: multicard long-sequence test path.
- Quantization: unknown.
- Special runtime flags: long sequence feature; chunk prefill.

## Version And Environment
- Affected vLLM-Ascend version: unknown; release mapping uses v0.13.0rc1 as patch base.
- Affected image: `quay.io/ascend/vllm-ascend:v0.13.0rc1` patch base candidate.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: derived `local/vllm-ascend:0.13.0rc1-pr5444`.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend NPU, likely multicard.
- Container/runtime notes: use `/mnt/data2/model_weights` for new reproduction.

## Fix Evidence
- Fixing PR: [#5444](https://github.com/vllm-project/vllm-ascend/pull/5444)
- Code diff summary: multiple commits labeled `bug fix`; added e2e multicard long sequence chunked prefill test.
- Files changed: `vllm_ascend/worker/pcp_utils.py`, `tests/e2e/multicard/long_sequence/test_chunked_prefill.py`.
- Suspected root cause: PCP utility state for chunked prefill did not handle long-sequence boundary conditions.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives v0.13.0rc1 patch base; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: unknown.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: latency/hang and output completion are useful.
- Traces: unknown.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_05444__fix_chunk_prefill_bug_for_long_sequence_feature/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_05444__fix_chunk_prefill_bug_for_long_sequence_feature/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: long prompt with chunked prefill enabled.
- Required oracle: crash/hang, latency spike, deterministic completion, token-count invariant.
- Required monitor: HTTP liveness, logs, token count.
- Mutation axes: prompt length, chunk boundary, max model length, batch size, shared prefix.
- Minimal seed sketch: control short prompt, toxic long prompt around chunk boundary, recovery short prompt.
- Why this is or is not fuzzable: GRIEF can mutate length and observe liveness, but exact chunked-prefill configuration and long-context model limits must be supplied.

## Next Actions
- Immediate next action: inspect PR test file and convert it into a minimal HTTP seed.
- Missing evidence: exact model, long prompt length, before/after logs.
- Owner: unknown

