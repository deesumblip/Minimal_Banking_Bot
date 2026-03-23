# Lab 4.1 – Reference solution for LLM Rubric Autograde

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 4.1 (Creating the Transfer Flow with Multiple Collect Steps).

---

## Required deliverable: level4/data/basics/transfer_money.yml

The file must contain a flow that:

1. **Flow structure** – Has a top-level `flows:` key and at least one flow (e.g. `transfer_money`) with `name`, `description`, and `steps`.

2. **Collect steps** – At least three steps that collect the transfer slots, in order (e.g. amount, then recipient, then account_from):
   - `collect: amount` (optional `description:`)
   - `collect: recipient` (optional `description:`)
   - `collect: account_from` (optional `description:`)

3. **Action step** – At least one step that calls the transfer action: `action: action_process_transfer`.

**Recommended:** Use clear **`description:`** text on each `collect:` step so the CALM LLM command generator fills slots. For free-text slots, a **simple rule** often works: **whole user message**, **any characters**, **length within a fixed range** (see example).

Example:

```yaml
flows:
  transfer_money:
    name: transfer money
    always_include_in_prompt: true
    if: true
    description: |
      Transfer money in USD. Steps: get dollar amount, then who receives it (any name or text), then which account to take it from, then run the transfer action.
    steps:
      - collect: amount
        description: |
          US dollar amount. Parse the user's message and set slot amount to the main number as text (e.g. 20 from "20 dollars").
      - collect: recipient
        description: |
          Payee: any free-text string. Set slot recipient to the user's full message (plain text), up to 100 characters.
      - collect: account_from
        description: |
          Source account. Set slot account_from to the user's full message (plain text), up to 120 characters.
      - action: action_process_transfer
```

---

## Rubric summary for autograde

- **File location:** transfer_money.yml exists in level4/data/basics/.
- **Flow structure:** Valid YAML with flows:, and a flow that has name, description, and steps.
- **Collect steps:** At least one step each with collect: amount, collect: recipient, collect: account_from (order may vary but all three required).
- **Action step:** At least one step with action: action_process_transfer.
