### 2.2 Understanding the Parameters

#### Dispatcher

The `dispatcher` is your way to communicate with the user:

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

The `tracker` contains conversation information (we'll use this more in Level 3):

```python
# Get conversation history (Level 3+)
events = tracker.events

# Get slots (Level 3+)
account = tracker.get_slot("account")
```

For Level 2, we don't use the tracker much - it's mainly for Level 3 when we add memory.

#### Domain

The `domain` contains your bot's configuration:

```python
# Access domain (rarely needed)
responses = domain.get("responses", {})
```

For Level 2, you typically don't need to access the domain directly.

**Next**: In Unit 3 you'll use this structure to create your own action, and in Lab 3.1 you'll build `action_holiday_hours.py`.

---
