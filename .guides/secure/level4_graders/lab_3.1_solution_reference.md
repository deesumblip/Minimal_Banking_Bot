# Lab 4.2 – Reference solution for LLM Rubric Autograde

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 4.2 (Writing the Action That Uses Multiple Slots).

---

## Required file: level4/actions/action_process_transfer.py

The student creates this file. It must:

1. Import from `typing`: `Any`, `Dict`, `List`, `Text`; from `rasa_sdk`: `Action`, `Tracker`, `CollectingDispatcher`.
2. Define class `ActionProcessTransfer(Action)` with:
   - `name(self)` returning `"action_process_transfer"`.
   - `run(self, dispatcher, tracker, domain)` that:
     - Reads the three slots: `amount`, `recipient`, `account_from` (e.g. via `tracker.get_slot("amount")` etc., with optional default).
     - Optionally validates or checks for placeholders; if missing/invalid, may send a single message asking for real values and `return []`.
     - Otherwise sends a demo transfer confirmation message that includes amount, account_from, and recipient (e.g. "(Demo) Transfer of $X from account Y to Z has been processed successfully.") and `return []`.

---

## Reference code (full file)

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
        recipient = tracker.get_slot("recipient") or ""
        account_from = tracker.get_slot("account_from") or ""

        placeholder_values = ["amount", "recipient", "account number", "user_account_number", ""]
        if (amount.lower() in [p.lower() for p in placeholder_values] or
            recipient.lower() in [p.lower() for p in placeholder_values] or
            account_from.lower() in [p.lower() for p in placeholder_values]):
            dispatcher.utter_message(
                text="I need the actual amount, recipient, and source account. Please provide real values."
            )
            return []

        dispatcher.utter_message(
            text=f"(Demo) Transfer of ${amount} from account {account_from} to {recipient} has been processed successfully."
        )
        return []
```

---

## Rubric summary

- **File exists:** level4/actions/action_process_transfer.py.
- **Class and name():** ActionProcessTransfer(Action), name() returns "action_process_transfer".
- **Reads slots:** run() uses tracker.get_slot("amount"), get_slot("recipient"), get_slot("account_from") (or equivalent).
- **Message:** Sends a confirmation message that includes the three slot values (and optionally handles placeholders/missing values).
