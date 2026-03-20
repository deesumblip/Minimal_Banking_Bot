# Lab 2.1: Sub-Agent Config - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 2 (Sub-Agent Layout and Config), Level 6.

**Task.** Create `level6/sub_agents/banking_assistant/` and `config.yml` with agent name, protocol (RASA), description, LLM model_group, and connections.mcp_servers. Run the assessment when done.

**Codio guide (Chapter 1.6).** The Lab 2.1 page includes: `{Check It!|assessment}(code-output-compare-501060001)`. Assessment JSON: `.guides/assessments/code-output-compare-501060001.json`.

---

## Assessment Setup (For Implementers)

**COMMAND:** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level6_graders/lab_2.1_grader.py`  
**Working Directory:** `/home/codio/workspace`. **Codio sequence:** `code-output-compare-501060001.json` — `Check 1: PASSED` … `Check 4: PASSED`, substring match, **`showFeedback`: false**.  
**Grader:** `.guides/secure/level6_graders/lab_2.1_grader.py`. **Points:** 10. Full pass: **` PASS: Lab 2.1 verification complete! Score: 10/10`**.

**Verifies:** config exists; banking_assistant; protocol; mcp_servers.
