To use tools in a conversation, you need a **flow** that brings the user to a point where the LLM can call them. In Level 5 we do that with:

1. A **flow** that collects the same slots as the transfer flow (amount, recipient, account_from) so the bot has context.
2. A **step** that runs an **action** (e.g. `action_process_transfer_with_tools`) which runs in a context where the LLM can invoke tools.

The flow does not list individual tools; it lists one action. That action runs in an environment where the LLM can call the registered tools (check_balance, process_transfer, get_account_info) based on the conversation.

## transfer_money_tools.yml

Create a flow (e.g. `data/basics/transfer_money_tools.yml`) with:

- **name** and **description** (e.g. "transfer money with tools" — the description helps the LLM understand when to trigger this flow).
- **steps**: collect amount, collect recipient, collect account_from, then `action: action_process_transfer_with_tools`.

## action_process_transfer_with_tools

Create an action class that runs in a context where the LLM can call tools. Rasa discovers the tools you registered in `endpoints.yml` and makes them available when this action runs; the LLM can then choose to invoke them (e.g. check_balance, process_transfer) based on the conversation. In this course the action uses a **minimal implementation**: it reads the collected slots, optionally validates them, and sends a demo confirmation message. In production you might also call the tool functions from Python or rely on the framework to let the LLM invoke them. In Lab 4.1 you will create this flow file and the action file (using the template below), and register the action in the domain.
