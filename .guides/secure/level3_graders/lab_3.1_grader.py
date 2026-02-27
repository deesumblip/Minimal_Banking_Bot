#!/usr/bin/env python3
"""
Lab 3.1: Defining a Slot in the Domain - Grader Script
Checks level3/domain/basics.yml for: slots section, account slot (text),
utter_ask_account response, action_check_balance_simple in actions.
Runs from workspace root; expects /home/codio/workspace.
"""

import os
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
DOMAIN_PATH = WORKSPACE_ROOT / "level3" / "domain" / "basics.yml"

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML is required. Activate the project venv: source .venv/bin/activate")
    sys.exit(1)

score = 0
max_score = 10

print("Running Lab 3.1 Assessment Checks...")
print("")

# Check 0: Domain file exists
print("Check 0: Verifying domain file exists...")
if not DOMAIN_PATH.exists():
    print("❌ Check 0: FAILED - level3/domain/basics.yml not found (0 points)")
    print("Hint: Add domain/basics.yml in the level3 folder with slots, responses, and actions.")
    print("FAIL")
    sys.exit(1)
print("✅ Check 0: PASSED - domain file exists")
score += 1
print("")

# Load YAML
try:
    with open(DOMAIN_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
except Exception as e:
    print("❌ FAILED - domain/basics.yml has YAML syntax errors:")
    print(f"   {e}")
    print("Hint: Check indentation (2 spaces), colons, and list dashes. Avoid tabs.")
    print("FAIL")
    sys.exit(1)

if not isinstance(data, dict):
    print("❌ FAILED - domain file must be a YAML mapping (key-value).")
    print("FAIL")
    sys.exit(1)

# Check 1: slots section (2 points)
print("Check 1: Verifying slots: section...")
slots = data.get("slots")
if not isinstance(slots, dict):
    print("❌ Check 1: FAILED - No top-level 'slots:' section or it is not a mapping (0 points)")
    print("Hint: Add a 'slots:' section at the top level with at least one slot.")
else:
    print("✅ Check 1: PASSED - slots: section present (2 points)")
    score += 2
print("")

# Check 2: account slot with type text (2 points)
print("Check 2: Verifying account slot (type text)...")
if not isinstance(slots, dict):
    print("❌ Check 2: FAILED - slots section missing (0 points)")
elif "account" not in slots:
    print("❌ Check 2: FAILED - 'account' slot not found under slots: (0 points)")
    print("Hint: Add 'account:' under slots: with type: text")
else:
    acc = slots["account"]
    slot_type = acc.get("type") if isinstance(acc, dict) else None
    if slot_type == "text" or (isinstance(slot_type, str) and slot_type.strip().lower() == "text"):
        print("✅ Check 2: PASSED - account slot with type text (2 points)")
        score += 2
    else:
        print("⚠️  Check 2: PARTIAL - account slot exists but type should be 'text' (1 point)")
        score += 1
print("")

# Check 3: utter_ask_account in responses (2 points)
print("Check 3: Verifying utter_ask_account response...")
responses = data.get("responses")
if not isinstance(responses, dict):
    print("❌ Check 3: FAILED - No 'responses:' section or it is not a mapping (0 points)")
elif "utter_ask_account" not in responses:
    print("❌ Check 3: FAILED - utter_ask_account not found under responses: (0 points)")
    print("Hint: Add utter_ask_account with at least one text message (e.g. 'What is your account number?')")
else:
    r = responses["utter_ask_account"]
    has_text = False
    if isinstance(r, list):
        for item in r:
            if isinstance(item, dict) and item.get("text"):
                has_text = True
                break
    if has_text:
        print("✅ Check 3: PASSED - utter_ask_account with message (2 points)")
        score += 2
    else:
        print("⚠️  Check 3: PARTIAL - utter_ask_account present but needs at least one text (1 point)")
        score += 1
print("")

# Check 4: action_check_balance_simple in actions (3 points)
print("Check 4: Verifying action_check_balance_simple in actions...")
actions = data.get("actions")
if not isinstance(actions, list):
    print("❌ Check 4: FAILED - No 'actions:' list or it is not a list (0 points)")
    print("Hint: Add an actions: section with - action_check_balance_simple")
elif "action_check_balance_simple" not in actions:
    print("❌ Check 4: FAILED - action_check_balance_simple not in actions list (0 points)")
    print("Hint: Add '- action_check_balance_simple' under the actions: section")
else:
    print("✅ Check 4: PASSED - action_check_balance_simple registered (3 points)")
    score += 3
print("")

# Summary
print("=" * 50)
if score >= max_score:
    print(f"✅ PASS: Lab 3.1 verification complete! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
    print("=" * 50)
    sys.exit(0)
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Review the failed checks above.")
    print("FAIL")
    print("=" * 50)
    sys.exit(1)
