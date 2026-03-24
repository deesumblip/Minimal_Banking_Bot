Level 5 completes tool calling for the main agent. Possible next steps (depending on your course):

- **Level 6: Sub-agents**, Delegate whole tasks to a separate agent (ReAct sub-agent) that uses its own tools (e.g. via MCP). The main agent orchestrates; the sub-agent runs until it signals completion.
- **More tools**, Add more tool functions (e.g. close_account, list_transactions) and export them in `__all__`.
- **NLU and intents**, Refine intents and training data so the agent reliably triggers the right flows (e.g. transfer_money vs. transfer_money_tools).
- **Channels**, Connect the agent to a channel and test tool calling there.

Your **level5** folder is the single source for this assistant: domain, flows, actions, tools, and config. Keep training from `level5` after any change.
