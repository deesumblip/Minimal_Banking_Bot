# Level 4: Multiple Slots

**Final bot** students have by the end of Level 4.

## Contents

- **Slots:** `account`, `amount`, `recipient`, `account_from` (for balance and transfers)
- **Responses:** greet, help, contact, goodbye, utter_ask_account, utter_ask_amount, utter_ask_recipient, utter_ask_account_from
- **Custom actions:** `action_bank_hours`, `action_check_balance_simple`, `action_process_transfer`
- **Flows:** greet, help, contact, goodbye, hours, check_balance, transfer_money
- **Config:** `config.yml`, `credentials.yml`, `endpoints.yml`
- **Domain:** `domain/basics.yml`
- **Data:** `data/basics/*.yml`, `data/system/patterns/patterns.yml`

## What this bot can do

- Everything Level 3 can do (greet, help, contact, goodbye, bank hours, check balance)
- **Transfer money:** collect amount, recipient, and source account via slots, then run `action_process_transfer`

Run from this folder with `RASA_LICENSE` and `OPENAI_API_KEY` set. Start the action server: `rasa run actions`.
