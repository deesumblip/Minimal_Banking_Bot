### 4.2 Session Start Pattern

The `pattern_session_start` flow automatically triggers when a new conversation begins.

**Why it matters**: When someone opens the chat, they shouldn't have to type "hello" to get a response. Session start runs as soon as the conversation starts, so you can greet them and optionally show help or contact info right away. That makes the bot feel welcoming instead of blank.

#### How It Works

```yaml
flows:
  pattern_session_start:
    description: Start the conversation with a greeting
    name: pattern session start
    nlu_trigger:
      - intent: session_start
    steps:
      - action: utter_greet
```

- **`pattern_session_start`**: Special name Rasa recognizes; triggers on new conversations.
- **`nlu_trigger: - intent: session_start`**: Triggers when conversation begins; no user message needed.
- **`steps: - action: utter_greet`**: Executes the greeting.

**Key Point**: The user doesn't need to say anything - the bot greets them automatically.

---
