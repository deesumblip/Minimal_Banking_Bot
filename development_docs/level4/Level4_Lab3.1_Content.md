**Starting point:** Work in **`level4/`** (see **Unit 0.1**).

**Objective.** Create `action_process_transfer` that reads `amount`, `recipient`, and `account_from`, re-prompts on placeholders, and sends a demo confirmation. This lab follows the **same two-step pattern** as the **check-balance** action lab: complete the **Fill in the Blanks** assessment first, then paste the full script and run the **code** assessment.

Students do **not** need to activate the virtual environment for this lab—**Check It!** only checks the saved file.

---

## Lab steps (Codio guide)

1. **Fill in the Blanks** — `{Check It!|assessment}(fill-in-the-blanks-401030010)`  
   - Assessment JSON: `.guides/assessments/fill-in-the-blanks-401030010.json`  
   - **Twelve blanks:** imports, `Action`, `name()`, return type, three slot reads (**recipient** includes **`[:100]`**), placeholder `if` (case-insensitive), re-prompt string, confirmation `f-string`, and `return []`.

2. **After you complete the blanks** — Open `level4/actions/action_process_transfer.py`, paste your completed script, save.

3. **Run the code assessment** — `{Check It!|assessment}(code-output-compare-401030001)`  
   - Assessment JSON: `.guides/assessments/code-output-compare-401030001.json`  
   - Grader: `.guides/secure/level4_graders/lab_3.1_grader.py`

**Guide:** **Lab 3.1** in Level 4, Unit 3.

**Prerequisite.** Domain from Lab 2.1 lists `action_process_transfer` under `actions:`.

**Optional.** After Lab 5.1, train and run Inspector on the transfer flow.

---

## See also

- Assessment setup: instructor materials under `level4/`
- Fill-in-the-blanks wording lives in `fill-in-the-blanks-401030010.json` (not duplicated here).
