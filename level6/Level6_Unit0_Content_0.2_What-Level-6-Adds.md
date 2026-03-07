Level 6 adds **orchestration with sub-agents**:

1. **Sub-agent** — A separate agent (e.g. `banking_assistant`) with its own config, description, and connection to MCP tools. It runs in a ReAct loop until it signals completion.
2. **Flow that calls the sub-agent** — A flow (e.g. `ask_banking_assistant`) with a step `call: banking_assistant`. When the user asks to talk to the assistant, the main agent runs this flow; the flow delegates to the sub-agent, which runs until done, then control returns to the main agent.
3. **MCP server and registration** — The sub-agent uses tools via MCP. You register the MCP server in `endpoints.yml` and reference it in the sub-agent config.

**Order of work:** Sub-agent config (Lab 2.1) → MCP registration (Lab 3.1) → Flow that calls the sub-agent (Lab 4.1) → Train and test (Labs 5.1, 5.2).
