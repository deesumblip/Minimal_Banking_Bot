`action_check_balance_simple` is already registered in the domain from Lab 2.1. This lab creates the Python file that implements it.

Create `level3/actions/action_check_balance_simple.py`:

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalanceSimple(Action):
    """Reads the account slot and returns a demo balance."""

    def name(self) -> Text:
        return "action_check_balance_simple"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        account = tracker.get_slot("account")

        dispatcher.utter_message(
            text=f"The balance for account {account} is $123.45."
        )
        return []
```

## Verify

`actions/action_check_balance_simple.py` should contain:

- A class `ActionCheckBalanceSimple` extending `Action`
- `name()` returning `"action_check_balance_simple"`
- `tracker.get_slot("account")` to read the slot
- `dispatcher.utter_message` sending a text response containing the account value
- `run()` returning `[]`

Use **Check It!** below to confirm.

{Check It!|assessment}(code-output-compare-2346557110)

---

