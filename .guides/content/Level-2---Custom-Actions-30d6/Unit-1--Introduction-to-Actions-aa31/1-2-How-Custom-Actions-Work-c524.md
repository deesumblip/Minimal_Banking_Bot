When a flow reaches a step with a custom action, Rasa sends a request to the action server. The action server runs the matching `run()` method, which uses `dispatcher.utter_message()` to build a response. The action server returns that response to Rasa, which sends it to the user.

```text
User: "What are your hours?"
    ↓
Flow: hours is triggered
    ↓
Flow step: - action: action_bank_hours
    ↓
Rasa finds action_bank_hours in actions/ folder
    ↓
Rasa executes the action's run() method
    ↓
Action sends message via dispatcher.utter_message()
    ↓
Agent responds with dynamic message
```

In this example, a user message activated a flow, which activated your code, which produced the reply. You write the logic, Rasa handles the execution.