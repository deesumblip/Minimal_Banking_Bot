# Lab 2.1: Sub-Agent Config - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 2 (Sub-Agent Layout and Config), Level 6.

**Task.** Create `level6/sub_agents/banking_assistant/` and `config.yml` with agent name, protocol (RASA), description, LLM model_group, and connections.mcp_servers. Run the assessment when done.

**Codio guide (Chapter 1.6).** The Lab 2.1 page includes: `{Check It!|assessment}(code-output-compare-501060001)`. Assessment JSON: `.guides/assessments/code-output-compare-501060001.json`.

---

## Assessment Setup (For Implementers)

**COMMAND:** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level6_graders/lab_2.1_grader.py`  
**Working Directory:** `/home/codio/workspace`. **Expected output:** `PASS` (substring match).  
**Grader:** `.guides/secure/level6_graders/lab_2.1_grader.py`. **Points:** 10.

**Verifies:** level6/sub_agents/banking_assistant/config.yml exists; file contains agent name banking_assistant, protocol RASA, and mcp_servers (or connections.mcp_servers).
