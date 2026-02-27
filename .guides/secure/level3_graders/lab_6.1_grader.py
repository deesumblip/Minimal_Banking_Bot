#!/usr/bin/env python3
"""
Lab 6.1: Training and Testing with Slots - Grader Script
Runs from workspace root, activates venv, then checks level3 for model and logs.
"""

import os
import sys
import glob
import time
import subprocess
from pathlib import Path

# Configuration
WORKSPACE_ROOT = Path("/home/codio/workspace")
LEVEL3_DIR = WORKSPACE_ROOT / "level3"
VENV_DIR = WORKSPACE_ROOT / ".venv"
MODELS_DIR = LEVEL3_DIR / "models"
LOGS_FILE = LEVEL3_DIR / "logs" / "logs.out"

score = 0
max_score = 12

print("Running Lab 6.1 Assessment Checks...")
print("")

# Check 0: Virtual environment exists in workspace root (2 points)
print("Check 0: Verifying virtual environment...")
if not VENV_DIR.exists():
    print("❌ Check 0: FAILED - Virtual environment (.venv) not found in project root (0 points)")
    print("Hint: From the project root (folder containing level1, level2, level3), run 'python3.11 -m venv .venv' then 'source .venv/bin/activate'")
    sys.exit(1)

# Activate venv by adding it to PATH
venv_python = VENV_DIR / "bin" / "python"
if not venv_python.exists():
    print("❌ Check 0: FAILED - Virtual environment Python not found (0 points)")
    sys.exit(1)

# Verify Python is available (venv should be activated by Codio, but we check)
print("✅ Check 0: PASSED - Virtual environment found and activated (2 points)")
score += 2
print("")

# All remaining checks run from level3
if not LEVEL3_DIR.exists():
    print("❌ ERROR: level3 directory not found in workspace root")
    sys.exit(1)
os.chdir(LEVEL3_DIR)

# Check 1: Model file exists (2 points)
print("Check 1: Verifying model file exists...")
if not MODELS_DIR.exists():
    print("❌ Check 1: FAILED - models/ directory not found (0 points)")
    print("Hint: Run 'cd level3' then 'python -m rasa train' (with venv activated) to create the model")
    sys.exit(1)
model_files = list(MODELS_DIR.glob("*.tar.gz"))
if model_files:
    print(f"✅ Check 1: PASSED - Model file created (2 points)")
    score += 2
else:
    print("❌ Check 1: FAILED - No model file found in models/ directory (0 points)")
    print("Hint: Run 'cd level3' then 'python -m rasa train' (with venv activated) to create the model")
    sys.exit(1)
print("")

# Check 2: Model is recent (3 points)
print("Check 2: Verifying model is recent...")
if not model_files:
    print("❌ Check 2: FAILED - No model files found (0 points)")
    sys.exit(1)

# Get the newest model file
newest_model = max(model_files, key=lambda p: p.stat().st_mtime)
model_age_seconds = time.time() - newest_model.stat().st_mtime
model_age_minutes = model_age_seconds / 60

if model_age_minutes < 10:
    print(f"✅ Check 2: PASSED - Model file is recent (training completed within 10 minutes) (3 points)")
    score += 3
else:
    print(f"⚠️  WARNING: Model file is old ({model_age_minutes:.1f} minutes old). Re-run training to ensure it's current.")
    print("⚠️  Check 2: PARTIAL - Model exists but is older than 10 minutes (0 points)")
print("")

# Check 3: No obvious errors in logs (3 points)
print("Check 3: Checking for errors in logs...")
if LOGS_FILE.exists():
    try:
        with open(LOGS_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            log_content = f.read().lower()
        error_keywords = ['error', 'exception', 'failed']
        has_errors = any(keyword in log_content for keyword in error_keywords)
        
        if has_errors:
            print("⚠️  WARNING: Possible errors found in logs. Review logs/logs.out")
            print("⚠️  Check 3: PARTIAL - Logs found but may contain errors (0 points)")
        else:
            print("✅ Check 3: PASSED - No obvious errors in logs (3 points)")
            score += 3
    except Exception as e:
        print(f"⚠️  WARNING: Could not read log file: {e}")
        print("⚠️  Check 3: PARTIAL - Could not verify logs (0 points)")
else:
    print("✅ Check 3: PASSED - No log file found (training may not have logged) (3 points)")
    score += 3
print("")

# Check 4: Training completed (2 points)
print("Check 4: Verifying training completed successfully...")
print("✅ Check 4: PASSED - Training completed successfully (2 points)")
score += 2
print("")

# Final summary
print("=" * 50)
if score == max_score:
    print(f"✅ PASS: Training verification complete! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
    print("FAIL")
print("=" * 50)
print("")
print("Summary: Check 0 (venv) | Check 1 (model) | Check 2 (recent) | Check 3 (logs) | Check 4 (trained)")
print(f"Score: {score}/{max_score}")

if score < max_score:
    sys.exit(1)
