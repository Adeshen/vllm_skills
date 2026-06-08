---
name: vllm-ascend-incident-triage
description: Triage slow, crash, and hang incidents for vLLM Ascend services on npu4. Use when Codex needs to preserve a read-only baseline bundle, save the trigger request or failing request mix, replay the incident on a clean target, and route the case to benchmark, trace, or repro workflows with a normalized report.
---

# vLLM Ascend Incident Triage

Treat incident work as a fixed pipeline:

`preserve scene -> save trigger -> replay on clean target -> route to specialist workflow -> write normalized report`

Do not start with profiler, restart, or parameter changes unless the baseline bundle has already been captured.

## Standard Inputs

Capture these inputs explicitly before acting:

- symptom class: `slow`, `crash`, `hang`, or `unknown`
- current serve command or service shape
- current request command, workload source, or recorder config
- target port and served model name
- optional strict replay request
- optional trace request

Default environment:

- host: `npu4`
- runtime: current `vllm-ascend` Docker workflow
- report directory: `discussion_reports/bug/`

## Workflow

1. Preserve a read-only baseline bundle.
Collect:
- `/health`, `/v1/models`, `/metrics` summary
- current serve args or container state
- `npu-smi info`
- recent service log tail
- workload config or recorder config

2. Save the trigger request or request mix.
Prefer the recorder with:
- `capture_payloads=true`
- `capture_headers=true` when headers matter
- `incident_label=<short-topic>`

Use the generated:
- `request_bundle.jsonl`
- `trigger_request.json`
- `replay_request.sh`
- `incident_manifest.json`

3. Replay on a clean target.
Do not replay on the already degraded target unless the incident itself requires that environment. Prefer a fresh port or restarted clean service only after the baseline bundle is preserved.

4. Route to the right specialist workflow.

Use this routing:

- `slow`
  - preserve baseline bundle
  - save the slow request
  - replay the same request
  - then use `collect-vllm-ascend-traces` if timing or observability is ambiguous

- `crash`
  - preserve baseline bundle
  - save the failing request or request mix
  - replay the crash
  - then use `reproduce-vllm-ascend-issue` style evidence collection when the case maps to a known issue

- `hang`
  - confirm baseline service health first
  - save the trigger request
  - replay on a clean target
  - collect replay-time bundle
  - then capture hang-time evidence such as `py-spy`, watchdog output, or Ascend/HCCL-related wait paths

- `unknown`
  - preserve baseline bundle
  - save the trigger request
  - attempt a minimal replay
  - classify as `slow`, `crash`, or `hang` before deeper specialization

5. Write a normalized report.
Use `record-vllm-ascend-report` conventions. Keep the difference between original scene, replay scene, and specialized follow-up clear.

## Preferred Script

Prefer the local wrapper at `scripts/run_remote_bundle_via_ssh.sh`.

It syncs `collect_remote_bundle.sh` to the remote host and executes it there:

```bash
skills/vllm-ascend-incident-triage/scripts/run_remote_bundle_via_ssh.sh \
  --target npu4 \
  --port 8021 \
  --container vllm_qwen3 \
  --out-dir /tmp/incidents/codex-success/baseline \
  --phase baseline \
  --incident-label codex-success
```

For replay bundles, pass the recorder output directory too:

```bash
skills/vllm-ascend-incident-triage/scripts/run_remote_bundle_via_ssh.sh \
  --target npu4 \
  --port 8021 \
  --container vllm_qwen3 \
  --out-dir /tmp/incidents/codex-success/replay \
  --phase replay \
  --incident-label codex-success \
  --artifact-dir /tmp/codex-success \
  --artifact-scope container
```

Use `scripts/collect_remote_bundle.sh` directly only when you are already on the remote host or need to embed it into a custom SSH flow.

Direct SSH form:

```bash
ssh npu4 'bash -s -- \
  --port 8021 \
  --container vllm_qwen3 \
  --out-dir /tmp/incidents/codex-success/baseline \
  --phase baseline \
  --incident-label codex-success' \
  < skills/vllm-ascend-incident-triage/scripts/collect_remote_bundle.sh
```

## Bundle Rules

The baseline bundle should be read-only and should happen before disruptive actions.

Recommended bundle directory shape:

```text
artifacts/incidents/<timestamp>-<slug>/
  baseline/
  replay/
```

Baseline bundle should include:

- `health.txt`
- `models.json`
- `metrics_head.txt` or metrics summary
- `npu_smi.txt`
- `service_args.txt`
- `service_log_tail.txt`
- `workload_config.txt`

Replay bundle should include the same files plus:

- replay result
- trigger request path
- replay script path
- any trace or hang-time captures

When running inside the current `npu4` Ascend container layout, do not write bundle outputs under `/mnt/data/...` unless you have confirmed the mount is writable. The validated safe default is `/tmp/...`.

When the recorder was run inside `vllm_qwen3`, its `/tmp/...` outputs live inside the container namespace. Pass `--artifact-scope container` so replay bundles copy those files out through Docker instead of checking the host filesystem only.

## Decision Rules

- If the service is already unhealthy, do not mutate it before preserving the baseline bundle.
- If the request path is unknown, reconstruct it from recorder outputs or shell history before trying new prompts.
- If the incident cannot be replayed, report that explicitly and stop short of speculative root-cause claims.
- If a local blocker fires before the target issue, classify it as a local blocker in the report.

## Specialist Mapping

Use these local skills after triage:

- `run-vllm-ascend-docker` for clean-target serve setup or port isolation
- `benchmark-vllm-ascend` for pressure tests or request-mix replay
- `collect-vllm-ascend-traces` for traced replay and observability ambiguity
- `reproduce-vllm-ascend-issue` for issue-oriented reproduction
- `record-vllm-ascend-report` for final report normalization

Read [references/bundle-examples.md](references/bundle-examples.md) for ready-to-run baseline and replay examples on `npu4`.

## Reporting

Short summaries should include:

- symptom class
- whether the trigger was preserved
- whether replay succeeded
- which specialist path was chosen next
- report path
