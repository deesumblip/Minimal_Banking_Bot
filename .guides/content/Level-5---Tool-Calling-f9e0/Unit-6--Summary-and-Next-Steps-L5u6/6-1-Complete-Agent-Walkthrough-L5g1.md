**Starting point:** Work in **`level5/`** after **Labs 2.0–5.1** (a trained model helps but is optional for this read-only tour).

Your Level 5 agent extends **Level 4 completion** with **tool calling**. **Unit 0.1** has the Level 4 inventory. **Unit 0.2** has the Level 5 lab table. This page is a **flow-level tour**, not a second copy of those lists.

## What your agent can do

- **Responses and flows:** Greet, help, contact, goodbye (responses).
- **Hours:** Bank hours (**`action_bank_hours`**). Holiday hours (**`action_holiday_hours`**).
- **Check balance:** Collect **`account`**, **`action_check_balance_simple`**.
- **Transfer (classic flow):** Collect **amount**, **recipient**, **account_from**, **`action_process_transfer`**.
- **Transfer with tools:** **`transfer_money_tools`**. Same slot collects, then **`action_process_transfer_with_tools`**. The LLM may call **`check_balance`**, **`process_transfer`**, **`get_account_info`**, … during that step.

## Flow Summary

| Flow                 | Slots collected        | Action / tools |
|----------------------|------------------------|----------------|
| check_balance        | account                | action_check_balance_simple |
| transfer_money       | amount, recipient, account_from | action_process_transfer |
| transfer_money_tools | amount, recipient, account_from | action_process_transfer_with_tools (LLM can call tools) |

Everything lives under **`level5/`**. **`transfer_money_tools`** reuses the transfer slots from **`transfer_money`**. Domain **`from_llm`** mappings. Including **`active_flow: transfer_money_tools`**. Route slot updates to the right flow (see **Lab 4.1**).

You train once from **`level5/`** and run a single assistant. In **Rasa Inspector**, use **separate conversations** (for example **New conversation**) when comparing **`transfer_money`** with **`transfer_money_tools`**.
