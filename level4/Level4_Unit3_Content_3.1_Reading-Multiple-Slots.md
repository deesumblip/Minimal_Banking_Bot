**Starting point:** Work in **`level4/`** (starter agent in **Unit 0.1**; pipeline in **Unit 0.2**).

In `action_check_balance_simple` you read one slot with `tracker.get_slot("account")`. In **`action_process_transfer`** you will read **three** slots.

## Reading Multiple Slots in the Action

Inside `run()` you read each slot the same way. For **`recipient`**, the course solution also **caps free text at 100 characters** (aligned with Lab 4.1’s flow `description:`), so the stored value matches the confirmation:

```python
amount = tracker.get_slot("amount") or ""
recipient = (tracker.get_slot("recipient") or "")[:100]
account_from = tracker.get_slot("account_from") or ""
```

The flow collects these before the action runs (or values may be empty / placeholder-like). Your action can:

- Treat placeholders case-insensitively and re-prompt with one message, then `return []`.
- Otherwise send a demo confirmation (e.g. starting with `(Demo) Transfer of $…`) and `return []`.

## Example: Complete action class

Below is the **reference** implementation. Create your file in **Lab 3.1** (fill-in-the-blanks, then paste into `level4/actions/action_process_transfer.py`).

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransfer(Action):
    """A custom action that processes a money transfer using multiple slots."""

    def name(self) -> Text:
        return "action_process_transfer"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        amount = tracker.get_slot("amount") or ""
        recipient = (tracker.get_slot("recipient") or "")[:100]
        account_from = tracker.get_slot("account_from") or ""

        placeholder_values = ["amount", "recipient", "account number", "user_account_number", ""]
        if (
            amount.lower() in [p.lower() for p in placeholder_values]
            or recipient.lower() in [p.lower() for p in placeholder_values]
            or account_from.lower() in [p.lower() for p in placeholder_values]
        ):
            dispatcher.utter_message(
                text="I need the actual amount, recipient, and source account. Please provide real values."
            )
            return []

        dispatcher.utter_message(
            text=(
                f"(Demo) Transfer of ${amount} from account {account_from} to {recipient} "
                "has been processed successfully."
            )
        )
        return []
```

In **Lab 3.1** you will create this action, then run the assessments.
