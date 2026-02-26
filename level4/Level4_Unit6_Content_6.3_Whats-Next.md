Level 4 completes the multi-slot transfer flow. Possible next steps (depending on your course):

- **Forms or validation** — Use Rasa forms or custom validation to enforce formats (e.g. amount as a number, account numbers with a pattern).
- **NLU and intents** — Add or refine intents and training data so the bot reliably recognizes "transfer money", "check balance", and other phrases.
- **More flows** — Add more flows that collect different slots and call different actions.
- **Channels** — Connect the bot to a channel (e.g. Slack, web chat) and test the same flows there.

Your **level4** folder is the single source for this assistant: domain, flows, actions, and config. Keep training from `level4` after any change to domain, data, or actions.
