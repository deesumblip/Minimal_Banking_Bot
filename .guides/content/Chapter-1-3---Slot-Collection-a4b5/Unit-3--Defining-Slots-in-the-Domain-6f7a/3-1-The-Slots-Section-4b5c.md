Slots are defined in the domain file, just like responses and actions.

## Domain Structure in Level 3

```yaml
version: "3.1"

slots:                    # NEW in Level 3
  account:
    type: text

responses:                # From Level 1 & 2 (unchanged)
  utter_greet:
    - text: "Hi! I'm a banking assistant..."
  # ... other responses
  utter_ask_account:      # NEW: Used when collecting account slot
    - text: "What is your account number?"

actions:                  # From Level 2 (unchanged)
  - action_bank_hours
  - action_check_balance_simple  # NEW: Uses the account slot
```

`slots:` is at the same indentation level as `responses:` and `actions:`.
