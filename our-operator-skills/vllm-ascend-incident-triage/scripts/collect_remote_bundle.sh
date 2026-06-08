#!/usr/bin/env bash
set -euo pipefail

PORT=""
CONTAINER="vllm_qwen3"
OUT_DIR=""
PHASE="baseline"
INCIDENT_LABEL=""
ARTIFACT_DIR=""
ARTIFACT_SCOPE="auto"
LOG_LINES="200"
METRICS_LINES="80"
HOST_LABEL=""

usage() {
  cat <<'EOF'
Usage:
  collect_remote_bundle.sh --port <port> --out-dir <dir> [options]

Options:
  --port <port>              Target vLLM port on the remote host.
  --out-dir <dir>            Remote output directory for the collected bundle.
  --container <name>         Docker container name. Default: vllm_qwen3
  --phase <baseline|replay>  Bundle phase label. Default: baseline
  --incident-label <label>   Short incident label for metadata.
  --artifact-dir <dir>       Existing remote recorder output directory to copy into the bundle.
  --artifact-scope <scope>   Where to resolve artifact-dir: auto, host, or container. Default: auto
  --log-lines <n>            Number of docker log lines to keep. Default: 200
  --metrics-lines <n>        Number of metrics lines to keep. Default: 80
  --host-label <label>       Optional host label override for metadata.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --port)
      PORT="${2:-}"
      shift 2
      ;;
    --container)
      CONTAINER="${2:-}"
      shift 2
      ;;
    --out-dir)
      OUT_DIR="${2:-}"
      shift 2
      ;;
    --phase)
      PHASE="${2:-}"
      shift 2
      ;;
    --incident-label)
      INCIDENT_LABEL="${2:-}"
      shift 2
      ;;
    --artifact-dir)
      ARTIFACT_DIR="${2:-}"
      shift 2
      ;;
    --artifact-scope)
      ARTIFACT_SCOPE="${2:-}"
      shift 2
      ;;
    --log-lines)
      LOG_LINES="${2:-}"
      shift 2
      ;;
    --metrics-lines)
      METRICS_LINES="${2:-}"
      shift 2
      ;;
    --host-label)
      HOST_LABEL="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "$PORT" || -z "$OUT_DIR" ]]; then
  usage >&2
  exit 2
fi

mkdir -p "$OUT_DIR"

SERVICE_URL="http://127.0.0.1:${PORT}"
COLLECTED_AT="$(date --iso-8601=seconds 2>/dev/null || date '+%Y-%m-%dT%H:%M:%S%z')"
HOSTNAME_VALUE="$(hostname)"
HOST_RECORD="${HOST_LABEL:-$HOSTNAME_VALUE}"

capture_http() {
  local name="$1"
  local url="$2"
  local dest="$OUT_DIR/$name"
  local status_dest="$OUT_DIR/${name%.txt}.status"
  local tmp
  tmp="$(mktemp)"
  local curl_exit=0
  local http_code="000"
  http_code="$(curl -sS -o "$tmp" -w '%{http_code}' "$url" 2>"$dest.stderr")" || curl_exit=$?
  cat "$tmp" > "$dest" || true
  rm -f "$tmp"
  printf 'curl_exit=%s\nhttp_code=%s\nurl=%s\n' "$curl_exit" "$http_code" "$url" > "$status_dest"
}

capture_head_metrics() {
  local dest="$OUT_DIR/metrics_head.txt"
  local status_dest="$OUT_DIR/metrics_head.status"
  local tmp
  tmp="$(mktemp)"
  local curl_exit=0
  local http_code="000"
  http_code="$(curl -sS -o "$tmp" -w '%{http_code}' "${SERVICE_URL}/metrics" 2>"$dest.stderr")" || curl_exit=$?
  sed -n "1,${METRICS_LINES}p" "$tmp" > "$dest" || true
  rm -f "$tmp"
  printf 'curl_exit=%s\nhttp_code=%s\nurl=%s\n' "$curl_exit" "$http_code" "${SERVICE_URL}/metrics" > "$status_dest"
}

capture_http "health.txt" "${SERVICE_URL}/health"
capture_http "models.json" "${SERVICE_URL}/v1/models"
capture_head_metrics

npu-smi info > "$OUT_DIR/npu_smi.txt" 2>&1 || true
df -h /tmp /mnt/data > "$OUT_DIR/filesystems.txt" 2>&1 || true

docker inspect "$CONTAINER" > "$OUT_DIR/docker_inspect.json" 2>"$OUT_DIR/docker_inspect.stderr" || true
docker top "$CONTAINER" -eo pid,ppid,cmd > "$OUT_DIR/docker_top.txt" 2>"$OUT_DIR/docker_top.stderr" || true
docker logs --tail "$LOG_LINES" "$CONTAINER" > "$OUT_DIR/service_log_tail.txt" 2>&1 || true
ps -efww > "$OUT_DIR/host_ps_efww.txt" 2>/dev/null || true

