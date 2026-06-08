# OTEL and Jaeger Workflow for `npu4`

## Local entrypoint

Use the existing script:

```bash
/bin/zsh -lc /Users/adeshen/Documents/obsidian/vllm_fault_inject_knowledge/llm_state_based/start_local_otel.sh
```

It is responsible for:

- starting local Jaeger
- creating reverse OTLP tunnels for `4317/4318`
- creating an API forward tunnel for local access
- checking the Jaeger API and the remote vLLM API

## Trace-enabled vLLM flags

Typical flags:

```bash
--otlp-traces-endpoint http://127.0.0.1:4318/v1/traces
--collect-detailed-traces model
```

The endpoint and the tunnel direction must agree. If the service can answer requests but Jaeger stays empty, check the OTLP target first.

## Trace verification

Check services:

```bash
curl --noproxy '*' 'http://127.0.0.1:16686/api/services'
```

Send a traced request:

```bash
curl http://127.0.0.1:8080/v1/completions \
  -H "Content-Type: application/json" \
  -H "traceparent: 00-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-bbbbbbbbbbbbbbbb-01" \
  -d '{"model":"<served_model_name>","prompt":"Hello","max_tokens":10}'
```

Query traces:

```bash
curl --noproxy '*' 'http://127.0.0.1:16686/api/traces?service=<service_name>&limit=5'
```

## Common failure patterns

- Jaeger UI up, no services: no spans reached the collector
- services exist, request not found: wrong service name or query timing
- API healthy, traces missing, logs mention export failure: OTLP endpoint or tunnel mismatch
- service started without trace flags: re-run with explicit trace options before blaming the tunnel
