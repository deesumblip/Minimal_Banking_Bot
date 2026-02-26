## Level 4 Summary

In this chapter you:

1. **Domain (Lab 4.1)** — Added three slots (`amount`, `recipient`, `account_from`) and three ask responses (`utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`), and registered `action_process_transfer` in the actions list.

2. **Action (Lab 4.2)** — Created `action_process_transfer.py`, which reads the three slots from the tracker and sends a transfer confirmation (and optionally validates placeholders).

3. **Flow (Lab 4.3)** — Created `transfer_money.yml` with three `collect:` steps (amount, recipient, account_from) and one `action:` step (action_process_transfer).

4. **Training and testing (Labs 4.4 and 4.5)** — Trained the Level 4 bot from the `level4` folder and ran the completion check (and optionally tested the transfer flow in Inspector).

## Key Ideas

- **Multiple slots** let the bot remember several values in one conversation and use them together in one action.
- The **order of `collect:` steps** in the flow is the order in which the bot asks for values.
- **Naming** stays consistent: slot names and `utter_ask_<slot_name>` in the domain must match the flow and the action’s `get_slot(...)` calls.

Your Level 4 bot is a single assistant that supports greet, help, contact, goodbye, hours, check_balance, and transfer_money flows.
