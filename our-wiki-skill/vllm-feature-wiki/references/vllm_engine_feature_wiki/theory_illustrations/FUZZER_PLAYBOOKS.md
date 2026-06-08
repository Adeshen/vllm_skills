# Fuzzer Playbooks

These playbooks translate feature theory into GRIEF-style or verification-style tests. They are intentionally generic; fill in exact model, image, and command only when local evidence supports it.

## Theory Map

| Playbook area | Deep dive | Best feature pages |
| --- | --- | --- |
| Shared prefix and KV reuse | [KV_CACHE_DEEP_DIVE.md](KV_CACHE_DEEP_DIVE.md) | [KV cache](../kv_cache/README.md), [prefix cache](../prefix_cache/README.md) |
| Scheduler liveness | [SCHEDULER_DEEP_DIVE.md](SCHEDULER_DEEP_DIVE.md) | [scheduler](../scheduler/README.md), [engine lifecycle](../engine_lifecycle/README.md) |
| Attention shape/context behavior | [ATTENTION_DEEP_DIVE.md](ATTENTION_DEEP_DIVE.md) | [attention](../attention/README.md) |
| Sampling/speculative correctness | [SAMPLING_AND_SPEC_DEEP_DIVE.md](SAMPLING_AND_SPEC_DEEP_DIVE.md) | [sampling](../sampling/README.md), [speculative decoding](../speculative_decoding/README.md) |
| Streaming/cancel cleanup | [STREAMING_LIFECYCLE_DEEP_DIVE.md](STREAMING_LIFECYCLE_DEEP_DIVE.md) | [streaming](../streaming/README.md), [engine lifecycle](../engine_lifecycle/README.md) |
| PD/Mooncake failure paths | [PD_MOONCAKE_DEEP_DIVE.md](PD_MOONCAKE_DEEP_DIVE.md) | [prefill/decode disaggregation](../prefill_decode_disaggregation/README.md), [distributed](../distributed/README.md), [metrics/tracing](../metrics_tracing/README.md) |
| Quantization/MoE output correctness | [QUANT_MOE_DEEP_DIVE.md](QUANT_MOE_DEEP_DIVE.md) | [quantization](../quantization/README.md), [moe](../moe/README.md) |
| Ascend backend lifecycle | [ASCEND_BACKEND_DEEP_DIVE.md](ASCEND_BACKEND_DEEP_DIVE.md) | [ascend backend](../ascend_backend/README.md), [engine lifecycle](../engine_lifecycle/README.md) |

## 1. Shared Prefix Cache Playbook

```text
control short request
warm request with long shared prefix
probe request with same prefix and different suffix
mutated-prefix request near block boundary
recovery canary
```

Mutation axes:

- shared prefix length
- suffix length
- boundary alignment
- batch/concurrency
- cache hash algorithm if exposed

Oracles:

- deterministic output stability
- latency/cache-hit proxy
- no 5xx
- no final cache/HBM leak

Best feature pages:

- [prefix cache](../prefix_cache/README.md)
- [KV cache](../kv_cache/README.md)

## 2. PD/Mooncake Failure-Path Playbook

```text
PD health canary
normal transfer request
induced or approximated transfer failure
/metrics scrape
decode-side recovery canary
prefill-side recovery canary
```

Mutation axes:

- connector type
- timeout/failure timing
- prompt length
- layerwise mode
- streaming/proxy path

Oracles:

- failure is explicit, not silent close
- metrics endpoint survives
- invalid blocks are not reused
- recovery canary succeeds

Best feature pages:

- [prefill/decode disaggregation](../prefill_decode_disaggregation/README.md)
- [distributed](../distributed/README.md)
- [metrics/tracing](../metrics_tracing/README.md)

## 3. Scheduler Liveness Playbook

```text
control request
burst of mixed short and long prompts
one toxic long/chunked/MTP request
short recovery canary under timeout
repeat with streaming enabled
```

Mutation axes:

- concurrency
- prompt length
- max tokens
- chunked prefill
- decode-only/full-decode-only mode
- graph/MTP on/off

Oracles:

- no hung request
- recovery canary completes
- no scheduler/proposer traceback
- latency does not explode beyond threshold

Best feature pages:

- [scheduler](../scheduler/README.md)
- [engine lifecycle](../engine_lifecycle/README.md)

## 4. Speculative Correctness Playbook

```text
baseline non-spec deterministic request
same prompt with speculative/MTP/EAGLE/suffix mode
repeated calls to exercise reused proposer state
recovery canary
```

Mutation axes:

- proposal length
- max tokens
- prompt family
- repeated-call count
- batch shape
- graph/FlashComm/MoE on/off

Oracles:

- deterministic output equivalence where expected
- accepted-token accounting
- no attention-mask index error
- no shape mismatch

Best feature pages:

- [speculative decoding](../speculative_decoding/README.md)
- [sampling](../sampling/README.md)
- [attention](../attention/README.md)

## 5. Streaming Lifecycle Playbook

```text
streaming control request
disconnect before first token
disconnect after first token
cancel long stream
recovery canary
```

Mutation axes:

- disconnect timing
- max tokens
- prompt length
- retry delay
- concurrency
- proxy/PD path

Oracles:

- no tokens after cancel
- no output handler 5xx
- request count returns to baseline
- recovery canary succeeds

Best feature pages:

- [streaming](../streaming/README.md)
- [engine lifecycle](../engine_lifecycle/README.md)

## 6. Quantization/Output Correctness Playbook

```text
reference backend or known-good model response
quantized vLLM-Ascend response
same prompt in batch with unrelated request
same prompt after warm cache
```

Mutation axes:

- quantization mode
- model family
- prompt type
- batch shape
- max tokens

Oracles:

- exact copy/factual output where possible
- reference-model comparison
- garbled text heuristic as weak signal
- batch invariance

Best feature pages:

- [quantization](../quantization/README.md)
- [sampling](../sampling/README.md)
- [moe](../moe/README.md)

## 7. Ascend Backend Lifecycle Playbook

```text
host device inspection
container device inspection
import smoke
/v1/models
tiny deterministic generation
feature-specific toxic trace
shutdown or restart
HBM baseline check
```

Mutation axes:

- visible device IDs
- model family
- graph mode
- quantization
- multi-instance count
- CPU locale

Oracles:

- startup health
- tiny generation works
- HBM returns near baseline
- logs contain no device-count or custom-op error

Best feature pages:

- [ascend backend](../ascend_backend/README.md)
- [engine lifecycle](../engine_lifecycle/README.md)
