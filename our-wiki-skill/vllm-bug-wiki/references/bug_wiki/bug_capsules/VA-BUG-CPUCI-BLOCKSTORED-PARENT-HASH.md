# Bug Capsule: CPU CI `BlockStored` parent block hash failure

## Identity
- Issue: local CPU CI failure, no GitHub issue identified
- Fixing PR: unknown
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: evidence path requested but not found locally during wiki construction
- Confidence: low until the CPU CI report is available

## Failure Summary
- Failure domain: CPU/mock CI, distributed ascend store, KV transfer unit test
- Failure symptom: `tests/ut/distributed/ascend_store/test_kv_transfer.py` failure where `BlockStored` requires `parent_block_hash`.
- Expected behavior: CPU/mock CI test should construct `BlockStored` with required fields or adapt to current API.
- Observed behavior: unknown; prompt states `BlockStored` requires `parent_block_hash`.
- User impact: CPU CI feasibility is blocked or noisy for KV transfer tests.

## Triggering Workload
- Model: none.
- Request shape: unit test.
- Prefix/cache behavior: KV transfer metadata.
- Batch/concurrency: none.
- Sampling params: none.
- Distributed/parallel setting: CPU/mock distributed ascend store test.
- Quantization: none.
- Special runtime flags: unknown.

## Version And Environment
- Affected vLLM-Ascend version: unknown.
- Affected image: unknown.
- Fixed vLLM-Ascend version: unknown.
- Fixed image: unknown.
- Upstream vLLM version: unknown.
- CANN version: not applicable or unknown.
- torch / torch-npu: unknown.
- Hardware: CPU/mock CI.
- Container/runtime notes: requested report path `/mnt/data/vllm_observe/vllm_ascend_cpu_ci_check/report_20260603/CPU_CI_FEASIBILITY_REPORT.md` did not exist on this machine at wiki construction time.

## Fix Evidence
- Fixing PR: unknown.
- Code diff summary: unknown.
- Files changed: unknown.
- Suspected root cause: unit-test fixture or compatibility layer did not include new `BlockStored.parent_block_hash` required field.
- Patch applies to affected commit: unknown.
- Patch application evidence: unknown.

## Reproduction Evidence
- Reproduction status: source report not available locally.
- Before-fix command: unknown.
- Before-fix result: prompt reports `BlockStored` requires `parent_block_hash`.
- After-fix command: unknown.
- After-fix result: unknown.
- Logs: unknown.
- Metrics: CI pass/fail.
- Traces: none.
- Artifacts: requested CPU CI report path was searched but not found; no local artifact link available.

## Fuzzer Discoverability
- Could GRIEF find this bug: no.
- Required seed type: unit test / CPU CI fixture.
- Required oracle: pytest failure.
- Required monitor: CI logs.
- Mutation axes: dependency version, `BlockStored` fixture shape.
- Minimal seed sketch: run `tests/ut/distributed/ascend_store/test_kv_transfer.py` in CPU/mock CI environment.
- Why this is or is not fuzzable: this is a test/API compatibility failure, not an inference request-triggered server bug.

## Next Actions
- Immediate next action: recover or regenerate the CPU CI feasibility report and link it here.
- Missing evidence: full traceback, dependency versions, failing commit, fix PR.
- Owner: unknown

