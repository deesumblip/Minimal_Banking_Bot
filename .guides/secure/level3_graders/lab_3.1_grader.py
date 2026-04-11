#!/usr/bin/env python3
"""
Lab 3.1: Defining a Slot in the Domain - Grader Script
Output format matches Level 2 Lab 6.2 template (level2 lab_4.1_grader.sh):
  Check 1–8 with leading space on PASSED lines (" Check N: PASSED - ..."), no emoji on pass;
  ❌ / ⚠️ on fail or partial; ========== summary band; exit 0 only on full score.

Checks level3/domain/basics.yml for: file exists, valid YAML, slots:, account, utter_ask_account,
three actions. Runs from workspace root; expects /home/codio/workspace.
"""

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

# Check 1: Domain file exists
print("Check 1: Verifying domain file exists...")
if not DOMAIN_PATH.exists():
    print("❌ Check 1: FAILED - level3/domain/basics.yml not found (0 points)")
    print("Hint: Add domain/basics.yml in the level3 folder with slots, responses, and actions.")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - level3/domain/basics.yml exists (1 point)")
score += 1
print("")

# Check 2: Valid YAML (gate; no points)
print("Check 2: Verifying YAML syntax and top-level structure...")
data = None
yaml_err = ""
try:
    with open(DOMAIN_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
except Exception as e:
    yaml_err = str(e)

if yaml_err:
    print("❌ Check 2: FAILED - domain/basics.yml has YAML syntax errors (0 points)")
    print(f"   {yaml_err}")
    print("Hint: Check indentation (2 spaces), colons, and list dashes. Avoid tabs.")
    print("FAIL")
    sys.exit(1)
if not isinstance(data, dict):
    print("❌ Check 2: FAILED - domain file must be a YAML mapping (key-value root) (0 points)")
    print("Hint: The file should start with keys like version:, responses:, actions:, not a bare list.")
    print("FAIL")
    sys.exit(1)
print(" Check 2: PASSED - valid YAML with a top-level mapping (required for following checks)")
print("")

slots = data.get("slots")
responses = data.get("responses")
actions = data.get("actions")

# Check 3: slots section (2 points)
print("Check 3: Verifying slots: section...")
if not isinstance(slots, dict):
    print("❌ Check 3: FAILED - No top-level 'slots:' section or it is not a mapping (0 points)")
    print("Hint: Add a 'slots:' section at the top level with at least one slot.")
else:
    print(" Check 3: PASSED - slots: section present (2 points)")
    score += 2
print("")

# Check 4: account slot with type text (2 points; 1 partial)
print("Check 4: Verifying account slot (type text)...")
if not isinstance(slots, dict):
    print("❌ Check 4: FAILED - slots section missing (0 points)")
    print("Hint: Add 'slots:' with an 'account:' entry and type: text")
elif "account" not in slots:
    print("❌ Check 4: FAILED - 'account' slot not found under slots: (0 points)")
    print("Hint: Add 'account:' under slots: with type: text")
else:
    acc = slots["account"]
    slot_type = acc.get("type") if isinstance(acc, dict) else None
    if slot_type == "text" or (
        isinstance(slot_type, str) and slot_type.strip().lower() == "text"
    ):
        print(" Check 4: PASSED - account slot with type text (2 points)")
        score += 2
    elif isinstance(acc, dict):
        print("⚠️  Check 4: PARTIAL - account slot exists but type should be 'text' (1 point)")
        score += 1
    else:
        print("❌ Check 4: FAILED - account slot must be a mapping with type: text (0 points)")
print("")

# Check 5: utter_ask_account in responses (2 points; 1 partial)
print("Check 5: Verifying utter_ask_account response...")
if not isinstance(responses, dict):
    print("❌ Check 5: FAILED - No 'responses:' section or it is not a mapping (0 points)")
    print("Hint: Keep a top-level responses: block and add utter_ask_account under it.")
elif "utter_ask_account" not in responses:
    print("❌ Check 5: FAILED - utter_ask_account not found under responses: (0 points)")
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
        print(" Check 5: PASSED - utter_ask_account with message (2 points)")
        score += 2
    else:
        print("⚠️  Check 5: PARTIAL - utter_ask_account present but needs at least one text (1 point)")
        score += 1
print("")

# Check 6: action_check_balance_simple in actions (1 point)
print("Check 6: Verifying action_check_balance_simple in actions...")
if not isinstance(actions, list):
    print("❌ Check 6: FAILED - No 'actions:' list or it is not a list (0 points)")
    print("Hint: Add an actions: section listing action_bank_hours, action_holiday_hours, and action_check_balance_simple")
elif "action_check_balance_simple" not in actions:
    print("❌ Check 6: FAILED - action_check_balance_simple not in actions list (0 points)")
    print("Hint: Add '- action_check_balance_simple' under the actions: section")
else:
    print(" Check 6: PASSED - action_check_balance_simple registered (1 point)")
    score += 1
print("")

# Check 7: action_bank_hours (1 point)
print("Check 7: Verifying action_bank_hours in actions...")
if not isinstance(actions, list):
    print("❌ Check 7: FAILED - actions list missing (0 points)")
elif "action_bank_hours" not in actions:
    print("❌ Check 7: FAILED - action_bank_hours missing from actions (0 points)")
    print("Hint: Include '- action_bank_hours' in the actions: list (see Lab 3.1 example).")
else:
    print(" Check 7: PASSED - action_bank_hours present (1 point)")
    score += 1
print("")

# Check 8: action_holiday_hours (1 point)
print("Check 8: Verifying action_holiday_hours in actions...")
if not isinstance(actions, list):
    print("❌ Check 8: FAILED - actions list missing (0 points)")
elif "action_holiday_hours" not in actions:
    print("❌ Check 8: FAILED - action_holiday_hours missing from actions (0 points)")
    print("Hint: Include '- action_holiday_hours' in the actions: list (pairs with holiday_hours flow).")
else:
    print(" Check 8: PASSED - action_holiday_hours present (1 point)")
    score += 1
print("")

# Summary (same band style as Level 2 Lab 4.1 / Lab 6.2 shell graders)
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 3.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (domain file) | Check 2 (valid YAML) | Check 3 (slots:) | "
    "Check 4 (account) | Check 5 (utter_ask_account) | Check 6 (action_check_balance_simple) | "
    "Check 7 (action_bank_hours) | Check 8 (action_holiday_hours)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
