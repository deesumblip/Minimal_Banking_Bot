# 1.1 What is a Slot?

A **slot** is a memory variable that stores information from the conversation. Slots allow your bot to remember what users tell it and use that information later.

## Slots = Bot Memory

Think of slots like a form that the bot fills out during the conversation:
- User provides information → Bot stores it in a slot
- Bot needs information → Bot asks user and stores answer in slot
- Action needs information → Bot reads it from the slot

## Example: Account Number

**Without slots (Level 2)**:
```
User: "Check my balance"
Bot: "I need your account number" (but forgets immediately)
User: "1234"
Bot: "What account number?" (forgot it!)
```

**With slots (Level 3)**:
```
User: "Check my balance"
Bot: "What is your account number?"
User: "1234"
Bot: [Stores "1234" in account slot]
Bot: "Balance for account 1234 is $123.45"
[Later in conversation]
User: "What's my balance?"
Bot: [Remembers account 1234 from slot]
Bot: "Balance for account 1234 is $123.45"
```
