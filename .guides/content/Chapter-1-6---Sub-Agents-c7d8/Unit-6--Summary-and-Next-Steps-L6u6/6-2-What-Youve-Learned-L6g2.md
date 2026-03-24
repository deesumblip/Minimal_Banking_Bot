In Level 6 you added:

1. **Sub-agent config (Lab 2.1)**, `sub_agents/banking_assistant/config.yml` with agent name, protocol (RASA), description, LLM config, and mcp_servers reference.
2. **MCP registration (Lab 3.1)**, `mcp_servers:` in endpoints.yml with name, url, and type so the sub-agent can use the MCP tools.
3. **Flow that calls the sub-agent (Lab 4.1)**, `ask_banking_assistant.yml` with a step `call: banking_assistant` and optional follow-up action.
4. **Training and testing (Labs 5.1, 5.2)**. Train from level6; run completion check and optionally test in Inspector.

The main agent orchestrates: it runs a flow that **calls** the sub-agent; the sub-agent runs autonomously until it completes, then control returns to the main agent.
