# Unit 1: Introduction to Actions

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
