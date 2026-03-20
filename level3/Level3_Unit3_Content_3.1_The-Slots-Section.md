You define slots in the domain file, in the same file where you already keep responses and actions. This page is the **define** step from **How Slots Work** earlier in this chapter. You add the slot and the matching ask response first. Later units cover collecting the slot in a flow and reading it in an action.

## Domain structure after Lab 3.1

The example below shows how your domain will look after you finish Lab 3.1. You add the `slots:` block and the `utter_ask_account` response. You also add `action_check_balance_simple` to the `actions:` list. The Level 3 starter already lists **`action_bank_hours`** and **`action_holiday_hours`**; after Lab 3.1 all three names below should be present so flows such as **`holiday_hours.yml`** validate when you train.

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

actions:                  # Starter includes Level 2 actions; you add action_check_balance_simple in Lab 3.1
  - action_bank_hours
  - action_holiday_hours
  - action_check_balance_simple
```

Remember that `slots:` sits at the same indentation level as `responses:` and `actions:`.
