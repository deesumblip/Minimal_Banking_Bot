# Unit 5: Using Actions in Flows

### 5.3 Mixing Responses and Actions

You can use both responses and actions in the same flow:

```yaml
flows:
  hours_and_contact:
    name: hours and contact
    description: Tell the user bank hours and provide contact information.
    steps:
      - action: action_bank_hours      # ← Action (custom code)
      - action: utter_contact          # ← Response (predefined text)
```

**Execution order**:
1. First: Action executes (returns dynamic hours)
2. Second: Response sends (static contact info)

---
