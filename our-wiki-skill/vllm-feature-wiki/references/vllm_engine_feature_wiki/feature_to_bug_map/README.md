# Feature To Bug Map

This map links feature state to current bug capsules. It is intentionally evidence-limited: if a workload trigger or verification test is not present in local evidence, it remains `unknown`.

Use this map after reading the feature page. The table below links the bug capsule; the theory/playbook table after it links the state-machine explanation and fuzzer strategy.

| Feature | Related bug capsule | Failure symptom | Workload trigger | Fuzzer seed type | Verification test |
| --- | --- | --- | --- | --- | --- |
| Engine lifecycle | [VA-BUG-6992-CPU-BINDING-LOCALE](../../bug_wiki/bug_capsules/VA-BUG-6992-CPU-BINDING-LOCALE.md) | startup/device placement failure | localized CPU binding subprocess output | not a GRIEF target | CPU binding unit tests with locale control |
| Engine lifecycle | [VA-BUG-7308-MULTI-INSTANCE-HBM](../../bug_wiki/bug_capsules/VA-BUG-7308-MULTI-INSTANCE-HBM.md) | HBM memory abnormal / OOM | single-card multi-service lifecycle | lifecycle harness plus request canaries | HBM baseline before/after service lifecycle |
| KV cache | [VA-BUG-7871-KV-LOAD-FAILURE-METRICS](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md) | metrics exception and internal server error | `kv_load_failure_policy=fail`, PD/Mooncake transfer failure | PD transfer-failure trace with recovery canary | Mooncake connector failure-path test and `/metrics` scrape |
| KV cache | [VA-BUG-6273-KVPOOL-LAYERWISE-POOLING](../../bug_wiki/bug_capsules/VA-BUG-6273-KVPOOL-LAYERWISE-POOLING.md) | pooling function abnormal | `use_layerwise=true` for pooling KV transfer config | pooling endpoint compare layerwise off/on | KV pool integration test, exact command unknown |
| KV cache | [VA-BUG-CPUCI-BLOCKSTORED-PARENT-HASH](../../bug_wiki/bug_capsules/VA-BUG-CPUCI-BLOCKSTORED-PARENT-HASH.md) | CPU CI fixture/API failure | `BlockStored` requires `parent_block_hash` | not a GRIEF target | `tests/ut/distributed/ascend_store/test_kv_transfer.py` |
| Prefix cache | [VA-BUG-5445-CHUNK-PREFILL-LONG-SEQUENCE](../../bug_wiki/bug_capsules/VA-BUG-5445-CHUNK-PREFILL-LONG-SEQUENCE.md) | long-sequence chunk prefill bug | long sequence with chunked prefill | boundary-length prompt with recovery canary | `tests/e2e/multicard/long_sequence/test_chunked_prefill.py` |
| Scheduler | [VA-BUG-4986-MTP-FULL-DECODE-HANG](../../bug_wiki/bug_capsules/VA-BUG-4986-MTP-FULL-DECODE-HANG.md) | server hang | FULL_DECODE_ONLY with MTP on DeepSeek V3.1 | MTP full-decode request plus recovery canary | MTP ACL graph integration test, exact command unknown |
| Scheduler | [VA-BUG-5445-CHUNK-PREFILL-LONG-SEQUENCE](../../bug_wiki/bug_capsules/VA-BUG-5445-CHUNK-PREFILL-LONG-SEQUENCE.md) | long prefill path does not complete correctly | long sequence with chunked prefill | long prompt around chunk boundary | e2e chunked prefill test |
| Attention | [VA-BUG-3024-EAGLE-ATTN-MASK-REPEATED-CALLS](../../bug_wiki/bug_capsules/VA-BUG-3024-EAGLE-ATTN-MASK-REPEATED-CALLS.md) | `attn_mask index out of range` | more than 100 calls to EAGLE Qwen3-8B | repeated EAGLE request loop | repeated-call EAGLE smoke, exact command unknown |
| Attention | [VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE](../../bug_wiki/bug_capsules/VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE.md) | tensor dimension mismatch | Qwen3.5 MoE with MTP and FLASHCOMM1 | special model/backend smoke | Qwen3.5 MoE MTP FlashComm startup/generation smoke |
| Sampling | [VA-BUG-7807-BLOCK-VERIFY-REJECTION-SAMPLING](../../bug_wiki/bug_capsules/VA-BUG-7807-BLOCK-VERIFY-REJECTION-SAMPLING.md) | incorrect block verify behavior | block verify in rejection sampling | deterministic spec-decode baseline comparison | `tests/ut/sample/test_rejection_sampler.py` |
| Sampling | [VA-BUG-5524-XGRAMMAR-TYPE-MISMATCH](../../bug_wiki/bug_capsules/VA-BUG-5524-XGRAMMAR-TYPE-MISMATCH.md) | xgrammar type mismatch | structured output bitmask application | JSON/schema structured-output request | schema validation plus dependency check |
| Streaming | unknown | cancel/disconnect lifecycle failure | unknown | streaming request -> disconnect/cancel -> recovery canary | GRIEF streaming seed smoke; cancel test missing |
| Speculative decoding | [VA-BUG-7807-BLOCK-VERIFY-REJECTION-SAMPLING](../../bug_wiki/bug_capsules/VA-BUG-7807-BLOCK-VERIFY-REJECTION-SAMPLING.md) | incorrect accepted-token/block verify behavior | rejection sampling block verify | spec off/on deterministic comparison | `tests/ut/sample/test_rejection_sampler.py` |
| Speculative decoding | [VA-BUG-4986-MTP-FULL-DECODE-HANG](../../bug_wiki/bug_capsules/VA-BUG-4986-MTP-FULL-DECODE-HANG.md) | server hang | FULL_DECODE_ONLY with MTP on DeepSeek V3.1 | MTP request plus recovery canary | MTP ACL graph integration test, exact command unknown |
| Speculative decoding | [VA-BUG-3024-EAGLE-ATTN-MASK-REPEATED-CALLS](../../bug_wiki/bug_capsules/VA-BUG-3024-EAGLE-ATTN-MASK-REPEATED-CALLS.md) | `attn_mask index out of range` | more than 100 calls to EAGLE Qwen3-8B | repeated EAGLE request loop | repeated-call EAGLE smoke, exact command unknown |
| LoRA | unknown | adapter isolation or load failure | unknown | base -> adapter A -> adapter B -> adapter A | adapter deterministic isolation test |
| Quantization | [VA-BUG-2318-W8A8-QWEN3-GARBLED](../../bug_wiki/bug_capsules/VA-BUG-2318-W8A8-QWEN3-GARBLED.md) | garbled output | W8A8 per-token quantized Qwen3 | deterministic prompt with reference output | reference comparison against known-good backend |
| MoE | [VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE](../../bug_wiki/bug_capsules/VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE.md) | tensor dimension mismatch | Qwen3.5 MoE with MTP and FLASHCOMM1 | MoE/MTP/FlashComm service smoke | startup/generation avoids shape error |
| MoE | [VA-BUG-8463-GPTOSS-MOE-OUTPUT-CORRECTNESS](../../bug_wiki/bug_capsules/VA-BUG-8463-GPTOSS-MOE-OUTPUT-CORRECTNESS.md) | incorrect inference result | GPT-OSS 120B inference | deterministic prompt with semantic/reference oracle | output comparison, exact prompt unknown |
| Distributed | [VA-BUG-6992-CPU-BINDING-LOCALE](../../bug_wiki/bug_capsules/VA-BUG-6992-CPU-BINDING-LOCALE.md) | CPU binding parse failure | Chinese OS language affects CPU binding parsing | not a GRIEF target | CPU binding unit tests with locale control |
| Distributed | [VA-BUG-7871-KV-LOAD-FAILURE-METRICS](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md) | PD/Mooncake failure escalates to 500/metrics exception | KV transfer failure | PD failure injection plus recovery canary | Mooncake connector tests and PD smoke |
| Prefill/decode disaggregation | [VA-BUG-7871-KV-LOAD-FAILURE-METRICS](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md) | transfer failure not handled cleanly | failed KV cache transmission | PD transfer-failure trace | before/after PD transfer failure test |
| Metrics/tracing | [VA-BUG-7871-KV-LOAD-FAILURE-METRICS](../../bug_wiki/bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md) | metrics exception on failure path | KV load failure | toxic trace followed by `/metrics` scrape | metrics endpoint must survive failure |
| Ascend backend | [VA-BUG-7308-MULTI-INSTANCE-HBM](../../bug_wiki/bug_capsules/VA-BUG-7308-MULTI-INSTANCE-HBM.md) | HBM memory abnormal / OOM | single-card multi-service | multi-service lifecycle plus request canaries | HBM baseline before/after service lifecycle |
| Ascend backend | [VA-BUG-6992-CPU-BINDING-LOCALE](../../bug_wiki/bug_capsules/VA-BUG-6992-CPU-BINDING-LOCALE.md) | startup/device placement failure | localized CPU binding subprocess output | not a GRIEF target | CPU binding locale unit test |
| Ascend backend | [VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE](../../bug_wiki/bug_capsules/VA-BUG-7996-MOE-MTP-FLASHCOMM-SHAPE.md) | custom op/backend shape mismatch | Qwen3.5 MoE + MTP + FLASHCOMM1 | special backend smoke | MoE/FlashComm generation smoke |

