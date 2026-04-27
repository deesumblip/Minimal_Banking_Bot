A slot is Rasa's memory variable. It stores a value from the conversation and makes it available to later steps, later turns, and other flows.
 
Without a slot:
 
> **User:** Check my balance.
> **Agent:** What's your account number?
> **User:** 1234
> **Agent:** What account number?
 
The agent had no place to put it.
 
With a slot:
 
> **User:** Check my balance.
> **Agent:** What's your account number?
> **User:** 1234
> **Agent:** Balance for account 1234 is $123.45.
 
Later:
 
> **User:** Can I transfer some money?
> **Agent:** How much would you like to transfer from account 1234?
 
The agent already has the account number. It doesn't ask again.
 
By the end of this level, your agent will ask for an account number, store it, and pass it to an action that returns a balance.

{Check It!|assessment}(multiple-choice-2132752574)
{Check It!|assessment}(multiple-choice-2467199161)
---
