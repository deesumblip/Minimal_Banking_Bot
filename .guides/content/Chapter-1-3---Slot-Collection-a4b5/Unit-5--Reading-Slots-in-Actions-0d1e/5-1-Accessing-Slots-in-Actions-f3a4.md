# 5.1 Accessing Slots in Actions

To use slot values in your actions, read them from the `tracker` parameter:

```python
def run(self, dispatcher, tracker, domain):
    account = tracker.get_slot("account")
    if account:
        dispatcher.utter_message(text=f"Balance for account {account} is $123.45")
    else:
        dispatcher.utter_message(text="I don't have your account number.")
    return []
```

Slots can be `None` if not set yet. Always check before using.

**Lab 5.1: Exploring Actions with Slots** lets you explore the real action file (`action_check_balance_simple.py`) to see how it reads the slot and handles placeholders.
