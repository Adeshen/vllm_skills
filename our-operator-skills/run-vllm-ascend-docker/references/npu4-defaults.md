# `npu4` Defaults for `vllm-ascend`

## Environment defaults

- SSH host: `npu4`
- data root: `/mnt/data`
- common container name: `vllm_qwen3`
- Docker root dir should be `/mnt/data/docker`

## Container recreation checklist

Recreate the container only after inspecting the current one.

Expected Ascend-related properties:

- `--network host`
- `--ipc=host`
- `--privileged`
- `/dev/davinci*`
- `/dev/davinci_manager`
- `/dev/hisi_hdc`
- `/dev/devmm_svm`
- `/mnt/data:/mnt/data`

Typical recreation shape:

```bash
docker stop vllm_qwen3 2>/dev/null || true
docker rm vllm_qwen3 2>/dev/null || true

docker run -dit --name vllm_qwen3 \
  --ipc=host \
  --network host \
  --privileged \
  --device=/dev/davinci0:rwm \
  --device=/dev/davinci1:rwm \
  --device=/dev/davinci2:rwm \
  --device=/dev/davinci3:rwm \
  --device=/dev/davinci_manager:rwm \
  --device=/dev/hisi_hdc:rwm \
  --device=/dev/devmm_svm:rwm \
  -v /usr/local/Ascend/driver:/usr/local/Ascend/driver:ro \
  -v /usr/local/dcmi:/usr/local/dcmi:ro \
  -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi:ro \
  -v /usr/local/sbin:/usr/local/sbin:ro \
  -v /mnt/data:/mnt/data \
  quay.io/ascend/vllm-ascend:v0.18.0rc1 \
  /bin/bash
```

## Generic serve templates

Single-card:

```bash
ASCEND_RT_VISIBLE_DEVICES=0 \
vllm serve <model_path> \
  --served-model-name <served_name> \
  --host 0.0.0.0 \
  --port <port> \
  --trust-remote-code \
  --gpu-memory-utilization <util> \
  --max-model-len <len>
```

Quantized W4A8:

```bash
ASCEND_RT_VISIBLE_DEVICES=0 \
vllm serve <model_path> \
  --served-model-name <served_name> \
  --host 0.0.0.0 \
  --port <port> \
  --trust-remote-code \
  --quantization ascend \
  --gpu-memory-utilization <util> \
  --max-model-len <len>
```

Multi-card TP:

```bash
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3 \
python3 -m vllm.entrypoints.openai.api_server \
  --model <model_path> \
  --trust-remote-code \
  --tensor-parallel-size <tp> \
  --served-model-name <served_name> \
  --max-model-len <len> \
  --host 0.0.0.0 \
  --port <port>
```

Long-context async/prefix variant:

```bash
ASCEND_RT_VISIBLE_DEVICES=<devices> \
HCCL_OP_EXPANSION_MODE=AIV \
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True \
VLLM_ASCEND_BALANCE_SCHEDULING=1 \
vllm serve <model_path> \
  --served-model-name <served_name> \
  --host 0.0.0.0 \
  --port <port> \
  --trust-remote-code \
  --gpu-memory-utilization <util> \
  --max-model-len <len> \
  --enable-chunked-prefill \
  --enable-prefix-caching \
  --async-scheduling
```

## Known gotchas

- `--gpu-memory-utilization` takes a value in `[0,1]`, not a percentage.
- `draft_model` speculative decoding may fail on affected `vllm-ascend` builds before other issues can surface.
- If free memory is already low on startup, changing the utilization value will not fix another process occupying the card.
- If `/mnt/data` disappeared after reboot, fix the mount and Docker root first.
