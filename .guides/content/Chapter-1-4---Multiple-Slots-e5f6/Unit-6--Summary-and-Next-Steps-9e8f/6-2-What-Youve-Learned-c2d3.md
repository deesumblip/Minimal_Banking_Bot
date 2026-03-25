**Starting point:** Chapter 1.4 assumed you began with the **final banking agent at the end of Chapter 1.3**; the summary below is what you **added** on top of that baseline in **`level4/`** (see **Unit 0.1**).

## Level 4 Summary

In this chapter you:

1. **Domain (Lab 2.1)**. Added three slots (`amount`, `recipient`, `account_from`) and three ask responses (`utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`), and registered `action_process_transfer` in the actions list while **keeping** the existing Level 2–3 action names so flows such as `holiday_hours` still train.

2. **Action (Lab 3.1)**. Created `action_process_transfer.py`, which reads the three slots, caps **recipient** at **100** characters, validates placeholders, and sends the demo transfer confirmation.

3. **Flow (Lab 4.1)**. Created `transfer_money.yml` with three `collect:` steps (amount, recipient, account_from) and one `action:` step (`action_process_transfer`), with **`description:`** text for CALM (free-text **recipient** up to **100** chars in the lab YAML).

4. **Training and testing (Labs 5.1 and 5.2)**. Trained from `level4` (Lab 5.1), then the **completion check** and **Inspector** with the **scripted transfer** in Lab 5.2 (amount → recipient → account → `(Demo) Transfer of $…`).

## Key Ideas

- **Multiple slots** let the agent remember several values in one conversation and use them together in one action.
- The **order of `collect:` steps** in the flow is the order in which the agent asks for values.
- **Naming** stays consistent: slot names and `utter_ask_<slot_name>` in the domain must match the flow and the action's `get_slot(...)` calls.

Your Level 4 agent is a single assistant that supports greet, help, contact, goodbye, hours, check_balance, and transfer_money flows.
