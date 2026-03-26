#!/usr/bin/env python3
"""
Lab 0.1: Pipeline config and endpoints — grader script
Output format matches Chapter 1.2 Lab 6.2 / Lab 2.1 template.

Runs from workspace root; checks level4/config.yml and level4/endpoints.yml.
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
LEVEL4 = WORKSPACE_ROOT / "level4"
CONFIG_PATH = LEVEL4 / "config.yml"
ENDPOINTS_PATH = LEVEL4 / "endpoints.yml"

score = 0
max_score = 10

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
    with open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    aid = (cfg or {}).get("assistant_id")
    if aid == "level4-agent":
        print(" Check 1: PASSED - config.yml present; assistant_id is level4-agent (2 points)")
        score += 2
    else:
        print(f"❌ Check 1: FAILED - assistant_id should be level4-agent, got {aid!r} (0 points)")
except Exception as e:
    print(f"❌ Check 1: FAILED - could not parse config.yml: {e} (0 points)")
print("")

# Check 2: CompactLLMCommandGenerator, not SearchReady (2 points)
print("Check 2: Verifying command generator in pipeline...")
try:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    pipeline = (cfg or {}).get("pipeline") or []
    names = [s.get("name") for s in pipeline if isinstance(s, dict)]
    has_compact = "CompactLLMCommandGenerator" in names
    has_search = "SearchReadyLLMCommandGenerator" in names
    if has_compact and not has_search:
        print(" Check 2: PASSED - pipeline uses CompactLLMCommandGenerator (not SearchReady) (2 points)")
        score += 2
    else:
        print("❌ Check 2: FAILED - pipeline must include CompactLLMCommandGenerator only (0 points)")
except Exception as e:
    print(f"❌ Check 2: FAILED - {e} (0 points)")
print("")

# Check 3: flow_retrieval and minimize_num_calls (2 points)
print("Check 3: Verifying flow_retrieval and minimize_num_calls...")
try:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    pipeline = (cfg or {}).get("pipeline") or []
    ok = False
    for step in pipeline:
        if not isinstance(step, dict):
            continue
        if step.get("name") != "CompactLLMCommandGenerator":
            continue
        fr = step.get("flow_retrieval") or {}
        if step.get("minimize_num_calls") is False and fr.get("turns_to_embed") == 5 and fr.get("num_flows") == 20:
            ok = True
        break
    if ok:
        print(" Check 3: PASSED - minimize_num_calls false; flow_retrieval 5 / 20 (2 points)")
        score += 2
    else:
        print("❌ Check 3: FAILED - expected minimize_num_calls: false, turns_to_embed: 5, num_flows: 20 (0 points)")
except Exception as e:
    print(f"❌ Check 3: FAILED - {e} (0 points)")
print("")

# Check 4: endpoints.yml structure and NLG (2 points)
print("Check 4: Verifying level4/endpoints.yml (action_endpoint, nlg)...")
if not ENDPOINTS_PATH.exists():
    print("❌ Check 4: FAILED - level4/endpoints.yml not found (0 points)")
else:
    try:
        with open(ENDPOINTS_PATH, encoding="utf-8") as f:
            ep = yaml.safe_load(f)
        ae = (ep or {}).get("action_endpoint") or {}
        nlg = (ep or {}).get("nlg") or {}
        llm = nlg.get("llm") or {}
        if (
            ae.get("actions_module") == "actions"
            and nlg.get("type") == "rephrase"
            and llm.get("model_group") == "gpt-4o-mini"
        ):
            print(" Check 4: PASSED - action_endpoint, nlg rephrase, model_group (2 points)")
            score += 2
        else:
            print("❌ Check 4: FAILED - check action_endpoint, nlg.type, llm.model_group (0 points)")
    except Exception as e:
        print(f"❌ Check 4: FAILED - {e} (0 points)")
print("")

# Check 5: model_groups model + temperature (2 points)
print("Check 5: Verifying model_groups (gpt-4o + temperature)...")
if not ENDPOINTS_PATH.exists():
    print("❌ Check 5: FAILED - level4/endpoints.yml not found (0 points)")
else:
    try:
        with open(ENDPOINTS_PATH, encoding="utf-8") as f:
            ep = yaml.safe_load(f)
        groups = (ep or {}).get("model_groups") or []
        found = None
        for g in groups:
            if isinstance(g, dict) and g.get("id") == "gpt-4o-mini":
                models = g.get("models") or []
                if models and isinstance(models[0], dict):
                    found = models[0]
                break
        if found and found.get("model") == "gpt-4o-2024-11-20" and found.get("temperature") == 0.1:
            print(" Check 5: PASSED - gpt-4o-2024-11-20 at temperature 0.1 (2 points)")
            score += 2
        else:
            print("❌ Check 5: FAILED - under id gpt-4o-mini use model gpt-4o-2024-11-20, temperature 0.1 (0 points)")
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
