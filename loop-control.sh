#!/usr/bin/env bash
# =============================================================================
# loop-control.sh — Cross-Platform Loop Engine CLI Client
# =============================================================================
# Lightweight curl wrapper for submitting state transition requests to the
# containerized Agnostic Loop Engine. Usable from CI/CD pipelines, Python
# scripts, or any terminal environment.
#
# Usage:
#   ./loop-control.sh transit <loop_id> <source_phase> <target_phase> [execution_logs]
#   ./loop-control.sh status  <loop_id>
#   ./loop-control.sh health
#
# Environment:
#   LOOP_ENGINE_URL  — Base URL of the loop engine (default: http://localhost:8080)
# =============================================================================
set -euo pipefail

LOOP_ENGINE_URL="${LOOP_ENGINE_URL:-http://localhost:8080}"

usage() {
  echo "Usage:"
  echo "  $0 transit <loop_id> <source_phase> <target_phase> [execution_logs]"
  echo "  $0 status  <loop_id>"
  echo "  $0 health"
  echo ""
  echo "Environment:"
  echo "  LOOP_ENGINE_URL  Base URL (default: http://localhost:8080)"
  exit 1
}

transit_state() {
  local loop_id="$1"
  local source="$2"
  local target="$3"
  local logs="${4:-}"

  local payload
  payload=$(cat <<EOF
{
  "loop_id": "${loop_id}",
  "source_phase": "${source}",
  "target_phase": "${target}",
  "execution_logs": "${logs}"
}
EOF
  )

  echo "→ Requesting transition: ${source} → ${target} for loop '${loop_id}'"
  curl -s -X POST "${LOOP_ENGINE_URL}/api/v1/loops/transit" \
    -H "Content-Type: application/json" \
    -d "${payload}" | python3 -m json.tool 2>/dev/null || echo "${payload}"
}

get_status() {
  local loop_id="$1"
  echo "→ Fetching status for loop '${loop_id}'"
  curl -s "${LOOP_ENGINE_URL}/api/v1/loops/${loop_id}/status" \
    | python3 -m json.tool 2>/dev/null || curl -s "${LOOP_ENGINE_URL}/api/v1/loops/${loop_id}/status"
}

health_check() {
  echo "→ Health check: ${LOOP_ENGINE_URL}/health"
  curl -s "${LOOP_ENGINE_URL}/health" \
    | python3 -m json.tool 2>/dev/null || curl -s "${LOOP_ENGINE_URL}/health"
}

# Main dispatch
if [ $# -lt 1 ]; then
  usage
fi

case "$1" in
  transit)
    [ $# -lt 4 ] && usage
    transit_state "$2" "$3" "$4" "${5:-}"
    ;;
  status)
    [ $# -lt 2 ] && usage
    get_status "$2"
    ;;
  health)
    health_check
    ;;
  *)
    echo "Unknown command: $1"
    usage
    ;;
esac
