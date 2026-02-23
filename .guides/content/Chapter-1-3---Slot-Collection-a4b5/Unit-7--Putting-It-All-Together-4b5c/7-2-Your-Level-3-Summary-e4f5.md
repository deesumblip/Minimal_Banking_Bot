Your bot can do all Level 1 and Level 2 capabilities (responses, flows, actions). It can remember user-provided information (slots) and ask for missing information and use it in actions (for example checking the balance for an account).

Key additions are the `slots:` section and `utter_ask_account` in the domain, the `check_balance.yml` flow with `collect: account`, and `action_check_balance_simple`, which reads the slot and handles placeholders. See **7.3 Best Practices** for slot naming and action tips.
