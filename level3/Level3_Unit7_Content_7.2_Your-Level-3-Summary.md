Your agent can do all Level 1 and Level 2 capabilities: responses, flows, and actions. It can remember user-provided information in slots and ask for missing information and use it in actions, such as checking the balance for an account.

Key additions are the `slots:` section and `utter_ask_account` in the domain, the `check_balance.yml` flow with `collect: account`, and `action_check_balance_simple`, which reads the slot and handles placeholders. Use clear slot names, keep `utter_ask_*` consistent with slot names, and validate slot values in your action.
