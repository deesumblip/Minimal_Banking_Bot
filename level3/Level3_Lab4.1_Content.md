Your goal is to **complete** the action file that reads the `account` slot and handles placeholder values. The domain already lists `action_check_balance_simple` from Lab 3.1; here you fill in the blanks so the Python file is correct.

---

## Fill-in-the-blanks exercise

1. **Create** the file `level3/actions/action_check_balance_simple.py` in your project.

2. **Copy the script below** into that file. The script has **eleven blanks** marked `(1)` through `(11)`.

3. **Replace each blank** with the correct code from the **Key** at the bottom of this section. Each blank is a single expression or value (one line). The blanks reinforce concepts from Level 1 (domain, responses), Level 2 (actions, `run`/`name`, dispatcher), and Level 3 (slots, placeholders).

4. **Save** the file, then **run the assessment**. The grader checks that the file exists, has the right structure, reads the slot, handles placeholders, and sends the balance message.

---

### Script (copy this into `level3/actions/action_check_balance_simple.py` and fill in the blanks)

```python
from typing import (5)

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalanceSimple((6)):
    """A custom action that reads a slot and returns a balance.

    - Reads the 'account' slot from conversation memory
    - Re-prompts if the slot contains a placeholder (e.g. "account number", "<missing>")
    - Otherwise sends a demo balance message
    """

    def name(self) -> Text:
        return (7)

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> (8):
        # Read the '(11)' slot from conversation memory (or "<missing>" if empty)
        account = (1)

        # Values that are not real account numbers—we re-ask if the slot has one of these
        placeholder_values = ["account number", "user_account_number", (9)]

        # If the slot is a placeholder, re-prompt and return
        if (2):
            dispatcher.utter_message(response=(3))
            return (10)

        # Otherwise send the demo balance message
        dispatcher.utter_message(text=(4))
        return (10)
```

---

### Key (what to put in each blank)

| Blank | Replace with | Concept (Level) |
|-------|------------------|------------------|
| **(1)** | `tracker.get_slot("account") or "<missing>"` | Reading a slot; default when empty (L3) |
| **(2)** | `account.lower() in [p.lower() for p in placeholder_values]` | Placeholder check (L3) |
| **(3)** | `"utter_ask_account"` | Response name from domain (L1/L3) |
| **(4)** | `f"(Demo) Balance for account {account} is $123.45."` | Sending a message (L2) |
| **(5)** | `Any, Dict, List, Text` | Typing imports for action signatures (L2) |
| **(6)** | `Action` | Base class for custom actions (L2) |
| **(7)** | `"action_check_balance_simple"` | Action name; must match domain `actions:` (L2) |
| **(8)** | `List[Dict[Text, Any]]` | Return type of `run()` — list of events (L2) |
| **(9)** | `"<missing>"` | Placeholder value when slot is empty (L3) |
| **(10)** | `[]` | `run()` must return a list (empty = no extra events) (L2) |
| **(11)** | `"account"` | Slot name; must match domain `slots:` and flow (L3) |

---

### After you finish

- **Verify** your domain (from Lab 3.1) lists `action_check_balance_simple` in the `actions:` section.
- **Run the assessment** when you're done.
- **Optional.** After Lab 6.1, train and run Inspector. Trigger the check_balance flow and watch the action use the slot and re-ask when the LLM extracts a placeholder.
