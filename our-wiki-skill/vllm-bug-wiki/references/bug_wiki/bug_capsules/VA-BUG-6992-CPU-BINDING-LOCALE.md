# Bug Capsule: CPU binding fails under Chinese OS locale

## Identity
- Issue: [vllm-ascend #6992](https://github.com/vllm-project/vllm-ascend/issues/6992)
- Fixing PR: [#7266](https://github.com/vllm-project/vllm-ascend/pull/7266), [#7274](https://github.com/vllm-project/vllm-ascend/pull/7274), [#8251](https://github.com/vllm-project/vllm-ascend/pull/8251)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue closed; all three PRs merged in local corpus
- Confidence: high for issue/PR linkage

## Failure Summary
- Failure domain: CPU binding, device allocator, subprocess locale parsing
- Failure symptom: CPU binding may fail when the OS language is Chinese.
- Expected behavior: CPU binding should parse device/process output independent of host language.
- Observed behavior: locale-dependent parsing failure.
- User impact: server startup or worker placement can fail on non-English hosts.

## Triggering Workload
- Model: unknown.
- Request shape: startup/environment path, not request-specific.
- Prefix/cache behavior: none.
- Batch/concurrency: none.
- Sampling params: none.
- Distributed/parallel setting: CPU binding for NPU process placement.
- Quantization: unknown.
- Special runtime flags: host `LANG` or subprocess locale.

## Version And Environment
- Affected vLLM-Ascend version: unknown; release mapping uses v0.16.0rc1 and v0.18.0rc1 as patch bases for related fixes.
- Affected image: patch base candidates include `v0.16.0rc1` and `v0.18.0rc1`.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: derived PR images `local/vllm-ascend:0.16.0rc1-pr7266`, `local/vllm-ascend:0.16.0rc1-pr7274`, `local/vllm-ascend:0.18.0rc1-pr8251`.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend NPU host where `npu-smi`/process output is localized.
- Container/runtime notes: enforce `LANG=C` for CPU binding subprocesses per PR commit messages.

## Fix Evidence
- Fixing PR: [#7266](https://github.com/vllm-project/vllm-ascend/pull/7266), [#7274](https://github.com/vllm-project/vllm-ascend/pull/7274), [#8251](https://github.com/vllm-project/vllm-ascend/pull/8251)
- Code diff summary: robustly parse `npu-smi` process rows and enforce C locale for CPU binding subprocesses.
- Files changed: `vllm_ascend/cpu_binding.py`, `tests/ut/device_allocator/test_cpu_binding.py`.
- Suspected root cause: parser assumed English output/locale-sensitive subprocess behavior.
- Patch applies to affected commit: unknown.
- Patch application evidence: release mapping gives patch-base rows for all three PRs; no apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: CPU binding may fail under Chinese OS language.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: none.
- Traces: none.
- Artifacts: [PR #7266 case](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07266__bug_cpu_binding_may_fail_where_the_operating_system_language_is_chinese/README.md), [PR #7274 case](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07274__bug_cpu_binding_may_fail_where_the_operating_system_language_is_chinese/README.md), [PR #8251 case](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_08251__bug_cpu_binding_may_fail_where_the_operating_system_language_is_chinese/README.md), [release mapping](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md).

## Fuzzer Discoverability
- Could GRIEF find this bug: no.
- Required seed type: environment/startup test with localized host process output.
- Required oracle: startup failure or unit-test failure.
- Required monitor: subprocess stderr/traceback.
- Mutation axes: `LANG`, localized `npu-smi` output fixture, CPU binding enabled/disabled.
- Minimal seed sketch: run CPU binding unit test with Chinese locale or mocked localized `npu-smi` rows.
- Why this is or is not fuzzable: the failure occurs before healthy HTTP serving and is not request-triggered.

## Next Actions
- Immediate next action: run CPU binding unit tests with `LANG=zh_CN.UTF-8` and `LANG=C` in a controlled environment.
- Missing evidence: exact issue command, before/after unit result, affected release.
- Owner: unknown

