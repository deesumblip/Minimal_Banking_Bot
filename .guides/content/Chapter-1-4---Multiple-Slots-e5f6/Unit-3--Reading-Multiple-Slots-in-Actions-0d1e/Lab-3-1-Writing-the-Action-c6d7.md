Your goal is to **complete** the action file that reads the `amount`, `recipient`, and `account_from` slots and sends a transfer confirmation. The domain already lists `action_process_transfer` from Lab 2.1. First complete the script in the fill-in-the-blanks exercise below; then put the complete script in the file tree and run the assessment.

---

## Fill-in-the-blanks exercise

1. **Complete the script below.** Fill in the twelve blanks marked `(1)` through `(12)` in order. Each blank is a single expression or value (one line). The blanks reinforce: typing imports, the Action base class, the action name, return type, reading three slots, placeholder/missing check, and sending the confirmation message.

2. **Reproduce the complete script in the file tree.** Create or open `level4/actions/action_process_transfer.py` and paste your completed script (with all blanks filled in) into that file. Save the file.

3. **Run the final assessment.** The grader checks that the file exists, has the right structure, reads all three slots, and sends the transfer confirmation message.

---

### After you finish

- **Verify** your domain (from Lab 2.1) lists `action_process_transfer` in the `actions:` section.
- **Run the assessment** when you're done.
- **Optional.** After Lab 5.1, train and run Inspector. Trigger the transfer flow and provide amount, recipient, and source account; watch the action send the confirmation.

---

### Script template (fill in blanks (1)–(12))

**What goes in each blank:**

- **(1)** — The typing names needed for action signatures: `Any`, `Dict`, `List`, and `Text`.
- **(2)** — The base class that every custom action must inherit from (from `rasa_sdk`).
- **(3)** — The action name string that must match the domain `actions:` list and the transfer_money flow.
- **(4)** — The return type of `run()`: a list of dictionaries (events).
- **(5)** — Expression that reads the `amount` slot from the tracker (with optional default).
- **(6)** — Expression that reads the `recipient` slot from the tracker.
- **(7)** — Expression that reads the `account_from` slot from the tracker.
- **(8)** — Condition: true when any of the three slot values is missing or is a placeholder (e.g. empty string or in placeholder list).
- **(9)** — The text to send when information is missing or placeholder (e.g. ask for real values).
- **(10)** — The value that `run()` must return in both branches (an empty list of events).
- **(11)** — The text for the demo transfer confirmation; include `amount`, `account_from`, and `recipient` so the user sees the transfer summary.
- **(12)** — Same as (10): return value for the success branch.

```python
from typing import (1)

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransfer((2)):
    """A custom action that processes a transfer using amount, recipient, and account_from slots.

    - Reads the amount, recipient, and account_from slots from conversation memory
    - Re-prompts if any slot is missing or contains a placeholder
    - Otherwise sends a demo transfer confirmation
    """

    def name(self) -> Text:
        return (3)

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> (4):
        # Read the three slots (or empty string if not set)
        amount = (5)
        recipient = (6)
        account_from = (7)

        # Values that are not real—we re-ask if any slot has one of these
        placeholder_values = ["amount", "recipient", "account number", "user_account_number", ""]
        if (8):
            dispatcher.utter_message(text=(9))
            return (10)

        # Otherwise send the demo transfer confirmation
        dispatcher.utter_message(text=(11))
        return (12)
```
