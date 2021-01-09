#!/usr/bin/env bash

set -euo pipefail

script_dir=$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")
repo_root=$(cd "${script_dir}" && git rev-parse --show-toplevel)

docker_tags=(
    -t atonal/puti:dev
)

for git_tag in $(git tag --points-at HEAD); do
    docker_tags+=("-t atonal/puti:${git_tag}")
done

# old build:
# docker build -t atonal/puti .

# multi-platform build:
docker buildx build "${docker_tags[@]}" --platform linux/amd64,linux/arm/v7 --push "${repo_root}"
