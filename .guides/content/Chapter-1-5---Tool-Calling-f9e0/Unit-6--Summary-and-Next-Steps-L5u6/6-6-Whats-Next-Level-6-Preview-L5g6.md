**Important. Building on Your Level 5 Agent**

When you move to Level 6, you will continue with the same banking agent. Level 6 doesn't start from scratch. It adds **sub-agents** (and related patterns) on top of your existing responses, flows, actions, slots, and tools.

Your Level 5 content stays: all responses, flows, actions, slots, the tools module, and the transfer_money_tools flow. Level 6 adds the ability to use multiple agents (e.g. a main agent that can hand off to a balance agent or a transfer agent) for more structured, multi-step conversations.

---

**Level 6: Sub-Agents** extends the assistant with multiple agents that can be invoked based on context.

## What Sub-Agents Enable

**Example.** Instead of one agent handling every intent, you can have a main agent that routes to a balance-check agent or a transfer agent. Each sub-agent can have its own flows, actions, and tools. The main agent decides when to call which sub-agent.

In Level 6 you'll see how to define sub-agents and wire them into your project so the main agent can delegate to them when appropriate.

## Key Concepts in Level 6

1. **Sub-agents**. Separate agents with their own flows and possibly tools.
2. **Handoff and routing**. The main agent decides when to invoke which sub-agent.
3. **Same project**. One codebase, one venv; multiple agents in the same Rasa project.

## When to Move to Level 6

Move to Level 6 when you want multiple specialized agents, clearer separation of concerns (e.g. balance vs transfer), or more complex conversation patterns that benefit from sub-agents.

Your Level 5 banking agent is the foundation. Level 6 adds the sub-agent layer on top.
