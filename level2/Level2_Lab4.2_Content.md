# Lab 4.2: Multiple Actions

You've now registered both actions in the domain: **action_bank_hours** (the example) and **action_holiday_hours** (the one you created in Lab 3.1). With both registered, Rasa can invoke them—in Unit 5 you'll connect them to flows. When you add more actions later, list each on its own line under `actions:` with a dash.

---

#### Review in Inspector (optional)

After you run the Lab 4.1 assessment, you can see how registration affects the bot. Train (`python -m rasa train`), then start and open the Rasa Inspector GUI (see Unit 6.3 for how). In the Inspector chat, try:

- **"What are your hours?"** — If the `hours` flow exists, the bot should use `action_bank_hours` and reply with bank hours.
- **"What are your holiday hours?"** — The bot likely won't handle this yet, because there's no flow that uses your action. You'll add that flow in Unit 5.

---
