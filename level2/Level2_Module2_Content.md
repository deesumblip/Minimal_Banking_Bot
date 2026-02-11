# Module 2: Understanding the Action Class

### 2.1 The Action Class Deep Dive

Let's examine the actual `action_bank_hours.py` file to understand how actions work.

**Why an action (not an utter)?** This action returns a *different* message depending on the current day—Saturday, Sunday, or weekday. That requires Python logic and `datetime`. A simple `utter_*` response can't change based on when the user asks, so we need an action.

#### Complete Action File

```python
from datetime import datetime
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A custom action that returns bank hours based on the current day.
    
    Uses datetime to tailor the message—this can't be done with a simple
    utter response because the message changes depending on when the user asks.
    """

    def name(self) -> Text:
        """Return the name of this action.
        
        This name must match what you put in domain/basics.yml
        under the 'actions:' list.
        """
        return "action_bank_hours"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """Execute the action.
        
        Returns different messages based on the current day of the week.
        """
        weekday = datetime.now().weekday()  # 0=Monday, 5=Saturday, 6=Sunday

        if weekday == 6:  # Sunday
            message = "Today is Sunday—we're closed."
        elif weekday == 5:  # Saturday
            message = "Today is Saturday—we're open 10am-2pm."
        else:  # Monday–Friday
            message = (
                "Our bank hours are Monday-Friday 9am-5pm, "
                "Saturday 10am-2pm. We're closed on Sundays."
            )

        dispatcher.utter_message(text=message)
        return []
```

#### Breaking Down Each Component

1. **Imports**:
   ```python
   from datetime import datetime
   from rasa_sdk import Action, Tracker
   from rasa_sdk.executor import CollectingDispatcher
   ```
   - `datetime` - Used to get the current day of the week
   - `Action` - Base class all actions inherit from
   - `Tracker` - Contains conversation history and slots (we'll use this in Level 3)
   - `CollectingDispatcher` - Used to send messages to the user

2. **Class Definition**:
   ```python
   class ActionBankHours(Action):
   ```
   - Must inherit from `Action`
   - Class name should be descriptive (convention: `Action` + descriptive name)

3. **`name()` Method**:
   ```python
   def name(self) -> Text:
       return "action_bank_hours"
   ```
   - Returns the action identifier
   - **Must match** what you register in `domain/basics.yml`
   - Convention: starts with `action_`

4. **`run()` Method**:
   ```python
   def run(self, dispatcher, tracker, domain):
   ```
   - **`dispatcher`**: Use this to send messages to the user
   - **`tracker`**: Access conversation history and slots (Level 3+)
   - **`domain`**: Access domain configuration (rarely needed)
   - **Returns**: List of events (usually empty `[]` for simple actions)

5. **Sending Messages**:
   ```python
   dispatcher.utter_message(text="Your message here")
   ```
   - This is how you send text to the user
   - Can also use `dispatcher.utter_message(response="utter_xyz")` to use a response

---

### 2.2 Understanding the Parameters

#### Dispatcher

The `dispatcher` is your way to communicate with the user:

```python
# Send a simple text message
dispatcher.utter_message(text="Hello!")

# Use a response from the domain
dispatcher.utter_message(response="utter_greet")

# Send multiple messages
dispatcher.utter_message(text="First message")
dispatcher.utter_message(text="Second message")
```

#### Tracker

The `tracker` contains conversation information (we'll use this more in Level 3):

```python
# Get conversation history (Level 3+)
events = tracker.events

# Get slots (Level 3+)
account = tracker.get_slot("account")
```

For Level 2, we don't use the tracker much - it's mainly for Level 3 when we add memory.

#### Domain

The `domain` contains your bot's configuration:

```python
# Access domain (rarely needed)
responses = domain.get("responses", {})
```

For Level 2, you typically don't need to access the domain directly.

---
