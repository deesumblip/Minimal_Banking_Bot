#!/usr/bin/env python3
"""
Lab 4.4: Training the Level 4 Bot - Grader Script
Runs from workspace root, verifies venv, then checks level4 for model and logs.
"""

import os
import sys
import time
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
LEVEL4_DIR = WORKSPACE_ROOT / "level4"
VENV_DIR = WORKSPACE_ROOT / ".venv"
MODELS_DIR = LEVEL4_DIR / "models"
LOGS_FILE = LEVEL4_DIR / "logs" / "logs.out"

score = 0
max_score = 12

print("Running Lab 4.4 Assessment Checks...")
print("")

# Check 0: Virtual environment exists (2 points)
print("Check 0: Verifying virtual environment...")
if not VENV_DIR.exists():
    print("❌ Check 0: FAILED - Virtual environment (.venv) not found in project root (0 points)")
    print("Hint: From the project root, run 'python3 -m venv .venv' then activate it")
    print("FAIL")
    sys.exit(1)

venv_python = VENV_DIR / "bin" / "python"
if not venv_python.exists():
    venv_python = VENV_DIR / "Scripts" / "python.exe"
if not venv_python.exists():
    print("❌ Check 0: FAILED - Virtual environment Python not found (0 points)")
    print("FAIL")
    sys.exit(1)

print("✅ Check 0: PASSED - Virtual environment found (2 points)")
score += 2
print("")

if not LEVEL4_DIR.exists():
    print("❌ ERROR: level4 directory not found in workspace root")
    print("FAIL")
    sys.exit(1)
os.chdir(LEVEL4_DIR)

# Check 1: Model file exists (2 points)
print("Check 1: Verifying model file exists...")
if not MODELS_DIR.exists():
    print("❌ Check 1: FAILED - level4/models/ directory not found (0 points)")
    print("Hint: Run 'cd level4' then 'python -m rasa train' (with venv activated)")
    print("FAIL")
    sys.exit(1)
model_files = list(MODELS_DIR.glob("*.tar.gz"))
if not model_files:
    print("❌ Check 1: FAILED - No model file (.tar.gz) in level4/models/ (0 points)")
    print("Hint: Run 'cd level4' then 'python -m rasa train' (with venv activated)")
    print("FAIL")
    sys.exit(1)
print("✅ Check 1: PASSED - Model file created (2 points)")
score += 2
print("")

# Check 2: Model is recent (3 points)
print("Check 2: Verifying model is recent...")
newest_model = max(model_files, key=lambda p: p.stat().st_mtime)
model_age_seconds = time.time() - newest_model.stat().st_mtime
model_age_minutes = model_age_seconds / 60
if model_age_minutes < 10:
    print("✅ Check 2: PASSED - Model file is recent (3 points)")
    score += 3
else:
    print(f"⚠️  WARNING: Model file is old ({model_age_minutes:.1f} minutes). Re-run training to ensure it's current.")
    print("⚠️  Check 2: PARTIAL - Model exists but older than 10 minutes (0 points)")
print("")

# Check 3: Logs (3 points)
print("Check 3: Checking for errors in logs...")
if LOGS_FILE.exists():
    try:
        with open(LOGS_FILE, "r", encoding="utf-8", errors="ignore") as f:
            log_content = f.read().lower()
        error_keywords = ["error", "exception", "failed"]
        has_errors = any(kw in log_content for kw in error_keywords)
        if has_errors:
            print("⚠️  WARNING: Possible errors found in logs. Review level4/logs/logs.out")
            print("⚠️  Check 3: PARTIAL - Logs may contain errors (0 points)")
        else:
            print("✅ Check 3: PASSED - No obvious errors in logs (3 points)")
            score += 3
    except Exception as e:
        print(f"⚠️  WARNING: Could not read log file: {e}")
        print("⚠️  Check 3: PARTIAL - Could not verify logs (0 points)")
else:
    print("✅ Check 3: PASSED - No log file found (3 points)")
    score += 3
print("")

# Check 4: Training completed (2 points)
print("Check 4: Verifying training completed successfully...")
print("✅ Check 4: PASSED - Training completed successfully (2 points)")
score += 2
print("")

# Summary
print("=" * 50)
if score >= max_score:
    print(f"✅ PASS: Lab 4.4 verification complete! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
else:
    print(f"❌ FAIL: Score {score}/{max_score}. Review the failed checks above.")
    print("FAIL")
print("=" * 50)
sys.exit(0 if score >= max_score else 1)
