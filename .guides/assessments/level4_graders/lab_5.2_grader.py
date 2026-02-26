#!/usr/bin/env python3
"""
Lab 4.5: Testing the Transfer Flow - Completion Check - Grader Script
Verifies Level 4 bot is complete: domain (slots + ask responses + action), action file,
transfer_money.yml flow, and a trained model. Runs from workspace root.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
LEVEL4 = WORKSPACE_ROOT / "level4"
DOMAIN_PATH = LEVEL4 / "domain" / "basics.yml"
ACTION_PATH = LEVEL4 / "actions" / "action_process_transfer.py"
FLOW_PATH = LEVEL4 / "data" / "basics" / "transfer_money.yml"
MODELS_DIR = LEVEL4 / "models"

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML required. Use project venv Python.")
    sys.exit(1)

score = 0
max_score = 10

print("Running Lab 4.5 Completion Check...")
print("")

# Check 1: Domain (3 points)
print("Check 1: Verifying domain has transfer slots, ask responses, and action...")
if not DOMAIN_PATH.exists():
    print("❌ Check 1: FAILED - level4/domain/basics.yml not found (0 points)")
else:
    try:
        with open(DOMAIN_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        slots = data.get("slots") or {}
        responses = data.get("responses") or {}
        actions = data.get("actions") or []
        has_slots = all(s in slots for s in ["amount", "recipient", "account_from"])
        has_asks = all(r in responses for r in ["utter_ask_amount", "utter_ask_recipient", "utter_ask_account_from"])
        has_action = "action_process_transfer" in actions
        if has_slots and has_asks and has_action:
            print("✅ Check 1: PASSED - Domain has transfer slots, ask responses, action_process_transfer (3 points)")
            score += 3
        else:
            missing = []
            if not has_slots: missing.append("slots amount/recipient/account_from")
            if not has_asks: missing.append("utter_ask_amount/recipient/account_from")
            if not has_action: missing.append("action_process_transfer in actions")
            print(f"❌ Check 1: FAILED - Domain missing: {missing} (0 points)")
    except Exception as e:
        print(f"❌ Check 1: FAILED - Could not parse domain: {e} (0 points)")
print("")

# Check 2: Action file (3 points)
print("Check 2: Verifying action_process_transfer.py reads three slots...")
if not ACTION_PATH.exists():
    print("❌ Check 2: FAILED - level4/actions/action_process_transfer.py not found (0 points)")
else:
    content = ACTION_PATH.read_text(encoding="utf-8")
    has_amount = "get_slot" in content and ("amount" in content)
    has_recipient = "recipient" in content and "get_slot" in content
    has_account_from = "account_from" in content and "get_slot" in content
    has_name = "action_process_transfer" in content and "def name" in content.lower()
    if has_amount and has_recipient and has_account_from and has_name:
        print("✅ Check 2: PASSED - Action file exists and reads amount, recipient, account_from (3 points)")
        score += 3
    else:
        print("❌ Check 2: FAILED - Action file must define name() and run() reading amount, recipient, account_from (0 points)")
print("")

# Check 3: Flow file (2 points)
print("Check 3: Verifying transfer_money.yml with collect steps and action...")
if not FLOW_PATH.exists():
    print("❌ Check 3: FAILED - level4/data/basics/transfer_money.yml not found (0 points)")
else:
    try:
        with open(FLOW_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        flows = data.get("flows") or {}
        collect_found = set()
        has_action_step = False
        for flow_def in flows.values() if isinstance(flows, dict) else []:
            if not isinstance(flow_def, dict):
                continue
            for step in flow_def.get("steps") or []:
                if isinstance(step, dict):
                    if "collect" in step:
                        collect_found.add(step.get("collect"))
                    if step.get("action") == "action_process_transfer":
                        has_action_step = True
        required_collect = {"amount", "recipient", "account_from"}
        if required_collect.issubset(collect_found) and has_action_step:
            print("✅ Check 3: PASSED - transfer_money.yml has collect steps and action (2 points)")
            score += 2
        else:
            print("❌ Check 3: FAILED - Flow must have collect amount/recipient/account_from and action: action_process_transfer (0 points)")
    except Exception as e:
        print(f"❌ Check 3: FAILED - Invalid YAML or structure: {e} (0 points)")
print("")

# Check 4: Model (2 points)
print("Check 4: Verifying trained model exists...")
if not MODELS_DIR.exists() or not list(MODELS_DIR.glob("*.tar.gz")):
    print("❌ Check 4: FAILED - No model file in level4/models/ (0 points)")
    print("Hint: Run 'cd level4' and 'python -m rasa train' with venv activated")
else:
    print("✅ Check 4: PASSED - Model file exists (2 points)")
    score += 2
print("")

# Summary
print("=" * 50)
if score >= max_score:
    print(f"✅ PASS: Lab 4.5 completion check passed! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
    print("=" * 50)
    sys.exit(0)
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Complete Labs 4.1–4.4 and re-run training if needed.")
    print("FAIL")
    print("=" * 50)
    sys.exit(1)
