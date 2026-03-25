# Lab 2.1 – Reference solution for LLM Rubric Autograde

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 2.1 (Adding Multiple Slots in the Domain).

---

## Required changes in level4/domain/basics.yml

1. **slots: section** – Must contain (in addition to any existing slots such as `account`) the three transfer slots: `amount`, `recipient`, `account_from`, each with `type: text` (or equivalent).

2. **Ask responses** – Under `responses:`, add:
   - `utter_ask_amount` with at least one text (e.g. "How much would you like to transfer?")
   - `utter_ask_recipient` with at least one text (e.g. "Who would you like to transfer money to?")
   - `utter_ask_account_from` with at least one text (e.g. "Which account would you like to transfer from?")

3. **action_process_transfer in actions** – Under `actions:`, add `action_process_transfer` to the list. The student will create the `.py` file in Lab 3.1.

4. **Do not remove Level 2/3 actions** – Flows such as `holiday_hours.yml` still call `action_holiday_hours`. If it is removed from the domain, `rasa train` fails. Keep `action_bank_hours`, `action_holiday_hours`, and `action_check_balance_simple` alongside `action_process_transfer`.

Example (additions only):

```yaml
slots:
  account:
    type: text
  amount:
    type: text
  recipient:
    type: text
  account_from:
    type: text

responses:
  # ... existing responses ...
  utter_ask_amount:
    - text: "How much would you like to transfer?"
      metadata:
        rephrase: False
  utter_ask_recipient:
    - text: "Who would you like to transfer money to?"
      metadata:
        rephrase: False
  utter_ask_account_from:
    - text: "Which account would you like to transfer from?"
      metadata:
        rephrase: False

actions:
  - action_bank_hours
  - action_check_balance_simple
  - action_process_transfer
```

Prefer **`rephrase: False`** on these three `utter_ask_*` responses: with CALM + LLM command generation, **`rephrase: True` during slot collection** can break filling later slots (e.g. recipient) and trigger “unable to understand you” fallbacks.

---

## Rubric summary for autograde

- **Slots:** amount, recipient, account_from present under slots: with valid type (e.g. text).
- **Ask responses:** utter_ask_amount, utter_ask_recipient, utter_ask_account_from present under responses: with at least one message each.
- **Actions:** action_process_transfer appears in the actions: list, and action_bank_hours, action_holiday_hours, action_check_balance_simple remain listed.
- **Validity:** File is valid YAML and existing Level 3 content (e.g. account slot, utter_ask_account, other actions) is preserved.
