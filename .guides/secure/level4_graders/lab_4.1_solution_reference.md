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

**Recommended:** Use **detailed `description:`** text on each `collect:` step so the CALM LLM command generator reliably fills slots (especially multi-word recipient names). See example below.

Example:

```yaml
flows:
  transfer_money:
    name: transfer money
    description: |
      User transfers money in USD. Collect in order: dollar amount, payee (free text),
      then source account; then run the transfer action.
    steps:
      - collect: amount
        description: |
          Dollar amount to send. Extract the numeric value from input like "50 dollars", "$50", or "fifty".
      - collect: recipient
        description: |
          Who receives the money. Map the user's entire message to this slot as plain text,
          including multi-word names (e.g. "Alice", "John Smith", "George W Bush").
      - collect: account_from
        description: |
          Source account number or label the user gives for the account to transfer from.
      - action: action_process_transfer
```

---

## Rubric summary for autograde

- **File location:** transfer_money.yml exists in level4/data/basics/.
- **Flow structure:** Valid YAML with flows:, and a flow that has name, description, and steps.
- **Collect steps:** At least one step each with collect: amount, collect: recipient, collect: account_from (order may vary but all three required).
- **Action step:** At least one step with action: action_process_transfer.
