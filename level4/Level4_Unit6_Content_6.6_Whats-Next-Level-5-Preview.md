**Starting point:** Chapter 1.4 assumed you began with the **final banking agent at the end of Chapter 1.3**; you then **added** the transfer flow in **`level4/`** (see **Unit 0.1**).

### Building on your existing banking agent

When you move to Level 5, you keep working on the same banking agent you built in Levels 1–4. Level 5 does not start from scratch. It adds **tool calling** on top of your existing responses, flows, actions, and slots.

Your existing Level 4 content stays: all responses, flows, actions, and slots (including the transfer flow). Level 5 adds a tools module, registration in endpoints, and flows/actions that use those tools so the LLM can invoke them.

---

## Level 5: Tool calling

Tool calling lets the assistant invoke registered functions based on the conversation.

### What tool calling enables

Instead of only running a fixed action that reads slots, the assistant can call tools such as `check_balance(account)` or `process_transfer(amount, from_account, to_account)`. You define these as Python functions; Rasa discovers them and the LLM can choose when to call them.

In Level 5 you add a `tools/` folder with tool functions, register them in `endpoints.yml`, and add flows or actions that use tool calling. Your Level 4 transfer flow and actions stay in place; Level 5 adds the tool-calling layer on top.

### Key ideas

1. **Tools module** — Python functions the assistant can invoke.
2. **Registration** — Tools are registered so Rasa and the LLM know they exist.
3. **Flow and action** — A flow can collect slots; an action can call tools based on context.

### When to move to Level 5

Move on when you want the assistant to choose and run functions dynamically from what the user said, or when you want banking operations structured as reusable tools. Your Level 4 agent remains the foundation.
