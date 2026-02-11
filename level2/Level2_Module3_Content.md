# Module 3: Creating Your First Action

### 3.1 Step-by-Step: Creating an Action

Let's create a simple action to practice. We'll create `action_bank_hours.py` (which already exists, but we'll understand how it was created).

#### Before You Begin

✅ **Checklist**:
- You understand basic Python syntax
- You know where the `actions/` folder is
- You have a text editor ready
- Your Level 1 bot is working

#### Step-by-Step Tutorial

**Step 1: Navigate to the Actions Folder**

1. In your project folder, navigate to the `actions/` folder
2. If it doesn't exist, create it
3. You should see `__init__.py` (if the folder exists)

**What you should see**: An `actions/` folder with `__init__.py` inside.

---

**Step 2: Create the Action File**

1. In the `actions/` folder, create a new file named `action_bank_hours.py`
2. Open it in your text editor

⚠️ **File naming**:
- Use lowercase with underscores: `action_bank_hours.py`
- Must start with `action_` (convention)
- The filename should match the action name

---

**Step 3: Add the Action Class Structure**

1. Add the imports at the top:
   ```python
   from typing import Any, Dict, List, Text
   
   from rasa_sdk import Action, Tracker
   from rasa_sdk.executor import CollectingDispatcher
   ```

2. Create the class:
   ```python
   class ActionBankHours(Action):
       def name(self) -> Text:
           return "action_bank_hours"
       
       def run(self, dispatcher, tracker, domain):
           dispatcher.utter_message(
               text="Our bank hours are Monday-Friday 9am-5pm, Saturday 10am-2pm. We're closed on Sundays."
           )
           return []
   ```

**Complete file**:
```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A simple custom action that returns bank hours."""

    def name(self) -> Text:
        return "action_bank_hours"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Our bank hours are Monday-Friday 9am-5pm, Saturday 10am-2pm. We're closed on Sundays."
        )
        return []
```

---

**Step 4: Verify Your Code**

Before saving, check:

✅ **Imports**: All required imports are present
✅ **Class name**: `ActionBankHours` (descriptive, starts with `Action`)
✅ **`name()` method**: Returns `"action_bank_hours"` (matches filename)
✅ **`run()` method**: Has correct parameters (`dispatcher`, `tracker`, `domain`)
✅ **Message sending**: Uses `dispatcher.utter_message()`
✅ **Return value**: Returns `[]` (empty list)

**Common mistakes to avoid**:
- ❌ Forgetting to inherit from `Action`
- ❌ Wrong return type in `name()` (should return string, not call it)
- ❌ Forgetting to return `[]` from `run()`
- ❌ Typos in method names (`run` not `runs`, `name` not `names`)

---

**Step 5: Save the File**

1. Save your file as `action_bank_hours.py` in the `actions/` folder
2. Your action is now created!

---

### 3.2 Understanding Action Execution

When Rasa executes your action:

1. **Rasa finds the action**: Looks for `action_bank_hours` in the `actions/` folder
2. **Rasa instantiates the class**: Creates an instance of `ActionBankHours`
3. **Rasa calls `name()`**: Verifies the action name matches
4. **Rasa calls `run()`**: Executes your custom code
5. **Your code runs**: Python executes your logic
6. **Message is sent**: `dispatcher.utter_message()` sends text to the user
7. **Action completes**: Returns empty list `[]`

**Key Point**: Rasa handles all the infrastructure - you just write the `run()` method with your logic.

---
