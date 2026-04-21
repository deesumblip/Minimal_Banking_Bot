When an action runs, Rasa passes a **tracker** object into `run()`. The tracker holds the conversation state, including any slot values that were collected earlier. You read a slot by calling `tracker.get_slot` with the slot name.

```python
def run(self, dispatcher, tracker, domain):
    account = tracker.get_slot("account")
    if account:
        dispatcher.utter_message(text=f"Balance for account {account} is $123.45")
    else:
        dispatcher.utter_message(text="I don't have your account number.")
    return []
```

A slot may be `None` if the user has not given a value yet. Check for that before you use the value in logic or in a message.

You will implement a fuller version of this pattern in **Lab 4.1** inside `action_check_balance_simple.py`. Unit 4.2 in this chapter explains how to handle bad or placeholder slot text. **Unit 5** then shows how to build the flow that collects the slot before your action runs.
