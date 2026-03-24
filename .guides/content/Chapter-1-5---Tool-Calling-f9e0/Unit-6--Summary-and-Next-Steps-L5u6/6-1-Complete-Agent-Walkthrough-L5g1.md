You now have a Level 5 agent that extends Level 4 with tool calling.

## What Your Agent Can Do

- **Level 1:** Greet, help, contact, goodbye (responses only).
- **Level 2:** Bank hours (action_bank_hours).
- **Level 3:** Check balance (collect account, action_check_balance_simple).
- **Level 4:** Transfer money (collect amount, recipient, account_from, action_process_transfer).
- **Level 5:** Transfer with tools, collect amount, recipient, account_from, then run action_process_transfer_with_tools; the LLM can call check_balance, process_transfer, get_account_info based on the conversation.

## Flow Summary

| Flow                 | Slots collected        | Action / tools |
|----------------------|------------------------|----------------|
| check_balance        | account                | action_check_balance_simple |
| transfer_money       | amount, recipient, account_from | action_process_transfer |
| transfer_money_tools | amount, recipient, account_from | action_process_transfer_with_tools (LLM can call tools) |

All flows and actions live in the **level5** folder. You train once from `level5` and run one assistant. Use Rasa Inspector to try each flow and confirm tool calling works in the transfer_money_tools flow.
