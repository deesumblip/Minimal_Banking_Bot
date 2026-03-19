In Unit 5.3 you saw how the flow ties slot collection to the action. You have already defined the slot and ask response in the domain (Lab 3.1) and **written** the action (Lab 4.1). In this lab you create the flow that ties them together: `check_balance.yml` with `collect: account` and `action: action_check_balance_simple`.

## Part 1: In Codio

1. **Create** the file `data/basics/check_balance.yml` in the `level3` folder.

2. **Add** the following flow:

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

3. **Verify.** The file is in `data/basics/`, and the flow has `name`, `description`, and `steps` with a first step `collect: account` and a second step `action: action_check_balance_simple`.

Run the assessment when done.

## Part 2: Running locally

1. Create `level3/data/basics/check_balance.yml` with the flow structure above.
2. Verify as in Part 1.

You're done when `data/basics/check_balance.yml` exists with a flow that has `collect: account` and `action: action_check_balance_simple`.
