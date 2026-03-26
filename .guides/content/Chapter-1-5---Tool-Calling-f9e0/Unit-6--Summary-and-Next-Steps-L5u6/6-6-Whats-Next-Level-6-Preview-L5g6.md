**Starting point:** After completing this chapter’s labs in **`level5/`**, you are ready to preview the next chapter.

**Building on your Chapter 1.5 agent**

When you move to **Chapter 1.6**, you continue with the same banking agent. Chapter 1.6 does **not** start from scratch. It adds **sub-agents** (and related patterns) on top of your existing responses, flows, actions, slots, and tools.

Your Chapter 1.5 content stays: all responses, flows, actions, slots, the **`tools/`** module, and **`transfer_money_tools`**. Chapter 1.6 adds multiple agents (for example a main agent that can hand off to a balance agent or a transfer agent) for more structured, multi-step conversations.

---

**Chapter 1.6 (Level 6): Sub-agents** extends the assistant with multiple agents that can be invoked based on context.

## What Sub-Agents Enable

**Example.** Instead of one agent handling every intent, you can have a main agent that routes to a balance-check agent or a transfer agent. Each sub-agent can have its own flows, actions, and tools. The main agent decides when to call which sub-agent.

In Chapter 1.6 you will define sub-agents and wire them into your project so the main agent can delegate when appropriate.

## Key concepts in Chapter 1.6

1. **Sub-agents.** Separate agents with their own flows and possibly tools.
2. **Handoff and routing.** The main agent decides when to invoke which sub-agent.
3. **Same project.** One codebase, one venv; multiple agents in the same Rasa project.

## When to move to Chapter 1.6

Move when you want multiple specialized agents, clearer separation of concerns (for example balance versus transfer), or more complex conversation patterns that benefit from sub-agents.

Your Chapter 1.5 banking agent is the foundation. Chapter 1.6 adds the sub-agent layer on top.
