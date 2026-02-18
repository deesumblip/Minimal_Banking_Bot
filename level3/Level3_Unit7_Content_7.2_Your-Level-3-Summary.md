# 7.2 Your Level 3 Banking Bot: Summary

**What your bot can do now:**
- All Level 1 and Level 2 capabilities (responses, flows, actions)
- Remember user-provided information (slots)
- Ask for missing information and use it in actions (e.g. check balance for an account)

**Key additions:** `slots:` and `utter_ask_account` in domain; `check_balance.yml` flow with `collect: account`; `action_check_balance_simple` that reads the slot and handles placeholders.

**Best practices:** Use descriptive slot names; always check for `None` or placeholders in actions; name ask responses `utter_ask_<slot_name>`.
