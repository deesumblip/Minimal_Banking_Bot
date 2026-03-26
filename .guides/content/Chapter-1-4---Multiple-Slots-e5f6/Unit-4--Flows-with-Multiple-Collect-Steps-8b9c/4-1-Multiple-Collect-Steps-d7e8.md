**Starting point:** Chapter 1.4 assumes you begin with the **final banking agent at the end of Chapter 1.3** (your **`level3/`** project). You **add** work in **`level4/`**—see **Unit 0.1** and **Unit 0.2**.

In Level 3 you created a flow with one `collect:` step (account) and one action step. In Level 4 you will create a flow with **three** `collect:` steps and then the action step.

## The transfer_money Flow

The flow will:

1. **Collect amount**. Step with `collect: amount`. When the slot is empty, Rasa uses `utter_ask_amount` to ask the user.
2. **Collect recipient**. Step with `collect: recipient`. When empty, Rasa uses `utter_ask_recipient`.
3. **Collect account_from**. Step with `collect: account_from`. When empty, Rasa uses `utter_ask_account_from`.
4. **Run the action**. Step with `action: action_process_transfer`, which reads all three slots and sends the confirmation.

Each `collect:` step can include a **`description:`** for the slot. In **Rasa Pro (CALM)**, the LLM **command generator** uses it when filling slots. For free-text payee/account fields, a **simple rule** works well: **whole user message**, **any characters**, **fixed length range** (see Lab 4.1). The important part is that the three collect steps appear in order, followed by the action step.

## Example: The transfer_money flow

Below is an example flow file. In Lab 4.1 you will create your own version (you may tune `name` and `description` to fit your agent).

```yaml
flows:
  transfer_money:
    name: transfer money
    always_include_in_prompt: true
    if: true
    description: |
      Transfer money in USD. Steps: get dollar amount, then who receives it (any name or text), then which account to take it from, then run the transfer action.
    steps:
      - collect: amount
        description: |
          US dollar amount. Parse the user's message and set slot amount to the main number as text (e.g. 20 from "20 dollars").
      - collect: recipient
        description: |
          Payee: any free-text string. Set slot recipient to the user's full message (plain text), up to 100 characters.
      - collect: account_from
        description: |
          Source account. Set slot account_from to the user's full message (plain text), up to 120 characters.
      - action: action_process_transfer
```

In **Lab 4.1** you will save this as `level4/data/basics/transfer_money.yml`. When you are done, use **Check It!** for Lab 4.1 (Codio).
