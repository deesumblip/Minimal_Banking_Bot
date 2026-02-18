# 6.2 Testing Slot Collection

## Basic Testing Workflow

1. **Train your bot**: From project root, activate venv, `cd level3`, then `python -m rasa train`.

2. **Start Inspector**:
   - **Codio**: Run `python -m rasa inspect --debug --log-file logs/logs.out` from `level3`. Leave the terminal open. Open the **Rasa Inspect** tab in the top menu bar (do not use Tools → Ports or port 5005).
   - **Local**: Same command from `level3`; then open **http://localhost:5005** (or …/inspect.html) in your browser.

3. **Test slot collection**:
   - Type "Check my balance"
   - Bot should ask: "What is your account number?"
   - Type "1234"
   - Bot should respond with balance for account 1234

4. **Test slot persistence**:
   - Type "What's my balance?" again
   - Bot should remember account 1234 (no asking)
   - Bot should respond immediately

5. **Verify Level 2 flows still work**:
   - Type "What are your hours?" → Should work (Level 2)
   - Type "Hello" → Should work (Level 1)
