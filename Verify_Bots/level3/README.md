# Level 3: Responses + Actions + Slots

**Final bot** students have by the end of Level 3.

## Contents

- **Slots:** `account` (used for balance checks)
- **Responses:** greet, help, contact, goodbye, utter_ask_account
- **Custom actions:** `action_bank_hours`, `action_check_balance_simple`
- **Flows:** greet, help, contact, goodbye, hours, check_balance
- **Config:** `config.yml`, `credentials.yml`, `endpoints.yml`
- **Domain:** `domain/basics.yml`
- **Data:** `data/basics/*.yml`, `data/system/patterns/patterns.yml`

## What this bot can do

- Greet the user and list what it can help with
- Explain capabilities (balance, transfers, bank hours, contact info)
- Give contact information (email, phone)
- Say goodbye
- **Provide bank hours** via the custom action `action_bank_hours`
- **Check balance:** ask for account number (slot), then run `action_check_balance_simple` to return a balance

Run from this folder with `RASA_LICENSE` and `OPENAI_API_KEY` set. Start the action server: `rasa run actions`.
