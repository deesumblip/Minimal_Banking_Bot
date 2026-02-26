# Lab 4.1: Adding Multiple Slots in the Domain - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 3: Adding Slots and Responses for Transfer (Level 4).

**Task.** In `domain/basics.yml` in the `level4` folder, add the slots `amount`, `recipient`, and `account_from` (each type text), the responses `utter_ask_amount`, `utter_ask_recipient`, and `utter_ask_account_from`, and register `action_process_transfer` in the `actions:` list. You will create the action file in Lab 4.2. Run the assessment when done.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has added the slots `amount`, `recipient`, and `account_from` to the `slots:` section, the three ask responses under `responses:`, and `action_process_transfer` in the `actions:` list in `level4/domain/basics.yml`.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Python script).

---

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 4.1 section in the Codio Guide Editor (Level 4 chapter).

2. **Add LLM Rubric Assessment.** Add assessment, then **LLM Rubric** / **Autograde**.

3. **Configure** – Use the **Instructor Provided Solution File**: `.guides/assessments/level4_graders/lab_4.1_solution_reference.md` (or `/home/codio/workspace/.guides/assessments/level4_graders/lab_4.1_solution_reference.md`). Define rubric criteria for: slots section with amount, recipient, account_from; utter_ask_amount, utter_ask_recipient, utter_ask_account_from with at least one text each; action_process_transfer in actions; valid YAML and Level 3 content preserved. Suggested total points: 10. **Show Rationale to Student:** After 1 attempt (or Always).

4. **Files tab** – Ensure the LLM can read: `/home/codio/workspace/level4/domain/basics.yml`

5. **Test.** Run with a complete domain (three slots, three ask responses, action_process_transfer in actions) for pass; with any missing for fail with feedback.

---

### Option B: Standard Code Test (Python script)

Use a Python grader for faster feedback. The script parses `level4/domain/basics.yml` and checks: file exists and is valid YAML; `slots:` section contains `amount`, `recipient`, `account_from` (each type text or equivalent); `responses:` contains `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from` with at least one text message each; `action_process_transfer` in the `actions:` list. Total: 10 points. On full score it prints `PASS` and `Successfully passed!`; otherwise `FAIL` and exit 1.

**Grader script location (in repo):**

```
.guides/assessments/level4_graders/lab_4.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/assessments/level4_graders/lab_4.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in COMMAND.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **10**. Enable **Allow partial points** if desired.
   - **Test case:** One test case. **EXPECTED OUTPUT:** `PASS`. **Enable substring match** so Codio passes when `PASS` appears in the output.
   - **SHOW RATIONALE TO STUDENT:** **AFTER [1] ATTEMPTS** (or **ALWAYS**).
   - **RATIONALE:** The grader checks that `level4/domain/basics.yml` exists, is valid YAML, and contains: **slots:** with **amount**, **recipient**, **account_from** (type text), the **utter_ask_amount**, **utter_ask_recipient**, **utter_ask_account_from** responses with at least one message each, and **action_process_transfer** in the **actions:** list. Review the script output for which check failed.
4. **Files.** Script at `.guides/assessments/level4_graders/lab_4.1_grader.py`; run from workspace so `git pull` keeps it in sync.

---

## Reference for rubric / grading

- **Solution reference:** `.guides/assessments/level4_graders/lab_4.1_solution_reference.md`
