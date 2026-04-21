# Level 2: Starter vs completion

Use this as the single reference for what ships in **`level2/`** and what students add to reach the **end of Level 2**.

## Starter (before Lab 3.1)

The repo’s **`level2/`** folder matches **Level 1 complete** plus one teaching artifact:

| Area | Files / contents |
|------|------------------|
| **Domain** | `domain/basics.yml` — `responses:` only (`utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`). **No** `actions:` section. |
| **Flows** | `data/basics/greet.yml`, `help.yml`, `contact.yml`, `goodbye.yml` only. **No** `hours.yml`, **no** `holiday_hours.yml`. |
| **Patterns** | `data/system/patterns/patterns.yml` |
| **Config** | `config.yml`, `credentials.yml`, `endpoints.yml` — same **tutorial LLM** pattern as Level 1 (`rasa_command_generation_model`); `endpoints.yml` adds **`action_endpoint`** for the `actions` package. |
| **Actions (Python)** | `actions/__init__.py`, `actions/action_bank_hours.py` (example for Units 2–3). **No** `action_holiday_hours.py`. |

Students need a working **Level 1** agent (above), **Rasa Pro** + env (`.env`, venv), and the example action file so they can study and copy the pattern. Nothing is missing to complete Labs **3.1 → 4.1 → 5.1** in order.

## After all Level 2 assignments (completion)

Students will have added:

| Deliverable | Lab |
|-------------|-----|
| `actions/action_holiday_hours.py` | 3.1 |
| `domain/basics.yml` with `actions:` listing `action_bank_hours` and `action_holiday_hours` | 4.1 |
| `data/basics/hours.yml` and `data/basics/holiday_hours.yml` | 5.1 |

The **`level3/`** folder in this repository is maintained as a **Level 2–complete** baseline (both actions + both flows + domain registrations) for Level 3, so instructors can compare or sync without using a partially edited `level2`.

## Text in guides

- **Before Lab 4.1:** Do **not** imply an `actions:` section or `hours.yml` exists in the starter.
- **Lab 4.1:** Students **add** the full `actions:` section with **both** action names (starter has none).
- **Lab 5.1:** Students **create** both YAML files; do **not** say “or open if already present” for the canonical starter.
