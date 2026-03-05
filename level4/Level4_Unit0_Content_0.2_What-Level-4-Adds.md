Level 4 adds **multiple slots** in one flow: the bot will remember several values in a single conversation and use them together in one action.

Your Level 3 bot will still work. You will add the transfer flow on top.

You will implement in this order: **domain** (Lab 2.1), then **the action that uses the slots** (Lab 3.1), then **the flow that collects them** (Lab 4.1), then **train and test** (Labs 5.1 and 5.2).

## What You'll Add

**Lab 2.1 — Domain.** You will update the domain:

- Add three slots: `amount`, `recipient`, `account_from` (each type text)
- Add three ask responses: `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from` so the bot can ask for each value
- Add `action_process_transfer` to the `actions:` list (you will create the Python file in Lab 3.1)

**Lab 3.1 — Action.** You will create the file `action_process_transfer.py`: the action that reads all three slots and sends a transfer confirmation (and optionally validates placeholders).

**Lab 4.1 — Flow.** You will create the flow file `data/basics/transfer_money.yml`. That flow will collect amount, then recipient, then account_from, then run `action_process_transfer`.

**Lab 5.1 — Training.** You will train your Level 4 bot from the `level4` folder.

**Lab 5.2 — Testing.** You will run the completion check and optionally test the transfer flow in Rasa Inspector.

**Unchanged.** All your Level 3 responses, flows, and actions stay as they are. You build Level 4 by adding these pieces.
