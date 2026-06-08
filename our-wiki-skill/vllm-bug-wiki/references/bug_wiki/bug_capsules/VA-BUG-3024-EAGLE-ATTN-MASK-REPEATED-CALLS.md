# Bug Capsule: EAGLE repeated-call attention mask index error

## Identity
- Issue: [vllm-ascend #3024](https://github.com/vllm-project/vllm-ascend/issues/3024)
- Fixing PR: [vllm-ascend #3187](https://github.com/vllm-project/vllm-ascend/pull/3187)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for issue/PR linkage

## Failure Summary
- Failure domain: EAGLE speculative decoding, attention mask, repeated calls/high concurrency
- Failure symptom: more than 100 calls to EAGLE Qwen3-8B often produce `attn_mask index out of range`.
- Expected behavior: repeated EAGLE calls should keep attention mask indices valid.
- Observed behavior: intermittent index out of range.
- User impact: long-running or high-volume speculative decode service may fail after repeated requests.

## Triggering Workload
- Model: EAGLE Qwen3-8B.
- Request shape: many repeated calls, maybe more than 100.
- Prefix/cache behavior: unknown.
- Batch/concurrency: repeated/high-concurrency situations per commit message.
- Sampling params: EAGLE/speculative path.
- Distributed/parallel setting: unknown.
- Quantization: unknown.
- Special runtime flags: EAGLE enabled.

## Version And Environment
- Affected vLLM-Ascend version: unknown; release mapping uses v0.10.2rc1 as patch base.
- Affected image: `quay.io/ascend/vllm-ascend:v0.10.2rc1` patch base candidate.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: derived `local/vllm-ascend:0.10.2rc1-pr3187`.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend NPU.
- Container/runtime notes: repeated-call stability campaign needed.

## Fix Evidence
- Fixing PR: [#3187](https://github.com/vllm-project/vllm-ascend/pull/3187)
- Code diff summary: commit says `[Eagle] Fix attn_mask index out of range in high concurrency situations`.
- Files changed: `vllm_ascend/spec_decode/eagle_proposer.py`.
- Suspected root cause: EAGLE proposer attention-mask state/indexing became invalid under repeated/high-concurrency calls.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives v0.10.2rc1 patch base; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: `attn_mask index out of range`.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: failure count over repeated calls.
- Traces: unknown.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_03187__multiple_calls_maybe_gt_100_to_eagle3_qwen3_8b_often_incurs_attn_mask_in/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_03187__multiple_calls_maybe_gt_100_to_eagle3_qwen3_8b_often_incurs_attn_mask_in/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: repeated EAGLE requests, high-iteration campaign.
- Required oracle: traceback/log detector, HTTP 5xx, post-failure recovery canary.
- Required monitor: server logs and liveness.
- Mutation axes: request count, concurrency, prompt length, draft length, max tokens.
- Minimal seed sketch: loop 150 deterministic EAGLE requests, then send recovery canary.
- Why this is or is not fuzzable: GRIEF can express repeated/high-concurrency traces, but needs EAGLE service configuration and enough iterations.

## Next Actions
- Immediate next action: convert issue trigger into a 150-request GRIEF seed once EAGLE service setup is known.
- Missing evidence: exact model paths, runtime flags, before/after logs.
- Owner: unknown

