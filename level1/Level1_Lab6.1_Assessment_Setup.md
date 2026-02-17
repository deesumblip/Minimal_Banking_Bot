# Lab 6.1: Training Your Bot - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 6: Training and Testing.

**Structure**: Part 1 (In Codio) and Part 2 (Running locally). Both follow the same order: **activate the virtual environment in the main project folder (root)** first, then **navigate to `level1`**, then train. Students use the terminal window (no separate "Open Tools → Terminal" step). **"Run the assessment when done"** appears at the end of Part 1 only; Part 2 ends with success criteria only.

### Your Task (summary)

Activate the virtual environment in the main project folder (root), navigate to `level1`, then train your bot by running:

```bash
cd level1
python -m rasa train
```

Wait for training to finish. A model file (`.tar.gz`) will be created in the `models/` folder.

### Verification

Before submitting, confirm:

- Training completed without errors
- A model file exists under `models/`

Run the assessment when you're done (Part 1 path).

---

#### Review in Inspector (optional)

After the assessment, open Rasa Inspector (see Unit 6.3). Try "hello", "help", and "contact" to confirm the correct flows trigger.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students can successfully train their Level 1 bot and that training completes without errors (model file created, no critical errors in logs).

**Lab workflow (for implementers)**: The student-facing lab instructs students to (1) use the terminal window, (2) go to the main project folder and activate the venv there, (3) then `cd level1`, (4) then run `python -m rasa train`. The line "Run the assessment when done" appears at the end of Part 1 (Codio) only, not in Part 2 (Running locally). The grader runs from `level1` and checks for model file and logs only; it does not depend on where the venv was activated.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level1_graders/lab_6.1_grader.sh
```

## Grader Script

The grader runs from **workspace root** (`/home/codio/workspace`): it activates the venv there, then `cd`s to `level1` for all other checks. It performs 5 checks (12 points total):

1. **Check 0 – Virtual environment** (2 pts): `.venv` exists in workspace root and is activated.
2. **Check 1 – Model file exists** (2 pts): at least one `.tar.gz` in `level1/models/`.
3. **Check 2 – Model recent** (3 pts): newest model is under 10 minutes old.
4. **Check 3 – Logs** (3 pts): if `logs/logs.out` exists, no "error"/"exception"/"failed"; if no log file, pass.
5. **Check 4 – Training completed** (2 pts): implied by passing above.

**Total: 12 points.** The script prints a line containing exactly `PASS` on full success and `FAIL` on failure so Codio’s Code Test can match expected output `PASS`. Output clear per-check messages and hints.

### Example student deliverable

Students activate the virtual environment in the main project folder (root), then navigate to `level1`, then run:

```bash
cd level1
python -m rasa train
```

Success = a new `.tar.gz` in `models/` and no errors in the terminal (and optionally no critical errors in logs).

## Assessment Setup and Configuration

1. **Navigate** to the Lab 6.1 section in the Codio Guide Editor.

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure:

   **General** – Name: *Lab 6.1: Training Your Bot*. Description: *Verify that the student successfully trained the Level 1 bot*. Points: `12` (when using the repo grader script; it has 5 checks totaling 12). Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/assessments/level1_graders/lab_6.1_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace` (grader script will cd to level1 for model checks; venv is checked in workspace root).

   **Grading** – Points: 12 (when using repo grader). Allow partial points: OFF. Case insensitive: ON. Ignore white spaces: ON. **Expected output**: set to `PASS` so Codio matches the line the script prints on success. (The script prints a line containing exactly "PASS" when all checks pass; if Codio uses "contains" matching, the line "✅ PASS: ..." also matches.)

3. **Grader script in repo** – The script is at `.guides/assessments/level1_graders/lab_6.1_grader.sh`. After pulling from GitHub, make it executable in Codio: `chmod +x /home/codio/workspace/.guides/assessments/level1_graders/lab_6.1_grader.sh`. The script checks venv in workspace root, then runs model/log checks from `level1`; max_score=12.

4. **Test** – Run the assessment in Codio after a student has run `rasa train` in `level1`; confirm it passes. Run in a workspace where no model exists; confirm it fails with a clear hint.
