#!/usr/bin/env python3
"""
Lab 3.1: Registering MCP - Grader (Level 6)
Output format matches Chapter 1.2 Lab 6.2 template.

Checks level6/endpoints.yml contains mcp_servers with at least one entry (name, url, type).
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
ENDPOINTS = WORKSPACE_ROOT / "level6" / "endpoints.yml"

score = 0
max_score = 10

print("Running Lab 3.1 Assessment Checks...")
print("")

# Check 1: file exists (2 points)
print("Check 1: Verifying level6/endpoints.yml exists...")
if not ENDPOINTS.exists():
    print("❌ Check 1: FAILED - level6/endpoints.yml not found (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - endpoints.yml found (2 points)")
score += 2
print("")

try:
    content = ENDPOINTS.read_text(encoding="utf-8")
except Exception as e:
    print(f"❌ Check 2: FAILED - Could not read endpoints.yml: {e} (0 points)")
    print("FAIL")
    sys.exit(1)

# Check 2: mcp_servers (4 points)
print("Check 2: Verifying top-level mcp_servers...")
if "mcp_servers" not in content:
    print("❌ Check 2: FAILED - endpoints.yml should contain top-level mcp_servers (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 2: PASSED - mcp_servers present (4 points)")
score += 4
print("")

# Check 3: name, url, type (4 points)
print("Check 3: Verifying server entry fields (name, url, type)...")
if "name:" not in content or "url:" not in content or "type:" not in content:
    print("❌ Check 3: FAILED - mcp_servers should have at least one entry with name, url, type (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 3: PASSED - name, url, and type present (4 points)")
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
print("Summary: Check 1 (endpoints file) | Check 2 (mcp_servers) | Check 3 (name, url, type)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
