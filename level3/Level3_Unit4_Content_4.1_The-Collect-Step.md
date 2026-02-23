# 4.1 The Collect Step

A flow can ask for information before running an action. You'll set this up with a **collect step**. This step tells Rasa to get this slot value before continuing. If the slot is empty, Rasa asks the user, using the `utter_ask_*` response you defined in the domain. Once the slot has a value, the flow continues.

## Syntax

```yaml
steps:
  - collect: account
    description: "account number"
```

- **`collect: account`**. The slot to collect.
- **`description:`**. Helps the LLM understand what to extract. Optional, but recommended.
