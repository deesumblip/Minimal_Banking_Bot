# Level 6: Sub-Agents

This folder is your **Level 6 starter**. It contains everything you need to get started with the Level 6 exercises.

## What you have to start (Level 5 end state)

- **Domain, config, credentials:** Same as Level 5 (slots, responses, actions, tools).
- **Flows:** greet, help, contact, goodbye, hours, check_balance, transfer_money, transfer_money_tools.
- **Actions:** action_bank_hours, action_check_balance_simple, action_process_transfer, action_process_transfer_with_tools.
- **Tools:** `tools/banking_tools.py` (check_balance, process_transfer, get_account_info), registered in `endpoints.yml`.
- **MCP server code:** `mcp_server/` is included so you can run the banking MCP server once you have registered it in Lab 3.1.

You can **train and run** this bot from the level6 folder (activate the project-root venv, then `cd level6`, then `rasa train` / `rasa run actions` / `rasa run` or `rasa inspect`).

## What you add in the Level 6 labs

- **Lab 2.1:** Create `sub_agents/banking_assistant/config.yml` (sub-agent config).
- **Lab 3.1:** Add `mcp_servers:` to `endpoints.yml` (so the sub-agent can use the MCP server).
- **Lab 4.1:** Create `data/basics/ask_banking_assistant.yml` (flow that calls the sub-agent).
- **Labs 5.1–5.2:** Train and run the completion check.

After you complete the labs, the bot will support **orchestration**: when the user asks to talk to the banking assistant, the main agent runs the `ask_banking_assistant` flow, which calls the ReAct sub-agent; the sub-agent uses MCP tools until it signals completion, then control returns to the main flow.

## How to run (after the labs)

1. **MCP server:** From level6: `python mcp_server/banking.py` (or the script that starts the banking MCP server on the URL you set in `endpoints.yml`).
2. **Action server:** From level6: `rasa run actions`.
3. **Rasa:** From level6: `rasa run` or `rasa inspect`. Open Inspector and trigger the "ask banking assistant" flow.

Set `RASA_LICENSE` (and `OPENAI_API_KEY` if required by your model config) in the environment before running.
