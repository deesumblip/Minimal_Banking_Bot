Create `level3/data/basics/check_balance.yml`:

```yaml
flows:
  check_balance:
    name: check account balance
    description: Ask the user for their account number and return their balance.
    persisted_slots:
      - account
    steps:
      - collect: account
        description: |
          A numeric account number consisting ONLY of digits (e.g., 123456, 987654321).
          CRITICAL: Do NOT extract this slot unless the user explicitly provides numbers.
          Do NOT extract from phrases like "account balance", "check account", "my account".
          Only extract when the user says actual digits like "123456" or "my account number is 789012".
        rejections:
          - if: not (slots.account matches "^[0-9]{4,}$")
            utter: utter_invalid_account
      - action: action_check_balance_simple
```

| Field | What it does |
|---|---|
| `description` (flow) | Tells the LLM when to trigger this flow |
| `persisted_slots` | Keeps the `account` value after the flow ends |
| `description` (collect) | Tells the LLM what a valid account value looks like |
| `rejections` | Rejects values that don't match the condition after extraction |
| `utter_invalid_account` | Sent when rejection fires, then `utter_ask_account` runs again |
| `action_check_balance_simple` | Reads the slot and returns the balance |

## Verify

`data/flows/check_balance.yml` should contain:

- A flow with id `check_balance` and a `description`
- `account` listed under `persisted_slots`
- A `collect: account` step with a `description` field
- A `rejections` block with a digits-only condition pointing to `utter_invalid_account`
- An `action: action_check_balance_simple` step after the collect

Use **Check It!** below to confirm.

{Check It!|assessment}(code-output-compare-1235165472)

