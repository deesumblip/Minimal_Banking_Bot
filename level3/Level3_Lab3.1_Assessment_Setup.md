# Lab 3.1: Defining a Slot in the Domain - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 3: Defining Slots in the Domain.

**Task**: Add `slots:` with `account` (type: text) and `utter_ask_account` response to `domain/basics.yml` in the `level3` folder. Run the assessment when done.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has added the `slots:` section with an `account` slot and the `utter_ask_account` response to `level3/domain/basics.yml`.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Bash script).

---

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 3.1 section in the Codio Guide Editor (Level 3).

2. **Add LLM Rubric Assessment** – Add assessment → **LLM Rubric** / **Autograde**.

3. **Configure** (see **Grading** tab below).

4. **Test**: Run with a complete domain (pass), with slots missing (fail with feedback), with utter_ask_account missing (fail with feedback).

---

#### LLM Rubric Autograde – Grading tab (exact settings and copy-paste rubric)

| Option | Set to |
|--------|--------|
| **Total Points** | **8** |
| **Instructor Provided Solution File** | `.guides/assessments/level3_graders/lab_3.1_solution_reference.md` (or `/home/codio/workspace/.guides/assessments/level3_graders/lab_3.1_solution_reference.md` if Codio requires absolute path) |
| **Defined Number of Attempts** | **Off** (leave toggle off) |
| **Show Rationale to Student** | **After [1] attempts** (select that radio, leave the number as 1) |

---

**Add Rubric** – Click **ADD RUBRIC** and add the following four criteria. For each criterion, paste the text below into the rubric description field and set the points as indicated. Enable **partial credit** for the assessment.

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
The domain file is valid YAML and existing Level 2 content (other responses, actions) is preserved. No required sections were removed. Award full points if file is valid and structure is intact; partial if minor issues; zero if file is invalid or critical content was deleted.
```

---

**Files tab**  
Configure the assessment so the LLM can read:

- `/home/codio/workspace/level3/domain/basics.yml`

---

### Option B: Standard Code Test (Bash script)

**Grader script location**:
```
.guides/assessments/level3_graders/lab_3.1_grader.sh
```

**Grader script** – Run from **workspace root**: activate venv, then `cd level3`. Check: `domain/basics.yml` exists; file contains `slots:` section; `account` slot present (type: text); `utter_ask_account` present under responses. Print `PASS` / `Successfully passed!` on full score; `FAIL` and exit 1 on failure. Suggested points: 6–8 total.

**Codio configuration** – Add Code Test → Standard Code Test.

- COMMAND: `bash /home/codio/workspace/.guides/assessments/level3_graders/lab_3.1_grader.sh`
- Working Directory: `/home/codio/workspace`
- Expected output: `PASS` or `Successfully passed!`
