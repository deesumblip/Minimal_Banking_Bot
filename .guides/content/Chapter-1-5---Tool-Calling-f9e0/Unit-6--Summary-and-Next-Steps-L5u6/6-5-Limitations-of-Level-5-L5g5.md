**Starting point:** Work in **`level5/`** (see **Unit 0.1**).

## What Chapter 1.5 cannot do (yet)

1. **Sub-agents and multi-agent flows.** Chapter 1.5 has one main agent that can call tools. It does not yet use sub-agents or hand off to specialized agents (for example separate balance versus transfer agents). Chapter 1.6 adds sub-agents so you can structure more complex conversations with multiple agents.

2. **Advanced tool patterns.** This chapter uses a single tools module and one flow that invokes an action in a tool-calling context. Production setups may use tool chains, conditional tool selection, or tools that call external APIs; you can extend your agent in that direction on your own.

3. **Built-in validation and forms.** As in Chapter 1.4, slots are simple (for example **text**). You can add validation in your action or tool code; Chapter 1.5 does not introduce Rasa forms or schema-based validation.

## When Chapter 1.5 is sufficient

Chapter 1.5 is a good fit when you want the LLM to dynamically choose and call **tools** based on what the user said, while keeping one main agent, one **`tools/`** module, and the same venv and project structure as Chapter 1.4.

## When you need more

Move to **Chapter 1.6** when you want sub-agents, multiple specialized agents, or more complex multi-agent conversation patterns. Your Chapter 1.5 agent remains the base; Chapter 1.6 adds the sub-agent layer on top.
