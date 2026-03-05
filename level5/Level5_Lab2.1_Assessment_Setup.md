# Lab 2.1: Creating the Tools Folder and banking_tools.py - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 2 (Creating Tool Functions), Level 5.

**Task.** Create the `tools/` folder in `level5` and add `tools/banking_tools.py` with at least three tool functions: `check_balance(account)`, `process_transfer(amount, from_account, to_account)`, and `get_account_info(account)`. Export them via `__all__`. Run the assessment when done.

**Codio guide (Chapter 1.5).** The Lab 2.1 page in the Chapter 1.5 guide includes: `{Check It!|assessment}(code-output-compare-501020001)`. Assessment JSON: `.guides/assessments/code-output-compare-501020001.json`.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has created `level5/tools/` and `level5/tools/banking_tools.py` with: the three functions (or equivalent names) with docstrings; `__all__` listing them; valid Python syntax.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Python script).

### Option A: LLM Rubric

Use solution reference `.guides/secure/level5_graders/lab_2.1_solution_reference.md`. Criteria: tools/ folder exists; banking_tools.py exists; check_balance, process_transfer, get_account_info defined; __all__ exports them; docstrings present. Points: 10. Files: `/home/codio/workspace/level5/tools/banking_tools.py`.

### Option B: Code Test

Python grader at `.guides/secure/level5_graders/lab_2.1_grader.py`. Checks: level5/tools/ exists; level5/tools/banking_tools.py exists; file contains "check_balance", "process_transfer", "get_account_info", "__all__". COMMAND: `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level5_graders/lab_2.1_grader.py`. Working Directory: `/home/codio/workspace`. Expected output: `PASS` (substring match).
