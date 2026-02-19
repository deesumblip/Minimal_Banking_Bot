You will do this in **Lab 4.1: Creating a Flow with Slot Collection**. The steps below are the detailed walkthrough for that lab.

Create the `check_balance.yml` flow that collects the account number.

**Step 1:** Create a new file `data/basics/check_balance.yml` in the `level3` folder.

**Step 2:** Add the flow:

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

**Step 3:** Verify: file in `data/basics/`, flow has `name`, `description`, `steps`, with `collect: account` then `action: action_check_balance_simple`.

Execution: user says "Check my balance" → if `account` is empty, bot asks "What is your account number?" (using `utter_ask_account`) → user provides value → bot stores it → flow runs `action_check_balance_simple`, which reads the slot.
