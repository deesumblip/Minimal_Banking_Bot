Your goal is to see how all pieces (Level 1, 2, and 3) work together in one conversation.

---

## Steps

1. **Start Inspector** (if not already running). From `level3` with venv active, run `python -m rasa inspect --debug --log-file logs/logs.out`. Open the **Rasa Inspect** tab (Codio) or http://localhost:5005 (local).

2. **Have a complete conversation.** On session start the bot greets you. Say "Check my balance" and the bot asks for your account number (slot empty). Say "1234" and the bot stores the account, runs the action, and replies with the balance. Say "What's my balance?" and the bot remembers 1234 and replies without asking again (slot persistence). Say "What are your hours?" and the Level 2 flow runs.

3. **Observe.** Use the debug panel to see which flow triggers and how the `account` slot is set and reused.

You're done when you see slot collection, persistence, and Level 1 and 2 flows in one session. This lab has no graded assessment.

---

## Check Your Knowledge

**1. What does "slot persistence" mean in this walkthrough?**

a) The slot value is stored in a database  
b) The bot remembers the account number across turns in the same session  
c) The slot is never cleared  
d) The bot asks for the account every time  

**2. In one session, which flows should you be able to trigger?**

a) Only Level 3 (check_balance)  
b) Only Level 1 (greet) and Level 3 (check_balance)  
c) Level 1 (greet), Level 2 (hours), and Level 3 (check_balance)  
d) Only Level 2 (hours)  

**3. Where can you see the `account` slot value during a conversation?**

a) In the terminal output only  
b) In the Rasa Inspect debug panel  
c) In `domain/basics.yml`  
d) You cannot see it  

---

### Answer Key

| Q | Answer | Brief explanation |
|---|--------|-------------------|
| 1 | **b** | Slot persistence means the bot keeps the slot value across turns in the same conversation. |
| 2 | **c** | The Level 3 bot includes all Level 1, 2, and 3 flows (greet, hours, check_balance, etc.). |
| 3 | **b** | The debug panel in Rasa Inspect shows slot values and which flow is active. |
