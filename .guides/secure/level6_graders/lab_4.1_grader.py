#!/usr/bin/env python3
"""
Lab 4.1: ask_banking_assistant Flow - Grader (Level 6)
Output format matches Level 2 Lab 6.2 template.

Checks level6/data/basics/ask_banking_assistant.yml exists and flow has call: banking_assistant.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
FLOW_FILE = WORKSPACE_ROOT / "level6" / "data" / "basics" / "ask_banking_assistant.yml"

score = 0
max_score = 10

print("Running Lab 4.1 Assessment Checks...")
print("")

# Check 1: file exists (2 points)
print("Check 1: Verifying ask_banking_assistant.yml exists...")
if not FLOW_FILE.exists():
    print("❌ Check 1: FAILED - level6/data/basics/ask_banking_assistant.yml not found (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - flow file found (2 points)")
score += 2
print("")

try:
    content = FLOW_FILE.read_text(encoding="utf-8")
except Exception as e:
    print(f"❌ Check 2: FAILED - Could not read flow file: {e} (0 points)")
    print("FAIL")
    sys.exit(1)

# Check 2: call: banking_assistant (5 points)
print("Check 2: Verifying call: banking_assistant...")
if "call:" not in content or "banking_assistant" not in content:
    print("❌ Check 2: FAILED - Flow should contain a step with call: banking_assistant (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 2: PASSED - call: banking_assistant present (5 points)")
score += 5
print("")

# Check 3: flow name ask_banking_assistant (3 points)
print("Check 3: Verifying flow name ask_banking_assistant...")
if "ask_banking_assistant" not in content:
    print("❌ Check 3: FAILED - Flow should be named ask_banking_assistant (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 3: PASSED - ask_banking_assistant name present (3 points)")
score += 3
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 4.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print("Summary: Check 1 (flow file) | Check 2 (call banking_assistant) | Check 3 (flow name)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
