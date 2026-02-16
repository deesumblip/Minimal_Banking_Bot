A complete conversation ties together system patterns, flows, and domain:

- **User opens chat** → `pattern_session_start` runs → `utter_greet` → bot greets.
- **User: "what can you help me with?"** → LLM matches `help` flow → `utter_help` → bot lists capabilities.
- **User: "how do I contact support?"** → LLM matches `contact` flow → `utter_contact` → bot gives contact info.
- **User: "thanks"** → Flow completes → `pattern_completed` → conversation ends, waits for next input.

Files involved: `data/system/patterns/patterns.yml` (session start), `domain/basics.yml` (responses), `data/basics/*.yml` (flows), `config.yml` (pipeline and policies).
