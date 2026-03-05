**Important. Building on Your Existing Banking Bot**

When you move to Level 5, you will continue working on the same banking bot you've built throughout Levels 1–4. Level 5 doesn't start from scratch. It adds **tool calling** on top of your existing responses, flows, actions, and slots.

Your existing Level 4 content stays: all responses, flows, actions, and slots (including the transfer flow). Level 5 adds a tools module, registration in endpoints, and flows/actions that use those tools so the LLM can invoke them.

---

**Level 5: Tool Calling** lets the assistant call functions (tools) based on the conversation.

## What Tool Calling Enables

**Example.** Instead of only running a fixed action that reads slots, the assistant can call tools such as `check_balance(account)` or `process_transfer(amount, from_account, to_account)`. You define these as Python functions; Rasa discovers them and the LLM can choose when to call them.

In Level 5 you'll add a `tools/` folder with tool functions, register them in `endpoints.yml`, and create a flow and action that use tool calling. Your Level 4 transfer flow and actions remain; Level 5 adds the tool-calling layer.

## Key Concepts in Level 5

1. **Tools module** — Python functions that the assistant can invoke.
2. **Registration** — Tools are registered so Rasa and the LLM know they exist.
3. **Flow and action** — A flow can collect slots and an action can call tools based on context.

## When to Move to Level 5

Move to Level 5 when you want the assistant to dynamically call functions (tools) based on what the user said, or when you want to structure banking operations as reusable tools.

Your Level 4 banking bot is the foundation. Level 5 adds tool calling on top of it.
