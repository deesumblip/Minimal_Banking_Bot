### 7.1 Complete Bot Walkthrough

**Why walk through a full conversation**: Seeing one end-to-end run from session start through user messages, flow triggers, and pattern completed ties everything together. You've edited domain, flows, and patterns separately. Here you see how they work in sequence so you can design better conversations and debug when something doesn't fire as expected.

A complete conversation ties together system patterns, flows, and domain:

- **User opens chat** → `pattern_session_start` runs → `utter_greet` → bot greets.
- **User: "what can you help me with?"** → LLM matches `help` flow → `utter_help` → bot lists capabilities.
- **User: "how do I contact support?"** → LLM matches `contact` flow → `utter_contact` → bot gives contact info.
- **User: "thanks"** → Flow completes → `pattern_completed` → conversation ends, waits for next input.

Files involved: `data/system/patterns/patterns.yml` for session start, `domain/basics.yml` for responses, `data/basics/*.yml` for flows, and `config.yml` for pipeline and policies.

---
