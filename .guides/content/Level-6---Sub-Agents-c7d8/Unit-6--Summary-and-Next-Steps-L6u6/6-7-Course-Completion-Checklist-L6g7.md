Before considering the course complete, ensure you can:

- Explain what a **sub-agent** is and how a flow step **call: agent_name** works (hand off, run until complete, return control).
- Create a **sub-agent config** in `sub_agents/<name>/config.yml` (agent name, protocol, description, LLM, **`configuration.module`** for **`BankingAssistantLiteAgent`**, mcp_servers).
- Add **mcp_servers** to **endpoints.yml** (name, url including **`/mcp`** for this repo’s server, type) so the sub-agent can use MCP tools.
- Create a **flow** that includes a step **call: banking_assistant** (and optionally a follow-up action).
- **Train** the Level 6 agent from the level6 folder and run the **completion check** (Lab 5.2).
- Optionally **test** the ask_banking_assistant flow in Inspector (with MCP server and action server running) and confirm the sub-agent runs.

If you can do all of the above, you have completed Level 6 and the course.
