# Module 1: Introduction to Actions

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
