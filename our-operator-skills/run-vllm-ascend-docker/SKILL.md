---
name: run-vllm-ascend-docker
description: Run, restart, and troubleshoot vLLM Ascend Docker services on npu4 for arbitrary models. Use when Codex needs to verify `/mnt/data2/model_weights`, inspect or recreate the vllm_qwen3 container, confirm Ascend device visibility, and launch vllm serve with model-specific parameters such as model path, served model name, tensor/data parallelism, quantization, context length, and advanced flags.
---

# Run vLLM Ascend Docker

Operate `vllm-ascend` on `npu4` conservatively. Confirm storage, Docker, and NPU visibility before changing serve arguments, and treat model settings as parameters rather than assuming a fixed template.

## Golden Rules

- Inspect before restart; preserve the current launch shape and logs when debugging.
- Change one risk dimension at a time: image, model, parallelism, quantization, context, scheduler flags, and cache flags should not all move together.
- Read [../shared/upstream-routes.md](../shared/upstream-routes.md) when borrowing generic vLLM deploy guidance; Ascend-specific flags and mounts still require local evidence.
- New model paths must use `/mnt/data2/model_weights`.

## Workflow

1. Confirm the environment first.
Check `/mnt/data2/model_weights`, Docker root, the target container, and NPU visibility before touching `vllm serve`.

2. Capture the current launch shape.
If a container or service already exists, inspect it before restarting or recreating it.

3. Parameterize the serve command.
Always make the model path, served name, parallelism, quantization, and context length explicit.

4. Change one risk dimension at a time.
If the user is debugging a failure, avoid changing model path, parallelism, quantization, and advanced scheduling flags all at once.

5. Verify with API checks.
Use `/v1/models` and a minimal request after each restart.

## Standard Checks

Run these in order:

- `ssh npu4 'df -h /mnt/data /mnt/data2; findmnt /mnt/data /mnt/data2 || true'`
- `ssh npu4 'docker info --format "{{.DockerRootDir}}"; docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"'`
- `ssh npu4 'docker inspect vllm_qwen3 --format "{{json .HostConfig.Devices}}" 2>/dev/null || true'`
- `ssh npu4 'ls /mnt/data2/model_weights 2>/dev/null | sed -n "1,40p"'`
- `ssh npu4 'npu-smi info'`

Historical runs may reference a legacy model-volume path; new runs should use `/mnt/data2/model_weights` after the volume migration. If `/mnt/data2/model_weights` is missing, fix the mount or storage problem before changing Docker or vLLM.

## Launch Guidance

Prefer the existing `vllm_qwen3` container when it is healthy and has the required device mappings. Recreate it only when device visibility, bind mounts, or image version are wrong.

For `vllm serve`, treat these as required inputs:

- `model_path`
- `served_model_name`
- `port`
- `tensor_parallel_size` and `data_parallel_size` when used
- `quantization`
- `gpu_memory_utilization`
- `max_model_len`

Treat these as optional advanced inputs:

- prefix caching
- async scheduling
- chunked prefill
- speculative config
- tool parser / reasoning parser
- additional config
- compilation config

Use the command patterns in [references/npu4-defaults.md](references/npu4-defaults.md).

## Failure Triage

Classify failures before proposing the next command:

- Mount failure: `/mnt/data2/model_weights` is absent or points to the wrong filesystem.
- Device visibility failure: `aclrtGetDeviceCount`, `davinci`, `torch_npu`, or zero visible NPUs in the container.
- Model/config failure: path missing, wrong served model name, invalid parameter shape, or unsupported speculative mode.
- Capacity failure: OOM, free-memory checks, over-large context, or parallelism that does not fit.

## Verification

Use this sequence:

- `ssh npu4 'curl -sS http://127.0.0.1:<port>/v1/models'`
- `ssh npu4 'curl -sS http://127.0.0.1:<port>/metrics | head -n 20'`
- `ssh npu4 'curl -sS http://127.0.0.1:<port>/v1/chat/completions -H "Content-Type: application/json" -d "{\"model\":\"<served>\",\"messages\":[{\"role\":\"user\",\"content\":\"Reply with exactly: hello\"}],\"max_tokens\":8,\"temperature\":0}"'`

If the model list is healthy but generation fails, keep the container and mount assumptions fixed and isolate the model arguments next.

## Validation

A service change is valid only when the final response reports the image/container, model path, served model name, port, parallelism/quantization/context settings, `/v1/models` result, and minimal generation result or the exact failure signature.
