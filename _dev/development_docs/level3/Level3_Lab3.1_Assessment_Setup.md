# Lab 3.1: Defining a Slot in the Domain - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 3: Defining Slots in the Domain.

**Task.** In `domain/basics.yml` in the `level3` folder, add the `slots:` section with `account` (type text), the `utter_ask_account` response, and register `action_check_balance_simple` in the `actions:` list together with `action_bank_hours` and `action_holiday_hours`. Run the assessment when done.

**Codio guide (Level 3).** The Lab 3.1 page in the Level 3 guide includes: `{Check It!|assessment}(code-output-compare-3187585640)`. Assessment JSON: `.guides/assessments/code-output-compare-3187585640.json`.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has added the `slots:` section with an `account` slot, the `utter_ask_account` response, and all three actions — `action_bank_hours`, `action_holiday_hours`, and `action_check_balance_simple` — in `level3/domain/basics.yml`.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Bash script).

---

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 3.1 section in the Codio Guide Editor (Level 3).

2. **Add LLM Rubric Assessment.** Add assessment, then **LLM Rubric** / **Autograde**.

3. **Configure** (see **Grading** tab below).

4. **Test.** Run with a complete domain (slots, utter_ask_account, all three actions including preloaded bank/holiday) for pass; with any of these missing for fail with feedback.

---

#### LLM Rubric Autograde – Grading tab (exact settings and copy-paste rubric)

| Option | Set to |
|--------|--------|
| **Total Points** | **10** |
| **Instructor Provided Solution File** | `.guides/secure/level3_graders/lab_3.1_solution_reference.md` (or `/home/codio/workspace/.guides/secure/level3_graders/lab_3.1_solution_reference.md` if Codio requires absolute path) |
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
Under "actions:" the list includes "action_bank_hours", "action_holiday_hours", and "action_check_balance_simple". Award full points if all three are present; zero if any is missing.
```

**Rubric 5** — Points: **2**  
Copy and paste this into the criterion description:

```
The domain file is valid YAML. Level 1 responses and the three expected action names are present. Award full points if the file is valid and complete; partial if minor issues; zero if the file is invalid or required entries are missing.
```

---

**Files tab**  
Configure the assessment so the LLM can read:

- `/home/codio/workspace/level3/domain/basics.yml`

---

### Option B: Standard Code Test (Python script)

Use a Python grader for faster feedback than the LLM rubric. The script matches the **Level 2 Lab 6.2** template (`code-output-compare-1597644299` + `lab_4.1_grader.sh` style): **Check 1–8** (1-based), **leading space** on pass lines (` Check N: PASSED - …`), no checkmark emoji on pass lines; **❌** / **⚠️** on fail/partial; **`==========================================`** score band; optional **Summary:** line. Same **Codio sequence** pattern as Lab 6.2: eight entries **`Check 1: PASSED`** … **`Check 8: PASSED`** with **`showFeedback`: false**.

| Check | What it verifies | Points |
|-------|------------------|--------|
| 1 | Domain file `level3/domain/basics.yml` exists | 1 |
| 2 | Valid YAML; root is a mapping (must pass; no points) | — |
| 3 | Top-level `slots:` section | 2 |
| 4 | `account` slot with `type: text` (partial if wrong type) | 2 |
| 5 | `utter_ask_account` with at least one `text:` (partial if empty) | 2 |
| 6 | `action_check_balance_simple` in `actions:` | 1 |
| 7 | `action_bank_hours` in `actions:` | 1 |
| 8 | `action_holiday_hours` in `actions:` | 1 |

**Total: 10 points.** On **10/10** it prints **` PASS: Lab 3.1 verification complete! Score: 10/10`** and exits **0**; otherwise **`❌ FAIL: Score …`** and exit **1**.

**Grader script location (in repo):**

```
.guides/secure/level3_graders/lab_3.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** Use the project venv’s Python so PyYAML is available without relying on pre-exec or shell activation:  
     `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level3_graders/lab_3.1_grader.py`  
     Leave **Pre-Exec** empty when using this.  
     **Alternative:** If your Codio image already has PyYAML for `python3`, you can use:  
     `python3 /home/codio/workspace/.guides/secure/level3_graders/lab_3.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in COMMAND above. Codio often runs pre-exec and COMMAND in separate shells, so activating the venv in pre-exec may not make PyYAML available to the grader. Using the venv’s interpreter path in COMMAND avoids that.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **10** (or match your course scale). Enable **Allow partial points** if you want partial credit for partial checks.
   - **Sequence / test cases:** The repo JSON uses **eight** substring matches, same layout as **Level 2 Lab 6.2** (`code-output-compare-1597644299`): `Check 1: PASSED` through `Check 8: PASSED`, each with **`showFeedback`: false**. Re-import from the repo if your Codio assessment still has a single `PASS` or old `Check 0–7` list.
   - **SHOW RATIONALE TO STUDENT:** Choose when students see the explanation. Recommended: **AFTER [1] ATTEMPTS** so they see the rationale after their first run (or **ALWAYS** if you want it visible immediately). Set the number in the box to 1 if using "AFTER … ATTEMPTS".
   - **RATIONALE** (the text box below): Paste or type a short explanation so students know what was checked. Example:
     > Same pattern as **Lab 6.2 (Level 2)**: **Check 1**–**Check 8** each appear as **PASSED** or **FAILED** in the script and as separate lines in Codio when the sequence is configured. **Check 2** must pass (valid YAML). Full credit: **` PASS: Lab 3.1 verification complete! Score: 10/10`**.
   - **SHOW EXPECTED ANSWER:** Optional; set to **Always** to match Lab 6.2, or **When grades are released**.

**Files.** The script lives in the repo at `.guides/secure/level3_graders/lab_3.1_grader.py`. Do not upload or paste it into the assessment; the Execution command runs this file from the workspace so `git pull` keeps the grader in sync. The script requires Python 3 and PyYAML. Use the venv’s Python in COMMAND (e.g. `/home/codio/workspace/.venv/bin/python3 …`) so the grader runs with PyYAML without depending on pre-exec or shell activation.
