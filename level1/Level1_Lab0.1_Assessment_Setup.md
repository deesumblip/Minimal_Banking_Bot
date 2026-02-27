# Lab 0.1: Create Virtual Environment and Install Rasa Pro - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab is part of Unit 0: Prerequisites and Setup.

---

### Your Task

1. Create a virtual environment in the **main project folder (root)** (the folder that contains `level1`, `level2`, and `.guides`): `python3.11 -m venv .venv` then `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\Activate.ps1` (Windows PowerShell). This same `.venv` is used for all levels in the course.
2. Install Rasa Pro: `pip install --no-cache-dir rasa-pro`.
3. Verify: `rasa --version` shows version info; `level1` has `domain/`, `data/`, and config files; **RASA_LICENSE** is set (see lab for how to set it for Codio vs local).

---

### Verification

- Virtual environment exists (`.venv/` in **project root**)
- `rasa --version` runs successfully (with venv activated)
- Project structure present in `level1/` (`domain/`, `data/`, config files)
- **RASA_LICENSE** is set (assessment checks that it is set, not its value)

Run the assessment when you're done.

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students have created a virtual environment in the **project root** (workspace root on Codio), installed Rasa Pro, and can run `rasa --version` successfully. The same venv is used for all levels.

### Assessment Type

**Standard Code Test** (Python script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level1_graders/lab_0.1_grader.py
```

## Grader Script

The grader should run from **workspace root** (`/home/codio/workspace`) and check:

1. **Virtual environment exists** – `.venv` directory in **workspace root** (not inside `level1`).
2. **Rasa is installed** – with venv activated from root, running `rasa --version` (or `python -m rasa --version`) succeeds.
3. **Project structure** – `level1/domain/` and `level1/data/` exist (optional).
4. **RASA_LICENSE is set** – environment variable is set (e.g. from `.env` or Codio env vars); grader checks presence only, never reads or prints the value.

Use clear PASS/FAIL messages and hints. Suggested total points: 7 (Step 1: 2, Step 2: 3, Step 3: 1, Step 4: 1).

## Assessment Setup and Configuration

1. **Navigate** to the Lab 0.1 section in the Codio Guide Editor.

2. **Add Code Test** – Standard Code Test. COMMAND: `python3 /home/codio/workspace/.guides/assessments/level1_graders/lab_0.1_grader.py` (or `python` if that is the default). Working Directory: **`/home/codio/workspace`** (project root, where `.venv` lives). Timeout: 60 seconds.

3. The grader script `.guides/assessments/level1_graders/lab_0.1_grader.py` runs from workspace root, checks for `.venv` there, verifies Rasa Pro via the venv Python, and optionally checks `level1/domain/` and `level1/data/`.

4. **Grading tab – partial points (Option 1: multiple test cases)**  
   Configure Codio so students get partial credit per step:
   - **Points:** 6 (total).
   - **Allow Partial Points:** ON.
   - **Substring Match:** ON (so expected strings can appear anywhere in the script output).
   - **Case Insensitive:** ON, **Ignore White Spaces:** ON (recommended).

   **Test cases** (use “ADD ITEM TO CHECK” to add four items):

   | # | EXPECTED OUTPUT (substring) | Points (if using per-item points) |
   |---|------------------------------|------------------------------------|
   | 1 | `Step 1: PASSED`             | 2 |
   | 2 | `Step 2: PASSED`             | 3 |
   | 3 | `Step 3: PASSED`             | 1 |
   | 4 | `Step 4: PASSED`             | 1 |

   If Codio assigns points per test case, set **2** for test case 1, **3** for test case 2, **1** for test case 3, **1** for test case 4 (total 7). Otherwise ensure the assessment total is 7 and partial credit is applied when only some of these substrings appear.

5. **Test** – Run after a student completes Lab 0.1 (venv in root + Rasa install + RASA_LICENSE set); confirm full pass (7/7). Run with venv but no Rasa; confirm partial pass (e.g. 2/7). Run in a fresh workspace without venv; confirm fail with hint.
