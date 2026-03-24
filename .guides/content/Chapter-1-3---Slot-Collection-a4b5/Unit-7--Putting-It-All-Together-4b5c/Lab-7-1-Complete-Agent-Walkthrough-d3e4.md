Your goal is to see how all pieces (Level 1, 2, and 3) work together in one conversation.

---

## Steps

1. **Start Inspector** (if not already running). From `level3` with venv active, run `python -m rasa inspect --debug --log-file logs/logs.out`. Open the **Rasa Inspect** tab (Codio) or http://localhost:5005 (local).

2. **Have a complete conversation.** On session start the agent greets you. Say "Check my balance" and the agent asks for your account number (slot empty). Say "1234" and the agent stores the account, runs the action, and replies with the balance. Say "What's my balance?" and the agent remembers 1234 and replies without asking again (slot persistence). Say "What are your hours?" and the Level 2 flow runs.

3. **Observe.** Use the debug panel to see which flow triggers and how the `account` slot is set and reused.

You're done when you see slot collection, persistence, and Level 1 and 2 flows in one session. This lab has no graded assessment.

---

## Check Your Knowledge

{Check It!|assessment}(multiple-choice-3020000001)

{Check It!|assessment}(multiple-choice-3020000002)

{Check It!|assessment}(multiple-choice-3020000003)
