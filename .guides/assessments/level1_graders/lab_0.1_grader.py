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

# Print initial status (some systems check first line)
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

# Verify venv Python is executable before proceeding
try:
    test_result = subprocess.run(
        [str(VENV_PYTHON), "--version"],
        capture_output=True,
        text=True,
        timeout=5,
        cwd=str(WORKSPACE_ROOT),
    )
    if test_result.returncode != 0:
        print("⚠️  Warning: Venv Python may not be executable")
except Exception as e:
    print(f"⚠️  Warning: Could not verify venv Python: {e}")

# Check 2: Rasa Pro is installed (3 points)
print("Check 2: Verifying Rasa Pro installation...")
rasa_found = False
version_info = ""

# Prepare environment with venv in PATH
venv_bin = str(VENV_DIR / "bin")
venv_scripts = str(VENV_DIR / "Scripts")
env = os.environ.copy()
env["PATH"] = os.pathsep.join([venv_bin, venv_scripts, env.get("PATH", "")])

# Method 0: Direct filesystem check - look for rasa package in site-packages
if not rasa_found:
    # Try common site-packages locations
    site_packages_locations = [
        VENV_DIR / "lib" / "python3.11" / "site-packages",
        VENV_DIR / "lib" / "python3.10" / "site-packages",
        VENV_DIR / "lib" / "python3.9" / "site-packages",
        VENV_DIR / "lib" / "site-packages",
    ]
    for site_pkg in site_packages_locations:
        rasa_pkg = site_pkg / "rasa"
        if rasa_pkg.exists() and rasa_pkg.is_dir():
            init_file = rasa_pkg / "__init__.py"
            if init_file.exists():
                # Try to read version from __init__.py or check for version file
                try:
                    with open(init_file, 'r') as f:
                        content = f.read(500)  # Read first 500 chars
                        if "__version__" in content:
                            version_info = "Rasa Pro (package found)"
                        else:
                            version_info = "Rasa Pro (installed)"
                    rasa_found = True
                    break
                except Exception:
                    version_info = "Rasa Pro (package found)"
                    rasa_found = True
                    break

# Method 1: Check if rasa-pro is installed via pip list
if not rasa_found:
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), "-m", "pip", "list"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(WORKSPACE_ROOT),
            env=env,
        )
        if result.returncode == 0:
            output = result.stdout.lower()
            if "rasa-pro" in output or "rasa pro" in output:
                # Extract version from pip list output
                for line in result.stdout.split("\n"):
                    if "rasa-pro" in line.lower() or "rasa pro" in line.lower():
                        parts = line.split()
                        if len(parts) >= 2:
                            version_info = f"Rasa Pro {parts[1]}"
                            rasa_found = True
                            break
    except Exception:
        pass

# Method 1b: Try using bash to activate venv and run rasa --version
if not rasa_found:
    try:
        activate_script = VENV_DIR / "bin" / "activate"
        if not activate_script.exists():
            activate_script = VENV_DIR / "Scripts" / "activate.bat"
        if activate_script.exists():
            # Use bash to source activate and run rasa --version
            bash_cmd = f"source {activate_script} && rasa --version"
            result = subprocess.run(
                ["bash", "-c", bash_cmd],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(WORKSPACE_ROOT),
                env=env,
            )
            if result.returncode == 0:
                output = result.stdout or result.stderr or ""
                version_info = output.strip().split("\n")[0]
                if "rasa pro" in output.lower() or "rasa" in output.lower():
                    rasa_found = True
    except Exception:
        pass

# Method 2: Try running rasa --version via venv Python
if not rasa_found:
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), "-m", "rasa", "--version"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(WORKSPACE_ROOT),
            env=env,
        )
        if result.returncode == 0:
            output = result.stdout or result.stderr or ""
            version_info = output.strip().split("\n")[0]
            if "rasa pro" in output.lower() or "rasa" in output.lower():
                rasa_found = True
    except Exception:
        pass

# Method 3: Try checking if rasa command exists in venv
if not rasa_found:
    rasa_cmd = VENV_DIR / "bin" / "rasa"
    if not rasa_cmd.exists():
        rasa_cmd = VENV_DIR / "Scripts" / "rasa.exe"
    if rasa_cmd.exists() and rasa_cmd.is_file():
        try:
            result = subprocess.run(
                [str(rasa_cmd), "--version"],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(WORKSPACE_ROOT),
                env=env,
            )
            if result.returncode == 0:
                output = result.stdout or result.stderr or ""
                version_info = output.strip().split("\n")[0]
                if "rasa pro" in output.lower() or "rasa" in output.lower():
                    rasa_found = True
        except Exception:
            pass

# Method 4: Try importing rasa via venv Python
if not rasa_found:
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), "-c", "import rasa; print(rasa.__version__)"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(WORKSPACE_ROOT),
            env=env,
        )
        if result.returncode == 0:
            version_info = f"Rasa Pro {result.stdout.strip()}"
            rasa_found = True
    except Exception:
        pass

# Method 5: Check if rasa package directory exists in site-packages
if not rasa_found:
    try:
        # Get site-packages location
        result = subprocess.run(
            [str(VENV_PYTHON), "-c", "import site; print(site.getsitepackages()[0])"],
            capture_output=True,
            text=True,
            timeout=5,
            cwd=str(WORKSPACE_ROOT),
            env=env,
        )
        if result.returncode == 0:
            site_packages = Path(result.stdout.strip())
            rasa_pkg = site_packages / "rasa"
            if rasa_pkg.exists() and rasa_pkg.is_dir():
                # Check for version file or __init__.py
                init_file = rasa_pkg / "__init__.py"
                if init_file.exists():
                    version_info = "Rasa Pro (package found)"
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
    print("Summary: Check 1 (venv in root) | Check 2 (Rasa Pro) | Check 3 (project structure)")
    print(f"Score: {score}/{max_score}")
    print("Successfully passed!")
    print("==========================================")
    sys.stdout.flush()
    # Print PASS as the very last line (some systems check last line)
    print("PASS")
    sys.stdout.flush()
    sys.exit(0)
else:
    print(f"❌ FAIL: Lab 0.1 setup incomplete. Score: {score}/{max_score}")
    print("Summary: Check 1 (venv in root) | Check 2 (Rasa Pro) | Check 3 (project structure)")
    print(f"Score: {score}/{max_score}")
    print("Review the failed checks above and try again.")
    print("==========================================")
    sys.stdout.flush()
    # Print FAIL as the very last line (some systems check last line)
    print("FAIL")
    sys.stdout.flush()
    sys.exit(1)
