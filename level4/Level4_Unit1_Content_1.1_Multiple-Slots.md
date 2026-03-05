In Level 3 you used one slot—`account`—so the bot could remember an account number for the balance check. In Level 4 you will use **multiple slots** in a single flow so the bot can remember several values at once.

## Multiple Slots = Several Values in One Flow

Think of the transfer flow:

- The user says they want to transfer money.
- The bot needs: **how much** (amount), **to whom** (recipient), and **from which account** (account_from).
- Each of these is stored in its own slot. The flow collects them one after another, then runs an action that reads all three and sends a confirmation.

So **multiple slots** means the bot keeps several named values in memory for the same conversation and uses them together in one action.

## Example: Transfer

**With one slot (Level 3 check_balance):**
```
User: "Check my balance"
Bot: "What is your account number?"
User: "1234"
Bot: [Stores 1234 in account slot] → action_check_balance_simple reads account → "Balance for 1234 is $123.45"
```

**With multiple slots (Level 4 transfer_money):**
```
User: "I want to transfer money"
Bot: "How much would you like to transfer?"
User: "50"
Bot: [Stores 50 in amount slot] "Who would you like to transfer money to?"
User: "Alice"
Bot: [Stores Alice in recipient slot] "Which account would you like to transfer from?"
User: "1234"
Bot: [Stores 1234 in account_from slot] → action_process_transfer reads amount, recipient, account_from → "Transfer of $50 from account 1234 to Alice processed."
```

You will define the three slots and three ask responses in the domain, then create the action and the flow that collect and use them.
