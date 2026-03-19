You've seen how to read a slot. Sometimes the LLM extracts generic text like "account number" instead of the actual number. In `action_check_balance_simple.py` the code does the following.

1. Read the slot with `account = tracker.get_slot("account") or "<missing>"`.
2. Check for placeholder values, for example "account number", "user_account_number", or "<missing>".
3. If it's a placeholder, re-prompt with `dispatcher.utter_message(response="utter_ask_account")` and return.
4. If it's a real value, use it in the response.

Always validate slot values before using them in logic or messages.

#### Patterns you already saw (so the lab blanks are not guesses)

From **Level 2** (`action_bank_hours.py` in *The Action Class Deep Dive*): you import `Any`, `Dict`, `List`, `Text` from `typing`; `Action`, `Tracker` from `rasa_sdk`; `CollectingDispatcher` from `rasa_sdk.executor`; you define `class ActionBankHours(Action):`, return `"action_bank_hours"` from `name()`, and type `run(...) -> List[Dict[Text, Any]]`. For this lab, use the **same pattern**: class **`ActionCheckBalanceSimple`** with **`action_check_balance_simple`** as the string in `name()` (PascalCase class + `action_` + snake_case name, like the bank-hours example).

From **Unit 4.1** you already saw `tracker.get_slot("account")`, an f-string balance line, and `return []`.

Putting the placeholder steps together in code (this matches what you will fill in **Lab 4.1**):

```python
placeholder_values = ["account number", "user_account_number", "<missing>"]

if account.lower() in [p.lower() for p in placeholder_values]:
    dispatcher.utter_message(response="utter_ask_account")
    return []

dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")
return []
```

The list comprehension compares the slot string to each placeholder **case-insensitively**—so `"Account Number"` still counts as a placeholder.

In **Lab 4.1** you'll **write** `action_check_balance_simple.py` with this logic. That lab includes a **fill-in-the-blanks** exercise (same script you paste into the file) and a **graded code assessment** that checks your action file (structure, slot read, placeholder handling, and balance message). Complete both assessments when you finish the lab. In the next unit you will create the flow that collects the slot and runs this action.
