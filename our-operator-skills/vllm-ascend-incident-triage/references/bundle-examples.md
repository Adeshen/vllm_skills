# Bundle Examples

Use these examples when collecting bundles on `npu4`.

## Baseline bundle for a healthy or slow live service

```bash
skills/vllm-ascend-incident-triage/scripts/run_remote_bundle_via_ssh.sh \
  --target npu4 \
  --port 8021 \
  --container vllm_qwen3 \
  --out-dir /tmp/incidents/codex-success/baseline \
  --phase baseline \
  --incident-label codex-success
```

## Replay bundle for a saved recorder run

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

## Replay bundle for a failed port

```bash
skills/vllm-ascend-incident-triage/scripts/run_remote_bundle_via_ssh.sh \
  --target npu4 \
  --port 8000 \
  --container vllm_qwen3 \
  --out-dir /tmp/incidents/codex-failure/replay \
  --phase replay \
  --incident-label codex-failure \
  --artifact-dir /tmp/codex-failure \
  --artifact-scope container
```

## Writable-path rule

The validated safe default for bundle outputs in the current `npu4` container workflow is `/tmp/...`.

Do not assume `/mnt/data/...` is writable from inside `vllm_qwen3`.
