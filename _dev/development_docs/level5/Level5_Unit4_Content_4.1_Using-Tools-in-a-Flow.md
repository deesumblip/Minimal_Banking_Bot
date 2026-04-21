**Starting point:** Work in **`level5/`** with **Labs 2.0, 2.1, and 3.1** complete (**`prompt_template`** + **`data/prompts/`**, **`tools/`**, and **`tools:`** in **`endpoints.yml`**). This page explains how a **flow** reaches a step where the LLM may call your tools; the **lab that follows** is where you implement it.

To use tools in a conversation, you need a **flow** that brings the user to a point where the LLM can call them. In Level 5 we do that with:

1. A **flow** that collects the same slots as the transfer flow (amount, recipient, account_from) so the agent has context.
2. A **step** that runs an **action** (e.g. `action_process_transfer_with_tools`) which runs in a context where the LLM can invoke tools.

The flow does not list individual tools; it lists one action. That action runs in an environment where the LLM can call the registered tools (check_balance, process_transfer, get_account_info) based on the conversation.

## Example: The transfer_money_tools flow

Below is an example of the flow file. The **lab that follows** has you create your own version (e.g. with a description that fits your agent). The structure is: collect the three slots, then run the action that enables tool calling.

```yaml
flows:
  transfer_money_tools:
    name: transfer money with tools
    description: |
      The agent collects amount, recipient, and source account.
      Then the LLM can call tools (check_balance, process_transfer, etc.)
      based on what the user says.
    steps:
      - collect: amount
        description: |
          The transfer amount in dollars. Extract from this message if the user already said it
          (same turn as starting the flow). Accept digits with or without $; commas may appear;
          phrases like "hundred" or "twenty dollars" are acceptable.
      - collect: recipient
        description: |
          Name or account identifier of who receives the money. Short reply (e.g. "Jamie" or an account number).
          Extract from this turn if they already named the recipient.
      - collect: account_from
        description: |
          Source account number or ID the money is sent from. Digits or short label;
          extract from this turn if the user already gave the source account.
      - action: action_process_transfer_with_tools
```

## Example: The action_process_transfer_with_tools action

The flow’s last step runs an **action** (not the tools directly). That action runs in a context where the LLM can call your registered tools. Below is a minimal action class. The **lab that follows** has you create your own action file following this pattern and register it in the domain.

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransferWithTools(Action):
    def name(self) -> Text:
        return "action_process_transfer_with_tools"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Optional: send a message. The LLM can call tools in this step.
        return []
```

In the **lab that follows**, you create the flow file and the action file (your own version of the examples above), and add `action_process_transfer_with_tools` to the domain `actions:` list.
