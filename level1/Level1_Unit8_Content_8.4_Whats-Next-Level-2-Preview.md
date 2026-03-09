### 8.4 What's Next: Level 2 Preview

**Why look ahead**: You've built a bot that only says what you put in the domain. Level 2 adds the ability to run Python code, for example to fetch live data or call APIs. Seeing what's next helps you decide when to stay in Level 1 and when to extend the same bot with actions.

Level 2 **builds on your existing Level 1 bot**. You keep the same domain and flows; you don't start a new bot.

**Level 2 adds**: Custom Python actions; new flows that use actions; action registration in the domain (`actions:` section).

**Example**: For "What are your bank hours?", Level 1 would need a static response. Level 2 uses `action_bank_hours` in Python for dynamic hours. You'll create the action class, register it, and add a flow that calls it.

---
