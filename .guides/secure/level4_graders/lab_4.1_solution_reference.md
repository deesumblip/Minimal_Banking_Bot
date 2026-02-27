# Lab 4.3 – Reference solution for LLM Rubric Autograde

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 4.3 (Creating the Transfer Flow with Multiple Collect Steps).

---

## Required deliverable: level4/data/basics/transfer_money.yml

The file must contain a flow that:

1. **Flow structure** – Has a top-level `flows:` key and at least one flow (e.g. `transfer_money`) with `name`, `description`, and `steps`.

2. **Collect steps** – At least three steps that collect the transfer slots, in order (e.g. amount, then recipient, then account_from):
   - `collect: amount` (optional `description:`)
   - `collect: recipient` (optional `description:`)
   - `collect: account_from` (optional `description:`)

3. **Action step** – At least one step that calls the transfer action: `action: action_process_transfer`.

Example:

```yaml
flows:
  transfer_money:
    name: transfer money
    description: |
      Demonstrates collecting multiple slots before executing an action.
      The bot will collect amount, recipient, and source account, then process the transfer.
    steps:
      - collect: amount
        description: "transfer amount"
      - collect: recipient
        description: "recipient name or account"
      - collect: account_from
        description: "source account number"
      - action: action_process_transfer
```

---

## Rubric summary for autograde

- **File location:** transfer_money.yml exists in level4/data/basics/.
- **Flow structure:** Valid YAML with flows:, and a flow that has name, description, and steps.
- **Collect steps:** At least one step each with collect: amount, collect: recipient, collect: account_from (order may vary but all three required).
- **Action step:** At least one step with action: action_process_transfer.
