#!/usr/bin/env python3
"""
Lab 3.1: Registering MCP - Grader
Checks level6/endpoints.yml contains mcp_servers with at least one entry (name, url, type).
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
ENDPOINTS = WORKSPACE_ROOT / "level6" / "endpoints.yml"

print("Running Lab 3.1 Assessment Checks...")
print("")

if not ENDPOINTS.exists():
    print("FAIL: level6/endpoints.yml not found")
    sys.exit(1)

try:
    content = ENDPOINTS.read_text(encoding="utf-8")
except Exception as e:
    print(f"FAIL: Could not read endpoints.yml: {e}")
    sys.exit(1)

if "mcp_servers" not in content:
    print("FAIL: endpoints.yml should contain top-level mcp_servers")
    sys.exit(1)

# Basic check for at least one server entry (name, url, type)
if "name:" not in content or "url:" not in content or "type:" not in content:
    print("FAIL: mcp_servers should have at least one entry with name, url, type")
    sys.exit(1)

print("PASS")
sys.exit(0)
