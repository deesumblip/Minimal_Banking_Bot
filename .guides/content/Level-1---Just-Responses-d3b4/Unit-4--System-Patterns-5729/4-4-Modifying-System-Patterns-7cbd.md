You can customize system patterns to change default behavior.

#### Example: Enhanced Session Start

Instead of just greeting, you might want to greet AND offer help:

```yaml
flows:
  pattern_session_start:
    name: pattern session start
    description: Start the conversation with a greeting
    nlu_trigger:
      - intent: session_start
    steps:
      - action: utter_greet
      - action: utter_contact
```

**Result**: When a user opens the chat, they see both the greeting and the help message back to back.

---