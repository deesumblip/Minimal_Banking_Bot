To use tools in a conversation, you need a **flow** that brings the user to a point where the LLM can call them. In Level 5 we do that with:

1. A **flow** that collects the same slots as the transfer flow (amount, recipient, account_from) so the bot has context.
2. A **step** that runs an **action** (e.g. `action_process_transfer_with_tools`) which runs in a context where the LLM can invoke tools.

The flow does not list individual tools; it lists one action. That action runs in an environment where the LLM can call the registered tools (check_balance, process_transfer, get_account_info) based on the conversation.

## transfer_money_tools.yml

Create a flow (e.g. `data/basics/transfer_money_tools.yml`) with:

- **name** and **description** (e.g. "transfer money with tools" — the description helps the LLM understand when to trigger this flow).
- **steps**: collect amount, collect recipient, collect account_from, then `action: action_process_transfer_with_tools`.

## action_process_transfer_with_tools

Create an action class that runs in a context where the LLM can call tools. The action can send a message and then let the LLM use the tools (e.g. to check balance or process the transfer) based on what the user said. In Lab 4.1 you will create this flow file and the action file, and register the action in the domain.
