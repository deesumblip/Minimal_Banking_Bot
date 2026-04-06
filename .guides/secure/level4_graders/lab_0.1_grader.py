#!/usr/bin/env python3
"""
Lab 0.1: Pipeline config and endpoints — grader script
Output format matches Chapter 1.2 Lab 6.2 / Lab 2.1 template.

Runs from workspace root; checks level4/config.yml and level4/endpoints.yml.

Uses only stdlib (no PyYAML) so it runs on Codio even when the assessment uses
plain python3 — same idea as Level 1 Lab 2.2 (lab_2.2_grader.py).
Workspace resolution matches Level 4 Lab 2.1 (path from script + CODIO_WORKSPACE).
"""

import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Same pattern as level4 lab_2.1_grader.py
_env = os.environ.get("CODIO_WORKSPACE", "").strip()
WORKSPACE_ROOT = Path(_env).expanduser() if _env else Path(__file__).resolve().parent.parent.parent.parent
if not WORKSPACE_ROOT.is_dir():
    WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent.parent

LEVEL4 = WORKSPACE_ROOT / "level4"
CONFIG_PATH = LEVEL4 / "config.yml"
ENDPOINTS_PATH = LEVEL4 / "endpoints.yml"

score = 0
max_score = 10


def _read_text(path: Path) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


print("Running Lab 0.1 pipeline checks...")
print("")

# Check 1: config.yml exists and assistant_id (2 points)
print("Check 1: Verifying level4/config.yml exists and assistant_id...")
if not CONFIG_PATH.exists():
    print("❌ Check 1: FAILED - level4/config.yml not found (0 points)")
    print("Hint: Paste your completed config from Lab 0.1 into level4/config.yml")
    print("FAIL")
    sys.exit(1)
try:
    cfg_text = _read_text(CONFIG_PATH)
except Exception as e:
    print(f"❌ Check 1: FAILED - could not read config.yml: {e} (0 points)")
    print("FAIL")
    sys.exit(1)

if not re.search(r"^\s*assistant_id:\s*[\"']?level4-agent[\"']?\s*$", cfg_text, re.MULTILINE):
    print(f"❌ Check 1: FAILED - assistant_id should be level4-agent (0 points)")
else:
    print(" Check 1: PASSED - config.yml present; assistant_id is level4-agent (2 points)")
    score += 2
print("")

# Check 2: CompactLLMCommandGenerator, not SearchReady (2 points)
print("Check 2: Verifying command generator in pipeline...")
if "SearchReadyLLMCommandGenerator" in cfg_text:
    print("❌ Check 2: FAILED - pipeline must include CompactLLMCommandGenerator only (0 points)")
elif re.search(r"name:\s*CompactLLMCommandGenerator\b", cfg_text):
    print(" Check 2: PASSED - pipeline uses CompactLLMCommandGenerator (not SearchReady) (2 points)")
    score += 2
else:
    print("❌ Check 2: FAILED - pipeline must include CompactLLMCommandGenerator only (0 points)")
print("")

# Check 3: flow_retrieval and minimize_num_calls (2 points)
print("Check 3: Verifying flow_retrieval and minimize_num_calls...")
ok3 = (
    re.search(r"^\s*minimize_num_calls:\s*false\s*$", cfg_text, re.MULTILINE)
    and re.search(r"^\s*turns_to_embed:\s*5\s*$", cfg_text, re.MULTILINE)
    and re.search(r"^\s*num_flows:\s*20\s*$", cfg_text, re.MULTILINE)
)
if ok3:
    print(" Check 3: PASSED - minimize_num_calls false; flow_retrieval 5 / 20 (2 points)")
    score += 2
else:
    print("❌ Check 3: FAILED - expected minimize_num_calls: false, turns_to_embed: 5, num_flows: 20 (0 points)")
print("")

# Check 4: endpoints.yml structure and NLG (2 points)
print("Check 4: Verifying level4/endpoints.yml (action_endpoint, nlg)...")
if not ENDPOINTS_PATH.exists():
    print("❌ Check 4: FAILED - level4/endpoints.yml not found (0 points)")
else:
    try:
        ep_text = _read_text(ENDPOINTS_PATH)
        if (
            re.search(r"^\s*actions_module:\s*[\"']?actions[\"']?\s*$", ep_text, re.MULTILINE)
            and re.search(r"^\s*type:\s*[\"']?rephrase[\"']?\s*$", ep_text, re.MULTILINE)
            and re.search(r"^\s*model_group:\s*[\"']?openai-gpt-5-1[\"']?\s*$", ep_text, re.MULTILINE)
        ):
            print(" Check 4: PASSED - action_endpoint, nlg rephrase, model_group (2 points)")
            score += 2
        else:
            print("❌ Check 4: FAILED - check action_endpoint, nlg.type, llm.model_group (0 points)")
    except Exception as e:
        print(f"❌ Check 4: FAILED - {e} (0 points)")
print("")

# Check 5: model_groups model + temperature (2 points)
print("Check 5: Verifying model_groups (openai-gpt-5-1 + temperature)...")
if not ENDPOINTS_PATH.exists():
    print("❌ Check 5: FAILED - level4/endpoints.yml not found (0 points)")
else:
    try:
        ep_text = _read_text(ENDPOINTS_PATH)
        if (
            re.search(r"^\s*-\s*id:\s*[\"']?openai-gpt-5-1[\"']?\s*$", ep_text, re.MULTILINE)
            and re.search(r"^\s*model:\s*[\"']?openai-gpt-5-1[\"']?\s*$", ep_text, re.MULTILINE)
            and re.search(r"^\s*temperature:\s*[\"']?0\.1[\"']?\s*$", ep_text, re.MULTILINE)
        ):
            print(" Check 5: PASSED - openai-gpt-5-1 at temperature 0.1 (2 points)")
            score += 2
        else:
            print("❌ Check 5: FAILED - under id openai-gpt-5-1 use model openai-gpt-5-1, temperature 0.1 (0 points)")
    except Exception as e:
        print(f"❌ Check 5: FAILED - {e} (0 points)")
print("")

print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 0.1 pipeline verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Fix blanks, paste into level4/, re-run.")
print("==========================================")
print("")
print("Summary: Check 1 (assistant_id) | Check 2 (Compact) | Check 3 (flow_retrieval) | Check 4 (nlg) | Check 5 (model_groups)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
