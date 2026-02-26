#!/usr/bin/env python3
"""
Lab 4.3: Creating the Transfer Flow - Grader Script
Checks level4/data/basics/transfer_money.yml for: file exists, valid YAML with flows:,
flow with collect: amount, collect: recipient, collect: account_from, action: action_process_transfer.
Runs from workspace root; expects /home/codio/workspace.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
FLOW_PATH = WORKSPACE_ROOT / "level4" / "data" / "basics" / "transfer_money.yml"

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML is required. Use the project venv Python: .venv/bin/python3")
    sys.exit(1)

score = 0
max_score = 8

print("Running Lab 4.3 Assessment Checks...")
print("")

# Check 0: File exists (2 points)
print("Check 0: Verifying transfer_money.yml exists...")
if not FLOW_PATH.exists():
    print("❌ Check 0: FAILED - level4/data/basics/transfer_money.yml not found (0 points)")
    print("Hint: Create the file in level4/data/basics/ with a flow that has collect amount, recipient, account_from and action: action_process_transfer")
    print("FAIL")
    sys.exit(1)
print("✅ Check 0: PASSED - file exists (2 points)")
score += 2
print("")

try:
    with open(FLOW_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
except Exception as e:
    print("❌ FAILED - transfer_money.yml has YAML syntax errors:")
    print(f"   {e}")
    print("FAIL")
    sys.exit(1)

if not isinstance(data, dict):
    print("❌ FAILED - file must be a YAML mapping.")
    print("FAIL")
    sys.exit(1)

flows = data.get("flows")
if not isinstance(flows, dict) or not flows:
    print("❌ Check 1: FAILED - No top-level 'flows:' section or it is empty (0 points)")
    print("FAIL")
    sys.exit(1)

# Check 1: flows with name and steps (2 points)
has_valid_flow = False
for flow_def in flows.values():
    if isinstance(flow_def, dict) and "name" in flow_def and "steps" in flow_def:
        has_valid_flow = True
        break
if has_valid_flow:
    print("✅ Check 1: PASSED - flows: with at least one flow (name, steps) (2 points)")
    score += 2
else:
    print("❌ Check 1: FAILED - At least one flow must have 'name' and 'steps' (0 points)")
print("")

# Check 2: collect amount, recipient, account_from (2 points)
collect_required = {"amount", "recipient", "account_from"}
collect_found = set()
for flow_def in flows.values() if isinstance(flows, dict) else []:
    if not isinstance(flow_def, dict):
        continue
    steps = flow_def.get("steps") or []
    for step in steps:
        if isinstance(step, dict) and "collect" in step:
            collect_found.add(step.get("collect"))
if collect_required.issubset(collect_found):
    print("✅ Check 2: PASSED - collect: amount, recipient, account_from found (2 points)")
    score += 2
else:
    missing = collect_required - collect_found
    print(f"❌ Check 2: FAILED - Missing collect steps: {missing} (0 points)")
    print("Hint: Add steps with collect: amount, collect: recipient, collect: account_from")
print("")

# Check 3: action: action_process_transfer (2 points)
has_action = False
for flow_def in flows.values() if isinstance(flows, dict) else []:
    if not isinstance(flow_def, dict):
        continue
    for step in flow_def.get("steps") or []:
        if isinstance(step, dict) and step.get("action") == "action_process_transfer":
            has_action = True
            break
    if has_action:
        break
if has_action:
    print("✅ Check 3: PASSED - action: action_process_transfer found (2 points)")
    score += 2
else:
    print("❌ Check 3: FAILED - No step with 'action: action_process_transfer' (0 points)")
    print("Hint: Add a step with action: action_process_transfer")
print("")

# Summary
print("=" * 50)
if score >= max_score:
    print(f"✅ PASS: Lab 4.3 verification complete! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
    print("=" * 50)
    sys.exit(0)
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Review the failed checks above.")
    print("FAIL")
    print("=" * 50)
    sys.exit(1)
