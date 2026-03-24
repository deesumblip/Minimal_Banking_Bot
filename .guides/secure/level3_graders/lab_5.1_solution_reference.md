# Lab 5.1 – Reference solution for LLM Rubric Autograde

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 5.1 (Creating a Flow with Slot Collection).

**Standard Code Test:** Grader **`lab_5.1_grader.py`** prints **Check 1–4** (Lab 3.1 / Lab 6.2 layout). Assessment **`code-output-compare-1235165472.json`** sequences **`Check 1: PASSED`** … **`Check 4: PASSED`**.

---

## Required deliverable: level3/data/basics/check_balance.yml

The file must contain a flow that:

1. **Flow structure** – Has a top-level `flows:` key and at least one flow (e.g. `check_balance`) with `name`, `description`, and `steps`.

2. **collect: account step** – At least one step must collect the account slot: `collect: account` (with optional `description: "account number"` or similar).

3. **action step** – At least one step must call the balance action: `action: action_check_balance_simple`.

Example:

```yaml
flows:
  check_balance:
    name: check a balance (demo)
    description: |
      Demonstrates a flow with slot collection.
      The agent will ask for an account number if not provided,
      then call the action to check the balance.
    steps:
      - collect: account
        description: "account number"
      - action: action_check_balance_simple
```

---

## Rubric summary for autograde

- **File location:** check_balance.yml exists in level3/data/basics/.
- **Flow structure:** Valid YAML with flows:, and a flow that has name, description, and steps.
- **collect: account:** At least one step uses collect: account (optional description).
- **action:** At least one step uses action: action_check_balance_simple.
