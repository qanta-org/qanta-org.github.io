#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
buzz_dir="${script_dir}/buzzes"

for shard in {a..z}; do
  gzip -dkf "${buzz_dir}/protobowl-buzzes-by-user-${shard}.json.gz"
done
