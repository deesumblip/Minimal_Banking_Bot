#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
LEVEL1_DIR="$ROOT_DIR/level1"
DOMAIN_FILE="$LEVEL1_DIR/domain/basics.yml"
BASICS_DATA_DIR="$LEVEL1_DIR/data/basics"

fail() {
  echo "FAIL: $1"
  exit 1
}

[[ -d "$LEVEL1_DIR" ]] || fail "Could not find level1 folder at $LEVEL1_DIR"
[[ -f "$DOMAIN_FILE" ]] || fail "Missing domain file: level1/domain/basics.yml"
[[ -d "$BASICS_DATA_DIR" ]] || fail "Missing flows folder: level1/data/basics/"

# Lab 7.2 asks for a NEW response + a NEW flow file. We look for a flow file
# in data/basics that is not one of the earlier lab files.
known_files=(
  "greet.yml"
  "help.yml"
  "contact.yml"
  "goodbye.yml"
  "check_balance.yml"
)

is_known() {
  local name="$1"
  for k in "${known_files[@]}"; do
    [[ "$name" == "$k" ]] && return 0
  done
  return 1
}

shopt -s nullglob
candidate_flows=()
for f in "$BASICS_DATA_DIR"/*.yml; do
  base="$(basename "$f")"
  if ! is_known "$base"; then
    candidate_flows+=("$f")
  fi
done
shopt -u nullglob

(( ${#candidate_flows[@]} > 0 )) || fail "No new flow file found in level1/data/basics/. Create a new .yml flow file (not greet/help/contact/goodbye)."

flow_file="${candidate_flows[0]}"

# Basic structure checks.
grep -Eq '^[[:space:]]*flows:' "$flow_file" || fail "Flow file $(basename "$flow_file") is missing a top-level 'flows:' key."
grep -Eq '^[[:space:]]+name:' "$flow_file" || fail "Flow file $(basename "$flow_file") is missing a 'name:' field."
grep -Eq '^[[:space:]]+description:' "$flow_file" || fail "Flow file $(basename "$flow_file") is missing a 'description:' field."

# Extract first utter_* action referenced in the flow.
utter_action="$(
  grep -Eo 'action:[[:space:]]*utter_[A-Za-z0-9_]+' "$flow_file" \
    | head -n 1 \
    | sed -E 's/.*(utter_[A-Za-z0-9_]+).*/\\1/'
)"

[[ -n "${utter_action:-}" ]] || fail "Flow file $(basename "$flow_file") does not reference any 'utter_*' action."

# Ensure the response exists in the domain.
grep -Eq "^[[:space:]]*$utter_action[[:space:]]*:" "$DOMAIN_FILE" || fail "Domain is missing response '$utter_action:' in level1/domain/basics.yml"

echo "Successfully passed!"
