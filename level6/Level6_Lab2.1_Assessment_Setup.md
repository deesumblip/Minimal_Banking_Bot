# Lab 2.1: Sub-Agent Config - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 2 (Sub-Agent Layout and Config), Level 6.

**Sequence (Chapter 1.5–style).**

1. **Fill in the blanks** — `fill-in-the-blanks-501060111` (`.guides/assessments/fill-in-the-blanks-501060111.json`). Produces complete **`config.yml`** YAML.
2. **Copy** the passed YAML to **`level6/sub_agents/banking_assistant/config.yml`**.
3. **Code Test** — `{Check It!|assessment}(code-output-compare-501060001)`.

**Codio guide (Chapter 1.6).** Lab 2.1 page lists both assessments in order.

---

## Assessment Setup (For Implementers)

**Fill-in:** `fill-in-the-blanks-501060111.json` — points 5; guidance in JSON `source.guidance`.

**Code Test — COMMAND:** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level6_graders/lab_2.1_grader.py`  
**Working Directory:** `/home/codio/workspace`. **Codio sequence:** `code-output-compare-501060001.json`.  
**Grader:** `.guides/secure/level6_graders/lab_2.1_grader.py`. **Points:** 10.

**Verifies:** config exists; `banking_assistant`; protocol; `mcp_servers`; `BankingAssistantLiteAgent` in `configuration.module`.
