# Lab 0.1: Create Virtual Environment and Install Rasa Pro - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab is part of Unit 0: Prerequisites and Setup.

---

### Your Task

1. Create a virtual environment in the `level1` folder: `python3.11 -m venv .venv` then `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\Activate.ps1` (Windows PowerShell).
2. Install Rasa Pro: `pip install --no-cache-dir rasa-pro`.
3. Verify: `rasa --version` shows version info; `domain/` and `data/` exist; environment variables (e.g. RASA_LICENSE, OPENAI_API_KEY) are set as required by your environment.

---

### Verification

- Virtual environment exists (`.venv/`)
- `rasa --version` runs successfully
- Project structure present (`domain/`, `data/`, config files)

Run the assessment when you're done.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students have created a virtual environment in `level1`, installed Rasa Pro, and can run `rasa --version` successfully.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level1_graders/lab_0.1_grader.sh
```

## Grader Script

The grader should run from `/home/codio/workspace/level1` (or project root) and check:

1. **Virtual environment exists** – e.g. `.venv` directory in `level1` (or workspace root)
2. **Rasa is installed** – running `python -m rasa --version` (or `rasa --version` with venv activated) succeeds
3. **Project structure** – `domain/` and `data/` exist (optional)

Use clear PASS/FAIL messages and hints. Suggested total points: 4–6 (adjust per course design).

## Assessment Setup and Configuration

1. **Navigate** to the Lab 0.1 section in the Codio Guide Editor.

2. **Add Code Test** – Standard Code Test. COMMAND: `bash /home/codio/workspace/.guides/assessments/level1_graders/lab_0.1_grader.sh`. Working Directory: `/home/codio/workspace/level1` (or as appropriate). Timeout: 60 seconds.

3. **Create** `.guides/assessments/level1_graders/lab_0.1_grader.sh` and make it executable.

4. **Test** – Run after a student completes Lab 0.1 (venv + Rasa install); confirm pass. Run in a fresh workspace without venv; confirm fail with hint.
