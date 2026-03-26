**Starting point:** Work in **`level4/`** (starter agent in **Unit 0.1**; pipeline in **Unit 0.2**).

**check_balance** uses one `collect:` step (`account`) and one action step. The **transfer** flow uses **three** `collect:` steps and then the action step.

## The transfer_money Flow

The flow will:

1. **Collect amount** — Step with `collect: amount`. When the slot is empty, Rasa uses `utter_ask_amount` to ask the user.
2. **Collect recipient** — Step with `collect: recipient`. When empty, Rasa uses `utter_ask_recipient`.
3. **Collect account_from** — Step with `collect: account_from`. When empty, Rasa uses `utter_ask_account_from`.
4. **Run the action** — Step with `action: action_process_transfer`, which reads all three slots and sends the confirmation.

Each `collect:` step can include a **`description:`** for the slot. In **Rasa Pro (CALM)**, the LLM **command generator** uses it when filling slots. For **free-text** slots (payee, account), a simple pattern is: **store the user’s full message**, **any characters**, **between a min and max length**—see Lab 4.1. The important part is that the three collect steps appear in order, followed by the action step.

## Example: The transfer_money flow

Below is an example of the flow file. You will create your own version in Lab 4.1 (e.g. with a name and description that fit your agent).

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

In **Lab 4.1** you will create the file `level4/data/basics/transfer_money.yml` with your own version of this flow. When you are done, run the assessment for Lab 4.1.
