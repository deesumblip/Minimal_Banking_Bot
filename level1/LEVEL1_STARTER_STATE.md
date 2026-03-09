# Level 1: Starter State (Before Students Start)

This document describes the Level 1 bot as it should be **before students do any labs**. Use it to reset a workspace or verify the initial state.

## Domain: `domain/basics.yml`

**Responses only** (no `utter_goodbye`, no `utter_hours`, no `utter_balance`):

- `utter_greet`
- `utter_help`
- `utter_contact`

Students add `utter_goodbye` in Lab 2.2 and the handout responses in Lab 3.5.

## Flows: `data/basics/`

**Exactly three files:**

- **greet.yml** – One step: `action: utter_greet` (students add a second step in Lab 3.3)
- **help.yml** – Standard help flow
- **contact.yml** – Standard contact flow

No `goodbye.yml`, `hours.yml`, or `balance.yml`; those are created in Labs 3.2, 3.4, and 3.5.

## System patterns: `data/system/patterns/patterns.yml`

- **pattern_session_start** – Single step: `action: utter_greet` (students may add a second step in Lab 4.2)
- **pattern_completed** – Standard `noop: true`, `next: END`

## Other

- **models/** – Empty (no trained model). Students run `rasa train` in Lab 6.1.
- **config.yml, credentials.yml, endpoints.yml** – Unchanged from project template.
- **.env** – Not in repo; students set `RASA_LICENSE` in Lab 0.1.

## Restoring to starter on Codio

If the workspace has been used and you want to reset Level 1 to this state:

1. Restore `domain/basics.yml` to the three responses above (see repo version).
2. Restore `data/basics/greet.yml` to a single step; keep `help.yml` and `contact.yml`; remove `goodbye.yml`, `hours.yml`, `balance.yml` if present.
3. Restore `data/system/patterns/patterns.yml` to session_start with only `utter_greet` if it was changed.
4. Delete any files in `level1/models/` so training is required again in Lab 6.1.