## Notes

- The strongest current request-fuzzer targets are scheduler liveness, KV/prefix cache, PD transfer, streaming lifecycle, and shape-crash cases where the target environment is already configured.
- Output correctness and quantization cases need reference or differential oracles.
- Startup, dependency, CPU binding, and CPU CI failures are valuable verification targets but not GRIEF HTTP-trace targets.

## Playbook And Deep-Dive Links

| Feature | Best deep dive | Best playbook |
| --- | --- | --- |
| Engine lifecycle | [ASCEND_BACKEND_DEEP_DIVE.md](../theory_illustrations/ASCEND_BACKEND_DEEP_DIVE.md) | [Ascend Backend Lifecycle Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#7-ascend-backend-lifecycle-playbook) |
| Scheduler | [SCHEDULER_DEEP_DIVE.md](../theory_illustrations/SCHEDULER_DEEP_DIVE.md) | [Scheduler Liveness Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#3-scheduler-liveness-playbook) |
| KV cache | [KV_CACHE_DEEP_DIVE.md](../theory_illustrations/KV_CACHE_DEEP_DIVE.md) | [Shared Prefix Cache Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#1-shared-prefix-cache-playbook) |
| Prefix cache | [KV_CACHE_DEEP_DIVE.md](../theory_illustrations/KV_CACHE_DEEP_DIVE.md) | [Shared Prefix Cache Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#1-shared-prefix-cache-playbook) |
| Attention | [ATTENTION_DEEP_DIVE.md](../theory_illustrations/ATTENTION_DEEP_DIVE.md) | [Speculative Correctness Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#4-speculative-correctness-playbook) |
| Sampling | [SAMPLING_AND_SPEC_DEEP_DIVE.md](../theory_illustrations/SAMPLING_AND_SPEC_DEEP_DIVE.md) | [Speculative Correctness Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#4-speculative-correctness-playbook) |
| Streaming | [STREAMING_LIFECYCLE_DEEP_DIVE.md](../theory_illustrations/STREAMING_LIFECYCLE_DEEP_DIVE.md) | [Streaming Lifecycle Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#5-streaming-lifecycle-playbook) |
| Speculative decoding | [SAMPLING_AND_SPEC_DEEP_DIVE.md](../theory_illustrations/SAMPLING_AND_SPEC_DEEP_DIVE.md) | [Speculative Correctness Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#4-speculative-correctness-playbook) |
| LoRA | [KV_CACHE_DEEP_DIVE.md](../theory_illustrations/KV_CACHE_DEEP_DIVE.md) | Adapter isolation seed in [Fuzzer Playbooks](../theory_illustrations/FUZZER_PLAYBOOKS.md) is still `unknown` / missing |
| Quantization | [QUANT_MOE_DEEP_DIVE.md](../theory_illustrations/QUANT_MOE_DEEP_DIVE.md) | [Quantization/Output Correctness Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#6-quantizationoutput-correctness-playbook) |
| MoE | [QUANT_MOE_DEEP_DIVE.md](../theory_illustrations/QUANT_MOE_DEEP_DIVE.md) | [Quantization/Output Correctness Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#6-quantizationoutput-correctness-playbook) |
| Distributed | [PD_MOONCAKE_DEEP_DIVE.md](../theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md) | [PD/Mooncake Failure-Path Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#2-pdmooncake-failure-path-playbook) |
| Prefill/decode disaggregation | [PD_MOONCAKE_DEEP_DIVE.md](../theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md) | [PD/Mooncake Failure-Path Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#2-pdmooncake-failure-path-playbook) |
| Metrics/tracing | [PD_MOONCAKE_DEEP_DIVE.md](../theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md) | [PD/Mooncake Failure-Path Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#2-pdmooncake-failure-path-playbook) |
| Ascend backend | [ASCEND_BACKEND_DEEP_DIVE.md](../theory_illustrations/ASCEND_BACKEND_DEEP_DIVE.md) | [Ascend Backend Lifecycle Playbook](../theory_illustrations/FUZZER_PLAYBOOKS.md#7-ascend-backend-lifecycle-playbook) |
