# Lab 3.1: Create Your Own Action

## Guide Content (For Students)

**Placement**: This lab follows Unit 3: Creating Your First Action.

---

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

### Quick Checklist (what the grader checks)

Before submitting, confirm:

- [ ] File is in the `actions/` folder and named `action_holiday_hours.py`
- [ ] You import `datetime` and use it (e.g. `datetime.now()`) to choose the message
- [ ] Class is `ActionHolidayHours(Action)`
- [ ] `name()` returns `"action_holiday_hours"`
- [ ] `run()` calls `dispatcher.utter_message()` and returns `[]`

Run the assessment when you're done.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that students can create a custom action file (`action_holiday_hours.py`) with the correct structure, imports, methods, and date-based logic (so the message depends on whether today is a holiday).

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:
```
.guides/assessments/level2_graders/lab_3.1_grader.sh
```

## Grader Script

```bash
#!/bin/bash
cd /home/codio/workspace/level2

score=0
max_score=12

echo "Running Lab 3.1 Assessment Checks..."
echo ""

# Check 0: Virtual environment exists and is activated (2 points)
echo "Check 0: Verifying virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ Check 0: FAILED - Virtual environment (.venv) not found (0 points)"
    echo "Hint: Create virtual environment with 'python3.11 -m venv .venv'"
else
    source .venv/bin/activate 2>/dev/null || true
    echo " Check 0: PASSED - Virtual environment found and activated (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 1: Actions folder exists (1 point)
echo "Check 1: Verifying actions folder exists..."
if [ ! -d "actions" ]; then
    echo "❌ Check 1: FAILED - actions/ folder not found (0 points)"
    echo "Hint: Create the actions folder with 'mkdir -p actions'"
else
    echo " Check 1: PASSED - actions/ folder exists (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 2: __init__.py exists in actions folder (1 point)
echo "Check 2: Verifying __init__.py exists..."
if [ ! -f "actions/__init__.py" ]; then
    echo "❌ Check 2: FAILED - actions/__init__.py not found (0 points)"
    echo "Hint: Create __init__.py in the actions folder (can be empty)"
else
    echo " Check 2: PASSED - actions/__init__.py exists (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 3: action_holiday_hours.py file exists (2 points)
echo "Check 3: Verifying action_holiday_hours.py exists..."
if [ ! -f "actions/action_holiday_hours.py" ]; then
    echo "❌ Check 3: FAILED - actions/action_holiday_hours.py not found (0 points)"
    echo "Hint: Create the action file in the actions/ folder"
else
    echo " Check 3: PASSED - action_holiday_hours.py file exists (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 4: Action file has correct imports (2 points)
echo "Check 4: Verifying action file imports..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "from rasa_sdk import Action" actions/action_holiday_hours.py 2>/dev/null && grep -q "from rasa_sdk.executor import CollectingDispatcher" actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 4: PASSED - Correct imports found (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 4: FAILED - Missing required imports (0 points)"
    echo "Hint: Import Action from rasa_sdk and CollectingDispatcher from rasa_sdk.executor"
fi
echo ""

# Check 4b: Action uses datetime for date-based logic (1 point)
echo "Check 4b: Verifying date-based logic (datetime)..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "datetime" actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 4b: PASSED - datetime used for date-based message (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 4b: FAILED - Action should use datetime to check if today is a holiday (0 points)"
    echo "Hint: Import datetime and use datetime.now() with .month and .day to choose your message"
fi
echo ""

# Check 5: Action class inherits from Action (1 point)
echo "Check 5: Verifying Action class structure..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "class ActionHolidayHours(Action)" actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 5: PASSED - ActionHolidayHours class inherits from Action (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 5: FAILED - ActionHolidayHours class not found or doesn't inherit from Action (0 points)"
    echo "Hint: Class should be 'class ActionHolidayHours(Action):'"
fi
echo ""

# Check 6: name() method exists and returns correct value (1 point)
echo "Check 6: Verifying name() method..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "def name" actions/action_holiday_hours.py 2>/dev/null && grep -q "return \"action_holiday_hours\"" actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 6: PASSED - name() method exists and returns 'action_holiday_hours' (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 6: FAILED - name() method missing or incorrect return value (0 points)"
    echo "Hint: name() method should return 'action_holiday_hours'"
fi
echo ""

# Check 7: run() method exists, uses dispatcher.utter_message, and returns [] (1 point)
echo "Check 7: Verifying run() method and message sending..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "def run" actions/action_holiday_hours.py 2>/dev/null && grep -q "dispatcher.utter_message" actions/action_holiday_hours.py 2>/dev/null && grep -q 'return \[\]' actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 7: PASSED - run() method exists, uses dispatcher.utter_message(), and returns [] (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 7: FAILED - run() must call dispatcher.utter_message() and return [] (0 points)"
    echo "Hint: run() must call dispatcher.utter_message() to send a message and return [] at the end"
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo " PASS: Action creation verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 0 (venv) | Check 1 (actions/) | Check 2 (__init__.py) | Check 3 (action file) | Check 4 (imports) | Check 4b (datetime) | Check 5 (class) | Check 6 (name()) | Check 7 (run())"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
```

