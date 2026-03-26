**Starting point:** Chapter 1.4 assumes you began with the **final banking agent at the end of Chapter 1.3** and extended it in **`level4/`** (see **Unit 0.1**).

## What Level 4 Cannot Do

1. **Tool calling.** The agent cannot yet call external tools or functions chosen dynamically by the LLM based on what the user said. Level 5 adds tool calling so the assistant can invoke functions (e.g. check balance, process transfer) as tools.

2. **Rich validation and forms.** Level 4 uses simple text slots and optional placeholder checks in actions. It does not use Rasa forms or built-in validation for formats (e.g. amount as number, account pattern). You can add validation in your action code; Level 5 and beyond can integrate tools and more structure.

3. **Dynamic flow selection.** Flows are fixed in the project; the agent does not create new flows at runtime. Level 4 is well-suited to predefined flows that collect a known set of slots.

## When Level 4 is Sufficient

Level 4 is a good fit when you need to collect several pieces of information in one conversation (e.g. amount, recipient, account for a transfer), run one action that uses all of them, and keep the same venv and project structure as Level 3.

## When You Need More

Move to Level 5 when you want the LLM to call tools (e.g. check balance, process transfer) as invocable functions, or when you want to structure your logic as tools that the assistant can select and run based on context.
