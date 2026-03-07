#!/usr/bin/env python3
"""
Lab 5.2: Completion Check Level 6 - Grader
Verifies all Level 6 artifacts: sub_agent config, mcp_servers, ask_banking_assistant flow.
Optionally checks for models/.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
LEVEL6 = WORKSPACE_ROOT / "level6"

def check(msg, cond):
    if not cond:
        print(f"FAIL: {msg}")
        sys.exit(1)

print("Running Lab 5.2 Completion Check...")
print("")

config = LEVEL6 / "sub_agents" / "banking_assistant" / "config.yml"
check("level6/sub_agents/banking_assistant/config.yml must exist", config.exists())

endpoints = LEVEL6 / "endpoints.yml"
check("level6/endpoints.yml must exist", endpoints.exists())
check("endpoints.yml must contain mcp_servers", "mcp_servers" in endpoints.read_text(encoding="utf-8"))

flow_file = LEVEL6 / "data" / "basics" / "ask_banking_assistant.yml"
check("level6/data/basics/ask_banking_assistant.yml must exist", flow_file.exists())
content = flow_file.read_text(encoding="utf-8")
check("Flow must contain call: banking_assistant", "call:" in content and "banking_assistant" in content)

print("PASS")
sys.exit(0)
