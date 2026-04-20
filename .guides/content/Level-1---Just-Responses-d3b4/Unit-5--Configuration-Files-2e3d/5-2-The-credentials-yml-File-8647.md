`credentials.yml` defines how your agent connects to chat interfaces. You do not need to modify this file in this course.

File Location: `credentials.yml` (root of your agent folder)

```yaml
rest:

socketio:
  bot_message_evt: bot_uttered
  session_persistence: true
  user_message_evt: user_uttered
```

| Field | What it does |
|---|---|
| `rest` | Enables the REST API channel. Empty means use defaults. |
| `socketio` | Enables the Socket.IO channel, used by the Rasa Inspector for testing in this course. |
| `bot_message_evt` | The event name emitted when the agent sends a message. |
| `session_persistence` | Keeps conversation state across messages. Required for multi-turn conversations. |
| `user_message_evt` | The event name emitted when the user sends a message. |

To connect additional channels such as Slack, Twilio, or a custom interface, add the relevant section to this file with the required credentials. Each channel Rasa supports has its own configuration block.

{Check It!|assessment}(multiple-choice-372693770)


---
