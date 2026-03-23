### Lab 3.1: Step-by-Step: Creating an Action

You've seen `action_bank_hours.py`—it uses `datetime` and conditional logic to return different messages based on the current day. That's why it's an action, not a simple `utter_*` response. In **Lab 3.2** you'll create your own action, **action_holiday_hours**, that also uses the current date: if today is a holiday (e.g. New Year's Day, Christmas), it says "We're closed today"; otherwise it returns the general holiday schedule. Same structure as `action_bank_hours`, but for holidays. Later (Labs 4.1 and 5.1) you'll register it and add a flow for it.

**What you learned from `action_bank_hours`**:
- Actions need imports (including `datetime` if you use the current date/time)
- The class inherits from `Action`
- `name()` returns the action identifier
- `run()` contains your logic—conditionals, calculations, etc.—and calls `dispatcher.utter_message()` to send the result

---

**Here's the full code for `action_bank_hours`.** You'll add it to your project in the steps below.

```python
from datetime import datetime
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A custom action that returns bank hours based on the current day."""

    def name(self) -> Text:
        return "action_bank_hours"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
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

---

### Your task

1. **Go to the `level2` folder** in your project (the folder that contains `actions/`, `domain/`, `data/`, etc.). If you're in the main project root, open or create the `level2` folder.
2. **Create the `actions` folder** inside `level2` if it doesn't exist (path: `level2/actions/`).
3. **Create a new file** at **`level2/actions/action_bank_hours.py`**.
4. **Copy and paste** the entire code block above into that file and **save**.
5. **In Codio**, use **Check It!** below to verify the file is in the correct location.

After you pass, complete **Lab 3.2** to create `action_holiday_hours.py` following the same pattern. Then you'll register it in the domain (Unit 4 / Lab 4.1) and add a flow for it (Unit 5 / Lab 5.1).

---

**When creating your action (Lab 3.2), verify**:

 **Imports**: Include `datetime` (you'll need it to check if today is a holiday); include Rasa SDK imports  
 **Class name**: Descriptive, starts with `Action` (e.g., `ActionHolidayHours`)  
 **`name()` method**: Returns the action name (matches filename)  
 **`run()` method**: Has correct parameters (`dispatcher`, `tracker`, `domain`)  
 **Message sending**: Uses `dispatcher.utter_message()`  
 **Return value**: Returns `[]` (empty list)

**Common mistakes to avoid**:
- ❌ Forgetting to inherit from `Action`
- ❌ Wrong return type in `name()` (should return string, not call it)
- ❌ Forgetting to return `[]` from `run()`
- ❌ Typos in method names (`run` not `runs`, `name` not `names`)

---

**In Codio**, use **Check It!** below to verify that `action_bank_hours.py` is in the correct location (`level2/actions/`).

{Check It!|assessment}(code-output-compare-2266471390)

---
