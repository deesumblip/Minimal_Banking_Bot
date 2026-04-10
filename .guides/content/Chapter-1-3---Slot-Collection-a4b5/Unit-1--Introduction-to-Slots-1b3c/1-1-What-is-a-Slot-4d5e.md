A **slot** is a memory variable that stores information from the conversation. Slots allow your agent to remember what users tell it and use that information later.

## Slots = Agent Memory

Think of slots like a form that the agent fills out during the conversation:

- User provides information → Agent stores it in a slot
- Agent needs information → Agent asks user and stores answer in slot
- Action needs information → Agent reads it from the slot

## Example: Account Number

**Without slots (Level 2)**:

User: "Check my balance"  
Agent: "I need your account number." The agent does not retain that intent across the next turn.  
User: "1234"  
Agent: "What account number?" It has already lost the thread of the balance request.

**With slots (Level 3)**:

User: "Check my balance"  
Agent: "What is your account number?"  
User: "1234"  
The agent stores **1234** in the **account** slot.  
Agent: "Balance for account 1234 is $123.45"

Later in the same conversation:

User: "What's my balance?"  
The agent still has **1234** in the **account** slot.  
Agent: "Balance for account 1234 is $123.45"

{Check It!|assessment}(multiple-choice-2132752574)
{Check It!|assessment}(multiple-choice-2467199161)
