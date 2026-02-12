# Unit 5: Using Actions in Flows

### 5.1 Actions vs. Responses in Flows

In Level 1, flows used `utter_*` responses. In Level 2, flows can use `action_*` actions.

#### Level 1 Flow (Response)

```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet  # ← Uses a response
```

#### Level 2 Flow (Action)

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours  # ← Uses an action
```

**Key Difference**: 
- `utter_*` = Predefined text (response)
- `action_*` = Custom Python code (action)

Both use `- action:` in the flow, but Rasa knows the difference based on the name.

---
