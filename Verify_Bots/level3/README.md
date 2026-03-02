# Level 3: Responses + Actions

**Final bot** students have by the end of Level 3.

## Contents

- **Responses** (greet, help, contact, goodbye)
- **Custom actions:** `action_bank_hours` (returns bank hours)
- **Flows:** greet, help, contact, goodbye, hours
- **Config:** `config.yml`, `credentials.yml`, `endpoints.yml`
- **Domain:** `domain/basics.yml`
- **Data:** `data/basics/*.yml`, `data/system/patterns/patterns.yml`

## What this bot can do

- Greet the user and list what it can help with
- Explain capabilities (balance, transfers, bank hours, contact info)
- Give contact information (email, phone)
- Say goodbye
- **Provide bank hours** via the custom action `action_bank_hours`

Run from this folder with `RASA_LICENSE` and `OPENAI_API_KEY` set: `rasa train`, then `rasa run` or `rasa inspect`. Start the action server separately if using custom actions at runtime.
