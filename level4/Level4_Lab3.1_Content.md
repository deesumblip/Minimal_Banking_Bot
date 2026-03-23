**Objective.** Create `action_process_transfer` that reads `amount`, `recipient`, and `account_from`, re-prompts on placeholders, and sends a demo confirmation. This lab follows the **same two-step pattern as Chapter 1.3 Lab 4.1** (*Exploring Actions with Slots*): complete the **Fill in the Blanks** assessment first, then paste the full script and run the **code** assessment.

Students do **not** need to activate the virtual environment for this lab—**Check It!** only checks the saved file.

---

## Student-facing flow (Codio guide)

1. **Fill in the Blanks** — `{Check It!|assessment}(fill-in-the-blanks-401030010)`  
   - Assessment JSON: `.guides/assessments/fill-in-the-blanks-401030010.json`  
   - Twelve blanks cover typing imports, `Action`, action name, return type, three `tracker.get_slot(...)` lines, placeholder `if`, re-prompt text, and `[]` / confirmation `f-string`.

2. **After you complete the blanks** — Open `level4/actions/action_process_transfer.py`, paste your completed script, save.

3. **Run the code assessment** — `{Check It!|assessment}(code-output-compare-401030001)`  
   - Assessment JSON: `.guides/assessments/code-output-compare-401030001.json`  
   - Grader: `.guides/secure/level4_graders/lab_3.1_grader.py`

**Canonical lab page:** `.guides/content/Chapter-1-4---Multiple-Slots-e5f6/Unit-3--Reading-Multiple-Slots-in-Actions-0d1e/Lab-3-1-Writing-the-Action-c6d7.md`

**Prerequisite.** Domain from Lab 2.1 lists `action_process_transfer` under `actions:`.

**Optional.** After Lab 5.1, train and run Inspector on the transfer flow.

---

## Instructor reference

- Setup and Codio options: `level4/Level4_Lab3.1_Assessment_Setup.md`
- Full exercise text and blanks live only in `fill-in-the-blanks-401030010.json` (not duplicated here).
