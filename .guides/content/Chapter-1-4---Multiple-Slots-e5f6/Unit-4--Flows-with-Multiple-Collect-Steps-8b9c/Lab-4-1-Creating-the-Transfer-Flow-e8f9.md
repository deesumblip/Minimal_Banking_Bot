In Unit 4 you saw an example of the transfer_money flow (YAML with three collect steps and the action step). You have already defined the slots and ask responses in the domain (Lab 2.1) and created the action (Lab 3.1). In this lab you will create your own version of the flow: `level4/data/basics/transfer_money.yml` with three collect steps and then `action_process_transfer`.

## Part 1: In Codio

1. **Create** the file `data/basics/transfer_money.yml` under the `level4` folder (use the file tree / editor—you do not need to activate the virtual environment for this lab; **Check It!** only checks your saved YAML).

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

**Why these `description` lines?** Rasa Pro’s **LLM command generator** uses them when **filling slots**. For payee and account, a **simple rule** works well: store the **entire user message** as text, **any characters**, within a **fixed length range** (here 1–100 for recipient, 1–120 for account). See also [Rasa’s guidance](https://rasa.com/docs/reference/config/components/llm-command-generators/#customizing-the-prompt).

3. **Verify.** The file is in `data/basics/`, and the flow has `name`, `description`, and `steps` with the three collect steps and the action step.

**Use Check It!** below when done (Codio).

{Check It!|assessment}(code-output-compare-401040001)

## Part 2: Running locally

1. In your editor, create `level4/data/basics/transfer_money.yml` with the flow structure above (no terminal or venv required for this lab).
2. Verify as in Part 1.

You're done when `data/basics/transfer_money.yml` exists with a flow that has `collect: amount`, `collect: recipient`, `collect: account_from`, and `action: action_process_transfer`.
