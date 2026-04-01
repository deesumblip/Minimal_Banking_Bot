**Starting point:** Work in **`level5/`** with your finished Chapter 1.5 agent.

What you do next depends on your course; common paths include:

- **Chapter 1.6 (Level 6): Sub-agents.** Hand off whole tasks to another agent (for example a ReAct sub-agent with its own tools, including via MCP). The main agent coordinates; the sub-agent runs until it finishes.
- **More tools.** Add functions such as **`close_account`** or **`list_transactions`** and list them in **`__all__`**.
- **NLU and intents.** Tune intents and stories so the right flow fires (**`transfer_money`** vs **`transfer_money_tools`**).
- **Channels.** Plug the assistant into a channel and test tool calling end-to-end.

Treat **`level5/`** as the single source: domain, flows, actions, tools, config. After edits, train from **`level5/`** with the project venv (**`python -m rasa train`**).
