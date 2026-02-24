# Lab 3.1: Defining a Slot in the Domain - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 3: Defining Slots in the Domain.

**Task.** In `domain/basics.yml` in the `level3` folder, add the `slots:` section with `account` (type text), the `utter_ask_account` response, and register `action_check_balance_simple` in the `actions:` list. Run the assessment when done.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has added the `slots:` section with an `account` slot, the `utter_ask_account` response, and `action_check_balance_simple` in the `actions:` list in `level3/domain/basics.yml`.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Bash script).

---

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 3.1 section in the Codio Guide Editor (Level 3).

2. **Add LLM Rubric Assessment.** Add assessment, then **LLM Rubric** / **Autograde**.

3. **Configure** (see **Grading** tab below).

4. **Test.** Run with a complete domain (slots, utter_ask_account, action_check_balance_simple in actions) for pass; with any of these missing for fail with feedback.

---

#### LLM Rubric Autograde – Grading tab (exact settings and copy-paste rubric)

| Option | Set to |
|--------|--------|
| **Total Points** | **10** |
| **Instructor Provided Solution File** | `.guides/assessments/level3_graders/lab_3.1_solution_reference.md` (or `/home/codio/workspace/.guides/assessments/level3_graders/lab_3.1_solution_reference.md` if Codio requires absolute path) |
| **Defined Number of Attempts** | **Off** (leave toggle off) |
| **Show Rationale to Student** | **After [1] attempts** (select that radio, leave the number as 1) |

---

**Add Rubric** – Click **ADD RUBRIC** and add the following five criteria. For each criterion, paste the text below into the criterion description field and set the points as indicated. Enable **partial credit** for the assessment.

**Rubric 1** — Points: **2**  
Copy and paste this into the criterion description:

```
The file level3/domain/basics.yml contains a top-level "slots:" section. The section exists and is valid YAML (e.g. slots: followed by at least one slot definition). Award full points if the slots section is present; zero if missing or malformed.
```

**Rubric 2** — Points: **2**  
Copy and paste this into the criterion description:

```
The "account" slot is defined under the slots section with type "text" (or equivalent valid type such as text). Award full points if account is present with a valid type; partial if account exists but type is wrong or missing; zero if account slot is not present.
```

**Rubric 3** — Points: **2**  
Copy and paste this into the criterion description:

```
Under "responses:" the student added "utter_ask_account" with at least one message (e.g. "- text: \"What is your account number?\""). Award full points if utter_ask_account exists with valid structure; partial if present but empty or malformed; zero if missing.
```

**Rubric 4** — Points: **2**  
Copy and paste this into the criterion description:

```
Under "actions:" the student added "action_check_balance_simple" to the list (e.g. "- action_check_balance_simple"). Award full points if action_check_balance_simple appears in the actions section; zero if missing.
```

**Rubric 5** — Points: **2**  
Copy and paste this into the criterion description:

```
The domain file is valid YAML and existing Level 2 content (other responses, actions) is preserved. No required sections were removed. Award full points if file is valid and structure is intact; partial if minor issues; zero if file is invalid or critical content was deleted.
```

---

**Files tab**  
Configure the assessment so the LLM can read:

- `/home/codio/workspace/level3/domain/basics.yml`

---

### Option B: Standard Code Test (Python script)

Use a Python grader for faster feedback than the LLM rubric. The script parses `level3/domain/basics.yml` and checks: file exists and is valid YAML; `slots:` section present; `account` slot with `type: text`; `utter_ask_account` under `responses:` with at least one text message; `action_check_balance_simple` in the `actions:` list. Total: 10 points. On full score it prints `PASS` and `Successfully passed!` and exits 0; otherwise prints `FAIL` and exits 1.

**Grader script location (in repo):**

```
.guides/assessments/level3_graders/lab_3.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND:**  
     `python3 /home/codio/workspace/.guides/assessments/level3_graders/lab_3.1_grader.py`  
     If Codio runs without the project venv activated and PyYAML is missing, use:  
     `source /home/codio/workspace/.venv/bin/activate && python3 /home/codio/workspace/.guides/assessments/level3_graders/lab_3.1_grader.py`
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** (or equivalent tab):
   - **Expected output / Match:** `PASS` or `Successfully passed!` (Codio may allow either; the script prints both on success).
   - **Points:** 10 (or match your course scale).
4. **Rationale (optional):** e.g. *The grader checks that `level3/domain/basics.yml` exists, is valid YAML, and contains the slots section with account (type text), utter_ask_account under responses, and action_check_balance_simple in the actions list.*

**Files.** The script lives in the repo at `.guides/assessments/level3_graders/lab_3.1_grader.py`. Do not upload or paste it into the assessment; the Execution command runs this file from the workspace so `git pull` keeps the grader in sync. The script requires Python 3 and PyYAML (available in the project `.venv`); if students run in a minimal environment, ensure the project venv is activated before the command (see COMMAND above).
