# Lab 5.1: Creating a Flow with Slot Collection - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 5: Collecting Slots in Flows.

**Task**: Create `data/basics/check_balance.yml` in the `level3` folder with a flow that has `collect: account` and `action: action_check_balance_simple`. Run the assessment when done.

**Codio guide (Chapter 1.3).** The Lab 5.1 page includes: `{Check It!|assessment}(code-output-compare-1235165472)`. Assessment JSON: `.guides/assessments/code-output-compare-1235165472.json`.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has created `level3/data/basics/check_balance.yml` with a flow containing a `collect: account` step and the `action_check_balance_simple` action step.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Python script).

---

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 5.1 section in the Codio Guide Editor (Level 3).

2. **Add LLM Rubric Assessment** – Add assessment → **LLM Rubric** / **Autograde**.

3. **Configure** (see **Grading** tab below).

4. **Test**: Run with a complete check_balance.yml (pass), with collect missing (fail with feedback), with action missing (fail with feedback).

---

#### LLM Rubric Autograde – Grading tab (exact settings and copy-paste rubric)

| Option | Set to |
|--------|--------|
| **Total Points** | **8** |
| **Instructor Provided Solution File** | `.guides/secure/level3_graders/lab_5.1_solution_reference.md` (or `/home/codio/workspace/.guides/secure/level3_graders/lab_5.1_solution_reference.md` if Codio requires absolute path) |
| **Defined Number of Attempts** | **Off** (leave toggle off) |
| **Show Rationale to Student** | **After [1] attempts** (select that radio, leave the number as 1) |

---

**Add Rubric** – Click **ADD RUBRIC** and add the following four criteria. For each criterion, paste the text below into the rubric description field and set the points as indicated. Enable **partial credit** for the assessment.

**Rubric 1** — Points: **2**  
Copy and paste this into the criterion description:

```
The file check_balance.yml exists in level3/data/basics/. The path is correct (data/basics/, not data/ root). Award full points if the file exists in the right location; zero if missing or in wrong folder.
```

**Rubric 2** — Points: **2**  
Copy and paste this into the criterion description:

```
The file has valid YAML with a top-level "flows:" key and at least one flow that has "name", "description", and "steps". Award full points if the flow structure is correct; partial if flows exist but name/description/steps are incomplete; zero if structure is wrong or file is invalid YAML.
```

**Rubric 3** — Points: **2**  
Copy and paste this into the criterion description:

```
At least one step in the flow uses "collect: account" (with optional "description:" for the slot, e.g. "account number"). Award full points if collect: account is present in steps; zero if missing or misspelled (e.g. collect: balance instead of account).
```

**Rubric 4** — Points: **2**  
Copy and paste this into the criterion description:

```
At least one step in the flow uses "action: action_check_balance_simple". Award full points if this action step is present; zero if missing or action name is wrong.
```

---

**Files tab**  
Configure the assessment so the LLM can read:

- `/home/codio/workspace/level3/data/basics/check_balance.yml`

---

### Option B: Standard Code Test (Python script)

Use a Python grader for faster feedback. Output matches **Lab 3.1 / Lab 6.2**: **Check 1–4**, leading-space PASSED lines, **`==========================================`** band, **` PASS: Lab 5.1 verification complete! Score: 8/8`**. The repo JSON **`code-output-compare-1235165472.json`** sequences **`Check 1: PASSED`** … **`Check 4: PASSED`** with **`showFeedback`: false**.

**Grader script location (in repo):**

```
.guides/secure/level3_graders/lab_5.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** Use the project venv’s Python so PyYAML is available:  
     `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level3_graders/lab_5.1_grader.py`  
     Leave **Pre-Exec** empty when using this.  
     **Alternative:** If your Codio image has PyYAML for `python3`:  
     `python3 /home/codio/workspace/.guides/secure/level3_graders/lab_5.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in COMMAND. Using the venv’s interpreter in COMMAND ensures PyYAML is available without relying on pre-exec or shell activation.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **8**. Enable **Allow partial points** if desired.
   - **Sequence:** Use repo **`code-output-compare-1235165472.json`** (four **`Check N: PASSED`** steps, **`showGuidanceAfterResponseOption`:** Never, **`showExpectedAnswerOption`:** Always).
   - **SHOW RATIONALE TO STUDENT:** Optional.
   - **RATIONALE** (text box): Example:
     > Four checks: file, flows structure, **collect: account**, **action: action_check_balance_simple**. Full credit **8/8** and **` PASS: Lab 5.1 verification complete!`**
   - **SHOW EXPECTED ANSWER:** **Always**.
4. **Files.** The script lives in the repo at `.guides/secure/level3_graders/lab_5.1_grader.py`. Do not upload it; run it from the workspace so `git pull` keeps the grader in sync. The script requires Python 3 and PyYAML; use the venv’s Python in COMMAND for consistency.
