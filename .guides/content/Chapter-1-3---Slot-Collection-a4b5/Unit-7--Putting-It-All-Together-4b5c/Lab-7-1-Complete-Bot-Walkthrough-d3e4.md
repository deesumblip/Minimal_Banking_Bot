**Objective**: See how all pieces (Level 1, 2, and 3) work together in one conversation.

---

## Steps

1. **Start Inspector** (if not already running). From `level3` with venv active:  
   `python -m rasa inspect --debug --log-file logs/logs.out`  
   Open the **Rasa Inspect** tab (Codio) or http://localhost:5005 (local).

2. **Have a complete conversation**:
   - **Session start** → Bot greets you.
   - **"Check my balance"** → Bot asks for account number (slot empty).
   - **"1234"** → Bot stores account, runs action, replies with balance.
   - **"What's my balance?"** → Bot remembers 1234, replies without asking again (slot persistence).
   - **"What are your hours?"** → Level 2 flow runs.

3. **Observe**: Use the debug panel to see which flow triggers and how the `account` slot is set and reused.

**Success criteria**: You see slot collection, persistence, and Level 1/2 flows in one session. No graded assessment.
