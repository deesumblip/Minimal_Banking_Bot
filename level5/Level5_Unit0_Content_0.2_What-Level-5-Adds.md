Level 5 adds **tool calling**: the LLM can dynamically select and invoke functions (tools) based on the conversation context.

You will implement in this order: **tools folder and banking_tools.py** (Lab 2.1), then **register tools in endpoints.yml** (Lab 3.1), then **the flow and action that use tools** (Lab 4.1), then **train and test** (Labs 5.1 and 5.2).

## What You'll Add

**Lab 2.1 — Tools folder.** You will create the `tools/` folder and `tools/banking_tools.py` with at least three tool functions: `check_balance(account)`, `process_transfer(amount, from_account, to_account)`, and `get_account_info(account)`. Each returns a dict; you will export them via `__all__`.

**Lab 3.1 — Register tools.** You will add a `tools:` section to `endpoints.yml` with `tools_module: "tools"` so Rasa can discover the tool functions.

**Lab 4.1 — Flow and action.** You will create the flow `data/basics/transfer_money_tools.yml` (collect amount, recipient, account_from) and the action `action_process_transfer_with_tools`. In that flow, the LLM can call the tools you defined based on what the user says.

**Lab 5.1 — Training.** You will train your Level 5 agent from the `level5` folder.

**Lab 5.2 — Testing.** You will run the completion check and test tool-calling behavior in Rasa Inspector.

**Unchanged.** All your Level 4 responses, flows, and actions stay as they are. You build Level 5 by adding these pieces.
