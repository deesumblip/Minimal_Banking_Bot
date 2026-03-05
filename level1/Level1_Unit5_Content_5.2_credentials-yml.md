### 5.2 credentials.yml

The `credentials.yml` file defines **how the bot connects to chat interfaces**.

**File Location**: `credentials.yml` (root of your bot folder)

#### Key sections

- **`rest:`** – Enables REST API access (empty = use defaults)
- **`socketio:`** – Enables Socket.IO; required for Inspector testing
- **`session_persistence: true`** – Keeps conversation state between messages; should stay `true`

For Level 1, you typically don't need to modify this file. To add Slack, Teams, or other channels, add the corresponding section with credentials.

---
