# Bug Reading Workflow

Use this workflow when a new vLLM-Ascend issue arrives. The goal is to turn a vague symptom into a concrete feature-state hypothesis.

## Start With A Story

Before searching for a patch, decide which request story failed:

- Admission/progress story: [SCHEDULER_DEEP_DIVE.md](SCHEDULER_DEEP_DIVE.md)
- Memory reuse story: [KV_CACHE_DEEP_DIVE.md](KV_CACHE_DEEP_DIVE.md)
- Shape/mask story: [ATTENTION_DEEP_DIVE.md](ATTENTION_DEEP_DIVE.md)
- Token-choice story: [SAMPLING_AND_SPEC_DEEP_DIVE.md](SAMPLING_AND_SPEC_DEEP_DIVE.md)
- Client disconnect story: [STREAMING_LIFECYCLE_DEEP_DIVE.md](STREAMING_LIFECYCLE_DEEP_DIVE.md)
- Cross-instance transfer story: [PD_MOONCAKE_DEEP_DIVE.md](PD_MOONCAKE_DEEP_DIVE.md)
- Quantized/expert-routing story: [QUANT_MOE_DEEP_DIVE.md](QUANT_MOE_DEEP_DIVE.md)
- Device/backend lifecycle story: [ASCEND_BACKEND_DEEP_DIVE.md](ASCEND_BACKEND_DEEP_DIVE.md)

## Step 1: Classify The First Visible Failure

| First visible symptom | Start here |
| --- | --- |
| startup/import/device failure | [engine lifecycle](../engine_lifecycle/README.md), [ascend backend](../ascend_backend/README.md) |
| HTTP 500 during request | [scheduler](../scheduler/README.md), [sampling](../sampling/README.md), [metrics/tracing](../metrics_tracing/README.md) |
| hung request, port still open | [scheduler](../scheduler/README.md), [streaming](../streaming/README.md), [distributed](../distributed/README.md) |
| wrong output with HTTP 200 | [sampling](../sampling/README.md), [quantization](../quantization/README.md), [moe](../moe/README.md) |
| error after shared-prefix or long-context workload | [KV cache](../kv_cache/README.md), [prefix cache](../prefix_cache/README.md), [attention](../attention/README.md) |
| PD/proxy/Mooncake error | [prefill/decode disaggregation](../prefill_decode_disaggregation/README.md), [distributed](../distributed/README.md) |

## Step 2: Identify The Stateful Object

Ask:

```text
What state existed before the failing request?
What state was created by the failing request?
What state should have been freed but maybe was not?
What state was reused from another request?
What state crossed a process/device boundary?
```

Examples:

- KV load failure: transferred block state crossed a connector boundary.
- Prefix cache bug: reused block state crossed a request boundary.
- EAGLE repeated-call bug: proposer/attention-mask state survived across many calls.
- CPU binding bug: startup subprocess parsing state crossed a locale boundary.

## Step 3: Map Symptom To Bug Pattern

| Pattern | State hypothesis | Minimal evidence to seek |
| --- | --- | --- |
| crash/500 | an impossible internal state reached error handling | stack trace, request JSON, feature flags |
| hang | scheduler/output/distributed state did not transition | timeout, logs, recovery canary result |
| wrong output | sampler/model/backend state accepted wrong tokens | prompt, deterministic params, reference output |
| metrics exception | observability state failed while recording a different failure | `/metrics` scrape, error logs, labels |
| memory leak/OOM | cleanup or ref-count state failed | HBM before/after, request lifecycle, block count |

## Step 4: Choose The First Reproduction Shape

Prefer smallest seed that creates and then stresses the suspected state:

```text
control -> create state -> reuse or mutate state -> observe failure -> recovery canary
```

Examples:

- Prefix cache: warm -> probe -> mutated suffix -> recovery.
- PD/Mooncake: normal transfer -> failure -> metrics scrape -> recovery.
- Speculative decode: spec off baseline -> spec on -> repeated calls -> recovery.
- Backend lifecycle: startup smoke -> toxic feature -> shutdown -> HBM baseline.

## Step 5: Choose Oracle And Monitor

| Bug class | Oracle | Monitor |
| --- | --- | --- |
| liveness | request completes within timeout | HTTP status, logs |
| output correctness | equals reference or deterministic baseline | response text/token IDs |
| cache consistency | no output drift, no leak, expected cache hit proxy | latency, KV events, HBM |
| distributed failure | explicit error and recovery succeeds | per-role logs, proxy status |
| metrics/tracing | observability endpoint survives toxic trace | `/metrics`, trace backend |

## Step 6: Connect To Existing Wiki

1. Search [feature_to_bug_map](../feature_to_bug_map/README.md) for a similar feature.
2. Open the linked bug capsule.
3. If the bug is new, create a capsule with unknown fields preserved.
4. Add a feature-page note only after the state pattern is clear.

## Good Working Hypotheses

Good:

```text
PD/Mooncake transfer failure leaves invalid block IDs visible to metrics path.
```

Too vague:

```text
Mooncake is broken.
```

Good:

```text
Speculative block verify accepts/rejects tokens with wrong h_block or p_i index.
```

Too vague:

```text
Spec decode output is bad.
```

Good:

```text
Qwen3 W8A8 dense model is missing packed module mapping, causing wrong quantized layer execution.
```

Too vague:

```text
Quantization is inaccurate.
```
