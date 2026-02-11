# Module 2: Understanding the Action Class

### 2.1 The Action Class Deep Dive

Let's examine the actual `action_bank_hours.py` file to understand how actions work.

#### Complete Action File

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A simple custom action that returns bank hours.
    
    This action doesn't use any slots (memory) - it just returns
    a hardcoded message. Perfect for learning how actions work!
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
        
        Args:
            dispatcher: Used to send messages back to the user
            tracker: Contains the conversation history and slots
            domain: The bot's domain configuration
            
        Returns:
            A list of events (usually empty for simple actions)
        """
        # This is where your custom logic goes!
        # For now, we just return a hardcoded message.
        dispatcher.utter_message(
            text="Our bank hours are Monday-Friday 9am-5pm, Saturday 10am-2pm. We're closed on Sundays."
        )
        return []
```

#### Breaking Down Each Component

1. **Imports**:
   ```python
   from rasa_sdk import Action, Tracker
   from rasa_sdk.executor import CollectingDispatcher
   ```
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
