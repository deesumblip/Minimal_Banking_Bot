# Unit 1: Introduction to Actions

### 1.3 The Action Class Structure

Every action is a Python class that inherits from `Action`. Here's the basic structure:

```python
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBankHours(Action):
    def name(self) -> Text:
        return "action_bank_hours"
    
    def run(self, dispatcher, tracker, domain):
        # Your custom code here
        dispatcher.utter_message("Your message here")
        return []
```

**Required Methods**:
1. **`name()`** - Returns the action name (must match what's in domain)
2. **`run()`** - Contains your custom logic

**Note**: In Unit 2 you'll see the full `action_bank_hours`—it uses `datetime` to return different messages for weekdays, Saturday, and Sunday. That's why it's an action, not a simple `utter_*` response.

---
