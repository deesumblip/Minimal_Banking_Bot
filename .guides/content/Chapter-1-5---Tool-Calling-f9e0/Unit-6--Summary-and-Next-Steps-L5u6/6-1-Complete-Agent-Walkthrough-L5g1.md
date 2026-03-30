**Starting point:** Work in **`level5/`** after **Labs 2.1–5.1** (trained model optional for read-only walkthrough).

You now have a Chapter 1.5 agent that extends **Chapter 1.4 completion** with **tool calling**.

## What your agent can do

- **Responses and flows:** Greet, help, contact, goodbye (responses).
- **Hours:** Bank hours (**`action_bank_hours`**); holiday hours (**`action_holiday_hours`**).
- **Check balance:** Collect **`account`**, **`action_check_balance_simple`**.
- **Transfer (classic flow):** Collect **amount**, **recipient**, **account_from**, **`action_process_transfer`**.
- **Transfer with tools:** **`transfer_money_tools`**—same collects, then **`action_process_transfer_with_tools`**; the LLM may call **`check_balance`**, **`process_transfer`**, **`get_account_info`**, … from the conversation.

## Flow Summary

| Flow                 | Slots collected        | Action / tools |
|----------------------|------------------------|----------------|
| check_balance        | account                | action_check_balance_simple |
| transfer_money       | amount, recipient, account_from | action_process_transfer |
| transfer_money_tools | amount, recipient, account_from | action_process_transfer_with_tools (LLM can call tools) |

All flows and actions live under **`level5/`**. The **`transfer_money_tools`** flow shares the transfer slots with **`transfer_money`**; your domain **`from_llm`** mappings (including **`active_flow: transfer_money_tools`**) are what let the assistant fill those slots in the right flow—see **Lab 4.1**.

You train once from **`level5`** and run one assistant. Use **Rasa Inspector** to try each flow: run **`transfer_money`** and **`transfer_money_tools`** in **separate conversations** (for example **New conversation**) if you want a clean comparison between the classic transfer action and the tool-enabled path.
