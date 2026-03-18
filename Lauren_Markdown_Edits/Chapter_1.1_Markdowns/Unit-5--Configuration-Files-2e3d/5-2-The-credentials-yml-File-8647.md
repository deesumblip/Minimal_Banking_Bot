

The `credentials.yml` file defines **how the bot connects to chat interfaces**.

**File Location**: `credentials.yml` (root of your bot folder)

#### Complete credentials.yml Breakdown

```yaml
rest:

socketio:
  bot_message_evt: bot_uttered
  session_persistence: true
  user_message_evt: user_uttered
```

#### Section-by-Section Explanation

1. **`rest:`** (empty)
   - Enables REST API access
   - Allows programmatic access to the bot
   - Empty means "use defaults"

2. **`socketio:`**
   - Enables Socket.IO interface
   - This is what Inspector uses for testing
   - Required for the web-based testing interface

3. **`bot_message_evt: bot_uttered`**
   - Event name when bot sends a message
   - Technical detail - usually don't need to change

4. **`session_persistence: true`**
   - Keeps conversation state between messages
   - Required for multi-turn conversations
   - Should always be `true`

5. **`user_message_evt: user_uttered`**
   - Event name when user sends a message
   - Technical detail - usually don't need to change

#### When You'd Modify This

- **Add Slack**: Add a `slack:` section with your Slack credentials
- **Add Teams**: Add a `msteams:` section
- **Add custom channel**: Add your custom channel configuration

For Level 1, you typically don't need to modify this file.

{Check It!|assessment}(multiple-choice-372693770)


---