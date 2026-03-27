# Lab 2.1: Creating the Tools Folder and banking_tools.py - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 2 (Creating Tool Functions), Level 5.

**Task.** Part 1: Complete the fill-in-the-blanks for `banking_tools.py`. Part 2: Create `level5/tools/`, `level5/tools/__init__.py`, and `level5/tools/banking_tools.py` with your completed script. Part 3: Run the code test. (The grader reads files only; no terminal commands are required for grading.)

**Codio guide (Chapter 1.5).** The Lab 2.1 page includes, in order:

1. `{Check It!|assessment}(fill-in-the-blanks-501020010)` — **5 points**
2. `{Check It!|assessment}(code-output-compare-501020001)` — **10 points**

**Assessment JSONs:**

- `.guides/assessments/fill-in-the-blanks-501020010.json`
- `.guides/assessments/code-output-compare-501020001.json`

---

## Assessment Setup (For Implementers)

### Fill-in-the-blanks (student Part 1)

**Task ID:** `fill-in-the-blanks-501020010`  
**Points:** 5  
**Pattern:** Same as Chapter 1.4 Lab 3.1 (`fill-in-the-blanks-401030010`): intro paragraph plus a **fenced** ` ```python ` block in the **`text`** field; **`__all__`** is a **complete line** (no blanks). **`tokens.text`** and **`tokens.blank`** hold **12** ordered blanks: **`str`** for **`check_balance`** and **`get_account_info`**, three docstrings, dict keys including **`account_type`** / **`status`** for **`get_account_info`** (no arbitrary demo literals).

### Code test (student Part 3)

Python grader at `.guides/secure/level5_graders/lab_2.1_grader.py`. **Lab 6.2-style:** **Check 1–4** with leading space on ` Check N: PASSED` lines, score band, **` PASS: Lab 2.1 verification complete! Score: 10/10`**. COMMAND: `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level5_graders/lab_2.1_grader.py`. WD: `/home/codio/workspace`. Codio: import sequence from `code-output-compare-501020001.json` (`Check 1: PASSED` … `Check 4: PASSED`, **`showFeedback`: false**).

**Solution reference (LLM Rubric / review):** `.guides/secure/level5_graders/lab_2.1_solution_reference.md`
