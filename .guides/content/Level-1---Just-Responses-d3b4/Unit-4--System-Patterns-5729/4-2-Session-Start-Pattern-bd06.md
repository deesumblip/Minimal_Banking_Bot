The `pattern_session_start` runs automatically when a new conversation begins, before the user says anything.

#### How It Works

```yaml
flows:
  pattern_session_start:
    name: pattern session start
    description: Start the conversation with a greeting
    nlu_trigger:
      - intent: session_start
    steps:
      - action: utter_greet
```


`nlu_trigger` activates a flow on a specific intent rather than through the LLM Command Generator. Here it listens for `session_start`, a built-in intent Rasa fires when a new session opens. No user message needed.

This is the only place in this course you will see `nlu_trigger`. For everything else, the command generator reads skill `description:` to decide which flows or sub-agents to start. This pattern bypasses that process entirely and activates on a system event instead.


#### Conversation Flow

```text
User opens chat
    ↓
Rasa detects new session
    ↓
pattern_session_start activates automatically
    ↓
Agent says utter_greet
    ↓
User sees: "Hi! I'm a banking assistant..."
```

**Key Point**: The user doesn't need to say anything, the agent greets them automatically once the session starts.

{Check It!|assessment}(multiple-choice-662755326)

---