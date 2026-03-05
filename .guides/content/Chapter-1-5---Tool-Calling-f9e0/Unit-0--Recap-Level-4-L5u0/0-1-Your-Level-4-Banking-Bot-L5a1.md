Before we add tool calling, here is a quick recap of what you built in Level 4. All of this remains unchanged. Level 5 builds on top of it.

## Level 5 Setup

The **level5** folder is set up as a copy of your Level 4 bot. Use the **same virtual environment** as in Level 4 (project root); there is no new venv inside `level5`. In this chapter you will:

- Create the `tools/` folder and `banking_tools.py` (Lab 2.1)
- Register tools in `endpoints.yml` (Lab 3.1)
- Add the `action_process_transfer_with_tools` action and `transfer_money_tools` flow (Lab 4.1)
- Train and test (Labs 5.1 and 5.2)

Everything else is your Level 4 content.

---

## What You Have from Level 4

### Domain (`domain/basics.yml`)

- Responses: `utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`, `utter_ask_account`, `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- Slots: `account`, `amount`, `recipient`, `account_from`
- Actions: `action_bank_hours`, `action_check_balance_simple`, `action_process_transfer`

### Flows (`data/basics/`)

- greet, help, contact, goodbye, hours, check_balance, transfer_money

### Actions (`actions/`)

- `action_bank_hours.py`, `action_check_balance_simple.py`, `action_process_transfer.py`

### Config

- Config, credentials, endpoints (no tools section yet). Config uses `assistant_id: level5-bot` (or similar).

---

## What Level 4 Couldn't Do

Your Level 4 bot used **actions** that are explicitly called in flows. It could not let the **LLM decide at runtime** which operations to perform (e.g. check balance vs. transfer) based on what the user said. Level 5 adds **tools**: functions the LLM can discover and call dynamically, so the bot can adapt to the conversation.
