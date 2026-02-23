# Lab 5.1: Creating a Flow with Slot Collection - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 5: Collecting Slots in Flows.

**Task**: Create `data/basics/check_balance.yml` in the `level3` folder with a flow that has `collect: account` and `action: action_check_balance_simple`. Run the assessment when done.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has created `level3/data/basics/check_balance.yml` with a flow containing a `collect: account` step and the `action_check_balance_simple` action step.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Bash script).

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
| **Instructor Provided Solution File** | `.guides/assessments/level3_graders/lab_5.1_solution_reference.md` (or `/home/codio/workspace/.guides/assessments/level3_graders/lab_5.1_solution_reference.md` if Codio requires absolute path) |
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

### Option B: Standard Code Test (Bash script)

**Grader script location**:
```
.guides/assessments/level3_graders/lab_5.1_grader.sh
```

**Grader script** – Run from **workspace root**: activate venv, then `cd level3`. Check: `data/basics/check_balance.yml` exists; file contains a flow with `collect: account` (or equivalent) and `action: action_check_balance_simple`. Print `PASS` / `Successfully passed!` on full score; `FAIL` and exit 1 on failure. Suggested points: 6–8.

**Codio configuration** – Add Code Test → Standard Code Test.

- COMMAND: `bash /home/codio/workspace/.guides/assessments/level3_graders/lab_5.1_grader.sh`
- Working Directory: `/home/codio/workspace`
- Expected output: `PASS` or `Successfully passed!`
