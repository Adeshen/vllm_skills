# Bug Capsule: Single-card multi-service HBM management abnormal

## Identity
- Issue: [vllm-ascend #7308](https://github.com/vllm-project/vllm-ascend/issues/7308)
- Fixing PR: [vllm-ascend #7427](https://github.com/vllm-project/vllm-ascend/pull/7427)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; PR merged in local corpus
- Confidence: high for issue/PR linkage

## Failure Summary
- Failure domain: HBM memory management, worker lifecycle, multi-instance serving
- Failure symptom: HBM memory management abnormal in single-card multi-service scenario.
- Expected behavior: multiple services on one card should account for and release HBM correctly.
- Observed behavior: abnormal HBM management / OOM risk.
- User impact: co-located services can exhaust or leak NPU memory.

## Triggering Workload
- Model: unknown.
- Request shape: single-card multiple service instances.
- Prefix/cache behavior: possible KV/HBM pressure; exact cache behavior unknown.
- Batch/concurrency: multi-instance.
- Sampling params: unknown.
- Distributed/parallel setting: single-card multi-service.
- Quantization: unknown.
- Special runtime flags: unknown.

## Version And Environment
- Affected vLLM-Ascend version: unknown; release mapping uses v0.17.0rc1 as patch base.
- Affected image: `quay.io/ascend/vllm-ascend:v0.17.0rc1` patch base candidate.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: derived `local/vllm-ascend:0.17.0rc1-pr7427`.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend single NPU.
- Container/runtime notes: multi-service HBM tests added.

## Fix Evidence
- Fixing PR: [#7427](https://github.com/vllm-project/vllm-ascend/pull/7427)
- Code diff summary: commit says `fix multi-instance OOM on single card`.
- Files changed: `vllm_ascend/worker/worker.py`, single-card multi-instance tests, worker unit tests, multicard offline inference test updates.
- Suspected root cause: worker memory accounting or cleanup did not handle multiple local instances sharing one NPU.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives v0.17.0rc1 patch base; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: HBM abnormal / OOM.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: HBM usage before/after instances.
- Traces: unknown.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07427__单卡多服务场景下_vllm_ascend_hbm内存管理异常/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07427__单卡多服务场景下_vllm_ascend_hbm内存管理异常/materials/code/changed_files.tsv), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: multi-service lifecycle/load seed.
- Required oracle: HBM baseline delta, OOM, service liveness.
- Required monitor: `npu-smi`/HBM monitor and process lifecycle logs.
- Mutation axes: number of services, request rate, model size, shutdown/restart, memory utilization.
- Minimal seed sketch: start two services on one NPU, send deterministic requests, stop one service, verify HBM returns near baseline and remaining service responds.
- Why this is or is not fuzzable: GRIEF request traces alone cannot start multiple services; a campaign harness around GRIEF can observe the memory lifecycle.

## Next Actions
- Immediate next action: inspect PR tests and reproduce as local multi-instance HBM smoke on npu4 only after confirming spare NPU capacity.
- Missing evidence: exact service commands, HBM readings, before/after results.
- Owner: unknown

