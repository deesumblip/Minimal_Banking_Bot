#!/usr/bin/env python3
"""
Lab 4.1: Adding Multiple Slots in the Domain - Grader Script
Checks level4/domain/basics.yml for: slots amount, recipient, account_from;
utter_ask_amount, utter_ask_recipient, utter_ask_account_from; action_process_transfer in actions.
Runs from workspace root; expects /home/codio/workspace.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
DOMAIN_PATH = WORKSPACE_ROOT / "level4" / "domain" / "basics.yml"

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML is required. Use the project venv Python: .venv/bin/python3")
    sys.exit(1)

score = 0
max_score = 10

print("Running Lab 4.1 Assessment Checks...")
print("")

# Check 0: Domain file exists
print("Check 0: Verifying domain file exists...")
if not DOMAIN_PATH.exists():
    print("❌ Check 0: FAILED - level4/domain/basics.yml not found (0 points)")
    print("Hint: Add domain/basics.yml in the level4 folder with slots, responses, and actions.")
    print("FAIL")
    sys.exit(1)
print("✅ Check 0: PASSED - domain file exists")
score += 1
print("")

try:
    with open(DOMAIN_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
except Exception as e:
    print("❌ FAILED - domain/basics.yml has YAML syntax errors:")
    print(f"   {e}")
    print("FAIL")
    sys.exit(1)

if not isinstance(data, dict):
    print("❌ FAILED - domain file must be a YAML mapping.")
    print("FAIL")
    sys.exit(1)

slots = data.get("slots") or {}
responses = data.get("responses") or {}
actions = data.get("actions")
if not isinstance(actions, list):
    actions = []

# Check 1: slots amount, recipient, account_from (3 points)
print("Check 1: Verifying slots amount, recipient, account_from...")
required_slots = ["amount", "recipient", "account_from"]
missing_slots = [s for s in required_slots if s not in slots]
if not missing_slots:
    print("✅ Check 1: PASSED - all three slots present (3 points)")
    score += 3
else:
    print(f"❌ Check 1: FAILED - missing slots: {missing_slots} (0 points)")
    print("Hint: Add amount, recipient, account_from under slots: with type: text")
print("")

# Check 2: utter_ask_amount, utter_ask_recipient, utter_ask_account_from (3 points)
print("Check 2: Verifying ask responses...")
required_asks = ["utter_ask_amount", "utter_ask_recipient", "utter_ask_account_from"]
missing_asks = []
for r in required_asks:
    if r not in responses:
        missing_asks.append(r)
    else:
        val = responses[r]
        has_text = isinstance(val, list) and val and isinstance(val[0], dict) and val[0].get("text")
        if not has_text:
            missing_asks.append(r)
if not missing_asks:
    print("✅ Check 2: PASSED - all three ask responses present (3 points)")
    score += 3
else:
    print(f"❌ Check 2: FAILED - missing or empty ask responses: {missing_asks} (0 points)")
    print("Hint: Add utter_ask_amount, utter_ask_recipient, utter_ask_account_from under responses: with - text: '...'")
print("")

# Check 3: action_process_transfer in actions (3 points)
print("Check 3: Verifying action_process_transfer in actions...")
if "action_process_transfer" in actions:
    print("✅ Check 3: PASSED - action_process_transfer registered (3 points)")
    score += 3
else:
    print("❌ Check 3: FAILED - action_process_transfer not in actions list (0 points)")
    print("Hint: Add - action_process_transfer under the actions: section")
print("")

# Summary
print("=" * 50)
if score >= max_score:
    print(f"✅ PASS: Lab 4.1 verification complete! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
    print("=" * 50)
    sys.exit(0)
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Review the failed checks above.")
    print("FAIL")
    print("=" * 50)
    sys.exit(1)
