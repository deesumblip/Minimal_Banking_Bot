#!/usr/bin/env python3
"""
Lab 5.2: Testing / Completion Check - Grader Script
Verifies all Level 5 artifacts: tools/, endpoints.yml tools, transfer_money_tools.yml,
action_process_transfer_with_tools, domain, and model. Runs from workspace root.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
LEVEL5 = WORKSPACE_ROOT / "level5"
TOOLS_DIR = LEVEL5 / "tools"
BANKING_TOOLS = TOOLS_DIR / "banking_tools.py"
ENDPOINTS_PATH = LEVEL5 / "endpoints.yml"
FLOW_PATH = LEVEL5 / "data" / "basics" / "transfer_money_tools.yml"
ACTION_PATH = LEVEL5 / "actions" / "action_process_transfer_with_tools.py"
DOMAIN_PATH = LEVEL5 / "domain" / "basics.yml"
MODELS_DIR = LEVEL5 / "models"

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML required. Use project venv Python.")
    sys.exit(1)

score = 0
max_score = 10

print("Running Lab 5.2 Completion Check...")
print("")

# Check 1: tools/ and banking_tools.py (2 points)
print("Check 1: Verifying tools folder and banking_tools.py...")
if TOOLS_DIR.is_dir() and BANKING_TOOLS.exists():
    content = BANKING_TOOLS.read_text(encoding="utf-8")
    if "__all__" in content and "check_balance" in content and "process_transfer" in content:
        print("✅ Check 1: PASSED - tools/ and banking_tools.py with __all__ (2 points)")
        score += 2
    else:
        print("❌ Check 1: FAILED - banking_tools.py must have __all__ and tool functions (0 points)")
else:
    print("❌ Check 1: FAILED - level5/tools/ or banking_tools.py not found (0 points)")
print("")

# Check 2: endpoints.yml tools (2 points)
print("Check 2: Verifying endpoints.yml tools section...")
if ENDPOINTS_PATH.exists():
    try:
        with open(ENDPOINTS_PATH, encoding="utf-8") as f:
            ep = yaml.safe_load(f)
        tools = ep.get("tools") or {}
        if tools.get("tools_module") == "tools":
            print("✅ Check 2: PASSED - endpoints.yml has tools_module (2 points)")
            score += 2
        else:
            print("❌ Check 2: FAILED - tools: tools_module: \"tools\" required (0 points)")
    except Exception as e:
        print(f"❌ Check 2: FAILED - {e} (0 points)")
else:
    print("❌ Check 2: FAILED - level5/endpoints.yml not found (0 points)")
print("")

# Check 3: transfer_money_tools.yml and action (3 points)
print("Check 3: Verifying flow and action file...")
flow_ok = False
action_ok = False
if FLOW_PATH.exists():
    try:
        with open(FLOW_PATH, encoding="utf-8") as f:
            fd = yaml.safe_load(f)
        flows = fd.get("flows") or {}
        for flow_def in flows.values() if isinstance(flows, dict) else []:
            if not isinstance(flow_def, dict):
                continue
            for step in flow_def.get("steps") or []:
                if isinstance(step, dict) and step.get("action") == "action_process_transfer_with_tools":
                    flow_ok = True
                    break
            if flow_ok:
                break
    except Exception:
        pass
if ACTION_PATH.exists():
    ac = ACTION_PATH.read_text(encoding="utf-8")
    action_ok = "action_process_transfer_with_tools" in ac and "def name" in ac.lower()
if flow_ok and action_ok:
    print("✅ Check 3: PASSED - transfer_money_tools.yml and action file (3 points)")
    score += 3
else:
    print("❌ Check 3: FAILED - Flow and action_process_transfer_with_tools.py required (0 points)")
print("")

# Check 4: Domain and model (3 points)
print("Check 4: Verifying domain and model...")
domain_ok = False
if DOMAIN_PATH.exists():
    try:
        with open(DOMAIN_PATH, encoding="utf-8") as f:
            dm = yaml.safe_load(f)
        domain_ok = "action_process_transfer_with_tools" in (dm.get("actions") or [])
    except Exception:
        pass
model_ok = MODELS_DIR.exists() and bool(list(MODELS_DIR.glob("*.tar.gz")))
if domain_ok and model_ok:
    print("✅ Check 4: PASSED - domain has action and model exists (3 points)")
    score += 3
elif domain_ok:
    print("⚠️ Check 4: PARTIAL - domain OK; run 'cd level5' and 'python -m rasa train' (1 point)")
    score += 1
else:
    print("❌ Check 4: FAILED - domain must list action_process_transfer_with_tools; train from level5 (0 points)")
print("")

# Summary
print("=" * 50)
if score >= max_score:
    print(f"✅ PASS: Lab 5.2 completion check passed! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
    print("=" * 50)
    sys.exit(0)
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Complete Labs 2.1–5.1 and re-run training if needed.")
    print("FAIL")
    print("=" * 50)
    sys.exit(1)
