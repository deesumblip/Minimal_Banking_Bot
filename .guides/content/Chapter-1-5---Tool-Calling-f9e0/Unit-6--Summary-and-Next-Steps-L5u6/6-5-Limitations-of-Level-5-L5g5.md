**Starting point:** Work in **`level5/`** with your Chapter 1.5 agent.

## What Chapter 1.5 does not cover (yet)

1. **Sub-agents and multi-agent flows.** You have one main assistant that can call tools. You do not yet delegate to sub-agents or split balance vs. transfer into separate agents. **Chapter 1.6** introduces sub-agents for richer multi-agent dialogue.

2. **Advanced tool patterns.** This course uses one tools module and one flow that reaches a tool-calling action. Real systems often chain tools, branch on context, or wrap HTTP APIs—you can grow there on your own.

3. **Built-in validation and forms.** Slots stay simple (**text**, as in Chapter 1.4). You can validate in actions or tools; this chapter does not add Rasa Forms or schema-only validation.

## When Chapter 1.5 is enough

Use it when you want the LLM to pick **tools** from context while keeping **one** assistant, **one** **`tools/`** module, and the same venv layout as Chapter 1.4.

## When to move on

Choose **Chapter 1.6** when you need sub-agents, several specialized agents, or heavier orchestration. Chapter 1.5 stays the foundation; 1.6 layers sub-agents on top.
