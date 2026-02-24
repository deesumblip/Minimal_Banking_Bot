Your goal is to **complete** the action file that reads the `account` slot and handles placeholder values. The domain already lists `action_check_balance_simple` from Lab 3.1; here you fill in the blanks so the Python file is correct.

---

## Fill-in-the-blanks exercise

1. **Create** the file `level3/actions/action_check_balance_simple.py` in your project.

2. **Copy the script below** into that file. The script has **eleven blanks** marked `(1)` through `(11)` **in order** as you read from top to bottom.

3. **Replace each blank** with the correct code from the **Key** at the bottom of this section. Each blank is a single expression or value (one line). The blanks reinforce concepts from Level 1 (domain, responses), Level 2 (actions, `run`/`name`, dispatcher), and Level 3 (slots, placeholders).

4. **Save** the file, then **run the assessment**. The grader checks that the file exists, has the right structure, reads the slot, handles placeholders, and sends the balance message.

---

### Script

Copy this into level3/actions/action_check_balance_simple.py and fill in the blanks.

**What goes in each blank (use the Key below to confirm):**

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

---

### Key (what to put in each blank)

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

---

### After you finish

- **Verify** your domain (from Lab 3.1) lists `action_check_balance_simple` in the `actions:` section.
- **Run the assessment** when you're done.
- **Optional.** After Lab 6.1, train and run Inspector. Trigger the check_balance flow and watch the action use the slot and re-ask when the LLM extracts a placeholder.
