#!/usr/bin/env python3
"""
Lab 2.0: Command-generator prompt - Grader Script (Level 5 / Level 5)
Output format matches Level 2 Lab 6.2 template.

Checks level5/data/prompts/command_prompt_v3_slot_names.jinja2 and
prompt_template on SearchReadyLLMCommandGenerator in config.yml.
Runs from workspace root; expects /home/codio/workspace.
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
PROMPT_REL = "data/prompts/command_prompt_v3_slot_names.jinja2"
PROMPT_FILE = LEVEL5_DIR / "data" / "prompts" / "command_prompt_v3_slot_names.jinja2"
CFG_PATH = LEVEL5_DIR / "config.yml"

score = 0
max_score = 10

print("Running Lab 2.0 Assessment Checks...")
print("")

# Check 1: Prompt file exists (5 points)
print("Check 1: Verifying command-generator prompt file...")
if not PROMPT_FILE.is_file():
    print(f"❌ Check 1: FAILED - Missing level5/{PROMPT_REL} (0 points)")
    print("Hint: Copy command_prompt_v3_slot_names.jinja2 from level5/resources/ to level5/data/prompts/")
    print("")
else:
    print(f" Check 1: PASSED - {PROMPT_REL} exists (5 points)")
    score += 5
    print("")

# Check 2: config.yml wires prompt_template (5 points)
print("Check 2: Verifying prompt_template in config.yml...")
if not CFG_PATH.is_file():
    print("❌ Check 2: FAILED - level5/config.yml not found (0 points)")
    print("")
else:
    try:
        with open(CFG_PATH, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Check 2: FAILED - Could not parse config.yml: {e} (0 points)")
        print("")
        cfg = None
    if cfg is not None:
        pipeline = cfg.get("pipeline") or []
        found = False
        for step in pipeline:
            if not isinstance(step, dict):
                continue
            if step.get("name") != "SearchReadyLLMCommandGenerator":
                continue
            found = True
            pt = step.get("prompt_template")
            if not pt:
                print("❌ Check 2: FAILED - Add prompt_template under SearchReadyLLMCommandGenerator (0 points)")
                print("Hint: prompt_template: data/prompts/command_prompt_v3_slot_names.jinja2")
            else:
                norm = str(pt).replace("\\", "/")
                if PROMPT_REL in norm:
                    print(" Check 2: PASSED - prompt_template references data/prompts/... (5 points)")
                    score += 5
                else:
                    print(
                        f"❌ Check 2: FAILED - prompt_template must reference {PROMPT_REL!r} (got {pt!r}) (0 points)"
                    )
            break
        if not found:
            print("❌ Check 2: FAILED - SearchReadyLLMCommandGenerator not found in pipeline (0 points)")
        print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 2.0 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print("Summary: Check 1 (prompt file) | Check 2 (prompt_template in config.yml)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
