# Lab 3.1: Writing the Action That Uses Multiple Slots - Assessment Setup

## Guide Content (For Students)

**Placement.** This lab follows Unit 4 (Reading Multiple Slots in Actions), Level 4.

**Task.** Create `level4/actions/action_process_transfer.py`: a custom action that reads the `amount`, `recipient`, and `account_from` slots, treats placeholder values as invalid (and optionally re-prompts or sends a single message), and otherwise sends a demo transfer confirmation. The domain already lists `action_process_transfer` from Lab 2.1. First complete the script in the fill-in-the-blanks exercise below; then put the complete script in the file tree and run the assessment.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has created `level4/actions/action_process_transfer.py` with: correct imports (Action, Tracker, CollectingDispatcher); class `ActionProcessTransfer(Action)`; `name()` returning `"action_process_transfer"`; `run()` that reads the three slots (`amount`, `recipient`, `account_from`), optionally validates or handles placeholders, and sends a confirmation message.

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Python script).

---

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 3.1 section in the Codio Guide Editor (Level 4 chapter).

2. **Add LLM Rubric Assessment** – Add assessment → **LLM Rubric** / **Autograde**.

3. **Configure** – Use the **Instructor Provided Solution File**: `.guides/assessments/level4_graders/lab_3.1_solution_reference.md`. Define rubric criteria for: file location and name; imports; class and `name()`; `run()` reading all three slots; confirmation message (and optional placeholder handling); returning `[]`. Suggested total points: 10. **Show Rationale to Student:** After 1 attempt (or Always).

4. **Files tab** – Ensure the LLM can read: `/home/codio/workspace/level4/actions/action_process_transfer.py`

5. **Test** – Run with a complete action file (pass); with missing slot reads or message (fail with feedback).

---

### Option B: Standard Code Test (Python script)

Use a Python grader for faster feedback. The script checks `level4/actions/action_process_transfer.py` for: file exists; required imports; class `ActionProcessTransfer(Action)`; `name()` returning `"action_process_transfer"`; `run()` reading `tracker.get_slot("amount")`, `get_slot("recipient")`, `get_slot("account_from")`; sending a message (dispatcher.utter_message). Total: 10 points. On full score it prints `PASS` and `Successfully passed!`; otherwise `FAIL` and exit 1.

**Grader script location (in repo):**

```
.guides/assessments/level4_graders/lab_3.1_grader.py
```

**Codio configuration (Standard Code Test):**

1. **Assessment** – Add assessment, then **Code Test** → **Standard Code Test**.
2. **Execution**:
   - **COMMAND (recommended):** `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/assessments/level4_graders/lab_3.1_grader.py`
   - **PRE-EXEC COMMAND:** Leave **empty**.
   - **Working Directory:** `/home/codio/workspace`
   - **Timeout:** `60` seconds
3. **Grading** tab:
   - **Points:** Set to **10**. Enable **Allow partial points** if desired.
   - **Test case:** One test case. **EXPECTED OUTPUT:** `PASS`. **Enable substring match**.
   - **SHOW RATIONALE TO STUDENT:** **AFTER [1] ATTEMPTS** (or **ALWAYS**).
   - **RATIONALE:** The grader checks that `level4/actions/action_process_transfer.py` exists and contains: correct imports, class **ActionProcessTransfer(Action)**, **name()** returning **"action_process_transfer"**, **run()** reading the **amount**, **recipient**, and **account_from** slots, and sending a confirmation message. Follow the lab steps and review the script output for which check failed.
4. **Files.** Script at `.guides/assessments/level4_graders/lab_3.1_grader.py`; run from workspace.

---

## Reference for rubric / grading

- **Solution reference:** `.guides/assessments/level4_graders/lab_3.1_solution_reference.md`

### Script template (implementers only)

Copy this into level4/actions/action_process_transfer.py; students fill in the blanks (1)–(12).

**What goes in each blank:**

- **(1)** — The typing names needed for action signatures: `Any`, `Dict`, `List`, and `Text`.
- **(2)** — The base class that every custom action must inherit from (from `rasa_sdk`).
- **(3)** — The action name string that must match the domain `actions:` list and the transfer_money flow.
- **(4)** — The return type of `run()`: a list of dictionaries (events).
- **(5)** — Expression that reads the `amount` slot from the tracker (with optional default).
- **(6)** — Expression that reads the `recipient` slot from the tracker.
- **(7)** — Expression that reads the `account_from` slot from the tracker.
- **(8)** — Condition: true when any of the three slot values is missing or is a placeholder (e.g. empty string or placeholder list).
- **(9)** — The text to send when information is missing or placeholder (e.g. ask for real values).
- **(10)** — The value that `run()` must return in both branches (an empty list of events).
- **(11)** — The text for the demo transfer confirmation; include `amount`, `account_from`, and `recipient` so the user sees the transfer summary.
- **(12)** — Same as (10): return value for the success branch.

```python
from typing import (1)

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransfer((2)):
    """A custom action that processes a transfer using amount, recipient, and account_from slots."""

    def name(self) -> Text:
        return (3)

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> (4):
        amount = (5)
        recipient = (6)
        account_from = (7)

        placeholder_values = ["amount", "recipient", "account number", "user_account_number", ""]
        if (8):
            dispatcher.utter_message(text=(9))
            return (10)

        dispatcher.utter_message(text=(11))
        return (12)
```

### Fill-in-the-blanks key (implementers only)

| Blank | Replace with | Concept |
|-------|------------------|--------|
| **(1)** | `Any, Dict, List, Text` | Typing imports for action signatures |
| **(2)** | `Action` | Base class for custom actions |
| **(3)** | `"action_process_transfer"` | Action name; must match domain and flow |
| **(4)** | `List[Dict[Text, Any]]` | Return type of `run()` |
| **(5)** | `tracker.get_slot("amount") or ""` | Reading the amount slot |
| **(6)** | `tracker.get_slot("recipient") or ""` | Reading the recipient slot |
| **(7)** | `tracker.get_slot("account_from") or ""` | Reading the account_from slot |
| **(8)** | `amount.lower() in [p.lower() for p in placeholder_values] or recipient.lower() in [p.lower() for p in placeholder_values] or account_from.lower() in [p.lower() for p in placeholder_values]` or a simpler check like `not amount or not recipient or not account_from` | Placeholder or missing check |
| **(9)** | `"I need the actual amount, recipient, and source account. Please provide real values."` | Message when values are missing/placeholder |
| **(10)** | `[]` | `run()` must return a list (empty = no extra events) |
| **(11)** | `f"(Demo) Transfer of ${amount} from account {account_from} to {recipient} has been processed successfully."` | Confirmation message with all three slots |
| **(12)** | `[]` | Same as (10) |
