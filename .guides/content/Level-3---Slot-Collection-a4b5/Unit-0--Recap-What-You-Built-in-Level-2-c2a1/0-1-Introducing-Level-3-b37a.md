Your Level 2 agent can run custom Python and look things up. It cannot remember anything between turns.

> **User:** Check my balance.
> **Agent:** What is your account number?
> **User:** 1234
> **Agent:** What account number?

The agent had no place to put it. That is the gap Level 3 closes. Rasa stores values from the conversation and makes them available to later steps, later turns, and other flows.

> **User:** Check my balance.
> **Agent:** What is your account number?
> **User:** 1234
> **Agent:** The balance for account 1234 is $123.45.

Later in the same session:

> **User:** Can I transfer some money?
> **Agent:** How much would you like to transfer from account 1234?

By the end of this level, your agent will ask for an account number, store it, and pass it to an action that returns a balance. You are adding your first slot, a new action, and one flow on top of everything from Level 2.

---