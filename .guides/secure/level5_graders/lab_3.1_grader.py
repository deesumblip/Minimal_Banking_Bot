#!/usr/bin/env python3
"""
Lab 3.1: Registering Tools in endpoints.yml - Grader Script (Level 5 / Level 5)
Output format matches Level 2 Lab 6.2 template.

Checks level5/endpoints.yml for: tools: section and tools_module: "tools".
Runs from workspace root; expects /home/codio/workspace.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
ENDPOINTS_PATH = WORKSPACE_ROOT / "level5" / "endpoints.yml"

try:
    import yaml
except ImportError:
    print("FAIL")
    print("Hint: PyYAML is required. Use the project venv Python.")
    sys.exit(1)

score = 0
max_score = 10

print("Running Lab 3.1 Assessment Checks...")
print("")

# Check 1: File exists
print("Check 1: Verifying endpoints.yml exists...")
if not ENDPOINTS_PATH.exists():
    print("❌ Check 1: FAILED - level5/endpoints.yml not found (0 points)")
    print("Hint: Create or copy endpoints.yml in level5/ with a tools: section")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - endpoints.yml exists (2 points)")
score += 2
print("")

try:
    with open(ENDPOINTS_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
except Exception as e:
    print("❌ Check 2: FAILED - endpoints.yml has YAML syntax errors (0 points)")
    print(f"   {e}")
    print("FAIL")
    sys.exit(1)

if not isinstance(data, dict):
    print("❌ Check 2: FAILED - endpoints.yml must be a YAML mapping (0 points)")
    print("FAIL")
    sys.exit(1)

# Check 2: tools key (4 points)
print("Check 2: Verifying tools: section...")
tools_section = data.get("tools")
if not isinstance(tools_section, dict):
    print("❌ Check 2: FAILED - No top-level 'tools:' section (0 points)")
    print("Hint: Add a 'tools:' key at the top level of endpoints.yml")
    print("FAIL")
    sys.exit(1)
print(" Check 2: PASSED - tools section present (4 points)")
score += 4
print("")

# Check 3: tools_module: "tools" (4 points)
print("Check 3: Verifying tools_module...")
tm = tools_section.get("tools_module")
if tm != "tools":
    print("❌ Check 3: FAILED - tools_module must be 'tools' (0 points)")
    print("Hint: Under tools:, add tools_module: \"tools\"")
    print("FAIL")
    sys.exit(1)
print(" Check 3: PASSED - tools_module: \"tools\" (4 points)")
score += 4
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 3.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print("Summary: Check 1 (endpoints file) | Check 2 (tools section) | Check 3 (tools_module)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
