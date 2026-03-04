# Level 6: Sub-Agents

**Final bot** students have by the end of Level 6.

## Contents

- Everything from Level 5 (slots, responses, actions, tools, flows: greet, help, contact, goodbye, hours, check_balance, transfer_money, transfer_money_tools).
- **Sub-agent:** `sub_agents/banking_assistant/` (ReAct sub-agent with LLM and MCP tools).
- **MCP server:** `mcp_server/banking.py` (exposes check_balance, process_transfer, get_account_info).
- **Flow:** `ask_banking_assistant` — delegates to the banking assistant sub-agent via `call: banking_assistant`.
- **Config:** `endpoints.yml` includes `mcp_servers` entry for `banking_mcp` at http://localhost:8080.

## What this bot can do

- Everything Level 5 can do (greet, help, contact, goodbye, bank hours, check balance, transfer, transfer with tools).
- **Orchestration:** When the user asks to talk to the banking assistant, the main agent runs the `ask_banking_assistant` flow, which **calls** the ReAct sub-agent. The sub-agent (LLM-powered) uses MCP tools (check_balance, process_transfer, get_account_info) and runs until it signals completion with `task_completed`.

## How to run

1. **Terminal 1 — MCP server:**  
   From this folder: `python mcp_server/banking.py`  
   (Listens on http://localhost:8080.)

2. **Terminal 2 — Action server:**  
   `rasa run actions`

3. **Terminal 3 — Rasa:**  
   `rasa run` or `rasa inspect`  
   Open Inspector (e.g. http://localhost:5005/webhooks/socketio/inspect.html). Trigger the "ask banking assistant" flow to talk to the sub-agent.

Set `RASA_LICENSE` and `OPENAI_API_KEY` in the environment (e.g. `.env` or `load_env.ps1`) before running.
