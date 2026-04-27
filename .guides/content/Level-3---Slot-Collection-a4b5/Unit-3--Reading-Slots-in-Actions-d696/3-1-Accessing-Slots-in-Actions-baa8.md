The **read** step in the define → collect → read pattern happens inside a custom action. When Rasa calls `run()`, it passes a `tracker` object that holds the full conversation state, including every slot collected so far.

```python
account = tracker.get_slot("account")
```

A slot returns `None` if it has not been set. Check for that before using the value in a message or in logic:

```python
account = tracker.get_slot("account")
if not account:
    dispatcher.utter_message(text="I don't have your account number.")
    return []
```

In Lab 3.1 the flow guarantees the slot is set before the action runs, so the None check is omitted for clarity. In production, always handle it.
 
{Check It!|assessment}(multiple-choice-932698064)
 
