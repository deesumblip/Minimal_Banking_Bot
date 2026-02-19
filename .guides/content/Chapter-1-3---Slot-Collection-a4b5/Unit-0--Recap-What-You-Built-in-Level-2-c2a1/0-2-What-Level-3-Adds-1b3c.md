Level 3 introduces **Slots**—the bot's memory. This enables:

- Remembering information from the conversation
- Storing user-provided data (like account numbers)
- Asking for missing information
- Using stored information in actions

**Your existing Level 2 bot continues to work**—Level 3 adds memory on top of it!

## What's New in Level 3

**New in Domain**:
- `slots:` section — Defines what the bot remembers
- `account` slot — Stores the user's account number
- New response `utter_ask_account` — Used when asking for account number

**New Files**:
- `actions/action_check_balance_simple.py` — Action that reads the `account` slot

**New Flows**:
- `data/basics/check_balance.yml` — Flow that collects account number before checking balance

**Unchanged**:
- All Level 2 responses remain
- All Level 2 flows remain
- All Level 2 actions remain
