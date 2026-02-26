# Lab 4.1: Creating the Transfer Flow with Multiple Collect Steps - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 5: Flows with Multiple Collect Steps (Level 4).

**Task.** Create `data/basics/transfer_money.yml` in the `level4` folder with a flow that has `collect: amount`, `collect: recipient`, `collect: account_from`, and `action: action_process_transfer`. Run the assessment when done.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has created `level4/data/basics/transfer_money.yml` with a flow containing the three collect steps (amount, recipient, account_from) and the `action_process_transfer` action step.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Python script).

---

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 4.1 section (Creating the Transfer Flow) in the Codio Guide Editor (Level 4 chapter).

2. **Add LLM Rubric Assessment** – Add assessment → **LLM Rubric** / **Autograde**.

3. **Configure** – Use the **Instructor Provided Solution File**: `.guides/assessments/level4_graders/lab_4.1_solution_reference.md`. Define rubric criteria for: file exists in level4/data/basics/; valid YAML with flows: and at least one flow with name, description, steps; steps include collect: amount, collect: recipient, collect: account_from; steps include action: action_process_transfer. Suggested total points: 8. **Show Rationale to Student:** After 1 attempt (or Always).

4. **Files tab** – Ensure the LLM can read: `/home/codio/workspace/level4/data/basics/transfer_money.yml`

5. **Test** – Run with a complete transfer_money.yml (pass); with a collect or action missing (fail with feedback).

---

### Option B: Standard Code Test (Python script)

Use a Python grader for faster feedback. The script checks `level4/data/basics/transfer_money.yml` for: file exists; valid YAML with top-level `flows:`; at least one flow with `name` and `steps`; steps contain `collect: amount`, `collect: recipient`, `collect: account_from`; steps contain `action: action_process_transfer`. Total: 8 points. On full score it prints `PASS` and `Successfully passed!`; otherwise `FAIL` and exit 1.

**Grader script location (in repo):**

```
.guides/assessments/level4_graders/lab_4.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/assessments/level4_graders/lab_4.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty**.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **8**. Enable **Allow partial points** if desired.
   - **Test case:** One test case. **EXPECTED OUTPUT:** `PASS`. **Enable substring match**.
   - **SHOW RATIONALE TO STUDENT:** **AFTER [1] ATTEMPTS** (or **ALWAYS**).
   - **RATIONALE:** The grader checks that `level4/data/basics/transfer_money.yml` exists, has valid YAML with a **flows:** section, at least one flow with **name** and **steps**, steps with **collect: amount**, **collect: recipient**, **collect: account_from**, and **action: action_process_transfer**. Review the script output to see which check failed.
4. **Files.** Script at `.guides/assessments/level4_graders/lab_4.1_grader.py`; run from workspace.

---

## Reference for rubric / grading

- **Solution reference:** `.guides/assessments/level4_graders/lab_4.1_solution_reference.md`
