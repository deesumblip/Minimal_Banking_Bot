In this course, custom actions are written using the Rasa SDK. Each action is a Python class that inherits from `Action` and requires you to implement two methods:

| Method | Purpose |
|---|---|
| `name()` | Returns the action name. Must match the name registered in the domain. |
| `run()` | Contains your custom logic. Sends responses via `dispatcher.utter_message()`. |

```python
from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBankHours(Action):

    def name(self) -> Text:
        return "action_bank_hours"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Your custom logic here
        dispatcher.utter_message(text="Your message here")
        return []
```

In this level, you will implement the full `action_bank_hours` implementation. It uses `datetime` to return different messages for weekdays, Saturday, and Sunday. That is what makes it an action rather than a static `utter_*` response.