# Level 2: Custom Actions

**Final bot** students have by the end of Level 2.

## Contents

- **Responses** (greet, help, contact, goodbye)
- **Custom actions:** `action_bank_hours`
- **Flows:** greet, help, contact, hours
- **Config:** `config.yml`, `credentials.yml`, `endpoints.yml`
- **Domain:** `domain/basics.yml`
- **Data:** `data/basics/*.yml`, `data/system/patterns/patterns.yml`

## What this bot can do

- Greet the user and list what it can help with
- Explain capabilities (balance, transfers, bank hours, contact info)
- Give contact information (email, phone)
- **Provide bank hours** via the custom action `action_bank_hours` (hours flow)

Run from this folder with `RASA_LICENSE` and `OPENAI_API_KEY` set. Start the action server for custom actions: `rasa run actions`.
