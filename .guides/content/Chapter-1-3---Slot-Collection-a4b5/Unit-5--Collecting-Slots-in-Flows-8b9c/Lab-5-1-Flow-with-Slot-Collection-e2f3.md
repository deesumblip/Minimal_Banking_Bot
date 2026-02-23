You have already defined the slot and ask response in the domain (Lab 3.1) and **written** the action (Lab 4.1). Now create the flow that ties them together: the `check_balance.yml` flow that collects the `account` slot and then runs `action_check_balance_simple`.

## Part 1: In Codio

1. **Terminal.** From the project root, run `source .venv/bin/activate`, then `cd level3`.

2. **Create** the file `data/basics/check_balance.yml` in the `level3` folder.

3. **Add** the following flow:

```yaml
flows:
  check_balance:
    name: check a balance (demo)
    description: |
      Demonstrates a flow with slot collection.
      The bot will ask for an account number if not provided,
      then call the action to check the balance.
    steps:
      - collect: account
        description: "account number"
      - action: action_check_balance_simple
```

4. **Verify.** The file is in `data/basics/`, and the flow has `name`, `description`, and `steps` with a first step `collect: account` and a second step `action: action_check_balance_simple`.

Run the assessment when done.

## Part 2: Running locally

1. From the project root, activate the venv, then `cd level3`.
2. Create `level3/data/basics/check_balance.yml` with the flow structure above.
3. Verify as in Part 1.

You're done when `data/basics/check_balance.yml` exists with a flow that has `collect: account` and `action: action_check_balance_simple`.
