# Level 5: Tool Calling

**Final bot** students have by the end of Level 5.

## Contents

- **Slots:** `account`, `amount`, `recipient`, `account_from` (for transfers)
- **Responses:** greet, help, contact, goodbye, utter_ask_* (account, amount, recipient, account_from)
- **Custom actions:** `action_bank_hours`, `action_check_balance_simple`, `action_process_transfer`, `action_process_transfer_with_tools`
- **Flows:** greet, help, contact, goodbye, hours, check_balance, transfer_money, transfer_money_tools
- **Config:** `config.yml`, `credentials.yml`, `endpoints.yml`
- **Domain:** `domain/basics.yml`
- **Data:** `data/basics/*.yml`, `data/system/patterns/patterns.yml`

## What this bot can do

- Everything Level 4 can do (greet, help, contact, goodbye, bank hours, check balance)
- **Transfer money:** collect amount, recipient, and source account via slots, then run `action_process_transfer`
- **Transfer with tools:** use `action_process_transfer_with_tools` so the LLM can call tools for transfer handling

Run from this folder with `RASA_LICENSE` and `OPENAI_API_KEY` set. Start the action server: `rasa run actions`.