{
  echo "service_url=${SERVICE_URL}"
  echo "phase=${PHASE}"
  echo "incident_label=${INCIDENT_LABEL}"
  echo "container=${CONTAINER}"
  echo "collected_at=${COLLECTED_AT}"
  echo "host=${HOST_RECORD}"
  echo "artifact_dir=${ARTIFACT_DIR}"
  echo "artifact_scope=${ARTIFACT_SCOPE}"
  echo "log_lines=${LOG_LINES}"
  echo "metrics_lines=${METRICS_LINES}"
} > "$OUT_DIR/workload_config.txt"

{
  echo "# docker-top matches"
  docker top "$CONTAINER" -eo pid,ppid,cmd 2>/dev/null | grep -E -- "--port ${PORT}( |$)|:${PORT}" || true
  echo
  echo "# host-ps matches"
  ps -efww | grep -E "vllm|api_server|serve" | grep -E -- "--port ${PORT}( |$)|:${PORT}" | grep -v grep || true
} > "$OUT_DIR/service_args.txt"

copy_artifacts_from_host() {
  mkdir -p "$OUT_DIR/incident_artifacts"
  for file in \
    incident_manifest.json \
    request_bundle.jsonl \
    trigger_request.json \
    replay_request.sh \
    summary.json \
    summary.md \
    requests.csv \
    metrics.csv; do
    if [[ -f "$ARTIFACT_DIR/$file" ]]; then
      cp -f "$ARTIFACT_DIR/$file" "$OUT_DIR/incident_artifacts/$file"
    fi
  done
}

copy_artifacts_from_container() {
  mkdir -p "$OUT_DIR/incident_artifacts"
  for file in \
    incident_manifest.json \
    request_bundle.jsonl \
    trigger_request.json \
    replay_request.sh \
    summary.json \
    summary.md \
    requests.csv \
    metrics.csv; do
    if docker exec "$CONTAINER" test -f "$ARTIFACT_DIR/$file" 2>/dev/null; then
      docker cp "$CONTAINER:$ARTIFACT_DIR/$file" "$OUT_DIR/incident_artifacts/$file" >/dev/null
    fi
  done
}

if [[ -n "$ARTIFACT_DIR" ]]; then
  artifact_source="missing"
  if [[ "$ARTIFACT_SCOPE" == "host" ]]; then
    if [[ -d "$ARTIFACT_DIR" ]]; then
      copy_artifacts_from_host
      artifact_source="host"
    fi
  elif [[ "$ARTIFACT_SCOPE" == "container" ]]; then
    if docker exec "$CONTAINER" test -d "$ARTIFACT_DIR" 2>/dev/null; then
      copy_artifacts_from_container
      artifact_source="container"
    fi
  else
    if [[ -d "$ARTIFACT_DIR" ]]; then
      copy_artifacts_from_host
      artifact_source="host"
    elif docker exec "$CONTAINER" test -d "$ARTIFACT_DIR" 2>/dev/null; then
      copy_artifacts_from_container
      artifact_source="container"
    fi
  fi

  if [[ "$artifact_source" == "missing" ]]; then
    printf 'artifact_dir_missing=%s\nartifact_scope=%s\n' "$ARTIFACT_DIR" "$ARTIFACT_SCOPE" > "$OUT_DIR/artifact_inventory.txt"
  else
    {
      echo "artifact_source=${artifact_source}"
      find "$OUT_DIR/incident_artifacts" -maxdepth 1 -type f | sort
    } > "$OUT_DIR/artifact_inventory.txt"
  fi
fi

python3 - "$OUT_DIR" "$PHASE" "$INCIDENT_LABEL" "$PORT" "$CONTAINER" "$SERVICE_URL" "$ARTIFACT_DIR" "$ARTIFACT_SCOPE" "$COLLECTED_AT" "$HOST_RECORD" <<'PY'
import json
import sys
from pathlib import Path

out_dir = Path(sys.argv[1])
phase, incident_label, port, container, service_url, artifact_dir, artifact_scope, collected_at, host_record = sys.argv[2:]
files = []
for path in sorted(out_dir.rglob("*")):
    if path.is_file():
        files.append(
            {
                "path": str(path.relative_to(out_dir)),
                "size_bytes": path.stat().st_size,
            }
        )

manifest = {
    "phase": phase,
    "incident_label": incident_label or None,
    "port": int(port),
    "container": container,
    "service_url": service_url,
    "artifact_dir": artifact_dir or None,
    "artifact_scope": artifact_scope,
    "collected_at": collected_at,
    "host": host_record,
    "file_count": len(files),
    "files": files,
}
(out_dir / "bundle_manifest.json").write_text(
    json.dumps(manifest, indent=2, ensure_ascii=False),
    encoding="utf-8",
)
PY

echo "[bundle] wrote ${OUT_DIR}"
