#!/usr/bin/env python3
"""
Lab 0.1: Create Virtual Environment and Install Rasa Pro - Grader Script
Runs from workspace root. Checks: venv in root, Rasa Pro installed, project structure.
"""

import os
import sys
import subprocess
from pathlib import Path

# Workspace root (Codio: /home/codio/workspace; local: use cwd)
WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
VENV_DIR = WORKSPACE_ROOT / ".venv"
LEVEL1_DIR = WORKSPACE_ROOT / "level1"

score = 0
max_score = 6

# Resolve venv Python (bin on Unix, Scripts on Windows) - use absolute paths
if (VENV_DIR / "bin" / "python").exists():
    VENV_PYTHON = (VENV_DIR / "bin" / "python").resolve()
elif (VENV_DIR / "Scripts" / "python.exe").exists():
    VENV_PYTHON = (VENV_DIR / "Scripts" / "python.exe").resolve()
else:
    VENV_PYTHON = None

print("Running Lab 0.1 Assessment Checks...")
print("")

# Check 1: Virtual environment exists in workspace root (2 points)
print("Check 1: Verifying virtual environment in project root...")
if not VENV_DIR.is_dir():
    print("❌ Check 1: FAILED - Virtual environment (.venv) not found in project root (0 points)")
    print("Hint: From the project root (folder containing level1, level2, .guides), run 'python3.11 -m venv .venv' then 'source .venv/bin/activate'")
    print("FAIL")
    sys.exit(1)
if VENV_PYTHON is None or not VENV_PYTHON.exists():
    print("❌ Check 1: FAILED - Virtual environment incomplete (no python found) (0 points)")
    print("FAIL")
    sys.exit(1)
print("✅ Check 1: PASSED - Virtual environment found in project root (2 points)")
score += 2
print("")

# Check 2: Rasa Pro is installed (3 points)
print("Check 2: Verifying Rasa Pro installation...")
rasa_found = False
version_info = ""

# Method 1: Try running rasa --version via venv Python
try:
    result = subprocess.run(
        [str(VENV_PYTHON), "-m", "rasa", "--version"],
        capture_output=True,
        text=True,
        timeout=10,
        cwd=str(WORKSPACE_ROOT),
        env=dict(os.environ, PATH=str(VENV_DIR / "bin") + os.pathsep + os.environ.get("PATH", "")),
    )
    if result.returncode == 0:
        version_info = (result.stdout or result.stderr or "").strip().split("\n")[0]
        if "Rasa Pro" in version_info or "rasa" in version_info.lower():
            rasa_found = True
except Exception:
    pass

# Method 2: Try checking if rasa command exists in venv
if not rasa_found:
    rasa_cmd = VENV_DIR / "bin" / "rasa"
    if not rasa_cmd.exists():
        rasa_cmd = VENV_DIR / "Scripts" / "rasa.exe"
    if rasa_cmd.exists():
        try:
            result = subprocess.run(
                [str(rasa_cmd), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(WORKSPACE_ROOT),
            )
            if result.returncode == 0:
                version_info = (result.stdout or result.stderr or "").strip().split("\n")[0]
                if "Rasa Pro" in version_info or "rasa" in version_info.lower():
                    rasa_found = True
        except Exception:
            pass

# Method 3: Try importing rasa via venv Python
if not rasa_found:
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), "-c", "import rasa; print(rasa.__version__)"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(WORKSPACE_ROOT),
        )
        if result.returncode == 0:
            version_info = f"Rasa Pro {result.stdout.strip()}"
            rasa_found = True
    except Exception:
        pass

if rasa_found:
    print(f"✅ Check 2: PASSED - Rasa Pro installed successfully: {version_info} (3 points)")
    score += 3
else:
    print("❌ Check 2: FAILED - Rasa Pro not installed or not accessible (0 points)")
    print("Hint: With venv activated from project root, run 'pip install --no-cache-dir rasa-pro'")
    print("FAIL")
    sys.exit(1)
print("")

# Check 3: Project structure (optional, 1 point)
print("Check 3: Verifying project structure...")
domain_ok = (LEVEL1_DIR / "domain").is_dir()
data_ok = (LEVEL1_DIR / "data").is_dir()
if not domain_ok or not data_ok:
    print("⚠️  Check 3: WARNING - Project structure may be incomplete (0 points)")
    print("Hint: Ensure level1/domain/ and level1/data/ directories exist")
else:
    print("✅ Check 3: PASSED - Project structure verified (level1/domain/, level1/data/) (1 point)")
    score += 1
print("")

# Final summary
print("==========================================")
if score >= 5:
    print(f"✅ PASS: Lab 0.1 setup complete! Score: {score}/{max_score}")
    print("PASS")
    print("Successfully passed!")
    print("==========================================")
    print("")
    print("Summary: Check 1 (venv in root) | Check 2 (Rasa Pro) | Check 3 (project structure)")
    print(f"Score: {score}/{max_score}")
    sys.exit(0)
else:
    print(f"❌ FAIL: Lab 0.1 setup incomplete. Score: {score}/{max_score}")
    print("FAIL")
    print("Review the failed checks above and try again.")
    print("==========================================")
    print("")
    print("Summary: Check 1 (venv in root) | Check 2 (Rasa Pro) | Check 3 (project structure)")
    print(f"Score: {score}/{max_score}")
    sys.exit(1)
