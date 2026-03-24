#!/usr/bin/env python3
"""
Lab 5.1: Training the Level 5 Agent - Grader Script
Output format matches Chapter 1.2 Lab 6.2 template.

Runs from workspace root; expects /home/codio/workspace.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
LEVEL5_DIR = WORKSPACE_ROOT / "level5"
VENV_DIR = WORKSPACE_ROOT / ".venv"
MODELS_DIR = LEVEL5_DIR / "models"

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

# Check 2: level5 exists and has required structure (3 points)
print("Check 2: Verifying level5 structure...")
required = [
    LEVEL5_DIR / "domain" / "basics.yml",
    LEVEL5_DIR / "config.yml",
    LEVEL5_DIR / "endpoints.yml",
    LEVEL5_DIR / "tools" / "banking_tools.py",
]
missing = [p for p in required if not p.exists()]
if not missing:
    print(" Check 2: PASSED - level5 has domain, config, endpoints, tools (3 points)")
    score += 3
else:
    print(f"❌ Check 2: FAILED - Missing: {[str(p.relative_to(WORKSPACE_ROOT)) for p in missing]} (0 points)")
print("")

# Check 3: Model file exists (5 points)
print("Check 3: Verifying trained model...")
if not MODELS_DIR.exists():
    print("❌ Check 3: FAILED - level5/models/ not found (0 points)")
    print("Hint: From project root: activate venv, cd level5, python -m rasa train")
else:
    model_files = list(MODELS_DIR.glob("*.tar.gz"))
    if not model_files:
        print("❌ Check 3: FAILED - No .tar.gz in level5/models/ (0 points)")
        print("Hint: Run 'cd level5' then 'python -m rasa train' with venv activated")
    else:
        print(" Check 3: PASSED - Model file exists (5 points)")
        score += 5
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 5.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print("Summary: Check 1 (venv) | Check 2 (level5 structure) | Check 3 (model)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
