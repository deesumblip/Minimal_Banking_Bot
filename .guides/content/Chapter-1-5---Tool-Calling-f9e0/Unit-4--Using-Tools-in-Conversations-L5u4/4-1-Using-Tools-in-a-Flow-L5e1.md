**Starting point:** Work in **`level5/`** with **Labs 2.0, 2.1, and 3.1** complete (**`prompt_template`**, **`tools/`**, and **`tools:`** in **`endpoints.yml`**).

To use tools in a conversation, you need a **flow** that brings the user to a point where the LLM can call them. In Chapter 1.5 we do that with:

1. A **flow** that collects the same slots as **`transfer_money`** (**amount**, **recipient**, **account_from**) so the agent has context.
2. A **step** that runs one **action** (`action_process_transfer_with_tools`) in a context where the LLM can invoke tools.
3. **Domain** updates so **`from_llm`** slot mappings include **`active_flow: transfer_money_tools`** for those three slots—otherwise the new flow cannot fill them reliably. You will complete that edit in the **fill-in-the-blanks** exercise in **Lab 4.1**.

The flow does **not** list individual tools; it lists one action. That action runs in an environment where the LLM can call the registered tools (**`check_balance`**, **`process_transfer`**, **`get_account_info`**, …) based on the conversation.

## Example: The transfer_money_tools flow

Below is the flow structure you will create in **Lab 4.1**. The **`transfer_money_tools`** key is the **flow id**; it must match **`active_flow`** in the domain for the transfer slots.

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

The flow’s last step runs an **action** (not the tools directly). That action should read the collected slots and send a clear user message so you can tell this path from the classic **`action_process_transfer`** demo. **Lab 4.1** provides a full reference **`run()`** implementation (with **`tracker.get_slot`** and **`dispatcher.utter_message`**); the automated check expects that pattern, not an empty **`return []`** stub.

You also add **`action_process_transfer_with_tools`** to the domain **`actions:`** list in the same lab.

## Command-generator prompt (Lab 2.0)

You already added **`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`** in **Lab 2.0**. That template nudges the LLM to use **domain slot names** (**`amount`**, **`recipient`**, …) instead of prefixed names that do not exist in your domain. **Do not** remove or replace it while you complete **Labs 2.1–5.2** unless you are deliberately customizing the command generator (outside the scope of these labs).
