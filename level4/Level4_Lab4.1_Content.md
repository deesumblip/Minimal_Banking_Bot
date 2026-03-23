In Unit 4 you saw an example of the transfer_money flow (YAML with three collect steps and the action step). You have already defined the slots and ask responses in the domain (Lab 2.1) and created the action (Lab 3.1). In this lab you will create your own version of the flow: `level4/data/basics/transfer_money.yml` with three collect steps and then `action_process_transfer`.

## Part 1: In Codio

You do **not** need to activate the virtual environment for this lab—**Check It!** only checks your saved YAML.

1. **Create** the file `data/basics/transfer_money.yml` under the `level4` folder (use the file tree / editor).

2. **Add** the following flow:

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

Rich **`description`** text on each `collect:` step helps the CALM **LLM command generator** fill slots reliably (especially multi-word recipient names).

3. **Verify.** The file is in `data/basics/`, and the flow has `name`, `description`, and `steps` with the three collect steps and the action step.

Run the assessment when done.

{Check It!|assessment}(code-output-compare-401040001)

## Part 2: Running locally

1. In your editor, create `level4/data/basics/transfer_money.yml` with the flow structure above (no terminal or venv required for this lab).
2. Verify as in Part 1.

You're done when `data/basics/transfer_money.yml` exists with a flow that has `collect: amount`, `collect: recipient`, `collect: account_from`, and `action: action_process_transfer`.
