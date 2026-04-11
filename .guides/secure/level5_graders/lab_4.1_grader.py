#!/usr/bin/env python3
"""
Lab 4.1: Creating the transfer_money_tools Flow and Action - Grader Script (Level 5)
Output format matches Level 2 Lab 6.2 template.

Checks level5/data/basics/transfer_money_tools.yml, action_process_transfer_with_tools.py,
domain actions, and from_llm slot conditions for transfer_money_tools. Runs from workspace root;
expects /home/codio/workspace.
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


def slot_has_active_flow(domain_data: dict, slot_name: str, flow_id: str) -> bool:
    """True if a from_llm mapping on slot_name includes active_flow: flow_id."""
    slots = domain_data.get("slots") or {}
    slot_def = slots.get(slot_name)
    if not isinstance(slot_def, dict):
        return False
    for m in slot_def.get("mappings") or []:
        if not isinstance(m, dict) or m.get("type") != "from_llm":
            continue
        for cond in m.get("conditions") or []:
            if isinstance(cond, dict) and cond.get("active_flow") == flow_id:
                return True
    return False


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

# Check 3: Action file, name(), and user-visible confirmation (2 points)
print("Check 3: Verifying action_process_transfer_with_tools.py...")
if not ACTION_PATH.exists():
    print("❌ Check 3: FAILED - level5/actions/action_process_transfer_with_tools.py not found (0 points)")
else:
    action_content = ACTION_PATH.read_text(encoding="utf-8")
    has_name = "action_process_transfer_with_tools" in action_content and "def name" in action_content.lower()
    has_run = "def run" in action_content.lower()
    uses_slots = "get_slot" in action_content and all(
        s in action_content for s in ("amount", "recipient", "account_from")
    )
    confirms = "utter_message" in action_content
    if has_name and has_run and uses_slots and confirms:
        print(" Check 3: PASSED - action with name(), run(), slot reads, utter_message (2 points)")
        score += 2
    else:
        print(
            "❌ Check 3: FAILED - action must implement run(), read amount/recipient/account_from "
            "via tracker.get_slot, and send at least one utter_message (0 points)"
        )
print("")

# Check 4: Domain lists action (1 point)
print("Check 4: Verifying domain actions list...")
domain_data = None
if not DOMAIN_PATH.exists():
    print("❌ Check 4: FAILED - level5/domain/basics.yml not found (0 points)")
else:
    try:
        with open(DOMAIN_PATH, encoding="utf-8") as f:
            domain_data = yaml.safe_load(f)
        actions = domain_data.get("actions") or []
        if "action_process_transfer_with_tools" in actions:
            print(" Check 4: PASSED - action in domain (1 point)")
            score += 1
        else:
            print("❌ Check 4: FAILED - Add action_process_transfer_with_tools to domain actions (0 points)")
    except Exception as e:
        print(f"❌ Check 4: FAILED - Could not parse domain: {e} (0 points)")
print("")

# Check 5: Domain slots allow transfer_money_tools flow (2 points)
print("Check 5: Verifying from_llm conditions include active_flow: transfer_money_tools...")
if domain_data is None:
    print("❌ Check 5: FAILED - domain not loaded (0 points)")
else:
    ok = True
    for slot_name in ("amount", "recipient", "account_from"):
        if not slot_has_active_flow(domain_data, slot_name, "transfer_money_tools"):
            ok = False
            break
    if ok:
        print(
            " Check 5: PASSED - amount, recipient, account_from map from_llm for "
            "transfer_money_tools (2 points)"
        )
        score += 2
    else:
        print(
            "❌ Check 5: FAILED - Each of amount, recipient, account_from needs "
            "from_llm conditions including active_flow: transfer_money_tools (0 points)"
        )
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 4.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (flow file) | Check 2 (flow steps) | Check 3 (action) | "
    "Check 4 (domain actions) | Check 5 (domain slot conditions)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
