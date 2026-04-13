**Starting point:** Work in **`level5/`** after **Labs 2.1–5.1** (trained model optional for read-only walkthrough).

You now have a Level 5 agent that extends Level 4 with tool calling.

## What Your Agent Can Do

- **Responses and flows:** Greet, help, contact, goodbye (responses).
- **Hours:** Bank hours (`action_bank_hours`); holiday hours (`action_holiday_hours`).
- **Check balance:** Collect `account`, `action_check_balance_simple`.
- **Transfer (classic flow):** Collect amount, recipient, account_from, `action_process_transfer`.
- **Transfer with tools:** `transfer_money_tools` — same collects, then `action_process_transfer_with_tools`; the LLM may call `check_balance`, `process_transfer`, `get_account_info`, … from the conversation.

## Flow Summary

| Flow                 | Slots collected        | Action / tools |
|----------------------|------------------------|----------------|
| check_balance        | account                | action_check_balance_simple |
| transfer_money       | amount, recipient, account_from | action_process_transfer |
| transfer_money_tools | amount, recipient, account_from | action_process_transfer_with_tools (LLM can call tools) |

All flows and actions live in the **level5** folder. You train once from `level5` and run one assistant. Use Rasa Inspector to try each flow and confirm tool calling works in the transfer_money_tools flow.
