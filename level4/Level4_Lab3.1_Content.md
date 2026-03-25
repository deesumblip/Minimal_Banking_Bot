**Starting point:** Chapter 1.4 assumes you began with the **final banking agent at the end of Chapter 1.3** and are extending **`level4/`** (see **`Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`**).

**Objective.** Create `action_process_transfer` that reads `amount`, `recipient`, and `account_from`, re-prompts on placeholders, and sends a demo confirmation. This lab follows the **same two-step pattern as Chapter 1.3 Lab 4.1** (*Exploring Actions with Slots*): complete the **Fill in the Blanks** assessment first, then paste the full script and run the **code** assessment.

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

**Canonical lab page:** `.guides/content/Chapter-1-4---Multiple-Slots-e5f6/Unit-3--Reading-Multiple-Slots-in-Actions-0d1e/Lab-3-1-Writing-the-Action-c6d7.md`

**Prerequisite.** Domain from Lab 2.1 lists `action_process_transfer` under `actions:`.

**Optional.** After Lab 5.1, train and run Inspector on the transfer flow.

---

## See also

- Assessment setup: `level4/Level4_Lab3.1_Assessment_Setup.md`
- Fill-in-the-blanks wording lives in `fill-in-the-blanks-401030010.json` (not duplicated here).
