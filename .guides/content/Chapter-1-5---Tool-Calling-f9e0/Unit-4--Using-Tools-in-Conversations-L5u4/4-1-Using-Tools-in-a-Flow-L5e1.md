**Starting point:** Work in **`level5/`** with **Labs 2.0, 2.1, and 3.1** done (**`prompt_template`**, **`tools/`**, **`tools:`** in **`endpoints.yml`**).

To use tools in dialogue, you need a **flow** that reaches a step where the LLM may call them. In Chapter 1.5 that means:

1. A **flow** that collects the same slots as **`transfer_money`** (**amount**, **recipient**, **account_from**) so context is available.
2. A **step** that runs one **action** (`action_process_transfer_with_tools`) in a tool-calling context.
3. **Domain** updates so **`from_llm`** mappings include **`active_flow: transfer_money_tools`** for those three slots—without that, the new flow will not fill slots reliably. **Lab 4.1** includes the fill-in-the-blanks for those conditions.

The flow never names individual tools; it names one **action**. That action runs where the LLM can still call registered tools (**`check_balance`**, **`process_transfer`**, **`get_account_info`**, …) as the conversation unfolds.

## Example: The transfer_money_tools flow

Below is the structure you build in **Lab 4.1**. The **`transfer_money_tools`** key is the **flow id**; it must match **`active_flow`** in the domain for the transfer slots.

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

The last step runs an **action**, not the tools directly. That action should read the collected slots and **utter** something distinct from the classic **`action_process_transfer`** path. **Lab 4.1** gives a reference **`run()`** using **`tracker.get_slot`** and **`dispatcher.utter_message`**; the grader expects that style, not an empty **`return []`** stub.

You also list **`action_process_transfer_with_tools`** under domain **`actions:`** in the same lab.

## Command-generator prompt (Lab 2.0)

**Lab 2.0** added **`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`**. That keeps **`set slot`** aligned with real domain names (**`amount`**, **`recipient`**, …) instead of invented prefixes. Keep it in place through **Labs 2.1–5.2** unless you are intentionally customizing the command generator (beyond this course).
