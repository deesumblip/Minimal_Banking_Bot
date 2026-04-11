Use **tools in the main agent** (Level 5) when the main flow collects slots and the LLM chooses which tool to call in that same context. Use **sub-agents** (Level 6) when you want to delegate a **whole task** to another agent that runs on its own (with its own LLM and tools) until it completes.

**Example:** "I want to talk to the banking assistant" → main agent runs the `ask_banking_assistant` flow → flow step `call: banking_assistant` → the banking assistant sub-agent handles the conversation (balance checks, transfers, questions) using MCP tools until it signals completion → control returns to the main agent.

In Level 6 you add one sub-agent (banking_assistant) and one flow (ask_banking_assistant) that calls it. You can extend the pattern later with more sub-agents and flows.
