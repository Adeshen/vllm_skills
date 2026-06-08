# State Invariants

Use this page as a bug-hunting checklist. A feature is healthy when these invariants keep holding across control, toxic, and recovery traces.

## Deep Dive Links

- Scheduler invariants: [SCHEDULER_DEEP_DIVE.md](SCHEDULER_DEEP_DIVE.md)
- KV/prefix invariants: [KV_CACHE_DEEP_DIVE.md](KV_CACHE_DEEP_DIVE.md)
- Attention invariants: [ATTENTION_DEEP_DIVE.md](ATTENTION_DEEP_DIVE.md)
- Sampling/speculative invariants: [SAMPLING_AND_SPEC_DEEP_DIVE.md](SAMPLING_AND_SPEC_DEEP_DIVE.md)
- Streaming/cancel invariants: [STREAMING_LIFECYCLE_DEEP_DIVE.md](STREAMING_LIFECYCLE_DEEP_DIVE.md)
- Distributed PD invariants: [PD_MOONCAKE_DEEP_DIVE.md](PD_MOONCAKE_DEEP_DIVE.md)
- Quant/MoE invariants: [QUANT_MOE_DEEP_DIVE.md](QUANT_MOE_DEEP_DIVE.md)
- Ascend backend invariants: [ASCEND_BACKEND_DEEP_DIVE.md](ASCEND_BACKEND_DEEP_DIVE.md)

## Request Lifecycle Invariants

| Invariant | Why it matters | Good test shape |
| --- | --- | --- |
| Every admitted request eventually reaches finished, failed, or cancelled. | Prevents scheduler limbo. | toxic request + timeout + recovery canary |
| Cleanup runs exactly once per request. | Prevents leaks and double-free behavior. | cancel/disconnect + logs + recovery canary |
| HTTP response state matches engine state. | Avoids proxy/client seeing success while engine failed. | force error path and inspect body/status |
| Recovery canary succeeds after toxic trace. | Catches stale global state. | control -> toxic -> recovery |

## KV Cache Invariants

| Invariant | Why it matters | Good test shape |
| --- | --- | --- |
| A physical KV block is either free or owned by one or more active/cache references. | Prevents premature reuse. | repeated shared-prefix requests |
| `ref_cnt` increases when a cached block is reused and decreases when request releases it. | Prevents leaks and stale blocks. | warm/probe/free/reuse trace |
| A block hash is assigned only when the block is full and cacheable. | Prevents false prefix hits. | boundary-length prompts |
| Parent hash and extra hashes distinguish different logical prefixes. | Prevents cross-adapter/multimodal/security cache confusion. | same tokens with different LoRA/media/cache salt |
| Transfer-failed blocks are invalidated before scheduler or metrics observes them as usable. | Prevents #7871-style failure paths. | PD failure injection + `/metrics` scrape |

## Scheduler Invariants

| Invariant | Why it matters | Good test shape |
| --- | --- | --- |
| Running set, waiting queue, and KV capacity agree. | Prevents starvation or over-admission. | mixed short/long burst |
| Finished requests release resource pressure before next admission decision. | Prevents false OOM or low throughput. | high-turnover small requests |
| Long prefill does not permanently block decode progress. | Protects tail latency. | long prompt + short canary stream |
| Graph/dynamic batch modes do not assume impossible shapes. | Prevents graph hang or shape crash. | shape sweep around chunk/batch boundaries |

## Distributed/PD Invariants

| Invariant | Why it matters | Good test shape |
| --- | --- | --- |
| Producer, connector, and consumer agree on each transfer's status. | Prevents partial state. | induced transfer failure |
| Proxy returns a clear client-visible result for downstream errors. | Prevents silent closes. | overlength or failed PD request |
| Rank/process failure is propagated to scheduler and metrics. | Prevents stuck service. | kill/fail one role in controlled test |
| Transfer cleanup handles both success and failure. | Prevents stale KV or resource leak. | fail -> recovery canary |

## Sampling And Speculative Invariants

| Invariant | Why it matters | Good test shape |
| --- | --- | --- |
| Accepted speculative tokens match target-model verification. | Prevents silent correctness bugs. | spec off/on deterministic comparison |
| Rejected draft tokens do not mutate committed KV/output state. | Prevents future token corruption. | prompts with forced rejection patterns |
| Structured-output bitmask shape/type matches sampler expectation. | Prevents xgrammar errors. | JSON schema smoke |
| Deterministic request is stable across batch shapes. | Catches batch invariance bugs. | single request vs same request inside batch |

## Ascend Backend Invariants

| Invariant | Why it matters | Good test shape |
| --- | --- | --- |
| Container sees the same NPU IDs as host inspection expects. | Avoids false vLLM-argument debugging. | `npu-smi` host/container smoke |
| Model path uses `/mnt/data2/model_weights` for new runs. | Avoids stale volume assumptions. | startup command review |
| HBM returns near baseline after service lifecycle. | Catches multi-instance leaks. | start two services -> stop one -> measure |
| CPU binding parsing is locale-stable. | Prevents startup failures on Chinese OS language. | `LANG=C` and Chinese locale unit tests |
| Quantization/backend model mapping matches model family. | Prevents garbled output. | reference comparison on quantized model |
