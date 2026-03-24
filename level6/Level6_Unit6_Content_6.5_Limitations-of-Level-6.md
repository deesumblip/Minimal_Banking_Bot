## What Level 6 Does Not Cover (in this course)

1. **Multiple sub-agents and complex routing** — You added one sub-agent and one flow. Production may use several sub-agents and routing logic; you can extend the pattern on your own.
2. **External (A2A) sub-agents** — This level uses the built-in ReAct sub-agent (RASA protocol). Other protocols (e.g. A2A) are not covered here.
3. **Slot handback and exit_if** — ReAct sub-agents can be task-specific (e.g. fill slots and return). This course uses a general-purpose sub-agent that runs until task_completed; advanced handback is not covered.
4. **MCP server implementation** — You registered an MCP server in endpoints.yml; the server implementation (e.g. mcp_server/banking.py) may be provided or simplified. Building a full MCP server from scratch is outside this level.

## When Level 6 is Sufficient

Level 6 is a good fit when you want one main agent that can delegate a full conversation to a banking assistant (or similar) sub-agent using MCP tools, with one codebase and one venv.

## When You Need More

Extend with more sub-agents, task-specific exit conditions, or external agents when your design requires them. Your Level 6 agent is the foundation.
