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

**Hints:** (1) typing names for action signatures; (2) base class for custom actions; (3) action name string matching the domain; (4) return type of `run()`; (5)–(7) read each slot from the tracker (use `or ""` if empty); (8) condition that is true when any slot is missing or is a placeholder; (9) message asking for real values; (10) and (12) empty list of events; (11) confirmation message including amount, account_from, and recipient.
