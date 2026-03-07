# Lab 4.1: ask_banking_assistant Flow - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 4 (Flow that Calls Sub-Agent), Level 6.

**Task.** Create `level6/data/basics/ask_banking_assistant.yml` with a flow that has a step `call: banking_assistant` (and optionally a follow-up action). Run the assessment when done.

**Codio guide (Chapter 1.6).** The Lab 4.1 page includes: `{Check It!|assessment}(code-output-compare-501060003)`.

---

## Assessment Setup (For Implementers)

**COMMAND:** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level6_graders/lab_4.1_grader.py`  
**Working Directory:** `/home/codio/workspace`. **Expected output:** `PASS`.  
**Grader:** `.guides/secure/level6_graders/lab_4.1_grader.py`. **Points:** 10.

**Verifies:** level6/data/basics/ask_banking_assistant.yml exists; flow contains step call: banking_assistant.
