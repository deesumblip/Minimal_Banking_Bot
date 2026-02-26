You have already defined the three slots and ask responses in the domain (Lab 4.1) and created the action (Lab 4.2). Now create the flow that ties them together: `transfer_money.yml` with three collect steps and then `action_process_transfer`.

## Part 1: In Codio

1. **Terminal.** From the project root, run `source .venv/bin/activate`, then `cd level4`.

2. **Create** the file `data/basics/transfer_money.yml` in the `level4` folder.

3. **Add** the following flow:

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

4. **Verify.** The file is in `data/basics/`, and the flow has `name`, `description`, and `steps` with the three collect steps and the action step.

Run the assessment when done.

## Part 2: Running locally

1. From the project root, activate the venv, then `cd level4`.
2. Create `level4/data/basics/transfer_money.yml` with the flow structure above.
3. Verify as in Part 1.

You're done when `data/basics/transfer_money.yml` exists with a flow that has `collect: amount`, `collect: recipient`, `collect: account_from`, and `action: action_process_transfer`.
