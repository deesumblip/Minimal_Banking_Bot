# Lab 6.1: Training and Testing with Slots - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 6: Training and Testing with Slots.

**Structure**: Part 1 (In Codio) and Part 2 (Running locally). Both follow the same order: **activate the virtual environment in the main project folder (root)** first, then **navigate to `level3`**, then train. **"Run the assessment when done"** appears at the end of Part 1 only; Part 2 ends with success criteria only.

### Your Task (summary)

Activate the virtual environment in the main project folder (root), navigate to `level3`, then train your agent by running:

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

**Codio guide (Chapter 1.3).** The Lab 6.1 page includes: `{Check It!|assessment}(code-output-compare-1029038275)`. Assessment JSON: `.guides/assessments/code-output-compare-1029038275.json`. Grader: `.guides/secure/level3_graders/lab_6.1_grader.py`.

---

#### Review in Inspector (optional)

After the assessment, open Rasa Inspector (see Unit 6.2). Use the **Rasa Inspect** tab on Codio. Try "Check my balance", then provide an account number; try "What are your hours?" to confirm Level 2 still works.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students can successfully train their Level 3 agent and that training completes without errors (model file created, no critical errors in logs). The same conventions as Level 1 and Level 2 apply: venv in workspace root, grader runs from root and `cd`s to `level3` for checks.

**Lab workflow**: Students (1) activate venv in project root, (2) `cd level3`, (3) run `python -m rasa train`. The grader script runs from **workspace root**, activates venv, then `cd`s to `level3` for model and log checks.

### Assessment Type

**Standard Code Test** (Python script)

## Grader Script Location

Save the grader script at:
```
.guides/secure/level3_graders/lab_6.1_grader.py
```

## Grader Script

The grader runs from **workspace root** (`/home/codio/workspace`): it verifies the venv exists, then `cd`s to `level3` for model and log checks. Output matches **Lab 3.1 / Lab 6.2** (Check **1–5**, leading-space PASSED lines, **`==========================================`** band).

1. **Check 1 – Virtual environment** (2 pts): `.venv` exists; Python in `bin/` or `Scripts/`.
2. **Check 2 – Model file** (2 pts): at least one `.tar.gz` in `level3/models/`.
3. **Check 3 – Model recent** (3 pts): newest model under 10 minutes old; otherwise **PARTIAL** (0 pts on that check).
4. **Check 4 – Logs** (3 pts): `logs/logs.out` without obvious errors, or no log file (pass).
5. **Check 5 – Artifacts** (2 pts): training bundle ready for inspect.

**Total: 12 points.** The repo assessment **`code-output-compare-1029038275.json`** sequences **`Check 1: PASSED`** … **`Check 5: PASSED`**. On full score: **` PASS: Lab 6.1 verification complete! Score: 12/12`**. Exit **1** if the score is below 12.

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
     `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level3_graders/lab_6.1_grader.py`  
     **Alternative:** If your Codio image already has the required modules for `python3`, you can use:  
     `python3 /home/codio/workspace/.guides/secure/level3_graders/lab_6.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in COMMAND above.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **12**. Enable **Allow partial points** if desired (Check 3 or 4 may be partial).
   - **Sequence:** Use repo **`code-output-compare-1029038275.json`** — five **`Check N: PASSED`** steps, **`showGuidanceAfterResponseOption`:** Never, **`showExpectedAnswerOption`:** Always (Lab 3.1 / Lab 6.2 layout).
   - **SHOW RATIONALE TO STUDENT:** Optional.
   - **RATIONALE** (text box): Example:
     > Five checks: venv, model file, recent model, logs, artifacts. Re-run **`python -m rasa train`** from **level3** if Check 3 or 4 is partial. Full credit **12/12**.
   - **SHOW EXPECTED ANSWER:** **Always**.
4. **Files.** The script lives in the repo at `.guides/secure/level3_graders/lab_6.1_grader.py`. Do not upload it; the Execution command runs it from the workspace so `git pull` keeps the grader in sync. No need to chmod (Python); use the venv’s Python in COMMAND if the environment does not provide dependencies globally.
5. **Test** – Run the assessment after a student has run `rasa train` in `level3` (pass); run in a workspace with no model in `level3` (fail with clear hint).
