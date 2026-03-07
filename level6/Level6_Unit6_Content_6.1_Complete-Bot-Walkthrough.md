Your Level 6 bot supports everything from Level 5 plus **orchestration**:

- **Level 1–4:** Greet, help, contact, goodbye, bank hours, check balance, transfer (with slots and action).
- **Level 5:** transfer_money_tools flow; LLM can call tools in that flow.
- **Level 6:** When the user asks to talk to the banking assistant, the main agent runs the **ask_banking_assistant** flow. That flow has a step `call: banking_assistant`. The **banking_assistant** sub-agent (ReAct + MCP tools) runs until it signals completion; then control returns to the main flow (e.g. utter_help).

All flows and the sub-agent live in the **level6** folder. You train once from `level6`. To run the full setup you start the MCP server, action server, and Rasa, then use Inspector to trigger the ask_banking_assistant flow.
