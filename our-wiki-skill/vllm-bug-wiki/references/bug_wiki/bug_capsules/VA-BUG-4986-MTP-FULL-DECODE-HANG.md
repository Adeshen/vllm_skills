# Bug Capsule: FULL_DECODE_ONLY MTP hang with DeepSeek V3.1

## Identity
- Issue: [vllm-ascend #4986](https://github.com/vllm-project/vllm-ascend/issues/4986)
- Fixing PR: [vllm-ascend #5046](https://github.com/vllm-project/vllm-ascend/pull/5046)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for issue/PR linkage

## Failure Summary
- Failure domain: MTP, ACL graph, DeepSeek, scheduler/liveness
- Failure symptom: server hangs when running FULL_DECODE_ONLY mode and enabling MTP with DeepSeek V3.1.
- Expected behavior: MTP full-decode-only requests complete or fail cleanly.
- Observed behavior: server hang.
- User impact: service becomes unresponsive for affected MTP deployment mode.

## Triggering Workload
- Model: DeepSeek V3.1.
- Request shape: unknown.
- Prefix/cache behavior: unknown.
- Batch/concurrency: unknown.
- Sampling params: MTP/speculative path.
- Distributed/parallel setting: unknown.
- Quantization: unknown.
- Special runtime flags: FULL_DECODE_ONLY mode, MTP, ACL graph.

## Version And Environment
- Affected vLLM-Ascend version: unknown; release mapping uses v0.12.0rc1 as patch base.
- Affected image: `quay.io/ascend/vllm-ascend:v0.12.0rc1` patch base candidate.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: derived `local/vllm-ascend:0.12.0rc1-pr5046`.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend NPU.
- Container/runtime notes: DeepSeek variants may require special image/model support; do not use as generic baseline.

## Fix Evidence
- Fixing PR: [#5046](https://github.com/vllm-project/vllm-ascend/pull/5046)
- Code diff summary: commit says `fix mtp aclgraph`.
- Files changed: `vllm_ascend/spec_decode/mtp_proposer.py`.
- Suspected root cause: MTP proposer state in ACL graph/full-decode-only path could deadlock or fail to advance.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives v0.12.0rc1 patch base; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: server hang.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: request latency/liveness.
- Traces: unknown.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_05046__server_hangs_when_running_full_decode_only_mode_and_enabling_mtp_with_de/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_05046__server_hangs_when_running_full_decode_only_mode_and_enabling_mtp_with_de/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: DeepSeek V3.1 MTP full-decode-only request seed.
- Required oracle: hung request, server liveness, recovery request failure.
- Required monitor: HTTP timeout, process logs, AICore utilization if available.
- Mutation axes: MTP on/off, graph on/off, max tokens, request count, decode-only mode.
- Minimal seed sketch: deterministic request with MTP/full-decode-only enabled, followed by recovery canary.
- Why this is or is not fuzzable: hang oracle is strong, but the special model/runtime mode must be provided externally.

## Next Actions
- Immediate next action: check model availability and whether FULL_DECODE_ONLY can be enabled on a controlled derived image.
- Missing evidence: exact runtime flags, model path, before/after logs.
- Owner: unknown

