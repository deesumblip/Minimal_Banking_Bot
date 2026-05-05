Create `data/basics/transfer_money.yml` under `level4/` and add the following:

```yaml
flows:
  transfer_money:
    name: transfer money
    description: |
      Transfer money in USD. Steps: get dollar amount, then who receives it (any name or text), then which account to take it from, then run the transfer action.
    steps:
      - collect: amount
        description: |
          US dollar amount. Parse the user's message and set slot amount to the main number as text (e.g. 20 from "20 dollars").
      - collect: recipient
        description: |
          Transfer recipient / payee (free text).
          Extract the recipient identifier from the user's message.
          - Good examples: "Jen", "Sarah Connor", "Fred", etc.
          - If the user provides a longer sentence, extract only the recipient part (e.g. "send it to Jen please" -> "Jen").
          - If the user provides multiple recipients (e.g. "Jen or Joe"), ask again (do not guess).
      - collect: account
        ask_before_filling: true
        description: |
          A numeric account number consisting ONLY of digits (e.g., 123456, 987654321).
          CRITICAL: Do NOT extract this slot unless the user explicitly provides numbers.
          Do NOT extract from phrases like "account balance", "check account", "my account".
          Only extract when the user says actual digits like "123456" or "my account number is 789012".
      - action: action_process_transfer
```

Remember: `account` has `ask_before_filling: true` because `check_balance` persists that slot, without it, a returning user's account would be silently reused. `amount` and `recipient` have no such risk, so they fill immediately if provided upfront.

Another way to enhance the conversation design of this flow would be to confirm with the user that everything has been properly collected before submitting the money transfer request - something to try building in after you have completed this course. 


**Use Check It!** below when done.

{Check It!|assessment}(code-output-compare-401040001)
