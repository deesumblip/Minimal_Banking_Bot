#!/usr/bin/env python3
"""
Lab 5.1: Training Level 6 - Grader
Checks level6/models/ exists and contains at least one model file (.tar.gz).
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
MODELS_DIR = WORKSPACE_ROOT / "level6" / "models"

print("Running Lab 5.1 Assessment Checks...")
print("")

if not MODELS_DIR.is_dir():
    print("FAIL: level6/models/ not found (run rasa train from level6)")
    sys.exit(1)

tar_files = list(MODELS_DIR.glob("*.tar.gz"))
if not tar_files:
    print("FAIL: level6/models/ has no .tar.gz model file")
    sys.exit(1)

print("PASS")
sys.exit(0)
