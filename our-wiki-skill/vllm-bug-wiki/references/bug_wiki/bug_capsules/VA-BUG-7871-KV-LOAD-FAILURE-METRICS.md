# Bug Capsule: KV load failure metrics exception

## Identity
- Issue: [vllm-ascend #7871](https://github.com/vllm-project/vllm-ascend/issues/7871)
- Fixing PR: [vllm-ascend #8959](https://github.com/vllm-project/vllm-ascend/pull/8959)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for issue/PR linkage; medium for root-cause detail

## Failure Summary
- Failure domain: KV transfer, Mooncake connector, metrics, PD disaggregation
- Failure symptom: KV load failure path triggers metrics exception and HTTP 500 with `kv_load_failure_policy=fail`.
- Expected behavior: failed KV load should invalidate affected blocks/end the request without crashing the metrics path or poisoning connector state.
- Observed behavior: internal server error and metrics exception on KV load failure path.
- User impact: PD/Mooncake deployments can turn a recoverable transfer failure into request failure or service instability.

## Triggering Workload
- Model: unknown; PR body mentions a GSM8K-based scenario and release mapping recommends `/mnt/data2/model_weights/Qwen3-1.7B-W4A8-V1` as a lightweight verification model.
- Request shape: PD/Mooncake request where first-part KV cache transmission fails.
- Prefix/cache behavior: KV transfer failure and invalid block handling.
- Batch/concurrency: unknown.
- Sampling params: unknown.
- Distributed/parallel setting: PD disaggregation with Mooncake KV transfer.
- Quantization: unknown.
- Special runtime flags: `kv_load_failure_policy=fail`.

## Version And Environment
- Affected vLLM-Ascend version: unknown; patch base release is v0.18.0 in release mapping.
- Affected image: `quay.io/ascend/vllm-ascend:v0.18.0` as verification base candidate.
- Fixed vLLM-Ascend version: unknown; derived verification image suggested as `local/vllm-ascend:0.18.0-pr8959`.
- Fixed image: no official fixed image proven locally.
- Upstream vLLM version: PR API body cites vLLM `v0.19.1` and upstream commit `d886c26d4d4fef7d079696beb4ece1cfb4b008a8`.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: NPU target; exact hardware unknown for issue; npu4 verification likely uses 910B3 if reproduced locally.
- Container/runtime notes: new reproduction commands should use `/mnt/data2/model_weights`.

## Fix Evidence
- Fixing PR: [#8959](https://github.com/vllm-project/vllm-ascend/pull/8959)
- Code diff summary: PR commit says `bugfix for transmit kv cache failure`; PR body says failed KV cache blocks are marked invalid and Mooncake layerwise connector adds a failure signal for cleanup.
- Files changed: `vllm_ascend/distributed/kv_transfer/kv_p2p/mooncake_connector.py`, `vllm_ascend/distributed/kv_transfer/kv_p2p/mooncake_layerwise_connector.py`, KV connector unit tests.
- Suspected root cause: KV transfer load failures were not propagated into block invalidation and connector cleanup consistently, letting metrics/scheduler observe invalid state.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives patch base v0.18.0 commit `e18643f8a4d5` and derived image recommendation; no `git apply --check` result in wiki pass.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: issue title and corpus row report metrics exception and internal server error.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: target oracle should verify metrics path no longer throws.
- Traces: unknown.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_08959__kv_load_failure_path_triggers_metrics_exception_and_internal_server_erro/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_08959__kv_load_failure_path_triggers_metrics_exception_and_internal_server_erro/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md), [raw PR #8959 JSON](../../issue_capsule/project_docs/release_image_mapping_20260603/raw_prs/pr_8959.json).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: PD/Mooncake KV transfer failure seed with a recovery request.
- Required oracle: 5xx/liveness, metrics scrape exception, invalid block/log monitor.
- Required monitor: HTTP status, `/metrics`, KV transfer logs; KV events would strengthen it.
- Mutation axes: KV failure timing, shared prefix, request size, connector timeout, fail/retry policy.
- Minimal seed sketch: start PD/Mooncake service, inject or provoke one failed KV transfer, send one request expected to fail gracefully, then send a deterministic recovery request and scrape `/metrics`.
- Why this is or is not fuzzable: HTTP traces alone cannot reliably create transport failure; with fault injection or connector instrumentation, GRIEF-style liveness and metrics oracles should catch it.

## Next Actions
- Immediate next action: run `git apply --check` for PR #8959 on v0.18.0 patch base, then build a derived image only if patch applies.
- Missing evidence: exact reproducer, CANN/torch context, before/after logs, official fixed release image.
- Owner: unknown

