# Bug Capsule: W8A8 per-token Qwen3 garbled output

## Identity
- Issue: [vllm-ascend #2318](https://github.com/vllm-project/vllm-ascend/issues/2318)
- Fixing PR: [vllm-ascend #7248](https://github.com/vllm-project/vllm-ascend/pull/7248)
- Related PRs: unknown
- Repository: `vllm-project/vllm-ascend`
- Status: issue status unknown locally; PR open in local corpus
- Confidence: medium; strong issue/PR link but not a merged fix

## Failure Summary
- Failure domain: quantization, Qwen3 dense model mapping, output correctness
- Failure symptom: W8A8 per-token quantized Qwen3 generates garbled output in vLLM but works in Transformers.
- Expected behavior: quantized Qwen3 output should be coherent and match reference behavior.
- Observed behavior: garbled output.
- User impact: quantized serving can silently return unusable text.

## Triggering Workload
- Model: Qwen3 W8A8 per-token quantized dense model.
- Request shape: inference request; exact prompt unknown.
- Prefix/cache behavior: unknown.
- Batch/concurrency: unknown.
- Sampling params: unknown.
- Distributed/parallel setting: unknown.
- Quantization: W8A8 per-token quantization.
- Special runtime flags: modelsllim quantization config path implied by diff.

## Version And Environment
- Affected vLLM-Ascend version: unknown.
- Affected image: unknown.
- Fixed vLLM-Ascend version: not fixed in local evidence; PR open.
- Fixed image: unknown.
- Upstream vLLM version: unknown.
- CANN version: unknown.
- torch / torch-npu: unknown.
- Hardware: Ascend NPU.
- Container/runtime notes: local npu4 has historical Qwen3-1.7B-W4A8-V1 smoke evidence, but this issue is W8A8 per-token Qwen3 and should not be conflated.

## Fix Evidence
- Fixing PR: [#7248](https://github.com/vllm-project/vllm-ascend/pull/7248)
- Code diff summary: commit says `fix: add qwen3 dense model to packed_modules_model_mapping`.
- Files changed: `vllm_ascend/quantization/modelslim_config.py`.
- Suspected root cause: Qwen3 dense model missing from packed modules mapping caused wrong quantized layer handling.
- Patch applies to affected commit: unknown.
- Patch application evidence: code material has base/head commits, but PR is open and no release mapping/apply check recorded.

## Reproduction Evidence
- Reproduction status: not reproduced in this wiki construction pass.
- Before-fix command: unknown.
- Before-fix result: garbled output.
- After-fix command: unknown.
- After-fix result: unknown; PR open.
- Logs: unknown.
- Metrics: output/reference text comparison.
- Traces: unknown.
- Artifacts: [PR case README](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07248__w8a8_per_token_quantized_qwen3_generates_garbled_output_in_vllm_but_work/README.md), [changed files](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/prs/pr_07248__w8a8_per_token_quantized_qwen3_generates_garbled_output_in_vllm_but_work/materials/code/changed_files.tsv).

## Fuzzer Discoverability
- Could GRIEF find this bug: partial.
- Required seed type: quantized Qwen3 deterministic output seed.
- Required oracle: reference backend comparison or text-quality heuristic.
- Required monitor: output text comparator.
- Mutation axes: quantization mode, model family, prompt, max tokens.
- Minimal seed sketch: ask a deterministic factual or copy task on quantized Qwen3 and compare against Transformers or unquantized baseline.
- Why this is or is not fuzzable: request trigger is simple, but garbled output needs a semantic/differential oracle.

## Next Actions
- Immediate next action: locate exact Qwen3 W8A8 model path and reference prompt from issue #2318.
- Missing evidence: affected release, model artifact, prompt, before/after output.
- Owner: unknown

