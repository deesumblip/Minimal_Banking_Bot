**Starting point:** Chapter 1.4 assumed you began with the **final banking agent at the end of Chapter 1.3**; you extended it in **`level4/`** (see **`Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`**).

Level 4 completes the multi-slot transfer flow. Possible next steps (depending on your course):

- **Forms or validation** — Use Rasa forms or custom validation to enforce formats (e.g. amount as a number, account numbers with a pattern).
- **NLU and intents** — Add or refine intents and training data so the agent reliably recognizes "transfer money", "check balance", and other phrases.
- **More flows** — Add more flows that collect different slots and call different actions.
- **Channels** — Connect the agent to a channel (e.g. Slack, web chat) and test the same flows there.

Your **level4** folder is the single source for this assistant: domain, flows, actions, and config. Keep training from `level4` after any change to domain, data, or actions.
