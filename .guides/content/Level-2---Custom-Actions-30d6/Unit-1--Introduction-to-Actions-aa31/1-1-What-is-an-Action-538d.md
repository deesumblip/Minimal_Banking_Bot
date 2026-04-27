Rasa has three action types: 
1. **Responses**: Send text or media to the user
2. **Custom actions**: Execute user-defined code
3. **Default actions**: Run automatically to manage conversation state. 

You worked with responses in Level 1. Level 2 introduces custom actions.

| | 1. Responses (`utter_*`) | 2. Custom Actions (`action_*`) | 3. Default Actions |
|---|---|---|---|
| **What it is** | Predefined text, rich media, or buttons | User-defined code executed by the action server | Built-in actions Rasa runs automatically behind the scenes |
| **Defined in** | `domain/basics.yml` under `responses:` | `actions/*.py`, registered in `domain/basics.yml` under `actions:` | Built into Rasa, no definition required |
| **Logic** | None, static text only | Any Python | Fixed behaviour, e.g. starting a new session, waiting for user input |
| **Example** | `action: utter_greet` | `action_bank_hours` | `action_session_start`, `action_listen` |

A custom action is user-defined code that executes during a conversation. In this course you will write custom actions as Python classes using the Rasa SDK. Where a response sends predefined text, a custom action can run any logic: calculations, database queries, API calls. It returns events to update the conversation state.

#### Example: Bank Hours

**Response (static):**

```yaml
utter_hours:
  - text: "We're open Monday-Friday 9am-5pm, Saturday 10am-2pm."
```

**Custom action (dynamic):**

```python
def run(self, dispatcher, domain):
    # Check current day
    # Check if it's a holiday
    # Return dynamic message: "We're open today until 5pm" or "We're closed today"
```

Use a response when the text never changes. Use a custom action when the reply depends on the current date, a database value, a calculation, or any condition evaluated at runtime.

---

