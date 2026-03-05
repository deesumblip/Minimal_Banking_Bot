You now have a Level 4 bot that extends Level 3 with a transfer flow.

## What Your Bot Can Do

- **Level 1:** Greet, help, contact, goodbye (responses only).
- **Level 2:** Bank hours (action_bank_hours).
- **Level 3:** Check balance — collect account number, then run action_check_balance_simple.
- **Level 4:** Transfer money — collect amount, recipient, and account_from, then run action_process_transfer and send a confirmation.

## Flow Summary

| Flow          | Slots collected        | Action                      |
|---------------|------------------------|-----------------------------|
| check_balance | account                | action_check_balance_simple |
| transfer_money| amount, recipient, account_from | action_process_transfer |

All flows and actions live in the **level4** folder. You train once from `level4` and run one assistant that supports all of these flows. Use Rasa Inspector to try each flow and confirm slots are collected and used correctly.
