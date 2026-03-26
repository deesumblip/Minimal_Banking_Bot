**Starting point:** Chapter 1.4 assumes you begin with the **final banking agent at the end of Chapter 1.3** (your **`level3/`** project). You **add** work in **`level4/`**—see **Unit 0.1** and **Unit 0.2**.

In Level 3 you used one slot (`account`) so the agent could remember an account number for the balance check. In Level 4 you will use **multiple slots** in a single flow so the agent can remember several values at once.

## Multiple slots: several values in one flow

Think of the transfer flow:

- The user says they want to transfer money.
- The agent needs: **how much** (amount), **to whom** (recipient), and **from which account** (account_from).
- Each of these is stored in its own slot. The flow collects them one after another, then runs an action that reads all three and sends a confirmation.

So **multiple slots** means the agent keeps several named values in memory for the same conversation and uses them together in one action.

## Example: Transfer

**One slot (Level 3 `check_balance`):**

```text
User:  "Check my balance"
Agent: "What is your account number?"
User:  "1234"
Agent: [Stores 1234 in the account slot] → action_check_balance_simple → "Balance for 1234 is $123.45"
```

**Multiple slots (Level 4 `transfer_money`):**

```text
User:  "I want to transfer money"
Agent: "How much would you like to transfer?"
User:  "50"
Agent: [Stores 50 in the amount slot] "Who would you like to transfer money to?"
User:  "Alice"
Agent: [Stores Alice in the recipient slot] "Which account would you like to transfer from?"
User:  "1234"
Agent: [Stores 1234 in the account_from slot] → action_process_transfer → "Transfer of $50 from account 1234 to Alice processed."
```

You will define the three slots and three ask responses in the domain, then add the action and the flow that collect and use them.
