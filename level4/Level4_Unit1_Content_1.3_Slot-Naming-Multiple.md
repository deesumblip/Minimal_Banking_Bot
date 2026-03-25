**Starting point:** Chapter 1.4 assumes you begin with the **final banking agent at the end of Chapter 1.3** (your **`level3/`** project). You **add** work in **`level4/`**—see **`Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`** and **`Level4_Unit0_Content_0.2_What-Level-4-Adds.md`**.

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
