# Lab 5.2: Completion Check Level 6 - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 5 (Testing Sub-Agents), Level 6.

**Task.** Run the completion check: verify sub_agents config, mcp_servers in endpoints.yml, ask_banking_assistant flow, and optionally trained model. Run the assessment when ready.

**Codio guide (Chapter 1.6).** The Lab 5.2 page includes: `{Check It!|assessment}(code-output-compare-501060005)`.

---

## Assessment Setup (For Implementers)

**COMMAND:** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level6_graders/lab_5.2_grader.py`  
**Working Directory:** `/home/codio/workspace`. **Expected output:** `PASS`.  
**Grader:** `.guides/secure/level6_graders/lab_5.2_grader.py`. **Points:** 10.

**Verifies:** All Level 6 artifacts: level6/sub_agents/banking_assistant/config.yml; level6/endpoints.yml mcp_servers; level6/data/basics/ask_banking_assistant.yml with call: banking_assistant; optionally level6/models/.
