# 0.2 What Level 3 Adds

Level 3 introduces **Slots**—the bot's memory. This enables:

- Remembering information from the conversation
- Storing user-provided data (like account numbers)
- Asking for missing information
- Using stored information in actions

**Your existing Level 2 bot continues to work**—Level 3 adds memory on top of it!

## What's New in Level 3

**New in Domain** (you'll add these in Lab 3.1):
- `slots:` section — Defines what the bot remembers
- `account` slot — Stores the user's account number
- New response `utter_ask_account` — Used when asking for account number

**New Files Provided** (already in `level3/actions/`):
- `actions/action_check_balance_simple.py` — Action that reads the `account` slot (provided; you'll explore it in Lab 5.1)

**New Flows** (you'll create this in Lab 4.1):
- `data/basics/check_balance.yml` — Flow that collects account number before checking balance

**Unchanged**:
- All Level 2 responses remain
- All Level 2 flows remain
- All Level 2 actions remain
