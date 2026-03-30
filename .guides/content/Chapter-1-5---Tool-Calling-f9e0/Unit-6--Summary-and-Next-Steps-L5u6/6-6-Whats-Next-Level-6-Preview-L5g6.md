**Starting point:** After this chapter’s labs in **`level5/`**, you can preview what comes next.

**Building on Chapter 1.5**

**Chapter 1.6** continues the **same** banking project. It does **not** reset the repo. It layers **sub-agents** on your current responses, flows, actions, slots, and tools.

You keep everything you built: responses, flows, actions, slots, **`tools/`**, and **`transfer_money_tools`**. Chapter 1.6 adds **multiple agents**—for example a main assistant that can hand off to a balance-focused or transfer-focused agent—for clearer, longer-running dialogue.

---

**Chapter 1.6 (Level 6): Sub-agents** lets more than one agent participate in the same project.

## What sub-agents enable

**Example.** A main agent can route to a balance specialist or a transfer specialist. Each sub-agent may own its own flows, actions, and tools. The main agent chooses when to delegate.

Chapter 1.6 shows how to define sub-agents and wire them so delegation works.

## Core ideas in Chapter 1.6

1. **Sub-agents.** Distinct agents with their own flows and optionally tools.
2. **Handoff and routing.** The main agent selects which sub-agent to invoke.
3. **One project.** Same codebase and venv; several agents in one Rasa app.

## When to open Chapter 1.6

Open it when you need several specialized agents, cleaner separation (balance vs. transfer), or orchestration that a single assistant cannot express cleanly.

Chapter 1.5 remains the base; 1.6 adds the sub-agent layer.
