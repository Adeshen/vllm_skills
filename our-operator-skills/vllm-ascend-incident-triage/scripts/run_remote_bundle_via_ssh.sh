#!/usr/bin/env bash
set -euo pipefail

TARGET="npu4"
REMOTE_SCRIPT="/tmp/collect_remote_bundle.sh"
PASS_ARGS=()

usage() {
  cat <<'EOF'
Usage:
  run_remote_bundle_via_ssh.sh [wrapper-options] -- <collector-options>
  run_remote_bundle_via_ssh.sh [wrapper-options] <collector-options>

Wrapper options:
  --target <ssh-target>         SSH target. Default: npu4
  --remote-script <path>        Remote path for the synced collector. Default: /tmp/collect_remote_bundle.sh
  -h, --help                    Show this help

All other arguments are passed through to collect_remote_bundle.sh.

Example:
  run_remote_bundle_via_ssh.sh \
    --target npu4 \
    --port 8021 \
    --container vllm_qwen3 \
    --out-dir /tmp/incidents/codex-success/baseline \
    --phase baseline \
    --incident-label codex-success
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    --remote-script)
      REMOTE_SCRIPT="${2:-}"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    --)
      shift
      PASS_ARGS+=("$@")
      break
      ;;
    *)
      PASS_ARGS+=("$1")
      shift
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COLLECTOR_SCRIPT="${SCRIPT_DIR}/collect_remote_bundle.sh"

if [[ ! -f "${COLLECTOR_SCRIPT}" ]]; then
  echo "collector script not found: ${COLLECTOR_SCRIPT}" >&2
  exit 1
fi

rsync -av "${COLLECTOR_SCRIPT}" "${TARGET}:${REMOTE_SCRIPT}"
ssh "${TARGET}" "chmod +x '${REMOTE_SCRIPT}' && bash '${REMOTE_SCRIPT}' $(printf '%q ' "${PASS_ARGS[@]}")"
