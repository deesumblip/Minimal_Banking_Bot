# 4.1 Accessing Slots in Actions

To use slot values in your actions, you read them from the `tracker` parameter.

```python
def run(self, dispatcher, tracker, domain):
    account = tracker.get_slot("account")
    if account:
        dispatcher.utter_message(text=f"Balance for account {account} is $123.45")
    else:
        dispatcher.utter_message(text="I don't have your account number.")
    return []
```

Slots can be `None` if not set yet, so always check before using them.

In **Lab 4.1** you'll **write** this action in `action_check_balance_simple.py`. In the next unit you will create the flow that collects the slot and runs this action.
