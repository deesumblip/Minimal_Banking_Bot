### Lab 3.2: Create Your Own Action

### Your Task

You've learned how actions are structured and how they work. Now create a **new** action: `action_holiday_hours`, which returns the bank's holiday schedule **based on today's date**. If today is a holiday, the action should say we're closed today; otherwise it should return the general holiday schedule. That way the response depends on the current date—so it has to be an action, not a single `utter_*` response. Follow the steps below.

---

### Step-by-Step Instructions

**Step 1 – Create the file**  
- In the `actions/` folder, create a new file named `action_holiday_hours.py`.

**Step 2 – Add the imports**  
At the top of the file, add:
- `from datetime import datetime` (so you can use the current date)
- `from rasa_sdk import Action, Tracker`
- `from rasa_sdk.executor import CollectingDispatcher`  
You can also add `from typing import Any, Dict, List, Text` for type hints.

**Step 3 – Define the class**  
- Create a class named `ActionHolidayHours` that inherits from `Action`  
  (same pattern as `ActionBankHours`, but with the new name).

**Step 4 – Implement `name()`**  
- Add a method `name(self)` that returns the string `"action_holiday_hours"`  
  (this must match the filename, without `.py`).  
- **Use double quotes** around the return value so the autograder recognizes it: `return "action_holiday_hours"`.

**Step 5 – Implement `run()` with date-based logic**  
- Add the `run()` method with parameters: `dispatcher`, `tracker`, and `domain`.  
- Get today's date: `now = datetime.now()`, then use `now.month` and `now.day` to decide the message.  
- **Holiday logic (copy this structure):**  
  - If `(now.month == 1 and now.day == 1)` → message = *"We're closed today for New Year's Day."*  
  - Else if `(now.month == 7 and now.day == 4)` → message = *"We're closed today for Independence Day."*  
  - Else if `(now.month == 12 and now.day == 25)` → message = *"We're closed today for Christmas."*  
  - Else → message = *"We're closed on New Year's Day, Independence Day, and Christmas. On other holidays we may have limited hours—please call ahead."*  
- Call `dispatcher.utter_message(text=message)` **once**.  
- At the end of `run()`, use the **literal** `return []` (type the empty list directly, not a variable) so the autograder passes.

**Step 6 – Save and verify**  
- Save the file and **in Codio** use **Check It!** below.

---

### Quick Checklist

Before submitting, confirm:

- File is in the `actions/` folder and named `action_holiday_hours.py`
- You import `datetime` and use it (e.g. `datetime.now()`) to choose the message
- Class is `ActionHolidayHours(Action)`
- `name()` returns `"action_holiday_hours"` (with **double quotes**)
- `run()` calls `dispatcher.utter_message()` and ends with the **literal** `return []`

**Use Check It!** below when done (Codio).

{Check It!|assessment}(code-output-compare-2266471391)
