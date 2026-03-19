# Lab 4.1: Writing the Action That Uses the Slot - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 4 (Reading Slots in Actions), after 4.1 and 4.2.

**Task.** Create `level3/actions/action_check_balance_simple.py`: a custom action that reads the `account` slot, treats placeholder values (e.g. "account number", "<missing>") as invalid and re-prompts with `utter_ask_account`, and otherwise sends a demo balance message. The domain already lists `action_check_balance_simple` from Lab 3.1. Students complete the **Fill in the blanks** assessment first (same script they paste into the file), then run the **Code Test**.

**Codio guide (Chapter 1.3).** The Lab 4.1 page includes:

- `{Check It!|assessment}(fill-in-the-blanks-2346557111)` — Fill in the blanks (5 pts). JSON: `.guides/assessments/fill-in-the-blanks-2346557111.json`.
- `{Check It!|assessment}(code-output-compare-2346557110)` — Code Output Compare (10 pts). JSON: `.guides/assessments/code-output-compare-2346557110.json`. Grader: `.guides/secure/level3_graders/lab_4.1_grader.py`.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has created `level3/actions/action_check_balance_simple.py` with: correct imports (Action, Tracker, CollectingDispatcher); class `ActionCheckBalanceSimple(Action)`; `name()` returning `"action_check_balance_simple"`; `run()` that reads the `account` slot, detects placeholder values, re-prompts with `utter_ask_account` when appropriate, and sends a balance message otherwise.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Python script).

---

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 4.1 section in the Codio Guide Editor (Level 3).

2. **Add LLM Rubric Assessment** – Add assessment → **LLM Rubric** / **Autograde**.

3. **Configure** – Use the **Instructor Provided Solution File**: `.guides/secure/level3_graders/lab_4.1_solution_reference.md` (or `/home/codio/workspace/.guides/secure/level3_graders/lab_4.1_solution_reference.md`). Define rubric criteria for: file location and name; imports; class and `name()`; `run()` reading slot; placeholder list and re-prompt with `utter_ask_account`; balance message; returning `[]`. Suggested total points: 8–10. **Show Rationale to Student:** After 1 attempt (or Always).

4. **Files tab** – Ensure the LLM can read: `/home/codio/workspace/level3/actions/action_check_balance_simple.py`

5. **Test** – Run with a complete action file (pass); with missing placeholder check or re-prompt (fail with feedback).

---

### Option B: Standard Code Test (Python script)

Use a Python grader for faster feedback. The script checks `level3/actions/action_check_balance_simple.py` for: file exists; required imports (Action, Tracker, CollectingDispatcher); class `ActionCheckBalanceSimple(Action)`; `name()` returning `"action_check_balance_simple"`; `run()` reading `tracker.get_slot("account")`; placeholder handling and `utter_ask_account` re-prompt; balance message. Total: 10 points. On full score it prints `PASS` and `Successfully passed!`; otherwise `FAIL` and exit 1. Checks are flexible (e.g. variable names and placeholder list contents can vary).

**Grader script location (in repo):**

```
.guides/secure/level3_graders/lab_4.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** Use the project venv’s Python so the environment is consistent:  
     `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level3_graders/lab_4.1_grader.py`  
     **Alternative:** `python3 /home/codio/workspace/.guides/secure/level3_graders/lab_4.1_grader.py` (no extra deps; script only reads the action file).
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in COMMAND.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **10**. Enable **Allow partial points** if you want partial credit for partial checks.
   - **Add item to check / Test case:** One test case. Leave **INPUT - ARGUMENTS** and **INPUT - STDIN** empty. **EXPECTED OUTPUT:** `PASS`. **Enable substring match** so Codio passes when `PASS` appears in the output (the script prints detailed check lines before `PASS`).
   - **SHOW RATIONALE TO STUDENT:** Recommended **AFTER [1] ATTEMPTS** (or **ALWAYS**). Set the number to 1 if using "AFTER … ATTEMPTS".
   - **RATIONALE** (text box): Example:
     > The grader checks that `level3/actions/action_check_balance_simple.py` exists and contains: correct imports, class **ActionCheckBalanceSimple(Action)**, **name()** returning **"action_check_balance_simple"**, **run()** reading the account slot, a placeholder check, re-prompt with **utter_ask_account** when the slot is a placeholder, and a balance message otherwise. Follow the lab steps and review the script output for which check failed.
   - **SHOW EXPECTED ANSWER:** Optional; **When grades are released** or **Always**.
4. **Files.** The script lives in the repo at `.guides/secure/level3_graders/lab_4.1_grader.py`. Do not upload it; run it from the workspace so `git pull` keeps the grader in sync. The script only reads the action file (no PyYAML); venv Python is optional but recommended for consistency.

---

## Reference for rubric / grading

- **Solution reference:** `.guides/secure/level3_graders/lab_4.1_solution_reference.md` (full reference code and rubric summary).

### Fill-in-the-blanks assessment (implementers)

Students complete blanks in **`.guides/assessments/fill-in-the-blanks-2346557111.json`** (taskId `fill-in-the-blanks-2346557111`). The token order in that file is the source of truth. Summary:

| Order | Correct blank | Concept |
|-------|----------------|---------|
| 1 | `Any, Dict, List, Text` | Typing for `run()` signature (L2) |
| 2 | `CollectingDispatcher` | Import from `rasa_sdk.executor` (L2) |
| 3 | `ActionCheckBalanceSimple` | Custom class name (L2) |
| 4 | `Action` | Base class (L2) |
| 5 | `action_check_balance_simple` | `name()` string; domain `actions:` (L2/L3) |
| 6 | `List[Dict[Text, Any]]` | Return type of `run()` (L2) |
| 7 | `get_slot` | Read slot from tracker (L3) |
| 8 | `"account"` | Slot name (L3) |
| 9 | `"<missing>"` | Default when slot empty (L3) |
| 10 | `"<missing>"` | Same token in `placeholder_values` (L3) |
| 11 | `account.lower() in [p.lower() for p in placeholder_values]` | Placeholder check (L3) |
| 12 | `utter_ask_account` | Domain `responses:` re-prompt (L1/L3) |
| 13 | `[]` | Return after re-prompt (L2) |
| 14 | `f"(Demo) Balance for account {account} is $123.45."` | Valid-slot branch; satisfies grader (L2) |
| 15 | `[]` | Return after balance message (L2) |

### Reference solution (copy-paste sanity check)

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalanceSimple(Action):
    """A custom action that reads a slot and returns a balance."""

    def name(self) -> Text:
        return "action_check_balance_simple"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        account = tracker.get_slot("account") or "<missing>"

        placeholder_values = ["account number", "user_account_number", "<missing>"]

        if account.lower() in [p.lower() for p in placeholder_values]:
            dispatcher.utter_message(response="utter_ask_account")
            return []

        dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")
        return []
```
