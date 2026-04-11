#!/usr/bin/env python3
"""
Lab 5.2: Testing / Completion Check - Grader Script (Level 5)
Output format matches Level 2 Lab 6.2 template (⚠️ for partial on model).

Verifies all Level 5 artifacts: tools/, endpoints.yml tools, Lab 2.0 prompt,
transfer_money_tools.yml, action_process_transfer_with_tools, domain, and model.
Runs from workspace root.
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML required. Use project venv Python.")
    sys.exit(1)

WORKSPACE_ROOT = Path("/home/codio/workspace")
LEVEL5 = WORKSPACE_ROOT / "level5"
TOOLS_DIR = LEVEL5 / "tools"
BANKING_TOOLS = TOOLS_DIR / "banking_tools.py"
ENDPOINTS_PATH = LEVEL5 / "endpoints.yml"
FLOW_PATH = LEVEL5 / "data" / "basics" / "transfer_money_tools.yml"
ACTION_PATH = LEVEL5 / "actions" / "action_process_transfer_with_tools.py"
DOMAIN_PATH = LEVEL5 / "domain" / "basics.yml"
MODELS_DIR = LEVEL5 / "models"

PROMPT_REL = "data/prompts/command_prompt_v3_slot_names.jinja2"


def verify_lab_2_0_command_prompt(level5_dir: Path) -> tuple[bool, str]:
    """Lab 2.0: prompt file exists and config wires prompt_template to it."""
    prompt_file = level5_dir / "data" / "prompts" / "command_prompt_v3_slot_names.jinja2"
    if not prompt_file.is_file():
        return False, f"Missing level5/{PROMPT_REL} (Lab 2.0)"
    cfg_path = level5_dir / "config.yml"
    if not cfg_path.is_file():
        return False, "level5/config.yml not found"
    try:
        with open(cfg_path, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
    except Exception as e:
        return False, f"Could not parse config.yml: {e}"
    pipeline = cfg.get("pipeline") or []
    for step in pipeline:
        if not isinstance(step, dict):
            continue
        if step.get("name") != "SearchReadyLLMCommandGenerator":
            continue
        pt = step.get("prompt_template")
        if not pt:
            return False, "Add prompt_template under SearchReadyLLMCommandGenerator (Lab 2.0)"
        norm = str(pt).replace("\\", "/")
        if PROMPT_REL in norm:
            return True, ""
        return False, f'prompt_template must reference {PROMPT_REL!r} (got {pt!r})'
    return False, "SearchReadyLLMCommandGenerator not found in pipeline (config.yml)"


score = 0
max_score = 10

print("Running Lab 5.2 Completion Check...")
print("")

# Check 1: tools/ and banking_tools.py (2 points)
print("Check 1: Verifying tools folder and banking_tools.py...")
if TOOLS_DIR.is_dir() and BANKING_TOOLS.exists():
    content = BANKING_TOOLS.read_text(encoding="utf-8")
    if "__all__" in content and "check_balance" in content and "process_transfer" in content:
        print(" Check 1: PASSED - tools/ and banking_tools.py with __all__ (2 points)")
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
            print(" Check 2: PASSED - endpoints.yml has tools_module (2 points)")
            score += 2
        else:
            print("❌ Check 2: FAILED - tools: tools_module: \"tools\" required (0 points)")
    except Exception as e:
        print(f"❌ Check 2: FAILED - {e} (0 points)")
else:
    print("❌ Check 2: FAILED - level5/endpoints.yml not found (0 points)")
print("")

# Check 3: Lab 2.0 — command-generator prompt (2 points)
print("Check 3: Verifying Lab 2.0 command-generator prompt...")
ok, hint = verify_lab_2_0_command_prompt(LEVEL5)
if ok:
    print(f" Check 3: PASSED - {PROMPT_REL} and prompt_template in config.yml (2 points)")
    score += 2
else:
    print(f"❌ Check 3: FAILED - {hint} (0 points)")
print("")

# Check 4: transfer_money_tools.yml and action (2 points)
print("Check 4: Verifying flow and action file...")
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
    print(" Check 4: PASSED - transfer_money_tools.yml and action file (2 points)")
    score += 2
else:
    print("❌ Check 4: FAILED - Flow and action_process_transfer_with_tools.py required (0 points)")
print("")

# Check 5: Domain and model (2 points; 1 partial)
print("Check 5: Verifying domain and model...")
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
    print(" Check 5: PASSED - domain has action and model exists (2 points)")
    score += 2
elif domain_ok:
    print("⚠️  Check 5: PARTIAL - domain OK; run 'cd level5' and 'python -m rasa train' (1 point)")
    score += 1
else:
    print("❌ Check 5: FAILED - domain must list action_process_transfer_with_tools; train from level5 (0 points)")
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 5.2 completion check passed! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Complete Labs 2.0–5.1 and re-run training if needed.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (tools) | Check 2 (endpoints) | Check 3 (Lab 2.0 prompt) | "
    "Check 4 (flow+action) | Check 5 (domain+model)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
