**Starting point:** Chapter 1.4 assumed you began with the **final banking agent at the end of Chapter 1.3**; you extended it in **`level4/`** (see **`Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`**).

Level 4 completes the multi-slot transfer flow. Depending on your course, you might explore:

- **Forms or validation** — Use Rasa forms or custom validation to enforce formats (for example amount as a number, account numbers matching a pattern).
- **NLU and intents** — Add or refine intents and training data so the agent reliably recognizes phrases such as “transfer money” and “check balance.”
- **More flows** — Add flows that collect different slots and call different actions.
- **Channels** — Connect the agent to a channel (Slack, web chat, and so on) and run the same flows there.

Your **`level4/`** folder is the single source for this assistant: domain, flows, actions, and config. After you change domain, data, or actions, train again from **`level4/`**.
