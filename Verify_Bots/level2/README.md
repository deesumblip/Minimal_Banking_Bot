# Level 2: Custom Actions

**Final bot** students have by the end of Level 2.

## Contents

- **Responses** (same as Level 1)
- **Custom actions:** `actions/` (placeholder/init; Level 2 introduces the pattern)
- **Flows:** greet, help, contact
- **Config:** `config.yml`, `credentials.yml`, `endpoints.yml`
- **Domain:** `domain/basics.yml`
- **Data:** `data/basics/*.yml`, `data/system/patterns/patterns.yml`

## What this bot can do

- Greet the user and list what it can help with
- Explain capabilities (balance, transfers, bank hours, contact info)
- Give contact information (email, phone)

Level 2 adds the **actions** module and wiring so students can add custom actions (e.g. bank hours) in later levels.

Run from this folder with `RASA_LICENSE` and `OPENAI_API_KEY` set: `rasa train`, then `rasa run` or `rasa inspect`.
