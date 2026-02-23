# 7.3 Best Practices

**Slot naming.** Use descriptive, lowercase names such as `account`, `user_name`, or `transfer_amount`. Avoid vague names like `a`, `slot1`, or `data`.

**In actions.** Always check for `None` before using a slot, e.g. `if account: ...` or `account = tracker.get_slot("account") or "<missing>"`. Validate placeholder values like "account number" or "<missing>" and re-prompt with `utter_ask_<slot_name>` when the value is not real.

**Ask responses.** Name ask responses `utter_ask_<slot_name>` so Rasa can match them to the slot. For example slot `account` uses `utter_ask_account`.
