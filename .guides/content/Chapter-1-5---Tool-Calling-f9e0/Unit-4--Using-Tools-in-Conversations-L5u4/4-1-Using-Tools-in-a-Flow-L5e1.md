**Starting point:** Work in **`level5/`** with **`tools/`** registered ( **Labs 2.1–3.1** ). This page explains how a **flow** reaches a step where the LLM may call your tools; you implement it in **Lab 4.1**.

To use tools in a conversation, you need a **flow** that brings the user to a point where the LLM can call them. In Chapter 1.5 we do that with:

1. A **flow** that collects the same slots as **`transfer_money`** (**amount**, **recipient**, **account_from**) so the agent has context.
2. A **step** that runs one **action** (`action_process_transfer_with_tools`) in a context where the LLM can invoke tools.

The flow does **not** list individual tools; it lists one action. That action runs in an environment where the LLM can call the registered tools (**`check_balance`**, **`process_transfer`**, **`get_account_info`**, …) based on the conversation.

## Example: The transfer_money_tools flow

Below is an example of the flow file. You will create your own version in **Lab 4.1** (for example with a **description** that fits your agent). The structure is: collect the three slots, then run the action that enables tool calling.

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
        description: "transfer amount"
      - collect: recipient
        description: "recipient name or account"
      - collect: account_from
        description: "source account number"
      - action: action_process_transfer_with_tools
```

## Example: The action_process_transfer_with_tools action

The flow’s last step runs an **action** (not the tools directly). That action runs in a context where the LLM can call your registered tools. Below is a minimal action class. You will create your own action file in Lab 4.1 following this pattern and register it in the domain.

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

In **Lab 4.1** you will create the flow file and the action file (your own version of the examples above), and add **`action_process_transfer_with_tools`** to the domain **`actions:`** list.
