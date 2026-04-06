#!/usr/bin/env python3
"""
Lab 5.2: Completion Check (Transfer Flow) — Grader Script
Output format matches Chapter 1.2 Lab 6.2 template.

Verifies Level 4 agent is complete: domain (slots + ask responses + Level 3 account/ask +
legacy actions + action), action file, transfer_money.yml flow, trained model,
CompactLLMCommandGenerator in config, and endpoints model_groups (Lab 0.1 pattern).
Runs from workspace root.
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Repo root: .guides/secure/level4_graders/<this file> → four parents up (Codio + local)
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent.parent
LEVEL4 = WORKSPACE_ROOT / "level4"
DOMAIN_PATH = LEVEL4 / "domain" / "basics.yml"
ACTION_PATH = LEVEL4 / "actions" / "action_process_transfer.py"
FLOW_PATH = LEVEL4 / "data" / "basics" / "transfer_money.yml"
MODELS_DIR = LEVEL4 / "models"
CONFIG_PATH = LEVEL4 / "config.yml"
ENDPOINTS_PATH = LEVEL4 / "endpoints.yml"

REQUIRED_LEGACY_ACTIONS = (
    "action_bank_hours",
    "action_holiday_hours",
    "action_check_balance_simple",
)

REQUIRED_SLOTS = ("amount", "recipient", "account_from", "account")
REQUIRED_ASKS = (
    "utter_ask_amount",
    "utter_ask_recipient",
    "utter_ask_account_from",
    "utter_ask_account",
)

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML required. Use project venv Python.")
    sys.exit(1)

POINTS_PER_CHECK = 2
max_score = 12
score = 0

print("Running Lab 5.2 completion check...")
print("")

# Check 1: Domain — transfer + Level 3 account/ask + legacy + action_process_transfer
print(
    "Check 1: Verifying domain has transfer slots, account + asks, legacy actions, "
    "and action_process_transfer..."
)
if not DOMAIN_PATH.exists():
    print("❌ Check 1: FAILED - level4/domain/basics.yml not found (0 points)")
else:
    try:
        with open(DOMAIN_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        slots = data.get("slots") or {}
        responses = data.get("responses") or {}
        actions = data.get("actions") or []
        has_slots = all(s in slots for s in REQUIRED_SLOTS)
        has_asks = all(r in responses for r in REQUIRED_ASKS)
        has_action = "action_process_transfer" in actions
        has_legacy = all(a in actions for a in REQUIRED_LEGACY_ACTIONS)
        if has_slots and has_asks and has_action and has_legacy:
            print(
                f" Check 1: PASSED - Domain complete including account/utter_ask_account "
                f"({POINTS_PER_CHECK} points)"
            )
            score += POINTS_PER_CHECK
        else:
            missing = []
            if not has_slots:
                missing.append("slots " + "/".join(REQUIRED_SLOTS))
            if not has_asks:
                missing.append("responses " + "/".join(REQUIRED_ASKS))
            if not has_action:
                missing.append("action_process_transfer in actions")
            if not has_legacy:
                missing.append(
                    "action_bank_hours, action_holiday_hours, action_check_balance_simple in actions"
                )
            print(f"❌ Check 1: FAILED - Domain missing: {missing} (0 points)")
    except Exception as e:
        print(f"❌ Check 1: FAILED - Could not parse domain: {e} (0 points)")
print("")

# Check 2: Action file
print("Check 2: Verifying action_process_transfer.py reads three transfer slots...")
if not ACTION_PATH.exists():
    print("❌ Check 2: FAILED - level4/actions/action_process_transfer.py not found (0 points)")
else:
    content = ACTION_PATH.read_text(encoding="utf-8")
    has_amount = "get_slot" in content and ("amount" in content)
    has_recipient = "recipient" in content and "get_slot" in content
    has_account_from = "account_from" in content and "get_slot" in content
    has_name = "action_process_transfer" in content and "def name" in content.lower()
    if has_amount and has_recipient and has_account_from and has_name:
        print(
            f" Check 2: PASSED - Action file reads amount, recipient, account_from "
            f"({POINTS_PER_CHECK} points)"
        )
        score += POINTS_PER_CHECK
    else:
        print(
            "❌ Check 2: FAILED - Action file must define name() and run() reading "
            "amount, recipient, account_from (0 points)"
        )
print("")

# Check 3: Flow file
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
            print(f" Check 3: PASSED - transfer_money.yml structure OK ({POINTS_PER_CHECK} points)")
            score += POINTS_PER_CHECK
        else:
            print(
                "❌ Check 3: FAILED - Flow must have collect amount/recipient/account_from "
                "and action: action_process_transfer (0 points)"
            )
    except Exception as e:
        print(f"❌ Check 3: FAILED - Invalid YAML or structure: {e} (0 points)")
print("")

# Check 4: Model
print("Check 4: Verifying trained model exists...")
if not MODELS_DIR.exists() or not list(MODELS_DIR.glob("*.tar.gz")):
    print("❌ Check 4: FAILED - No model file in level4/models/ (0 points)")
    print("Hint: Run 'cd level4' and 'python -m rasa train' with venv activated")
else:
    print(f" Check 4: PASSED - Model file exists ({POINTS_PER_CHECK} points)")
    score += POINTS_PER_CHECK
print("")

# Check 5: Pipeline in config.yml
print("Check 5: Verifying level4/config.yml uses CompactLLMCommandGenerator...")
if not CONFIG_PATH.exists():
    print("❌ Check 5: FAILED - level4/config.yml not found (0 points)")
else:
    try:
        with open(CONFIG_PATH, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        pipeline = (cfg or {}).get("pipeline") or []
        names = []
        for step in pipeline:
            if isinstance(step, dict) and step.get("name"):
                names.append(step["name"])
        has_compact = "CompactLLMCommandGenerator" in names
        has_search_ready = "SearchReadyLLMCommandGenerator" in names
        if has_compact and not has_search_ready:
            print(
                f" Check 5: PASSED - pipeline uses CompactLLMCommandGenerator (not SearchReady) "
                f"({POINTS_PER_CHECK} points)"
            )
            score += POINTS_PER_CHECK
        elif has_search_ready:
            print("❌ Check 5: FAILED - config uses SearchReadyLLMCommandGenerator (0 points)")
            print(
                "Hint: Chapter 1.4 requires CompactLLMCommandGenerator. Edit level4/config.yml, "
                "then retrain."
            )
        else:
            print("❌ Check 5: FAILED - pipeline must include CompactLLMCommandGenerator (0 points)")
    except Exception as e:
        print(f"❌ Check 5: FAILED - could not parse config.yml: {e} (0 points)")
print("")

# Check 6: endpoints.yml model_groups (same criterion as Lab 0.1 Check 5)
print("Check 6: Verifying level4/endpoints.yml model_groups (openai-gpt-5-1 → model + temperature)...")
if not ENDPOINTS_PATH.exists():
    print("❌ Check 6: FAILED - level4/endpoints.yml not found (0 points)")
else:
    try:
        with open(ENDPOINTS_PATH, encoding="utf-8") as f:
            ep = yaml.safe_load(f)
        groups = (ep or {}).get("model_groups") or []
        found = None
        for g in groups:
            if isinstance(g, dict) and g.get("id") == "openai-gpt-5-1":
                models = g.get("models") or []
                if models and isinstance(models[0], dict):
                    found = models[0]
                break
        if found and found.get("model") == "openai-gpt-5-1" and found.get("temperature") == 0.1:
            print(
                f" Check 6: PASSED - openai-gpt-5-1 at temperature 0.1 ({POINTS_PER_CHECK} points)"
            )
            score += POINTS_PER_CHECK
        else:
            print(
                "❌ Check 6: FAILED - under id openai-gpt-5-1 use model openai-gpt-5-1, "
                "temperature 0.1 (0 points)"
            )
            print("Hint: Align level4/endpoints.yml with Unit 0.2 / Lab 0.1.")
    except Exception as e:
        print(f"❌ Check 6: FAILED - {e} (0 points)")
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 5.2 completion check passed! Score: {score}/{max_score}")
else:
    print(
        f"❌ FAIL: Score {score}/{max_score}. Fix Labs 0.1, 2.1, 3.1, 4.1, or 5.1 as needed; "
        "then re-run."
    )
print("==========================================")
print("")
print(
    "Summary: Check 1 (domain) | Check 2 (action) | Check 3 (flow) | Check 4 (model) | "
    "Check 5 (config) | Check 6 (endpoints)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
