#!/usr/bin/env python3
"""
Lab 2.1: Sub-Agent Config - Grader (Level 6 / Level 6)
Output format matches Level 2 Lab 6.2 template.

Checks level6/sub_agents/banking_assistant/config.yml exists and has agent name, protocol,
mcp_servers, and configuration.module for BankingAssistantLiteAgent (course / tutorial LLM).
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
CONFIG = WORKSPACE_ROOT / "level6" / "sub_agents" / "banking_assistant" / "config.yml"

score = 0
max_score = 10

print("Running Lab 2.1 Assessment Checks...")
print("")

# Check 1: config exists and readable (2 points)
print("Check 1: Verifying banking_assistant config.yml exists...")
if not CONFIG.exists():
    print("❌ Check 1: FAILED - level6/sub_agents/banking_assistant/config.yml not found (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - config.yml found (2 points)")
score += 2
print("")

try:
    content = CONFIG.read_text(encoding="utf-8")
except Exception as e:
    print(f"❌ Check 2: FAILED - Could not read config: {e} (0 points)")
    print("FAIL")
    sys.exit(1)

# Check 2: banking_assistant name (3 points)
print("Check 2: Verifying agent name banking_assistant...")
if "banking_assistant" not in content:
    print("❌ Check 2: FAILED - config.yml should contain agent name banking_assistant (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 2: PASSED - banking_assistant present (3 points)")
score += 3
print("")

# Check 3: protocol (3 points)
print("Check 3: Verifying protocol (e.g. RASA)...")
if "RASA" not in content and "protocol" not in content.lower():
    print("❌ Check 3: FAILED - config.yml should contain protocol (e.g. RASA) (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 3: PASSED - protocol present (3 points)")
score += 3
print("")

# Check 4: mcp_servers (2 points)
print("Check 4: Verifying mcp_servers under connections...")
if "mcp_servers" not in content:
    print("❌ Check 4: FAILED - config.yml should contain mcp_servers (under connections) (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 4: PASSED - mcp_servers present (2 points)")
score += 2
print("")

# Check 5: configuration.module + Lite agent (required for tutorial LLM)
print("Check 5: Verifying configuration.module (BankingAssistantLiteAgent)...")
if "module" not in content or "BankingAssistantLiteAgent" not in content:
    print(
        "❌ Check 5: FAILED - config.yml should set configuration.module to "
        "actions.banking_assistant_lite_agent.BankingAssistantLiteAgent (0 points)"
    )
    print("FAIL")
    sys.exit(1)
print(" Check 5: PASSED - configuration.module includes BankingAssistantLiteAgent")
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 2.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (config file) | Check 2 (banking_assistant) | Check 3 (protocol) | "
    "Check 4 (mcp_servers) | Check 5 (module / BankingAssistantLiteAgent)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
