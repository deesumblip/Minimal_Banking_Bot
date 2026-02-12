# Unit 4: Registering Actions in the Domain

### 4.4 Multiple Actions

In this level you have (at least) two actions: the example **action_bank_hours** and the action you created in Lab 3.1, **action_holiday_hours**. List them both under `actions:`:

```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
```

When you add more actions later, list each on its own line with a dash.

---

#### Review in Inspector (optional)

After you run the Lab 4.1 assessment, you can see how registration affects the bot. Train (`python -m rasa train`), then start and open the Rasa Inspector GUI (see Unit 6.3 for how). In the Inspector chat, try:

- **"What are your hours?"** — If the `hours` flow exists, the bot should use `action_bank_hours` and reply with bank hours.
- **"What are your holiday hours?"** — The bot likely won't handle this yet, because there's no flow that uses your action. You'll add that flow in Unit 5.

---
