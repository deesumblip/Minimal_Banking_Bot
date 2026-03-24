Your goal is to test your Level 3 agent in Inspector so you see slot collection and persistence in action.

**Prerequisite.** Complete Lab 6.1 (training). A model file must exist in `level3/models/`.

---

## Part 1: In Codio

1. **Start Inspector.** In the terminal, from `level3` with venv active, run `python -m rasa inspect --debug`. Leave the terminal open. When you see "Starting Worker" in the terminal, open the **Rasa Inspect** tab in the top menu bar (do not use Tools → Ports or port 5005).

2. **Test slot collection.** Type "Check my balance". The agent should ask "What is your account number?" Type "1234". The agent should respond with the balance for account 1234.

3. **Test slot persistence.** Type "What's my balance?" again. The agent should remember account 1234 (no asking) and respond immediately.

4. **Verify Level 2 flows still work.** Type "What are your hours?" and the Level 2 flow should work. Type "Hello" and Level 1 should work.

You're done when slot collection asks for the account when needed, the slot persists across turns, and Level 1 and 2 flows still respond. This lab has no assessment; it is completion-based.

---

## Part 2: Running locally

Use the same steps as Part 1. From the project root, activate the venv, then `cd level3`. Run `python -m rasa inspect --debug`, then open **http://localhost:5005** (or …/inspect.html) in your browser. Test as above.

You can use the debug panel in Inspector to see slot values if you want to explore further.

---

## Check Your Knowledge

{Check It!|assessment}(multiple-choice-2446085116)

{Check It!|assessment}(multiple-choice-3751028362)

{Check It!|assessment}(multiple-choice-2697467428)
