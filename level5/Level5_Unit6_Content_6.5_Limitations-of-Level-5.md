**Work in \`level5/\`:** These limits apply to the **`level5/`** banking agent.

## What Level 5 Cannot Do (Yet)

1. **Sub-agents and multi-agent flows.** Level 5 has one main agent that can call tools. It does not yet use sub-agents or hand off to specialized agents (e.g. separate balance vs transfer agents). Level 6 adds sub-agents so you can structure more complex conversations with multiple agents.

2. **Advanced tool patterns.** This level uses a single tools module and one flow that invokes an action in a tool-calling context. Production setups may use tool chains, conditional tool selection, or tools that call external APIs; you can extend Level 5 in that direction on your own.

3. **Built-in validation and forms.** As in Level 4, slots are simple (e.g. text). You can add validation in your action or tool code, but Level 5 does not introduce Rasa forms or schema-based validation.

## When Level 5 is Sufficient

Level 5 is a good fit when you want the LLM to dynamically choose and call functions (tools) based on what the user said, while keeping one main agent, one tools module, and the same venv and project structure as Level 4.

## When You Need More

Move to Level 6 when you want sub-agents, multiple specialized agents, or more complex multi-agent conversation patterns. Your Level 5 agent remains the base; Level 6 adds the sub-agent layer on top.
