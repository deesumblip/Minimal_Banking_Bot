**Starting point:** Work in **`level4/`** (see **Unit 0.1**).

In Unit 4 you saw an example of the transfer_money flow (YAML with three collect steps and the action step). You have already defined the slots and ask responses in the domain (Lab 2.1) and created the action (Lab 3.1). In this lab you will create your own version of the flow: `level4/data/basics/transfer_money.yml` with three collect steps and then `action_process_transfer`.

## Part 1: In Codio

You do **not** need to activate the virtual environment for this lab—**Check It!** only checks your saved YAML.

1. **Create** the file `data/basics/transfer_money.yml` under the `level4` folder (use the file tree / editor).

2. **Add** the following flow:

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

**`always_include_in_prompt`** / **`if`** help keep this flow visible to the command generator (see **Unit 0.2** section 2 in Level 4). Each **`collect:`** **`description:`** should stay **short** and clear. **Retrain** after saving.

3. **Verify.** The file is in `data/basics/`, and the flow has `name`, `description`, and `steps` with the three collect steps and the action step.

Run the assessment when done.

{Check It!|assessment}(code-output-compare-401040001)

## Part 2: Running locally

1. In your editor, create `level4/data/basics/transfer_money.yml` with the flow structure above (no terminal or venv required for this lab).
2. Verify as in Part 1.

You're done when `data/basics/transfer_money.yml` exists with a flow that has `collect: amount`, `collect: recipient`, `collect: account_from`, and `action: action_process_transfer`.
