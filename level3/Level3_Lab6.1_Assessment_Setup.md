# Lab 6.1: Training and Testing with Slots - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 6: Training and Testing with Slots.

**Structure**: Part 1 (In Codio) and Part 2 (Running locally). Both follow the same order: **activate the virtual environment in the main project folder (root)** first, then **navigate to `level3`**, then train. **"Run the assessment when done"** appears at the end of Part 1 only; Part 2 ends with success criteria only.

### Your Task (summary)

Activate the virtual environment in the main project folder (root), navigate to `level3`, then train your bot by running:

```bash
cd level3
python -m rasa train
```

Wait for training to finish. A model file (`.tar.gz`) will be created in the `models/` folder.

### Verification

Before submitting, confirm:

- Training completed without errors
- A model file exists under `level3/models/`

Run the assessment when you're done (Part 1 path).

---

#### Review in Inspector (optional)

After the assessment, open Rasa Inspector (see Unit 6.2). Use the **Rasa Inspect** tab on Codio. Try "Check my balance", then provide an account number; try "What are your hours?" to confirm Level 2 still works.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students can successfully train their Level 3 bot and that training completes without errors (model file created, no critical errors in logs). The same conventions as Level 1 and Level 2 apply: venv in workspace root, grader runs from root and `cd`s to `level3` for checks.

**Lab workflow**: Students (1) activate venv in project root, (2) `cd level3`, (3) run `python -m rasa train`. The grader script runs from **workspace root**, activates venv, then `cd`s to `level3` for model and log checks.

### Assessment Type

**Standard Code Test** (Python script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level3_graders/lab_6.1_grader.py
```

## Grader Script

The grader runs from **workspace root** (`/home/codio/workspace`): it verifies the venv exists, then checks `level3` for model and log files. It performs the following checks:

1. **Check 0 – Virtual environment** (2 pts): `.venv` exists in workspace root and Python is available.
2. **Check 1 – Model file exists** (2 pts): at least one `.tar.gz` in `level3/models/`.
3. **Check 2 – Model recent** (3 pts): newest model is under 10 minutes old (uses file modification time).
4. **Check 3 – Logs** (3 pts): if `level3/logs/logs.out` exists, checks for "error"/"exception"/"failed" (case-insensitive); if no log file, passes.
5. **Check 4 – Training completed** (2 pts): implied by passing above.

**Total: 12 points.** The script must print a line containing `PASS` and `Successfully passed!` on full success so Codio's expected-output match works. On failure print `FAIL` and exit 1.

**Why Python?** Python provides better file timestamp handling, more robust log parsing, and clearer error messages than Bash for these checks.

### Example student deliverable

Students activate the virtual environment in the main project folder (root), then navigate to `level3`, then run:

```bash
cd level3
python -m rasa train
```

Success = a new `.tar.gz` in `level3/models/` and no errors in the terminal.

## Codio configuration (Standard Code Test)

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** Use the project venv’s Python so dependencies are available:  
     `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/assessments/level3_graders/lab_6.1_grader.py`  
     **Alternative:** If your Codio image already has the required modules for `python3`, you can use:  
     `python3 /home/codio/workspace/.guides/assessments/level3_graders/lab_6.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in COMMAND above.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **12** (or match your course scale). The script reports partial checks; you can enable **Allow partial points** if Codio supports it for this test type.
   - **Add item to check / Test case:** Add one test case. Leave **INPUT - ARGUMENTS** and **INPUT - STDIN** empty. In **EXPECTED OUTPUT**, enter: `PASS` (the script prints this on success; you may also match `Successfully passed!` if Codio allows).
   - **SHOW RATIONALE TO STUDENT:** Recommended: **AFTER [1] ATTEMPTS** (or **ALWAYS**). Set the number to 1 if using "AFTER … ATTEMPTS".
   - **RATIONALE** (text box): Example:
     > The grader verifies the virtual environment in project root, that a model file (`.tar.gz`) exists in `level3/models/`, that the model is recent, and that logs do not show critical errors. Ensure you ran `python -m rasa train` from the `level3` folder with the venv activated.
   - **SHOW EXPECTED ANSWER:** Optional; **When grades are released** or **Always** so students see that the expected output is `PASS`.
4. **Files.** The script lives in the repo at `.guides/assessments/level3_graders/lab_6.1_grader.py`. Do not upload it; the Execution command runs it from the workspace so `git pull` keeps the grader in sync. No need to chmod (Python); use the venv’s Python in COMMAND if the environment does not provide dependencies globally.
5. **Test** – Run the assessment after a student has run `rasa train` in `level3` (pass); run in a workspace with no model in `level3` (fail with clear hint).
