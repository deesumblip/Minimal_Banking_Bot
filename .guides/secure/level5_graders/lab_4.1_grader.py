#!/usr/bin/env python3
"""
Lab 4.1: Creating the transfer_money_tools Flow and Action - Grader Script (Level 5)
Output format matches Chapter 1.2 Lab 6.2 template.

Checks level5/data/basics/transfer_money_tools.yml, action_process_transfer_with_tools.py,
and domain actions. Runs from workspace root; expects /home/codio/workspace.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
LEVEL5 = WORKSPACE_ROOT / "level5"
FLOW_PATH = LEVEL5 / "data" / "basics" / "transfer_money_tools.yml"
ACTION_PATH = LEVEL5 / "actions" / "action_process_transfer_with_tools.py"
DOMAIN_PATH = LEVEL5 / "domain" / "basics.yml"

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML is required. Use the project venv Python.")
    sys.exit(1)

score = 0
max_score = 10

print("Running Lab 4.1 Assessment Checks...")
print("")

# Check 1: Flow file exists (2 points)
print("Check 1: Verifying transfer_money_tools.yml exists...")
if not FLOW_PATH.exists():
    print("❌ Check 1: FAILED - level5/data/basics/transfer_money_tools.yml not found (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - flow file exists (2 points)")
score += 2
print("")

# Check 2: Flow has collect and action (3 points)
try:
    with open(FLOW_PATH, encoding="utf-8") as f:
        flow_data = yaml.safe_load(f)
except Exception as e:
    print("❌ Check 2: FAILED - transfer_money_tools.yml has YAML errors (0 points)")
    print(f"   {e}")
    print("FAIL")
    sys.exit(1)

flows = flow_data.get("flows") or {}
collect_found = set()
has_action_step = False
for flow_def in flows.values() if isinstance(flows, dict) else []:
    if not isinstance(flow_def, dict):
        continue
    for step in flow_def.get("steps") or []:
        if isinstance(step, dict):
            if "collect" in step:
                collect_found.add(step.get("collect"))
            if step.get("action") == "action_process_transfer_with_tools":
                has_action_step = True
required_collect = {"amount", "recipient", "account_from"}
print("Check 2: Verifying flow has collect steps and action...")
if required_collect.issubset(collect_found) and has_action_step:
    print(" Check 2: PASSED - collect amount/recipient/account_from and action (3 points)")
    score += 3
else:
    print(
        "❌ Check 2: FAILED - Flow must have collect amount, recipient, account_from "
        "and action: action_process_transfer_with_tools (0 points)"
    )
print("")

# Check 3: Action file exists and name() (3 points)
print("Check 3: Verifying action_process_transfer_with_tools.py...")
if not ACTION_PATH.exists():
    print("❌ Check 3: FAILED - level5/actions/action_process_transfer_with_tools.py not found (0 points)")
else:
    action_content = ACTION_PATH.read_text(encoding="utf-8")
    has_name = "action_process_transfer_with_tools" in action_content and "def name" in action_content.lower()
    if has_name:
        print(" Check 3: PASSED - action file with correct name (3 points)")
        score += 3
    else:
        print("❌ Check 3: FAILED - action must define name() returning 'action_process_transfer_with_tools' (0 points)")
print("")

# Check 4: Domain lists action (2 points)
print("Check 4: Verifying domain actions list...")
if not DOMAIN_PATH.exists():
    print("❌ Check 4: FAILED - level5/domain/basics.yml not found (0 points)")
else:
    try:
        with open(DOMAIN_PATH, encoding="utf-8") as f:
            domain_data = yaml.safe_load(f)
        actions = domain_data.get("actions") or []
        if "action_process_transfer_with_tools" in actions:
            print(" Check 4: PASSED - action in domain (2 points)")
            score += 2
        else:
            print("❌ Check 4: FAILED - Add action_process_transfer_with_tools to domain actions (0 points)")
    except Exception as e:
        print(f"❌ Check 4: FAILED - Could not parse domain: {e} (0 points)")
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 4.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print("Summary: Check 1 (flow file) | Check 2 (flow steps) | Check 3 (action py) | Check 4 (domain)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
