# vLLM Bug Wiki Examples

## Example 1: "Create capsule for issue #7871"

1. Search local evidence for `7871` and PR number.
2. Read issue cache, PR-centric corpus, release mapping, and existing fuzzer docs.
3. Fill capsule fields from evidence only.
4. Link related feature pages: KV cache, PD, metrics/tracing.
5. Update `INDEX.md`, workload pattern, and fuzzer findability if needed.
6. Validate.

## Example 2: "Add CPU CI failure"

1. Open CPU CI report.
2. Identify test path, exception, expected schema, and dependency context.
3. Create a capsule with `Fuzzer Discoverability: no` unless request-level reproduction exists.
4. Link `ci_and_environment/README.md`.
5. Leave release/image fields `unknown` if not proven.

## Example 3: "Refresh release matrix after a new image"

1. Open release/image/bugfix mapping.
2. Verify image tag, vLLM-Ascend version, upstream vLLM version, and CANN context from primary sources.
3. Update `release_matrix/README.md`.
4. Do not claim a bug is fixed in an image unless mapping or PR evidence supports it.

## Example 4: "Assess if GRIEF can find a bug"

1. Identify whether the symptom appears through HTTP request behavior, metrics, logs, or startup only.
2. Map to seed type: shared prefix, long prefill, streaming cancel, PD transfer, structured output, quantized correctness, MoE shape, lifecycle.
3. Pick oracle and monitor.
4. Mark `partial` if special NPU mode or backend instrumentation is required.

## Example 5: "Attach a verification skill route"

1. Read `references/vllm_skills.md`.
2. Choose the closest official skill: deploy, endpoint benchmark, random synthetic benchmark, or prefix-cache benchmark.
3. Add the route to `Next Actions` or `Reproduction Evidence` as a plan, not as completed evidence.
4. Preserve exact commands as `unknown` until they are adapted to the local Ascend environment.
