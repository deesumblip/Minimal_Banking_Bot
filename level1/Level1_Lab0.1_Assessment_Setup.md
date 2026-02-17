# Lab 0.1: Create Virtual Environment and Install Rasa Pro - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab is part of Unit 0: Prerequisites and Setup.

---

### Your Task

1. Create a virtual environment in the **main project folder (root)** (the folder that contains `level1`, `level2`, and `.guides`): `python3.11 -m venv .venv` then `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\Activate.ps1` (Windows PowerShell). This same `.venv` is used for all levels in the course.
2. Install Rasa Pro: `pip install --no-cache-dir rasa-pro`.
3. Verify: `rasa --version` shows version info; `level1` has `domain/`, `data/`, and config files; environment variables (e.g. RASA_LICENSE, OPENAI_API_KEY) are set as required by your environment.

---

### Verification

- Virtual environment exists (`.venv/` in **project root**)
- `rasa --version` runs successfully (with venv activated)
- Project structure present in `level1/` (`domain/`, `data/`, config files)

Run the assessment when you're done.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students have created a virtual environment in the **project root** (workspace root on Codio), installed Rasa Pro, and can run `rasa --version` successfully. The same venv is used for all levels.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level1_graders/lab_0.1_grader.sh
```

## Grader Script

The grader should run from **workspace root** (`/home/codio/workspace`) and check:

1. **Virtual environment exists** – `.venv` directory in **workspace root** (not inside `level1`).
2. **Rasa is installed** – with venv activated from root, running `rasa --version` (or `python -m rasa --version`) succeeds.
3. **Project structure** – `level1/domain/` and `level1/data/` exist (optional).

Use clear PASS/FAIL messages and hints. Suggested total points: 4–6 (adjust per course design).

## Assessment Setup and Configuration

1. **Navigate** to the Lab 0.1 section in the Codio Guide Editor.

2. **Add Code Test** – Standard Code Test. COMMAND: `bash /home/codio/workspace/.guides/assessments/level1_graders/lab_0.1_grader.sh`. Working Directory: **`/home/codio/workspace`** (project root, where `.venv` lives). Timeout: 60 seconds.

3. **Create** `.guides/assessments/level1_graders/lab_0.1_grader.sh` and make it executable. The script should `cd` to workspace root, check for `.venv` there, activate it, then run `rasa --version`.

4. **Test** – Run after a student completes Lab 0.1 (venv in root + Rasa install); confirm pass. Run in a fresh workspace without venv; confirm fail with hint.
