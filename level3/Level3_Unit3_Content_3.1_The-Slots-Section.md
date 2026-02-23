Slots are defined in the domain file, just like responses and actions. This is the **define** step you saw in Unit 1.2: you add the slot and the ask response so that flows and actions can use them.

## Domain Structure in Level 3

After Lab 3.1 your domain will look like this. The `slots:` section and `utter_ask_account` response are what you add. The actions list keeps your Level 2 actions and you add `action_check_balance_simple` in Lab 3.1.

```yaml
version: "3.1"

slots:                    # You add this in Lab 3.1
  account:
    type: text

responses:                # From Level 1 & 2 (unchanged) plus one new response
  utter_greet:
    - text: "Hi! I'm a banking assistant..."
  # ... other responses
  utter_ask_account:      # You add this in Lab 3.1; Rasa uses it when collecting the account slot
    - text: "What is your account number?"

actions:                  # From Level 2 (unchanged); you add action_check_balance_simple in Lab 3.1
  - action_bank_hours
  - action_check_balance_simple
```

`slots:` is at the same indentation level as `responses:` and `actions:`.
