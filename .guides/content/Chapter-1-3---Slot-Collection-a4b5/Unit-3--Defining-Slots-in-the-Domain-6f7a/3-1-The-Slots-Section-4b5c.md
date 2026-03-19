You define slots in the domain file, in the same file where you already keep responses and actions. This page is the **define** step from **How Slots Work** earlier in this chapter. You add the slot and the matching ask response first. Later units cover collecting the slot in a flow and reading it in an action.

## Domain structure after Lab 3.1

The example below shows how your domain will look after you finish Lab 3.1. You add the `slots:` block and the `utter_ask_account` response. You also add `action_check_balance_simple` to the `actions:` list. Your existing Level 2 actions stay in the list.

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
  - action_holiday_hours   # Include if your Level 2 bot had this action (keep it; do not remove)
  - action_check_balance_simple
```

If your `level3` domain does not list `action_holiday_hours`, your `actions:` list can list `action_bank_hours` and `action_check_balance_simple`. If you already have `action_holiday_hours` from Level 2, keep that line and add `action_check_balance_simple` as another entry.

Remember that `slots:` sits at the same indentation level as `responses:` and `actions:`.

{Check It!|assessment}(multiple-choice-2551391875)
