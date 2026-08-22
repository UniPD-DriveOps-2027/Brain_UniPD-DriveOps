#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
IMAGE="${BRAIN_IMAGE:-unipd-driveops/brain:jazzy}"

echo "Building Brain image: ${IMAGE}"
echo "The OAK-D camera runtime is installed into this image once."
docker build \
  --file "${SCRIPT_DIR}/Dockerfile" \
  --tag "${IMAGE}" \
  "${REPO_DIR}"

echo "Brain image ready: ${IMAGE}"
