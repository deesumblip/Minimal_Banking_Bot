#!/usr/bin/env python3
"""
Lab 4.1: Writing the Action That Uses the Slot - Grader Script
Checks level3/actions/action_check_balance_simple.py for: correct class, name(),
run() that reads account slot, placeholder check, re-prompt with utter_ask_account,
and balance message. Uses flexible checks (no exact string match).
Runs from workspace root; expects /home/codio/workspace.
"""

import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
ACTION_PATH = WORKSPACE_ROOT / "level3" / "actions" / "action_check_balance_simple.py"

score = 0
max_score = 10

print("Running Lab 4.1 Assessment Checks...")
print("")

# Check 0: Action file exists
print("Check 0: Verifying action file exists...")
if not ACTION_PATH.exists():
    print("❌ Check 0: FAILED - level3/actions/action_check_balance_simple.py not found (0 points)")
    print("Hint: Create the file in level3/actions/ with the name action_check_balance_simple.py")
    print("FAIL")
    sys.exit(1)
print("✅ Check 0: PASSED - action file exists")
score += 1
print("")

try:
    content = ACTION_PATH.read_text(encoding="utf-8")
except Exception as e:
    print("❌ FAILED - Could not read the action file:")
    print(f"   {e}")
    print("FAIL")
    sys.exit(1)

# Normalize for checks (ignore case for some keywords)
content_lower = content.lower()

# Check 1: Required imports (2 points)
print("Check 1: Verifying imports...")
has_action = "action" in content_lower and "rasa_sdk" in content
has_tracker = "tracker" in content_lower and "rasa_sdk" in content
has_dispatcher = "collectingdispatcher" in content_lower or "dispatcher" in content_lower
if has_action and has_tracker and has_dispatcher:
    print("✅ Check 1: PASSED - Action, Tracker, and CollectingDispatcher (or dispatcher) present (2 points)")
    score += 2
else:
    missing = []
    if not has_action: missing.append("Action from rasa_sdk")
    if not has_tracker: missing.append("Tracker from rasa_sdk")
    if not has_dispatcher: missing.append("CollectingDispatcher from rasa_sdk.executor")
    print("❌ Check 1: FAILED - Missing or incorrect imports (0 points)")
    print("Hint: Import Action, Tracker from rasa_sdk and CollectingDispatcher from rasa_sdk.executor")
print("")

# Check 2: Class ActionCheckBalanceSimple(Action) (1 point)
print("Check 2: Verifying class definition...")
if re.search(r"class\s+ActionCheckBalanceSimple\s*\(\s*Action\s*\)", content):
    print("✅ Check 2: PASSED - ActionCheckBalanceSimple(Action) found (1 point)")
    score += 1
else:
    print("❌ Check 2: FAILED - Class ActionCheckBalanceSimple(Action) not found (0 points)")
    print("Hint: Define class ActionCheckBalanceSimple(Action):")
print("")

# Check 3: name() returns "action_check_balance_simple" (1 point)
print("Check 3: Verifying name() method...")
if re.search(r'return\s+["\']action_check_balance_simple["\']', content) or \
   'action_check_balance_simple' in content and "def name" in content_lower:
    print("✅ Check 3: PASSED - name() returns 'action_check_balance_simple' (1 point)")
    score += 1
else:
    print("❌ Check 3: FAILED - name() must return the string 'action_check_balance_simple' (0 points)")
print("")

# Check 4: run() reads account slot (2 points)
print("Check 4: Verifying slot read...")
if "get_slot" in content and '"account"' in content or "'account'" in content:
    print("✅ Check 4: PASSED - run() reads account slot (tracker.get_slot('account')) (2 points)")
    score += 2
else:
    print("❌ Check 4: FAILED - run() must read the slot with tracker.get_slot('account') (0 points)")
    print("Hint: account = tracker.get_slot('account') or '<missing>'")
print("")

# Check 5: Placeholder check and re-prompt (2 points)
print("Check 5: Verifying placeholder handling and re-prompt...")
has_utter_ask = 'utter_ask_account' in content and 'utter_message' in content_lower
has_placeholder_idea = any(x in content_lower for x in ["placeholder", "account number", "<missing>", "missing"])
if has_utter_ask and has_placeholder_idea:
    print("✅ Check 5: PASSED - Re-prompts with utter_ask_account when slot is placeholder (2 points)")
    score += 2
else:
    if not has_utter_ask:
        print("❌ Check 5: FAILED - Must call dispatcher.utter_message(response='utter_ask_account') when slot is a placeholder (0 points)")
    else:
        print("❌ Check 5: FAILED - Must detect placeholder values (e.g. list with 'account number', '<missing>') and re-prompt (0 points)")
    print("Hint: If account (lowercased) is in your placeholder list, call dispatcher.utter_message(response='utter_ask_account') and return []")
print("")

# Check 6: Balance message (1 point)
print("Check 6: Verifying balance message...")
if "utter_message" in content_lower and ("balance" in content_lower or "account" in content) and "text" in content_lower:
    print("✅ Check 6: PASSED - Sends a message with balance/account for non-placeholder (1 point)")
    score += 1
else:
    print("❌ Check 6: FAILED - When slot is valid, send a message (e.g. dispatcher.utter_message(text=f'(Demo) Balance for account {account} is ...')) (0 points)")
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
