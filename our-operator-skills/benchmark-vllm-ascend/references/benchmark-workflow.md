# Benchmark Workflow on `npu4`

## Canonical local sources

- `vllm_ascend/scripts/run_evalscope_with_kv_record.sh`
- `vllm_ascend/scripts/record_kv_cache_usage.py`
- `vllm_ascend/scripts/generate_random_prefix_dataset.py`
- `vllm_ascend/scripts/send_long_token_requests.py`

## Canonical remote layout

- `/mnt/data/vllm_observe/scripts`
- `/mnt/data/vllm_observe/datasets`
- `/mnt/data/vllm_observe/kv_records`
- `/mnt/data/vllm_observe/evalscope`

## Sync pattern

Use targeted sync for the scripts you need. Example:

```bash
scp vllm_ascend/scripts/run_evalscope_with_kv_record.sh npu4:/mnt/data/vllm_observe/scripts/
scp vllm_ascend/scripts/record_kv_cache_usage.py npu4:/mnt/data/vllm_observe/scripts/
scp vllm_ascend/scripts/generate_random_prefix_dataset.py npu4:/mnt/data/vllm_observe/scripts/
```

For prompt files or datasets:

```bash
scp <local_prompt_or_dataset> npu4:/mnt/data/vllm_observe/datasets/
```

## Long prompt preparation

Generate a dataset remotely:

```bash
ssh npu4 'python3 /mnt/data/vllm_observe/scripts/generate_random_prefix_dataset.py --help'
```

If using a large fixed prompt, verify its tokenized length inside the runtime environment before load testing.

## Benchmark command

```bash
BASE_URL=http://127.0.0.1:<port> \
MODEL=<served_model_name> \
PARALLEL=<parallel> \
NUMBER=<requests> \
MAX_TOKENS=<max_tokens> \
STREAM=true \
LOG_EVERY_N_QUERY=1 \
PROMPT_FILE=/mnt/data/vllm_observe/datasets/<prompt.txt> \
OUTPUT_ROOT=/mnt/data/vllm_observe/<run_name> \
SCRIPT_ROOT=/mnt/data/vllm_observe/scripts \
/mnt/data/vllm_observe/scripts/run_evalscope_with_kv_record.sh
```

## Artifact review

Expect these outputs:

- `evalscope_perf_<timestamp>.log`
- `evalscope/runs/<timestamp>/...`
- `kv_evalscope_<timestamp>.csv`
- `kv_evalscope_<timestamp>.log`

Use them to separate:

- service API health problems
- engine crash signatures
- throughput or latency regressions
- KV pressure patterns
