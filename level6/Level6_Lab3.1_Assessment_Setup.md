# Lab 3.1: Registering MCP - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 3 (MCP and ReAct Config), Level 6.

**Task.** Add `mcp_servers:` to `level6/endpoints.yml` with at least one entry (name, url, type). Run the assessment when done.

**Codio guide (Chapter 1.6).** The Lab 3.1 page includes: `{Check It!|assessment}(code-output-compare-501060002)`.

---

## Assessment Setup (For Implementers)

**COMMAND:** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level6_graders/lab_3.1_grader.py`  
**Working Directory:** `/home/codio/workspace`. **Expected output:** `PASS`.  
**Grader:** `.guides/secure/level6_graders/lab_3.1_grader.py`. **Points:** 10.

**Verifies:** level6/endpoints.yml contains top-level mcp_servers with at least one server (name, url, type).
