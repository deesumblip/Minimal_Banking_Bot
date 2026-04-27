Your Level 2 agent can run custom Python and look things up. But it won't remember anything once a turn ends. 

If you were to try this interaction with the agent you built so far:

> **User:** Check my balance.
> **Agent:** ...

The agent can't answer because it doesn't know which account the user wants to check, and it has no way to ask, remember the reply, and carry that forward.

That's the gap Level 3 closes. Rasa can store values from the conversation and use them later: ask for an account number, hold onto it, pass it to an action when the time comes. That's what memory gives you, without any manual state management on your part.

By the end of this level, your agent will ask for an account number, store it, and hand it to an action that returns a balance. Everything from Level 2 stays, you're adding one slot, one response, one action, and one flow. Like each the two levels prior, you'll build, train, and test just like you would in a Rasa project. 