**Starting point:** Work in **`level5/`** after **Labs 2.0–5.1** (a trained model helps but is optional for this read-only tour).

Your Chapter 1.5 agent extends **Chapter 1.4 completion** with **tool calling**.

## What your agent can do

- **Responses and flows:** Greet, help, contact, goodbye (responses).
- **Hours:** Bank hours (**`action_bank_hours`**); holiday hours (**`action_holiday_hours`**).
- **Check balance:** Collect **`account`**, **`action_check_balance_simple`**.
- **Transfer (classic flow):** Collect **amount**, **recipient**, **account_from**, **`action_process_transfer`**.
- **Transfer with tools:** **`transfer_money_tools`**—same slot collects, then **`action_process_transfer_with_tools`**; the LLM may call **`check_balance`**, **`process_transfer`**, **`get_account_info`**, … during that step.

## Flow Summary

| Flow                 | Slots collected        | Action / tools |
|----------------------|------------------------|----------------|
| check_balance        | account                | action_check_balance_simple |
| transfer_money       | amount, recipient, account_from | action_process_transfer |
| transfer_money_tools | amount, recipient, account_from | action_process_transfer_with_tools (LLM can call tools) |

Everything lives under **`level5/`**. **`transfer_money_tools`** reuses the transfer slots from **`transfer_money`**; domain **`from_llm`** mappings (including **`active_flow: transfer_money_tools`**) route slot updates to the right flow—see **Lab 4.1**.

You train once from **`level5`** and run a single assistant. In **Rasa Inspector**, use **separate conversations** (for example **New conversation**) when comparing **`transfer_money`** with **`transfer_money_tools`**.
