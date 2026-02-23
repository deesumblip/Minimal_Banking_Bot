# Lab 4.1 – Reference solution for graders (action file)

Use this file as the **Instructor Provided Solution** for Lab 4.1 (Writing the Action That Uses the Slot) if you add an LLM Rubric or script to grade the action file. Lab 4.1 is currently ungraded; this reference is for instructors and future autograding.

---

## Required file: `level3/actions/action_check_balance_simple.py`

The student creates this file. It must:

1. Import from `typing`: `Any`, `Dict`, `List`, `Text`; from `rasa_sdk`: `Action`, `Tracker`, `CollectingDispatcher`.
2. Define class `ActionCheckBalanceSimple(Action)` with:
   - `name(self)` returning `"action_check_balance_simple"`.
   - `run(self, dispatcher, tracker, domain)` that:
     - Reads the slot: `account = tracker.get_slot("account") or "<missing>"`.
     - Uses a placeholder list (e.g. `["account number", "user_account_number", "<missing>"]`).
     - If `account` (lowercased) is in that list: call `dispatcher.utter_message(response="utter_ask_account")` and `return []`.
     - Otherwise: call `dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")` and `return []`.

---

## Reference code (full file)

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalanceSimple(Action):
    """A custom action that reads a slot and returns a balance.
    
    This demonstrates:
    - How to read slots (conversation memory) from the tracker
    - How to handle placeholder values that the LLM might extract incorrectly
    - How to re-prompt the user if needed
    """

    def name(self) -> Text:
        return "action_check_balance_simple"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Read the 'account' slot from conversation memory
        account = tracker.get_slot("account") or "<missing>"
        
        # Check if the account is a placeholder value
        placeholder_values = ["account number", "user_account_number", "<missing>"]
        if account.lower() in [p.lower() for p in placeholder_values]:
            dispatcher.utter_message(response="utter_ask_account")
            return []
        
        dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")
        return []
```

---

## Rubric summary (if grading is added)

- **File exists:** `level3/actions/action_check_balance_simple.py`.
- **Reads slot:** Uses `tracker.get_slot("account")` (or equivalent).
- **Placeholder check:** Has a list of placeholder strings and checks the slot value against it.
- **Re-prompt:** When placeholder: calls `dispatcher.utter_message(response="utter_ask_account")` and returns.
- **Balance message:** Otherwise sends a message containing the account value (e.g. demo balance).
