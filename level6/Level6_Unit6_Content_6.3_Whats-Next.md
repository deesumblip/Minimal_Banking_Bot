Possible next steps after Level 6:

- **More sub-agents** — Add other specialized agents (e.g. support, loans) and flows that call them.
- **Task-specific sub-agents** — Use exit conditions and slot handback for sub-agents that fill slots and return to the main flow.
- **NLU and intents** — Refine intents and training data so the agent reliably triggers ask_banking_assistant vs other flows.
- **Channels and deployment** — Connect the agent to channels and deploy with MCP server and Rasa in the same environment.

Your Level 6 banking agent is a full orchestration example: one main agent that can delegate to a ReAct sub-agent with MCP tools.
