You've seen how to read a slot. Sometimes the LLM extracts generic text like "account number" instead of the actual number. In `action_check_balance_simple.py` the code does the following.

1. Read the slot with `account = tracker.get_slot("account") or "<missing>"`.
2. Check for placeholder values, for example "account number", "user_account_number", or "<missing>".
3. If it's a placeholder, re-prompt with `dispatcher.utter_message(response="utter_ask_account")` and return.
4. If it's a real value, use it in the response.

Always validate slot values before using them in logic or messages.

In **Lab 5.1** you'll open `action_check_balance_simple.py` and see this in the code. That lab has no graded assessment.
