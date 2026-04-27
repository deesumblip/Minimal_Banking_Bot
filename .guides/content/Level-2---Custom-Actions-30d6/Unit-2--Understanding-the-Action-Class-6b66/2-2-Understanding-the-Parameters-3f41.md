`run()` receives three arguments from Rasa. Here is what each one gives you:


#### Dispatcher

The `dispatcher` sends messages back to the user.

```python
# Send a simple text message
dispatcher.utter_message(text="Hello!")

# Use a response from the domain
dispatcher.utter_message(response="utter_greet")

# Send multiple messages
dispatcher.utter_message(text="First message")
dispatcher.utter_message(text="Second message")
```

#### Tracker

The `tracker` holds conversation state, (i.e. slot values, event history, the latest user message). We'll use this more in Level 3:

```python
# Get conversation history (Level 3+)
events = tracker.events

# Get slots (Level 3+)
account = tracker.get_slot("account")
```


#### Domain

The `domain` provides access to your agent's configuration. Rarely needed in practice, and we won't use it in this course. 

```python
# Access domain (rarely needed)
responses = domain.get("responses", {})
```

**Next**: In Unit 3 you'll use this structure to create your own action, and in Lab 3.1 you'll build `action_holiday_hours.py`.

---
