The `pattern_session_start` flow automatically triggers when a new conversation begins.

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

#### Breaking It Down

1. **`pattern_session_start`**: Special name Rasa recognizes
   - Must be exactly this name
   - Rasa automatically triggers this on new conversations

2. **`nlu_trigger: - intent: session_start`**: When to trigger
   - `session_start` is a special intent Rasa generates
   - Triggers automatically when conversation begins
   - No user message needed

3. **`steps: - action: utter_greet`**: What to do
   - Executes when pattern triggers
   - In this case, greets the user

#### Conversation Flow

```
User opens chat
    ↓
Rasa detects new session
    ↓
pattern_session_start triggers automatically
    ↓
Bot says utter_greet
    ↓
User sees: "Hi! I'm a banking assistant..."
```

**Key Point**: The user doesn't need to say anything - the bot greets them automatically.

{Check It!|assessment}(multiple-choice-662755326)


---