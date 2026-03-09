### 4.4 Modifying System Patterns

You can customize system patterns to change default behavior. That way the first thing users see, or the way a turn ends, matches your design. For example, you might show greet plus help, or greet plus contact.

#### Example: Enhanced Session Start

Add a second step to greet and show help:

```yaml
flows:
  pattern_session_start:
    description: Start the conversation with a greeting
    name: pattern session start
    nlu_trigger:
      - intent: session_start
    steps:
      - action: utter_greet
      - action: utter_help
```

**Result**: When a user opens the chat, they see both the greeting and the help message.

---
