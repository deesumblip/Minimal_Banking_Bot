**Objective**: Test your Level 3 bot in Inspector so you see slot collection and persistence in action.

**Prerequisite**: Complete Lab 6.1 (training). A model file must exist in `level3/models/`.

---

## Part 1: In Codio

1. **Start Inspector** (if not already running):
   - In the terminal (from `level3` with venv active):  
     `python -m rasa inspect --debug --log-file logs/logs.out`
   - Leave the terminal open. Open the **Rasa Inspect** tab in the top menu bar (do not use Tools → Ports or port 5005).

2. **Test slot collection**:
   - Type **"Check my balance"**
   - Bot should ask: "What is your account number?"
   - Type **"1234"**
   - Bot should respond with balance for account 1234

3. **Test slot persistence**:
   - Type **"What's my balance?"** again
   - Bot should remember account 1234 (no asking) and respond immediately

4. **Verify Level 2 flows still work**:
   - Type **"What are your hours?"** → Level 2 flow should work
   - Type **"Hello"** → Level 1 should work

**Success criteria**: Slot collection asks for account when needed; slot persists across turns; Level 1 and 2 flows still respond.

---

## Part 2: Running locally

Use the same steps as Part 1. From project root, activate venv, then `cd level3`. Run `python -m rasa inspect --debug --log-file logs/logs.out`, then open **http://localhost:5005** (or …/inspect.html) in your browser. Test as above.

---

**No assessment** for this lab; it is completion-based. Use the debug panel in Inspector to see slot values if you want to explore further.
