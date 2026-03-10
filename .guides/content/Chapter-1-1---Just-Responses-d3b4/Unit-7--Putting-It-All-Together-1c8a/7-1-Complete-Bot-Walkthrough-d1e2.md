A complete conversation ties together system patterns, flows, and domain:

- **User opens chat** → `pattern_session_start` runs → `utter_greet` → bot greets.
- **User: "what can you help me with?"** → LLM matches `help` flow → `utter_help` → bot lists capabilities.
- **User: "how do I contact support?"** → LLM matches `contact` flow → `utter_contact` → bot gives contact info.
- **User: "thanks"** → Flow completes → `pattern_completed` → conversation ends, waits for next input.

Files involved: `data/system/patterns/patterns.yml` (session start), `domain/basics.yml` (responses), `data/basics/*.yml` (flows), `config.yml` (pipeline and policies).

---

**Objective**: Understand how all pieces work together in a complete conversation.

#### Steps

1. **Start Inspector** (if not already running).
2. **Have a complete conversation**: Open a new session (triggers `pattern_session_start`), ask for help, ask for contact info, end the conversation.
3. **Observe**: Which flow triggers for each message; use debug output to see LLM understanding; see how flows and responses connect.

**AI Coach**: Ask "How does the bot decide which flow to trigger?" or "What happens when I start a new conversation?"
