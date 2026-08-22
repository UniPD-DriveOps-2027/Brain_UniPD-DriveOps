#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE="${BRAIN_IMAGE:-unipd-driveops/brain:jazzy}"
CONTAINER="${BRAIN_CONTAINER:-unipd-brain}"
START_MODE="false"

usage() {
  cat <<'EOF'
Usage: ./docker/run.sh [--normal-start|--random-start]

The OAK-D camera is launched by Brain's hardware launch. The container needs
host networking for ROS 2 and privileged hardware access for OAK/GPIO.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --normal-start) START_MODE="false"; shift ;;
    --random-start) START_MODE="true"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "ERROR: unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if ! docker image inspect "${IMAGE}" >/dev/null 2>&1; then
  echo "ERROR: Brain image is missing: ${IMAGE}" >&2
  echo "Build it once with: ${SCRIPT_DIR}/build.sh" >&2
  exit 1
fi

exec docker run --rm -it \
  --name "${CONTAINER}" \
  --privileged \
  --network host \
  --ipc host \
  --env "ROS_DOMAIN_ID=${ROS_DOMAIN_ID:-0}" \
  --env "RMW_IMPLEMENTATION=${RMW_IMPLEMENTATION:-rmw_fastrtps_cpp}" \
  --volume /etc/localtime:/etc/localtime:ro \
  "${IMAGE}" \
  ros2 launch brain_bringup hardware.launch.py "random_start:=${START_MODE}"
