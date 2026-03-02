# Level 1: Just Responses

**Final bot** students have by the end of Level 1.

## Contents

- **Responses only** (no slots, no custom actions)
- **Flows:** greet, help, contact, goodbye, branch locations (Lab 7.2 example)
- **Config:** `config.yml`, `credentials.yml`, `endpoints.yml`
- **Domain:** `domain/basics.yml`
- **Data:** `data/basics/*.yml`, `data/system/patterns/patterns.yml`

## What this bot can do

- Greet the user and list what it can help with
- Explain capabilities (balance, transfers, bank hours, contact info)
- Give contact information (email, phone)
- Say goodbye
- Provide branch locations and hours (example Lab 7.2 feature)

Run from this folder with `RASA_LICENSE` and `OPENAI_API_KEY` set: `rasa train`, then `rasa run` or `rasa inspect`.
