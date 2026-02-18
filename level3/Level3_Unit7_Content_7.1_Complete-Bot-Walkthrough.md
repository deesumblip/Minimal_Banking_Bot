# 7.1 Complete Bot Walkthrough

A full conversation with the Level 3 bot:

1. **Session start** → Bot: "Hi! I'm a banking assistant. How can I help you today?"
2. **User:** "Check my balance" → Flow: `check_balance`. Slot `account` empty → Bot: "What is your account number?"
3. **User:** "1234" → Bot stores "1234" in `account` slot → Action runs → Bot: "(Demo) Balance for account 1234 is $123.45."
4. **User:** "What's my balance?" → Flow: `check_balance`. Slot `account` already "1234" → Bot skips asking, runs action → Bot: "(Demo) Balance for account 1234 is $123.45."
5. **User:** "What are your hours?" → Level 2 flow `hours` → `action_bank_hours` runs.

Levels 1, 2, and 3 work together: responses, actions, and slot memory.
