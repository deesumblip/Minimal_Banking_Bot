You already know how to read a slot from the tracker. Sometimes the language model fills the slot with generic text instead of a real account number, for example the phrase "account number" instead of digits. The action for this chapter treats those cases as placeholders and asks the user again.

Here is the logic you will use in `action_check_balance_simple.py`.

1. Read the slot with `account = tracker.get_slot("account") or "<missing>"`.
2. Build a list of values that count as placeholders, such as `"account number"`, `"user_account_number"`, and `"<missing>"`.
3. If the current value is a placeholder, send the ask response with `dispatcher.utter_message(response="utter_ask_account")` and return from `run()`.
4. If the value looks real, send your balance message with `dispatcher.utter_message(text=...)`.

Always validate slot values before you trust them in business logic or user-facing text.

#### Quick review

Lab 4.1 is the next page in this unit. It uses only ideas you have already seen in Chapter 1.2 and earlier pages in Chapter 1.3.

**Level 2 reference.** Open `action_bank_hours.py` in Chapter 1.2, in the lesson called *The Action Class Deep Dive*. That file shows the imports from `typing`, `rasa_sdk`, and `rasa_sdk.executor`. It shows a class that subclasses `Action`, a `name()` method whose string matches the domain, and a `run()` method with return type `List[Dict[Text, Any]]`. Most simple actions end `run()` with `return []`.

**Lab 4.1 naming.** Use the same pattern with new names. The class is `ActionCheckBalanceSimple`. The string from `name()` is `action_check_balance_simple`. That mirrors how `ActionBankHours` pairs with `action_bank_hours`.

**Unit 4.1 in this chapter.** You already saw `tracker.get_slot("account")`, an f-string in a balance-style message, and `return []`.

**Code you will reuse in Lab 4.1.** The block below is the placeholder branch and the success branch. It matches the fill-in-the-blanks exercise and the grader.

```python
placeholder_values = ["account number", "user_account_number", "<missing>"]

if account.lower() in [p.lower() for p in placeholder_values]:
    dispatcher.utter_message(response="utter_ask_account")
    return []

dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")
return []
```

The condition compares the slot string to each placeholder without caring about letter case. For example, `"Account Number"` still counts as a placeholder.

In **Lab 4.1** you will create `action_check_balance_simple.py` using this logic. The lab has a fill-in-the-blanks exercise for the full script, then a graded code check on the file you save. After Lab 4.1, **Unit 5** shows how to add the flow that collects the slot and runs this action.
