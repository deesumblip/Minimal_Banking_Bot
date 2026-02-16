# Lab 6.1: Training Your Bot - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 6: Training and Testing.

---

### Your Task

Train your bot from the `level1` folder (with virtual environment activated) by running:

```bash
python -m rasa train
```

Wait for training to finish. A model file (`.tar.gz`) will be created in the `models/` folder.

---

### Verification

Before submitting, confirm:

- Training completed without errors
- A model file exists under `models/`

Run the assessment when you're done.

---

#### Review in Inspector (optional)

After the assessment, open Rasa Inspector (see Unit 6.3). Try "hello", "help", and "contact" to confirm the correct flows trigger.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students can successfully train their Level 1 bot and that training completes without errors (model file created, no critical errors in logs).

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level1_graders/lab_6.1_grader.sh
```

## Grader Script

The grader should run from `/home/codio/workspace/level1` and check:

1. **Model file exists** (e.g. 2 points) – at least one `.tar.gz` file in `models/`
2. **No critical errors** (e.g. 2 points) – optional: check `logs/logs.out` for "error"/"exception"/"failed"; if no log file, pass this check

**Total suggested points**: 4

Structure the script like the Level 2 Lab 6.1 grader but use paths for `level1` (e.g. `cd /home/codio/workspace/level1`, check `models/*.tar.gz`, `logs/logs.out`). Output clear PASS/FAIL messages and hints.

### Example student deliverable

Students run (from `level1` with venv active):

```bash
python -m rasa train
```

Success = a new `.tar.gz` in `models/` and no errors in the terminal (and optionally no critical errors in logs).

## Assessment Setup and Configuration

1. **Navigate** to the Lab 6.1 section in the Codio Guide Editor.

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure:

   **General** – Name: *Lab 6.1: Training Your Bot*. Description: *Verify that the student successfully trained the Level 1 bot*. Points: `4`. Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/assessments/level1_graders/lab_6.1_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace/level1`.

   **Grading** – Points: 4. Allow partial points: OFF. Case insensitive: ON. Ignore white spaces: ON. Match script output to expected "PASS" or similar success message.

3. **Create the grader script** – Add `.guides/assessments/level1_graders/lab_6.1_grader.sh` (create the directory if needed). Script should `cd /home/codio/workspace/level1` (or use that as working directory), then run the checks above. Make the script executable: `chmod +x lab_6.1_grader.sh`.

4. **Test** – Run the assessment in Codio after a student has run `rasa train` in `level1`; confirm it passes. Run in a workspace where no model exists; confirm it fails with a clear hint.
