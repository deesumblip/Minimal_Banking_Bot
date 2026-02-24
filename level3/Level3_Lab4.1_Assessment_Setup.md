# Lab 4.1: Writing the Action That Uses the Slot - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 4 (Reading Slots in Actions), after 4.1 and 4.2.

**Task.** Create `level3/actions/action_check_balance_simple.py`: a custom action that reads the `account` slot, treats placeholder values (e.g. "account number", "<missing>") as invalid and re-prompts with `utter_ask_account`, and otherwise sends a demo balance message. The domain already lists `action_check_balance_simple` from Lab 3.1. Run the assessment when done.

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

3. **Configure** – Use the **Instructor Provided Solution File**: `.guides/assessments/level3_graders/lab_4.1_solution_reference.md` (or `/home/codio/workspace/.guides/assessments/level3_graders/lab_4.1_solution_reference.md`). Define rubric criteria for: file location and name; imports; class and `name()`; `run()` reading slot; placeholder list and re-prompt with `utter_ask_account`; balance message; returning `[]`. Suggested total points: 8–10. **Show Rationale to Student:** After 1 attempt (or Always).

4. **Files tab** – Ensure the LLM can read: `/home/codio/workspace/level3/actions/action_check_balance_simple.py`

5. **Test** – Run with a complete action file (pass); with missing placeholder check or re-prompt (fail with feedback).

---

### Option B: Standard Code Test (Python script)

Use a Python grader for faster feedback. The script checks `level3/actions/action_check_balance_simple.py` for: file exists; required imports (Action, Tracker, CollectingDispatcher); class `ActionCheckBalanceSimple(Action)`; `name()` returning `"action_check_balance_simple"`; `run()` reading `tracker.get_slot("account")`; placeholder handling and `utter_ask_account` re-prompt; balance message. Total: 10 points. On full score it prints `PASS` and `Successfully passed!`; otherwise `FAIL` and exit 1. Checks are flexible (e.g. variable names and placeholder list contents can vary).

**Grader script location (in repo):**

```
.guides/assessments/level3_graders/lab_4.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** Use the project venv’s Python so the environment is consistent:  
     `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/assessments/level3_graders/lab_4.1_grader.py`  
     **Alternative:** `python3 /home/codio/workspace/.guides/assessments/level3_graders/lab_4.1_grader.py` (no extra deps; script only reads the action file).
   - **PRE-EXEC COMMAND:** Leave **empty** when using the venv Python path in COMMAND.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **10**. Enable **Allow partial points** if you want partial credit for partial checks.
   - **Add item to check / Test case:** One test case. Leave **INPUT - ARGUMENTS** and **INPUT - STDIN** empty. **EXPECTED OUTPUT:** `PASS`.
   - **SHOW RATIONALE TO STUDENT:** Recommended **AFTER [1] ATTEMPTS** (or **ALWAYS**). Set the number to 1 if using "AFTER … ATTEMPTS".
   - **RATIONALE** (text box): Example:
     > The grader checks that `level3/actions/action_check_balance_simple.py` exists and contains: correct imports, class **ActionCheckBalanceSimple(Action)**, **name()** returning **"action_check_balance_simple"**, **run()** reading the account slot, a placeholder check, re-prompt with **utter_ask_account** when the slot is a placeholder, and a balance message otherwise. Follow the lab steps and review the script output for which check failed.
   - **SHOW EXPECTED ANSWER:** Optional; **When grades are released** or **Always**.
4. **Files.** The script lives in the repo at `.guides/assessments/level3_graders/lab_4.1_grader.py`. Do not upload it; run it from the workspace so `git pull` keeps the grader in sync. The script only reads the action file (no PyYAML); venv Python is optional but recommended for consistency.

---

## Reference for rubric / grading

- **Solution reference:** `.guides/assessments/level3_graders/lab_4.1_solution_reference.md` (full reference code and rubric summary).

### Script template (implementers only)

Copy this into level3/actions/action_check_balance_simple.py; students fill in the blanks (1)–(11).

**What goes in each blank:**

- **(1)** — The typing names needed for action signatures: `Any`, `Dict`, `List`, and `Text`.
- **(2)** — The base class that every custom action must inherit from (from `rasa_sdk`).
- **(3)** — The action name string that must match the name used in the domain `actions:` list and in flows.
- **(4)** — The return type of `run()`: a list of dictionaries (events).
- **(5)** — The slot name that matches the domain `slots:` and the flow that collects it.
- **(6)** — Expression that reads the `account` slot from the tracker and uses a default string when the slot is empty.
- **(7)** — The placeholder string used when the slot is empty; also add it to the `placeholder_values` list.
- **(8)** — Condition: true when `account` (case-insensitive) is one of the placeholder values.
- **(9)** — The response name from the domain that asks the user for their account (must match a key under `responses:`).
- **(10)** — The value that `run()` must return in both branches (an empty list of events).
- **(11)** — The text to send for the balance message; include the `account` variable so the user sees their account.

```python
from typing import (1)

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalanceSimple((2)):
    """A custom action that reads a slot and returns a balance.

    - Reads the 'account' slot from conversation memory
    - Re-prompts if the slot contains a placeholder (e.g. "account number", "<missing>")
    - Otherwise sends a demo balance message
    """

    def name(self) -> Text:
        return (3)

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> (4):
        # Read the '(5)' slot from conversation memory (or "<missing>" if empty)
        account = (6)

        # Values that are not real account numbers—we re-ask if the slot has one of these
        placeholder_values = ["account number", "user_account_number", (7)]

        # If the slot is a placeholder, re-prompt and return
        if (8):
            dispatcher.utter_message(response=(9))
            return (10)

        # Otherwise send the demo balance message
        dispatcher.utter_message(text=(11))
        return (10)
```

### Fill-in-the-blanks key (implementers only)

| Blank | Replace with | Concept (Level) |
|-------|------------------|------------------|
| **(1)** | `Any, Dict, List, Text` | Typing imports for action signatures (L2) |
| **(2)** | `Action` | Base class for custom actions (L2) |
| **(3)** | `"action_check_balance_simple"` | Action name; must match domain `actions:` (L2) |
| **(4)** | `List[Dict[Text, Any]]` | Return type of `run()` — list of events (L2) |
| **(5)** | `"account"` | Slot name; must match domain `slots:` and flow (L3) |
| **(6)** | `tracker.get_slot("account") or "<missing>"` | Reading a slot; default when empty (L3) |
| **(7)** | `"<missing>"` | Placeholder value when slot is empty (L3) |
| **(8)** | `account.lower() in [p.lower() for p in placeholder_values]` | Placeholder check (L3) |
| **(9)** | `"utter_ask_account"` | Response name from domain (L1/L3) |
| **(10)** | `[]` | `run()` must return a list (empty = no extra events) (L2) |
| **(11)** | `f"(Demo) Balance for account {account} is $123.45."` | Sending a message (L2) |
