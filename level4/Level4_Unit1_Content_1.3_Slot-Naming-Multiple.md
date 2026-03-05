The same naming conventions you used in Level 3 apply when you add multiple slots.

## Slot Names

- Use clear, lowercase names: `amount`, `recipient`, `account_from`.
- Slot names must match exactly between:
  - The **domain** (`slots:` section)
  - The **flow** (`collect: slot_name` in steps)
  - The **action** (`tracker.get_slot("slot_name")`)

## Ask Responses

- For each slot you collect, define a response named `utter_ask_<slot_name>` in the domain.
- For the slot `amount` → `utter_ask_amount`
- For the slot `recipient` → `utter_ask_recipient`
- For the slot `account_from` → `utter_ask_account_from`

Rasa uses these responses when the corresponding slot is empty during the flow. In Lab 2.1 you will add the three slots and the three ask responses to the domain.