### Example student deliverable (for grading reference)

Students should produce a file at `actions/action_holiday_hours.py`. The following is a minimal example that satisfies the grader (exact wording of messages may vary):

```python
from datetime import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHolidayHours(Action):
    def name(self):
        return "action_holiday_hours"

    def run(self, dispatcher, tracker, domain):
        now = datetime.now()
        if (now.month == 1 and now.day == 1):
            message = "We're closed today for New Year's Day."
        elif (now.month == 7 and now.day == 4):
            message = "We're closed today for Independence Day."
        elif (now.month == 12 and now.day == 25):
            message = "We're closed today for Christmas."
        else:
            message = (
                "We're closed on New Year's Day, Independence Day, and Christmas. "
                "On other holidays we may have limited hours—please call ahead."
            )
        dispatcher.utter_message(text=message)
        return []
```

## Assessment Setup and Configuration

1. **Create the page** – New Codio Guide page **Lab 3.1: Create Your Own Action** (standalone: folder tree, guide editor, terminal). Add the **Guide Content** section above as the page content.

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure each tab as follows.

   **General** – Name: *Lab 3.1: Create Your Own Action*. Description: *Verify that students can create action_holiday_hours.py with correct structure and date-based logic*. Points: `12`. Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/assessments/level2_graders/lab_3.1_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace/level2`.

   **Grading**
   - **Points**: `12` – Total points for this assessment.
   - **Allow partial points**: `OFF` – Single run; the script reports one pass/fail outcome, so partial credit is not used.
   - **Use maximum score**: `OFF` – No cap; the student can earn the full point value.
   - **Case insensitive**: `ON` – Output comparison ignores letter case so minor casing differences do not fail the test.
   - **Ignore white spaces**: `ON` – Extra spaces or newlines in the script output do not cause a failure.
   - **Substring match**: `ON` – Pass if the expected string appears anywhere in the output (full output need not match exactly).
   - **Test case** (one case):
     - **INPUT – Arguments**: leave empty – No command-line arguments are passed to the script.
     - **INPUT – STDIN**: leave empty – No stdin is fed to the script.
     - **Expected output**: ` PASS: Action creation verification complete!` (include the leading space) – The test passes when the script’s stdout contains this string (i.e. when all checks pass).
   - **Show expected answer**: `ALWAYS` – Students can see the required output phrase after submission.
   - **Show rationale to student**: `NEVER` (or as desired) – Controls whether the instructor rationale is shown to the student.
   - **Defined number of attempts**: `OFF` – No limit on submission attempts (or set a limit if desired).
   - **Rationale** (optional): e.g. *The grader checks that `actions/action_holiday_hours.py` exists, has the correct imports (including `datetime`), class `ActionHolidayHours(Action)`, `name()` returning `'action_holiday_hours'`, and `run()` calling `dispatcher.utter_message()` and returning `[]`.*

   **Files** – Create the grader script at `.guides/assessments/level2_graders/lab_3.1_grader.sh` and make it executable: `chmod +x .guides/assessments/level2_graders/lab_3.1_grader.sh`.

3. **Save & Test** the assessment. Enable **Learning Analytics** if desired.

---
