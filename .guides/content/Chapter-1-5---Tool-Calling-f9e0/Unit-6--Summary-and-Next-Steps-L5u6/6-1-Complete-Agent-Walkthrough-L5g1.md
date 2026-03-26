**Starting point:** Work in **`level5/`** after **Labs 2.1–5.1** (trained model optional for read-only walkthrough).

You now have a Chapter 1.5 agent that extends **Chapter 1.4 completion** with **tool calling**.

## What your agent can do

- **Chapter 1.1:** Greet, help, contact, goodbye (responses).
- **Chapter 1.2:** Bank hours (**`action_bank_hours`**); holiday hours (**`action_holiday_hours`**).
- **Chapter 1.3:** Check balance (collect **`account`**, **`action_check_balance_simple`**).
- **Chapter 1.4:** Transfer money (collect **amount**, **recipient**, **account_from**, **`action_process_transfer`**).
- **Chapter 1.5:** **`transfer_money_tools`**—same collects, then **`action_process_transfer_with_tools`**; the LLM may call **`check_balance`**, **`process_transfer`**, **`get_account_info`**, … from the conversation.

## Flow Summary

| Flow                 | Slots collected        | Action / tools |
|----------------------|------------------------|----------------|
| check_balance        | account                | action_check_balance_simple |
| transfer_money       | amount, recipient, account_from | action_process_transfer |
| transfer_money_tools | amount, recipient, account_from | action_process_transfer_with_tools (LLM can call tools) |

All flows and actions live under **`level5/`**. You train once from **`level5`** and run one assistant. Use **Rasa Inspector** to try each flow and confirm tool calling in **`transfer_money_tools`**.
