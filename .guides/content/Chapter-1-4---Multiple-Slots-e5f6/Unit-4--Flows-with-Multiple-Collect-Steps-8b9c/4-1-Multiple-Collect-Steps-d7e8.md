In Level 3 you created a flow with one `collect:` step (account) and one action step. In Level 4 you will create a flow with **three** `collect:` steps and then the action step.

## The transfer_money Flow

The flow will:

1. **Collect amount** — Step with `collect: amount`. When the slot is empty, Rasa uses `utter_ask_amount` to ask the user.
2. **Collect recipient** — Step with `collect: recipient`. When empty, Rasa uses `utter_ask_recipient`.
3. **Collect account_from** — Step with `collect: account_from`. When empty, Rasa uses `utter_ask_account_from`.
4. **Run the action** — Step with `action: action_process_transfer`, which reads all three slots and sends the confirmation.

Each `collect:` step can include a **`description:`** for the slot. In **Rasa Pro (CALM)**, the LLM **command generator** uses these descriptions when filling slots—short one-line descriptions are often **not enough** for free-text names (multi-word payees). Use **clear, explicit** descriptions (see Lab 4.1 example). The important part is that the three collect steps appear in order, followed by the action step.

## Example: The transfer_money flow

Below is an example of the flow file. You will create your own version in Lab 4.1 (e.g. with a name and description that fit your bot).

```yaml
flows:
  transfer_money:
    name: transfer money
    description: |
      User transfers money in USD. Collect amount, payee (free text), source account; then action.
    steps:
      - collect: amount
        description: |
          Dollar amount. Extract the numeric value from "50 dollars", "$50", etc.
      - collect: recipient
        description: |
          Payee as free text; include multi-word names (e.g. "Alice", "George W Bush").
      - collect: account_from
        description: |
          Source account number or label from the user.
      - action: action_process_transfer
```

In **Lab 4.1** you will create the file `level4/data/basics/transfer_money.yml` with your own version of this flow. When you are done, **in Codio** use **Check It!** for Lab 4.1.
