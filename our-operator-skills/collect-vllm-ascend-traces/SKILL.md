---
name: collect-vllm-ascend-traces
description: Collect end-to-end traces for vLLM Ascend services on npu4 using local Jaeger and OTEL tunnels. Use when Codex needs to start or verify the local Jaeger stack, establish SSH forwarding, launch or inspect a trace-enabled vLLM service, send requests with trace headers, and confirm that traces are exported and queryable.
---

# Collect vLLM Ascend Traces

Collect traces end to end: local Jaeger, SSH tunnels, trace-enabled vLLM, and request verification. Do not treat the collector, transport, and service-export paths as the same failure domain.

## Golden Rules

- Confirm collector, tunnel, service flags, and traced request separately.
- Do not restart or relaunch a service just because traces are missing; classify the missing-trace domain first.
- Read [../shared/upstream-routes.md](../shared/upstream-routes.md) when borrowing observability vocabulary from Phoenix, LangSmith, NVIDIA, or evaluation skills.
- Evidence is queryable spans plus the command/request/log path that produced them.

## Workflow

1. Start or verify local Jaeger.
Use the existing local script when possible instead of rebuilding the tunnel flow manually.

2. Verify tunnel state.
Confirm OTLP reverse forwarding and API forwarding before changing server flags.

3. Verify the service is trace-enabled.
Check `--otlp-traces-endpoint` and `--collect-detailed-traces` in the service args or logs.

4. Send a traced request.
Use a request with `traceparent` so the run is easy to find in Jaeger.

5. Query Jaeger and report the result.
Report whether spans were exported, which service name appeared, and whether the missing-trace problem is local, transport, or server-side.

## Standard Checks

- `curl --noproxy '*' -s http://127.0.0.1:16686/api/services`
- `curl --noproxy '*' -s http://127.0.0.1:8080/v1/models`
- `ssh npu4 'ps -efww | grep -E "otlp|collect-detailed-traces|vllm" | grep -v grep'`

## Preferred Path

Use [references/otel-jaeger-workflow.md](references/otel-jaeger-workflow.md) for:

- local Jaeger startup
- SSH forwarding pattern
- trace-enabled service flags
- Jaeger API verification

## Failure Classification

Classify missing traces before changing the service:

- local collector failure: Jaeger not listening or not responding
- tunnel failure: reverse OTLP or forward API tunnel missing
- service export failure: API works but logs show export errors or wrong OTLP endpoint
- visibility mismatch: traces exported, but wrong service name or wrong query target
- request issue: service is traced but the test request or headers were wrong

## Reporting

Summaries should include:

- whether Jaeger was already running or newly started
- which ports and tunnels were used
- the vLLM trace flags observed
- the request used to generate a trace
- the Jaeger service name and whether traces were queryable

## Validation

Trace collection is successful only when Jaeger returns a service name and at least one queryable trace for the tested request. If traces are missing, the final response must classify the failure domain as collector, tunnel, service export, visibility mismatch, or request issue.
