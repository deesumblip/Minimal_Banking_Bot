# Lab 4.1 – Reference solution for LLM Rubric Autograde

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 4.1 (Adding Multiple Slots in the Domain).

---

## Required changes in level4/domain/basics.yml

1. **slots: section** – Must contain (in addition to any existing slots such as `account`) the three transfer slots: `amount`, `recipient`, `account_from`, each with `type: text` (or equivalent).

2. **Ask responses** – Under `responses:`, add:
   - `utter_ask_amount` with at least one text (e.g. "How much would you like to transfer?")
   - `utter_ask_recipient` with at least one text (e.g. "Who would you like to transfer money to?")
   - `utter_ask_account_from` with at least one text (e.g. "Which account would you like to transfer from?")

3. **action_process_transfer in actions** – Under `actions:`, add `action_process_transfer` to the list. The student will create the .py file in Lab 4.2.

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
        rephrase: True
  utter_ask_recipient:
    - text: "Who would you like to transfer money to?"
      metadata:
        rephrase: True
  utter_ask_account_from:
    - text: "Which account would you like to transfer from?"
      metadata:
        rephrase: True

actions:
  - action_bank_hours
  - action_check_balance_simple
  - action_process_transfer
```

---

## Rubric summary for autograde

- **Slots:** amount, recipient, account_from present under slots: with valid type (e.g. text).
- **Ask responses:** utter_ask_amount, utter_ask_recipient, utter_ask_account_from present under responses: with at least one message each.
- **Actions:** action_process_transfer appears in the actions: list.
- **Validity:** File is valid YAML and existing Level 3 content (e.g. account slot, utter_ask_account, other actions) is preserved.
