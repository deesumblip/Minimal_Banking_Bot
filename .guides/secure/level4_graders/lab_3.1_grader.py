#!/usr/bin/env python3
"""
Lab 4.2: Writing the Action That Uses Multiple Slots - Grader Script
Checks level4/actions/action_process_transfer.py for: correct class, name(),
run() reading amount, recipient, account_from slots, and sending a message.
Runs from workspace root; expects /home/codio/workspace.
"""

import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
ACTION_PATH = WORKSPACE_ROOT / "level4" / "actions" / "action_process_transfer.py"

score = 0
max_score = 10

print("Running Lab 4.2 Assessment Checks...")
print("")

# Check 0: Action file exists
print("Check 0: Verifying action file exists...")
if not ACTION_PATH.exists():
    print("❌ Check 0: FAILED - level4/actions/action_process_transfer.py not found (0 points)")
    print("Hint: Create the file in level4/actions/ with the name action_process_transfer.py")
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

content_lower = content.lower()

# Check 1: Required imports (2 points)
print("Check 1: Verifying imports...")
has_action = "action" in content_lower and "rasa_sdk" in content
has_tracker = "tracker" in content_lower and "rasa_sdk" in content
has_dispatcher = "collectingdispatcher" in content_lower or "dispatcher" in content_lower
if has_action and has_tracker and has_dispatcher:
    print("✅ Check 1: PASSED - Action, Tracker, and CollectingDispatcher present (2 points)")
    score += 2
else:
    print("❌ Check 1: FAILED - Missing or incorrect imports (0 points)")
    print("Hint: Import Action, Tracker from rasa_sdk and CollectingDispatcher from rasa_sdk.executor")
print("")

# Check 2: Class ActionProcessTransfer(Action) (1 point)
print("Check 2: Verifying class definition...")
if re.search(r"class\s+ActionProcessTransfer\s*\(\s*Action\s*\)", content):
    print("✅ Check 2: PASSED - ActionProcessTransfer(Action) found (1 point)")
    score += 1
else:
    print("❌ Check 2: FAILED - Class ActionProcessTransfer(Action) not found (0 points)")
print("")

# Check 3: name() returns "action_process_transfer" (1 point)
print("Check 3: Verifying name() method...")
if re.search(r'return\s+["\']action_process_transfer["\']', content) or (
    "action_process_transfer" in content and "def name" in content_lower
):
    print("✅ Check 3: PASSED - name() returns 'action_process_transfer' (1 point)")
    score += 1
else:
    print("❌ Check 3: FAILED - name() must return the string 'action_process_transfer' (0 points)")
print("")

# Check 4: run() reads all three slots (3 points)
print("Check 4: Verifying run() reads amount, recipient, account_from...")
has_amount = "get_slot" in content and ('"amount"' in content or "'amount'" in content)
has_recipient = "recipient" in content and "get_slot" in content
has_account_from = "account_from" in content and "get_slot" in content
if has_amount and has_recipient and has_account_from:
    print("✅ Check 4: PASSED - run() reads amount, recipient, account_from (3 points)")
    score += 3
else:
    missing = []
    if not has_amount: missing.append("amount")
    if not has_recipient: missing.append("recipient")
    if not has_account_from: missing.append("account_from")
    print(f"❌ Check 4: FAILED - run() must read all three slots; missing or unclear: {missing} (0 points)")
    print("Hint: amount = tracker.get_slot('amount') or ''; same for recipient and account_from")
print("")

# Check 5: Sends a message (1 point)
print("Check 5: Verifying confirmation message...")
if "utter_message" in content_lower and ("transfer" in content_lower or "amount" in content or "recipient" in content):
    print("✅ Check 5: PASSED - Sends a message (e.g. transfer confirmation) (1 point)")
    score += 1
else:
    print("❌ Check 5: FAILED - When slots are valid, send a message (dispatcher.utter_message(text=...)) (0 points)")
print("")

# Summary
print("=" * 50)
if score >= max_score:
    print(f"✅ PASS: Lab 4.2 verification complete! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
    print("=" * 50)
    sys.exit(0)
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Review the failed checks above.")
    print("FAIL")
    print("=" * 50)
    sys.exit(1)
