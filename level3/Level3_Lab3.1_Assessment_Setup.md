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
   - **COMMAND (recommended):** Use the project venv’s Python so PyYAML is available without relying on pre-exec or shell activation:  
     `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/assessments/level3_graders/lab_3.1_grader.py`  
     Leave **Pre-Exec** empty when using this.  
     **Alternative:** If your Codio image already has PyYAML for `python3`, you can use:  
     `python3 /home/codio/workspace/.guides/assessments/level3_graders/lab_3.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in COMMAND above. Codio often runs pre-exec and COMMAND in separate shells, so activating the venv in pre-exec may not make PyYAML available to the grader. Using the venv’s interpreter path in COMMAND avoids that.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **10** (or match your course scale). Enable **Allow partial points** if you want partial credit for partial checks.
   - **Add item to check / Test case:** Add one test case. Leave **INPUT - ARGUMENTS** and **INPUT - STDIN** empty. In **EXPECTED OUTPUT**, enter: `PASS` (the script prints this on success). You can optionally also match `Successfully passed!` if Codio allows multiple expected strings; one match is enough.
   - **SHOW RATIONALE TO STUDENT:** Choose when students see the explanation. Recommended: **AFTER [1] ATTEMPTS** so they see the rationale after their first run (or **ALWAYS** if you want it visible immediately). Set the number in the box to 1 if using "AFTER … ATTEMPTS".
   - **RATIONALE** (the text box below): Paste or type a short explanation so students know what was checked. Example:
     > The grader checks that `level3/domain/basics.yml` exists, is valid YAML, and contains: a **slots:** section, an **account** slot with **type: text**, the **utter_ask_account** response under **responses:** with at least one message, and **action_check_balance_simple** in the **actions:** list. Review the script output for which check failed and fix that part of the domain file.
   - **SHOW EXPECTED ANSWER:** Optional; set to **When grades are released** or **Always** if you want students to see that the expected output is `PASS`.

**Files.** The script lives in the repo at `.guides/assessments/level3_graders/lab_3.1_grader.py`. Do not upload or paste it into the assessment; the Execution command runs this file from the workspace so `git pull` keeps the grader in sync. The script requires Python 3 and PyYAML. Use the venv’s Python in COMMAND (e.g. `/home/codio/workspace/.venv/bin/python3 …`) so the grader runs with PyYAML without depending on pre-exec or shell activation.
