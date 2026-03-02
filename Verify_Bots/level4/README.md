# Level 4: Multiple Slots

**Final bot** students have by the end of Level 4.

## Contents

- **Slots:** `account` (used for balance checks)
- **Responses:** greet, help, contact, goodbye, utter_ask_account
- **Custom actions:** `action_bank_hours`, `action_check_balance_simple`
- **Flows:** greet, help, contact, goodbye, hours, check_balance
- **Config:** `config.yml`, `credentials.yml`, `endpoints.yml`
- **Domain:** `domain/basics.yml`
- **Data:** `data/basics/*.yml`, `data/system/patterns/patterns.yml`

## What this bot can do

- Everything Level 3 can do (greet, help, contact, goodbye, bank hours)
- **Check balance:** ask for account number (slot), then run `action_check_balance_simple` to return a balance

The bot remembers the user's account in the `account` slot during the check-balance flow.

Run from this folder with `RASA_LICENSE` and `OPENAI_API_KEY` set. Start the action server for custom actions: `rasa run actions`.
