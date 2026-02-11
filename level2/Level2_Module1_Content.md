# Module 1: Introduction to Actions

### 1.1 What is an Action?

An **action** is custom Python code that your bot can execute. Actions allow your bot to do more than just say predefined text - they can perform calculations, access databases, call APIs, and execute any Python logic you write.

#### Actions vs. Responses

**Responses (`utter_*`)**:
- Predefined text messages
- No custom logic
- Just sends text to the user
- Defined in `domain/basics.yml` under `responses:`

**Actions (`action_*`)**:
- Custom Python code
- Can execute any logic
- Can access databases, APIs, perform calculations
- Defined in Python files in `actions/` folder
- Registered in `domain/basics.yml` under `actions:`

#### When to Use Actions

✅ **Use actions when you need**:
- Dynamic responses (e.g., "We're open today until 5pm" - changes based on current day)
- Calculations (e.g., calculating interest, fees)
- Data processing (e.g., formatting dates, validating input)
- External integrations (e.g., checking account balance from a database)
- Conditional logic (e.g., different responses based on conditions)

❌ **Don't use actions for**:
- Simple static text (use responses instead)
- Messages that never change
- Text that doesn't require any processing

#### Example: Bank Hours

**Level 1 approach** (static response):
```yaml
utter_hours:
  - text: "We're open Monday-Friday 9am-5pm, Saturday 10am-2pm."
```

**Level 2 approach** (dynamic action):
```python
def run(self, dispatcher, tracker, domain):
    # Check current day
    # Check if it's a holiday
    # Return dynamic message: "We're open today until 5pm" or "We're closed today"
```

---

### 1.2 How Actions Work

When a flow calls an action, here's what happens:

```
User sends message: "What are your hours?"
    ↓
Flow: hours is triggered
    ↓
Flow step: - action: action_bank_hours
    ↓
Rasa finds action_bank_hours in actions/ folder
    ↓
Rasa executes the action's run() method
    ↓
Action executes Python code
    ↓
Action sends message via dispatcher.utter_message()
    ↓
Bot responds with dynamic message
```

**Key Point**: Actions are Python classes that Rasa calls when needed. You write the logic, Rasa handles the execution.

---

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

**Note**: In Module 2 you'll see the full `action_bank_hours`—it uses `datetime` to return different messages for weekdays, Saturday, and Sunday. That's why it's an action, not a simple `utter_*` response.

---
