In Level 3 you created a flow with one `collect:` step (account) and one action step. In Level 4 you will create a flow with **three** `collect:` steps and then the action step.

## The transfer_money Flow

The flow will:

1. **Collect amount** — Step with `collect: amount`. When the slot is empty, Rasa uses `utter_ask_amount` to ask the user.
2. **Collect recipient** — Step with `collect: recipient`. When empty, Rasa uses `utter_ask_recipient`.
3. **Collect account_from** — Step with `collect: account_from`. When empty, Rasa uses `utter_ask_account_from`.
4. **Run the action** — Step with `action: action_process_transfer`, which reads all three slots and sends the confirmation.

Each `collect:` step can optionally include a `description:` for the slot (e.g. for documentation or tools). The important part is that the three collect steps appear in order, followed by the action step.

## Lab 4.3

In **Lab 4.3** you will create the file `level4/data/basics/transfer_money.yml` with this flow. When you are done, run the assessment for Lab 4.3.
