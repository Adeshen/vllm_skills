# Distributed / PD

## Common Failure Symptoms
- KV transfer failure poisons subsequent requests.
- Proxy closes request without returning useful error.
- P/D nodes hang while ports remain open.
- Multi-node or PP/DP topology hits KV key errors.

## Issue/PR Examples
- [VA-BUG-7871](../bug_capsules/VA-BUG-7871-KV-LOAD-FAILURE-METRICS.md): PD/Mooncake KV transfer failure handling.
- [VA-BUG-6273](../bug_capsules/VA-BUG-6273-KVPOOL-LAYERWISE-POOLING.md): KV pool layerwise pooling transfer.
- Open corpus cases #8975/#9149 and #2649/#9046 are good future PD capsules after source review.

## Workload Trigger Axes
- PD topology and connector type.
- Mooncake versus TCP transfer.
- Proxy presence.
- Request length crossing `max_model_len`.
- Transfer failure, timeout, and post-failure recovery.

## Useful Fuzzer Seed Shapes
- PD canary request, toxic overlength or transfer-failure request, recovery request.
- Shared-prefix PD warm/probe across producer/consumer.
- Proxy streaming request with client disconnect.

## Useful Oracle/Monitor Design
- Request-level error propagation.
- Producer and consumer logs.
- Proxy status and body integrity.
- KV transfer metrics and retry counters.
- Recovery canary correctness.

## Evidence Still Missing
- Reproducible Mooncake failure injection method.
- Trace-enabled PD service on npu4.
- Before/after logs for PR #8959.

