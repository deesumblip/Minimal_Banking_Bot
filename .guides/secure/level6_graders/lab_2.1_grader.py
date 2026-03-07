#!/usr/bin/env python3
"""
Lab 2.1: Sub-Agent Config - Grader
Checks level6/sub_agents/banking_assistant/config.yml exists and has agent name, protocol, mcp_servers.
Runs from workspace root; expects /home/codio/workspace on Codio.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]  # repo root when run locally
CONFIG = WORKSPACE_ROOT / "level6" / "sub_agents" / "banking_assistant" / "config.yml"

score = 0
max_score = 10

print("Running Lab 2.1 Assessment Checks...")
print("")

if not CONFIG.exists():
    print("FAIL: level6/sub_agents/banking_assistant/config.yml not found")
    sys.exit(1)

try:
    content = CONFIG.read_text(encoding="utf-8")
except Exception as e:
    print(f"FAIL: Could not read config: {e}")
    sys.exit(1)

if "banking_assistant" not in content:
    print("FAIL: config.yml should contain agent name banking_assistant")
    sys.exit(1)
score += 3

if "RASA" not in content and "protocol" not in content.lower():
    print("FAIL: config.yml should contain protocol (e.g. RASA)")
    sys.exit(1)
score += 3

if "mcp_servers" not in content:
    print("FAIL: config.yml should contain mcp_servers (under connections)")
    sys.exit(1)
score += 4

print("PASS")
sys.exit(0)
