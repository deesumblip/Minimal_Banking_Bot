#!/usr/bin/env python3
"""
Lab 5.1: Training the Level 5 Agent - Grader Script
Output format matches Chapter 1.2 Lab 6.2 template.

Runs from workspace root; expects /home/codio/workspace.

Checks include Lab 2.0: data/prompts/command_prompt_v3_slot_names.jinja2 and
prompt_template on SearchReadyLLMCommandGenerator in config.yml.
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML is required. Use the project venv Python.")
    sys.exit(1)

WORKSPACE_ROOT = Path("/home/codio/workspace")
LEVEL5_DIR = WORKSPACE_ROOT / "level5"
VENV_DIR = WORKSPACE_ROOT / ".venv"
MODELS_DIR = LEVEL5_DIR / "models"

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

print("Running Lab 5.1 Assessment Checks...")
print("")

# Check 1: Virtual environment exists (2 points)
print("Check 1: Verifying virtual environment...")
if not VENV_DIR.exists():
    print("❌ Check 1: FAILED - .venv not found in project root (0 points)")
    print("FAIL")
    sys.exit(1)
venv_python = VENV_DIR / "bin" / "python"
if not venv_python.exists():
    venv_python = VENV_DIR / "Scripts" / "python.exe"
if not venv_python.exists():
    print("❌ Check 1: FAILED - venv Python not found (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - Virtual environment found (2 points)")
score += 2
print("")

# Check 2: level5 exists and has required structure (2 points)
print("Check 2: Verifying level5 structure...")
required = [
    LEVEL5_DIR / "domain" / "basics.yml",
    LEVEL5_DIR / "config.yml",
    LEVEL5_DIR / "endpoints.yml",
    LEVEL5_DIR / "tools" / "banking_tools.py",
]
missing = [p for p in required if not p.exists()]
if not missing:
    print(" Check 2: PASSED - level5 has domain, config, endpoints, tools (2 points)")
    score += 2
else:
    print(f"❌ Check 2: FAILED - Missing: {[str(p.relative_to(WORKSPACE_ROOT)) for p in missing]} (0 points)")
print("")

# Check 3: Lab 2.0 — command-generator prompt file + prompt_template (2 points)
print("Check 3: Verifying Lab 2.0 command-generator prompt...")
ok, hint = verify_lab_2_0_command_prompt(LEVEL5_DIR)
if ok:
    print(f" Check 3: PASSED - {PROMPT_REL} and prompt_template in config.yml (2 points)")
    score += 2
else:
    print(f"❌ Check 3: FAILED - {hint} (0 points)")
print("")

# Check 4: Model file exists (4 points)
print("Check 4: Verifying trained model...")
if not MODELS_DIR.exists():
    print("❌ Check 4: FAILED - level5/models/ not found (0 points)")
    print("Hint: From project root: activate venv, cd level5, python -m rasa train")
else:
    model_files = list(MODELS_DIR.glob("*.tar.gz"))
    if not model_files:
        print("❌ Check 4: FAILED - No .tar.gz in level5/models/ (0 points)")
        print("Hint: Run 'cd level5' then 'python -m rasa train' with venv activated")
    else:
        print(" Check 4: PASSED - Model file exists (4 points)")
        score += 4
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 5.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print("Summary: Check 1 (venv) | Check 2 (level5 structure) | Check 3 (Lab 2.0 prompt) | Check 4 (model)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
