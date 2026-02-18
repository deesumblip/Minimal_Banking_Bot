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

## Assessment Setup and Configuration

1. **Navigate** to the Lab 6.1 section in the Codio Guide Editor (Level 3).

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure:

   **General** – Name: *Lab 6.1: Training and Testing with Slots*. Description: *Verify that the student successfully trained the Level 3 bot*. Points: `12`. Language: `Python`.

   **Execution** – COMMAND: `python3 /home/codio/workspace/.guides/assessments/level3_graders/lab_6.1_grader.py`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace`.

   **Grading** – Points: 12. Allow partial points: OFF. **Expected output**: `PASS` or `Successfully passed!`.

3. **Grader script in repo** – After pulling from GitHub, make it executable: `chmod +x /home/codio/workspace/.guides/assessments/level3_graders/lab_6.1_grader.py`.

4. **Test** – Run the assessment in Codio after a student has run `rasa train` in `level3`; confirm it passes. Run in a workspace where no model exists in `level3`; confirm it fails with a clear hint.
