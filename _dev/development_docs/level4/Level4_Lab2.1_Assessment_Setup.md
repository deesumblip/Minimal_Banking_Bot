# Lab 2.1: Adding Multiple Slots in the Domain - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 3: Adding Slots and Responses for Transfer (Level 4).

**Task.** In `domain/basics.yml` in the `level4` folder, add the slots `amount`, `recipient`, and `account_from` (each type text), keep the Level 3 **`account`** slot and **`utter_ask_account`** response, add `utter_ask_amount`, `utter_ask_recipient`, and `utter_ask_account_from`, and register `action_process_transfer` in the `actions:` list. You will create the action file in Lab 3.1. Run the assessment when done.

**Codio guide (Level 4).** The Lab 2.1 page in the Level 4 guide includes: `{Check It!|assessment}(code-output-compare-401020001)`. Assessment JSON: `.guides/assessments/code-output-compare-401020001.json`.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has added the slots `amount`, `recipient`, and `account_from` to the `slots:` section (and kept **`account`**), the four ask responses (`utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`, **`utter_ask_account`**) under `responses:`, and `action_process_transfer` in the `actions:` list in `level4/domain/basics.yml`, and that **Level 2/3 actions** (`action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`) were **not removed** when adding the transfer action (otherwise `rasa train` fails because flows still reference them).

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Python script).

---

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 2.1 section in the Codio Guide Editor (Level 4 chapter).

2. **Add LLM Rubric Assessment.** Add assessment, then **LLM Rubric** / **Autograde**.

3. **Configure** – Use the **Instructor Provided Solution File** from **`.guides/secure/level4_graders/`** (lab 2.1 solution reference, next to **`lab_2.1_grader.py`**). Define rubric criteria for: slots section with amount, recipient, account_from; utter_ask_amount, utter_ask_recipient, utter_ask_account_from with at least one text each; action_process_transfer in actions; valid YAML and Level 3 content preserved. Suggested total points: 10. **Show Rationale to Student:** After 1 attempt (or Always).

4. **Files tab** – Ensure the LLM can read: `/home/codio/workspace/level4/domain/basics.yml`

5. **Test.** Run with a complete domain (three slots, three ask responses, action_process_transfer in actions) for pass; with any missing for fail with feedback.

---

### Option B: Standard Code Test (Python script)

Use a Python grader for faster feedback. Output matches the **Level 2 Lab 6.2** template (same as **Level 3 Lab 3.1**): **Check 1–5** (1-based), leading space on pass lines (` Check N: PASSED - …`), **==========================================** score band, **` PASS: Lab 2.1 verification complete! Score: 12/12`** on full pass; exit **0** only on **12/12**. The script parses `level4/domain/basics.yml` and checks: file exists; valid YAML; `slots:` contains `amount`, `recipient`, `account_from`, and **`account`**; `responses:` has the four ask utterances (including **`utter_ask_account`**) with text; `action_process_transfer` in `actions:`; **Level 3 actions** `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple` still in `actions:`.

**Grader script location (in repo):**

```
.guides/secure/level4_graders/lab_2.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level4_graders/lab_2.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in COMMAND.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **12**. Enable **Allow partial points** if desired.
   - **Sequence:** Re-import from `.guides/assessments/code-output-compare-401020001.json`: five substring matches `Check 1: PASSED` … `Check 5: PASSED`, each **`showFeedback`: false**. **`matchSubstring`: true**. **`showGuidanceAfterResponseOption`:** **Never**; **`showExpectedAnswerOption`:** **Always** (matches Lab 3.1 / Lab 6.2).
   - **SHOW RATIONALE TO STUDENT:** **AFTER [1] ATTEMPTS** (or **ALWAYS**).
   - **RATIONALE:** The grader checks that `level4/domain/basics.yml` exists, is valid YAML, and contains: **slots:** with **amount**, **recipient**, **account_from** (type text), the **utter_ask_amount**, **utter_ask_recipient**, **utter_ask_account_from** responses with at least one message each, **action_process_transfer** in the **actions:** list, and **action_bank_hours**, **action_holiday_hours**, **action_check_balance_simple** still listed under **actions:**. Review the script output for which check failed.
4. **Files.** Script at `.guides/secure/level4_graders/lab_2.1_grader.py`; run from workspace so `git pull` keeps it in sync.

---

## Reference for rubric / grading

- **Solution reference:** **`.guides/secure/level4_graders/`** (lab 2.1, alongside **`lab_2.1_grader.py`**)
