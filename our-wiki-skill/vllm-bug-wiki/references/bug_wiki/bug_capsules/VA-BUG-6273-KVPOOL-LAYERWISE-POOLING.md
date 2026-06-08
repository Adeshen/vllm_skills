# Bug Capsule: Layerwise KV pool transfer abnormal for pooling

## Identity
- Issue: [vllm-ascend #6273](https://github.com/vllm-project/vllm-ascend/issues/6273)
- Fixing PR: [vllm-ascend #5168](https://github.com/vllm-project/vllm-ascend/pull/5168)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR closed in local corpus
- Confidence: medium; issue/PR link is strong but PR is closed rather than merged in local row

## Failure Summary
- Failure domain: KV pool, layerwise transfer, pooling function
- Failure symptom: pooling function is abnormal when `use_layerwise` is set to true for pooling KV transfer config.
- Expected behavior: pooling mode should work with layerwise KV transfer.
- Observed behavior: abnormal pooling behavior.
- User impact: pooling/embedding-style deployments using KV transfer can be incorrect or unusable.

## Triggering Workload
- Model: unknown.
- Request shape: pooling workload.
- Prefix/cache behavior: KV pool transfer with layerwise enabled.
- Batch/concurrency: unknown.
- Sampling params: none or pooling-specific.
- Distributed/parallel setting: KV pool scheduler/worker path.
- Quantization: unknown.
- Special runtime flags: `use_layerwise=true` in pooling KV transfer config.

## Version And Environment
- Affected vLLM-Ascend version: unknown.
- Affected image: unknown.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: unknown.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend NPU.
- Container/runtime notes: unknown.

## Fix Evidence
- Fixing PR: [#5168](https://github.com/vllm-project/vllm-ascend/pull/5168)
- Code diff summary: commits are mostly generic `fix`; changed docs and KV pool scheduler/worker/transfer files.
- Files changed: `vllm_ascend/distributed/kvpool/ascend_store_connector.py`, `config_data.py`, `kv_transfer.py`, `pool_scheduler.py`, `pool_worker.py`, KV pool docs.
- Suspected root cause: pooling KV transfer layerwise mode had inconsistent scheduler/worker/connector behavior.
- Patch applies to affected commit: unknown.
- Patch application evidence: PR code material has base/head commits but no release mapping row or apply check found.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: pooling function abnormal.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: unknown.
- Traces: KV transfer traces would help.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_05168__when_use_layerwise_is_set_to_true_for_pooling_kv_transfer_config_the_poo/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_05168__when_use_layerwise_is_set_to_true_for_pooling_kv_transfer_config_the_poo/materials/code/changed_files.tsv).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: pooling endpoint / embedding request with layerwise KV transfer.
- Required oracle: pooling output validity, HTTP errors, connector logs.
- Required monitor: liveness and KV pool logs; semantic pooling oracle if correctness-only.
- Mutation axes: pooling request size, layerwise on/off, KV transfer config, batch size.
- Minimal seed sketch: compare pooling output with layerwise disabled/enabled for identical input.
- Why this is or is not fuzzable: ordinary chat-completion GRIEF seeds will miss pooling endpoints and config-specific KV transfer behavior.

## Next Actions
- Immediate next action: inspect cached issue body for exact pooling command and determine whether PR #5168 was superseded.
- Missing evidence: PR merge/fix status, release mapping, exact workload, before/after output.
- Owner: unknown

