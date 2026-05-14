#!/usr/bin/env bash
# CI-only: narrow the working tree before codio-assignment-publish-action.
# Committed .guides/content/index.json on main stays the full course; this
# overwrites it locally for the publish job only.
set -euo pipefail

cp .guides/content/index.level6-assignment.json .guides/content/index.json

rm -rf level1 level2 level3 level4 level5

shopt -s nullglob
for d in .guides/content/Level-*; do
  if [[ "$d" != ".guides/content/Level-6---Sub-Agents-c7d8" ]]; then
    rm -rf "$d"
  fi
done
