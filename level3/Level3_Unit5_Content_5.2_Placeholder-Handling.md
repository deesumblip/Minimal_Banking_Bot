# 5.2 Placeholder Handling

Sometimes the LLM extracts generic text like "account number" instead of the actual number. In `action_check_balance_simple.py` we:

1. Read the slot: `account = tracker.get_slot("account") or "<missing>"`
2. Check for placeholder values (e.g. "account number", "user_account_number", "<missing>")
3. If it's a placeholder, re-prompt: `dispatcher.utter_message(response="utter_ask_account")` and return
4. If it's a real value, use it in the response

Always validate slot values before using them in logic or messages.

**Lab 5.1: Exploring Actions with Slots** – Open `action_check_balance_simple.py` and see how it reads the slot and handles placeholders. No graded assessment.
