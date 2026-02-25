#!/usr/bin/env python3
"""
Lab 5.1: Creating a Flow with Slot Collection - Grader Script
Checks level3/data/basics/check_balance.yml for: file exists, valid YAML with flows:,
a flow with name/description/steps, collect: account step, action: action_check_balance_simple.
Runs from workspace root; expects /home/codio/workspace.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
FLOW_PATH = WORKSPACE_ROOT / "level3" / "data" / "basics" / "check_balance.yml"

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML is required. Use the project venv Python: .venv/bin/python3")
    sys.exit(1)

score = 0
max_score = 8

print("Running Lab 5.1 Assessment Checks...")
print("")

# Check 0: File exists (2 points)
print("Check 0: Verifying check_balance.yml exists...")
if not FLOW_PATH.exists():
    print("❌ Check 0: FAILED - level3/data/basics/check_balance.yml not found (0 points)")
    print("Hint: Create the file in level3/data/basics/ with a flow that has collect: account and action: action_check_balance_simple")
    print("FAIL")
    sys.exit(1)
print("✅ Check 0: PASSED - file exists (2 points)")
score += 2
print("")

# Load YAML
try:
    with open(FLOW_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
except Exception as e:
    print("❌ FAILED - check_balance.yml has YAML syntax errors:")
    print(f"   {e}")
    print("Hint: Check indentation (2 spaces), colons, and list dashes. Avoid tabs.")
    print("FAIL")
    sys.exit(1)

if not isinstance(data, dict):
    print("❌ FAILED - file must be a YAML mapping (key-value).")
    print("FAIL")
    sys.exit(1)

# Check 1: flows: section and at least one flow with name, description, steps (2 points)
print("Check 1: Verifying flows: and flow structure...")
flows = data.get("flows")
if not isinstance(flows, dict) or not flows:
    print("❌ Check 1: FAILED - No top-level 'flows:' section or it is empty (0 points)")
    print("Hint: Add a 'flows:' key with at least one flow (e.g. check_balance) that has name, description, and steps.")
else:
    has_valid_flow = False
    for flow_id, flow_def in flows.items():
        if not isinstance(flow_def, dict):
            continue
        if "name" in flow_def and "steps" in flow_def:
            has_valid_flow = True
            break
    if has_valid_flow:
        print("✅ Check 1: PASSED - flows: with at least one flow (name, steps) (2 points)")
        score += 2
    else:
        print("❌ Check 1: FAILED - At least one flow must have 'name' and 'steps' (0 points)")
        print("Hint: Each flow under flows: should have name:, description: (optional), and steps: list.")
print("")

# Check 2: collect: account in steps (2 points)
print("Check 2: Verifying collect: account step...")
has_collect_account = False
if isinstance(flows, dict):
    for flow_def in flows.values():
        if not isinstance(flow_def, dict):
            continue
        steps = flow_def.get("steps")
        if not isinstance(steps, list):
            continue
        for step in steps:
            if isinstance(step, dict) and step.get("collect") == "account":
                has_collect_account = True
                break
        if has_collect_account:
            break
if has_collect_account:
    print("✅ Check 2: PASSED - collect: account found in steps (2 points)")
    score += 2
else:
    print("❌ Check 2: FAILED - No step with 'collect: account' (0 points)")
    print("Hint: Add a step with collect: account (optional description: 'account number').")
print("")

# Check 3: action: action_check_balance_simple in steps (2 points)
print("Check 3: Verifying action: action_check_balance_simple step...")
has_action = False
if isinstance(flows, dict):
    for flow_def in flows.values():
        if not isinstance(flow_def, dict):
            continue
        steps = flow_def.get("steps")
        if not isinstance(steps, list):
            continue
        for step in steps:
            if isinstance(step, dict) and step.get("action") == "action_check_balance_simple":
                has_action = True
                break
        if has_action:
            break
if has_action:
    print("✅ Check 3: PASSED - action: action_check_balance_simple found (2 points)")
    score += 2
else:
    print("❌ Check 3: FAILED - No step with 'action: action_check_balance_simple' (0 points)")
    print("Hint: Add a step with action: action_check_balance_simple")
print("")

# Summary
print("=" * 50)
if score >= max_score:
    print(f"✅ PASS: Lab 5.1 verification complete! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
    print("=" * 50)
    sys.exit(0)
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Review the failed checks above.")
    print("FAIL")
    print("=" * 50)
    sys.exit(1)
