Level 3 used one `collect:` step to gather a single value before running an action. The same pattern scales to multiple slots: the flow collects each value in order, stores them, and passes all of them to the action at the end.
 
The transfer flow needs three values: the account number, how much to transfer, and who receives it. `account` already exists from Level 3. You add `amount` and `recipient`. The flow collects all three in order, then runs `action_process_transfer`.
 
```text
User:  "I want to transfer money"
Agent: "What is your account number?"
User:  "1234"
Agent: "How much would you like to transfer?"
User:  "50"
Agent: "Who would you like to transfer money to?"
User:  "Alice"
Agent: "Transfer of $50 from account 1234 to Alice processed."
```
 
If the user already checked their balance earlier in the same session, `account` is already set. The flow skips asking for it and goes straight to amount. This is slot persistence working across flows.
 
The same three rules from Level 3 apply: define each slot in the domain, collect it in the flow, read it in the action.
