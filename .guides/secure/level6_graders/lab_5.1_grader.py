#!/usr/bin/env python3
"""
Lab 5.1: Training Level 6 - Grader
Output format matches Chapter 1.2 Lab 6.2 template.

Checks level6/models/ exists and contains at least one model file (.tar.gz).
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
MODELS_DIR = WORKSPACE_ROOT / "level6" / "models"

score = 0
max_score = 10

print("Running Lab 5.1 Assessment Checks...")
print("")

# Check 1: models directory (4 points)
print("Check 1: Verifying level6/models/ exists...")
if not MODELS_DIR.is_dir():
    print("❌ Check 1: FAILED - level6/models/ not found (run rasa train from level6) (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - models directory found (4 points)")
score += 4
print("")

# Check 2: .tar.gz model (6 points)
print("Check 2: Verifying trained model file...")
tar_files = list(MODELS_DIR.glob("*.tar.gz"))
if not tar_files:
    print("❌ Check 2: FAILED - level6/models/ has no .tar.gz model file (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 2: PASSED - model archive present (6 points)")
score += 6
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 5.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print("Summary: Check 1 (models directory) | Check 2 (.tar.gz model)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
