# Scheduler

## Common Failure Symptoms
- Requests hang while service still listens.
- Queue drains incorrectly after a failed or cancelled request.
- Recovery requests time out after a toxic trace.
- Incorrect scheduling around long prefill/decode transitions.

## Issue/PR Examples
- [VA-BUG-4986](../bug_capsules/VA-BUG-4986-MTP-FULL-DECODE-HANG.md): FULL_DECODE_ONLY with MTP hangs.
- [VA-BUG-5445](../bug_capsules/VA-BUG-5445-CHUNK-PREFILL-LONG-SEQUENCE.md): long-sequence chunk prefill path.
- PR-centric corpus also lists open PD hang cases #8975/#9149, kept out of initial capsules until more evidence is curated.

## Workload Trigger Axes
- Request burst size.
- Long prefill followed by short decode canary.
- Decode-only or full-decode-only modes.
- MTP/speculative enabled.
- Timeout/retry sequence.

## Useful Fuzzer Seed Shapes
- Control -> toxic long/decode-only request -> recovery canary.
- Burst of mixed prompt lengths.
- Timed multi-request trace with waits and strict per-request timeout.

## Useful Oracle/Monitor Design
- Hung request timeout.
- Service liveness and `/v1/models` health after toxic trace.
- Queue/log keywords for stuck scheduling.
- AICore utilization if available on NPU campaigns.

## Evidence Still Missing
- Exact #4986 startup and request command.
- Scheduler queue instrumentation for GRIEF.
- Before/after latency and liveness metrics.

