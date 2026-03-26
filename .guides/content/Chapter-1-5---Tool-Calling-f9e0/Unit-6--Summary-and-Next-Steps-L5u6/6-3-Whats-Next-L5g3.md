**Starting point:** Work in **`level5/`** with your Chapter 1.5 agent (the Chapter 1.4 baseline plus the labs you completed in this chapter).

Chapter 1.5 completes **tool calling** for the main agent. Possible next steps (depending on your course):

- **Chapter 1.6 (Level 6): Sub-agents.** Delegate whole tasks to a separate agent (ReAct sub-agent) that uses its own tools (for example via MCP). The main agent orchestrates; the sub-agent runs until it signals completion.
- **More tools.** Add more tool functions (for example **`close_account`**, **`list_transactions`**) and export them in **`__all__`**.
- **NLU and intents.** Refine intents and training data so the agent reliably triggers the right flows (**`transfer_money`** versus **`transfer_money_tools`**).
- **Channels.** Connect the agent to a channel and test tool calling there.

Your **`level5/`** folder is the single source for this assistant: domain, flows, actions, tools, and config. Train from **`level5/`** after any change (**`python -m rasa train`** from **`level5/`** with the project venv active).
