#!/usr/bin/env python3
"""
Lab 2.1: Creating the Tools Folder and banking_tools.py - Grader Script
Checks level5/tools/ and level5/tools/banking_tools.py for: check_balance, process_transfer,
get_account_info, __all__. Runs from workspace root; expects /home/codio/workspace.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
TOOLS_DIR = WORKSPACE_ROOT / "level5" / "tools"
BANKING_TOOLS = TOOLS_DIR / "banking_tools.py"

score = 0
max_score = 10

print("Running Lab 2.1 Assessment Checks...")
print("")

# Check 0: tools/ folder exists
print("Check 0: Verifying level5/tools/ exists...")
if not TOOLS_DIR.is_dir():
    print("❌ Check 0: FAILED - level5/tools/ not found (0 points)")
    print("Hint: Create the tools folder inside level5")
    print("FAIL")
    sys.exit(1)
print("✅ Check 0: PASSED - tools folder exists")
score += 2
print("")

# Check 1: banking_tools.py exists
print("Check 1: Verifying banking_tools.py exists...")
if not BANKING_TOOLS.exists():
    print("❌ Check 1: FAILED - level5/tools/banking_tools.py not found (0 points)")
    print("Hint: Create banking_tools.py in level5/tools/")
    print("FAIL")
    sys.exit(1)
print("✅ Check 1: PASSED - banking_tools.py exists")
score += 2
print("")

try:
    content = BANKING_TOOLS.read_text(encoding="utf-8")
except Exception as e:
    print("❌ FAILED - Could not read banking_tools.py:")
    print(f"   {e}")
    print("FAIL")
    sys.exit(1)

# Check 2: Required function names (4 points)
print("Check 2: Verifying tool functions...")
required = ["check_balance", "process_transfer", "get_account_info"]
missing = [f for f in required if f not in content]
if not missing:
    print("✅ Check 2: PASSED - check_balance, process_transfer, get_account_info present (4 points)")
    score += 4
else:
    print(f"❌ Check 2: FAILED - missing: {missing} (0 points)")
    print("Hint: Define functions check_balance(account), process_transfer(amount, from_account, to_account), get_account_info(account)")
print("")

# Check 3: __all__ (2 points)
print("Check 3: Verifying __all__ export...")
if "__all__" in content:
    print("✅ Check 3: PASSED - __all__ present (2 points)")
    score += 2
else:
    print("❌ Check 3: FAILED - __all__ not found (0 points)")
    print("Hint: Add __all__ = ['check_balance', 'process_transfer', 'get_account_info']")
print("")

# Summary
print("=" * 50)
if score >= max_score:
    print(f"✅ PASS: Lab 2.1 verification complete! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
    print("=" * 50)
    sys.exit(0)
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Review the failed checks above.")
    print("FAIL")
    print("=" * 50)
    sys.exit(1)
