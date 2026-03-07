#!/usr/bin/env python3
"""
Lab 4.1: ask_banking_assistant Flow - Grader
Checks level6/data/basics/ask_banking_assistant.yml exists and flow has call: banking_assistant.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
FLOW_FILE = WORKSPACE_ROOT / "level6" / "data" / "basics" / "ask_banking_assistant.yml"

print("Running Lab 4.1 Assessment Checks...")
print("")

if not FLOW_FILE.exists():
    print("FAIL: level6/data/basics/ask_banking_assistant.yml not found")
    sys.exit(1)

try:
    content = FLOW_FILE.read_text(encoding="utf-8")
except Exception as e:
    print(f"FAIL: Could not read flow file: {e}")
    sys.exit(1)

if "call:" not in content or "banking_assistant" not in content:
    print("FAIL: Flow should contain a step with call: banking_assistant")
    sys.exit(1)

if "ask_banking_assistant" not in content:
    print("FAIL: Flow should be named ask_banking_assistant")
    sys.exit(1)

print("PASS")
sys.exit(0)
