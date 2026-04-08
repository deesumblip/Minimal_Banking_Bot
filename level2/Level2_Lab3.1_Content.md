# Lab 3.1: Create Your Own Action

### Your Task

**Unit 2.1** walks through the full **`action_bank_hours.py`** example. This lab creates **`action_holiday_hours`**: the bank's holiday schedule **based on today's date**—same Rasa action pattern, with holiday date logic instead of weekday logic.

**Codio guide:** Unit 3 opens with this lab. Students complete the **Fill in the blanks** assessment first, paste into **`level2/actions/action_holiday_hours.py`**, then run the **Code Test**. The optional manual steps below match that solution if you are editing without Codio.

---

### Step-by-Step Instructions (optional manual build)

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

**Step 5 – Implement `run()` with date-based logic**  
- Add the `run()` method with parameters: `dispatcher`, `tracker`, and `domain`.  
- Get today's date, e.g. `now = datetime.now()` and use `now.month` and `now.day` to check if today is a holiday.  
- **If today is a holiday** (e.g. New Year's Day Jan 1, Independence Day July 4, or Christmas Dec 25—you can use these or your own list): set a message like *"We're closed today for [holiday name]."*  
- **Otherwise**: set a message with the general holiday schedule, e.g. *"We're closed on New Year's Day, Independence Day, and Christmas. On other holidays we may have limited hours—please call ahead."*  
- Call `dispatcher.utter_message(text=message)` **once** with whichever message you chose.  
- At the end of `run()`, return `[]` (an empty list).

**Step 6 – Save and verify**  
- Save the file and run the assessment below.

---

### Quick Checklist

Before submitting, confirm:

- File is in the `actions/` folder and named `action_holiday_hours.py`
- You import `datetime` and use it (e.g. `datetime.now()`) to choose the message
- Class is `ActionHolidayHours(Action)`
- `name()` returns `"action_holiday_hours"`
- `run()` calls `dispatcher.utter_message()` and returns `[]`

Run the assessment when you're done.

---

### When Rasa executes your action

When Rasa executes your action:

1. **Rasa finds the action**: Looks for the action in the `actions/` folder
2. **Rasa instantiates the class**: Creates an instance of your action class
3. **Rasa calls `name()`**: Verifies the action name matches what's registered
4. **Rasa calls `run()`**: Executes your custom code
5. **Your code runs**: Python executes your logic
6. **Message is sent**: `dispatcher.utter_message()` sends text to the user
7. **Action completes**: Returns empty list `[]`

**Key Point**: Rasa handles all the infrastructure, you just write the `run()` method with your logic.

---
