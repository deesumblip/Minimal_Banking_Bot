In Level 3 you read one slot in `action_check_balance_simple` with `tracker.get_slot("account")`. In Level 4 you will read **three** slots in `action_process_transfer`.

## Reading Multiple Slots in the Action

Inside `run()` of your action you can read each slot the same way:

```python
amount = tracker.get_slot("amount") or ""
recipient = tracker.get_slot("recipient") or ""
account_from = tracker.get_slot("account_from") or ""
```

The flow will have collected these before the action runs (or the slots may be empty/placeholder if the LLM filled them with generic text). Your action can:

- Check that all three have real values (not empty or placeholder).
- If any are missing or placeholder, send one message asking for real values and `return []`.
- Otherwise, send a confirmation message that uses amount, account_from, and recipient (e.g. "Transfer of $X from account Y to Z processed.") and `return []`.

## Example: Complete action class

Below is an example of the full action file. You will create your own version in Lab 3.1 (using the fill-in-the-blanks exercise or writing it from scratch following this pattern).

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransfer(Action):
    """Reads amount, recipient, account_from; re-prompts if missing; else sends transfer confirmation."""

    def name(self) -> Text:
        return "action_process_transfer"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        amount = tracker.get_slot("amount") or ""
        recipient = tracker.get_slot("recipient") or ""
        account_from = tracker.get_slot("account_from") or ""

        placeholder_values = ["amount", "recipient", "account number", "user_account_number", ""]
        if amount in placeholder_values or recipient in placeholder_values or account_from in placeholder_values:
            dispatcher.utter_message(text="Please provide a real amount, recipient, and source account.")
            return []

        dispatcher.utter_message(
            text=f"Transfer of ${amount} from account {account_from} to {recipient} processed."
        )
        return []
```

In **Lab 3.1** you will create your own version of this action in `level4/actions/action_process_transfer.py` (you can use the fill-in-the-blanks script in the lab), then **in Codio** use **Check It!** for that lab.
