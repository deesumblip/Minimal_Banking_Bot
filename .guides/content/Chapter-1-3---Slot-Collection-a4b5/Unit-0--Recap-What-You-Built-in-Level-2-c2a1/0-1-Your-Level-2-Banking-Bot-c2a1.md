# 0.1 Your Level 2 Banking Bot

Before we add slots (memory), let's recap what you've already built in Level 2. **All of this remains unchanged**—Level 3 builds on top of it!

## What You Have from Level 2

**Domain File (`domain/basics.yml`)**:
- All Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`)
- `actions:` section with `action_bank_hours` registered

**Flows (`data/basics/`)**:
- All Level 1 flows (`greet`, `help`, `contact`)
- New Level 2 flow (`hours`) that uses `action_bank_hours`

**Actions (`actions/`)**:
- `action_bank_hours.py` — Returns bank hours dynamically

**System Patterns**: Unchanged from Level 1

**Configuration Files**: Unchanged from Level 2

## What Level 2 Couldn't Do

Your Level 2 bot could execute custom Python code, but it couldn't:
- Remember information from the conversation
- Store user-provided data
- Use information from earlier in the conversation
- Ask for missing information and remember it

**Example**: If a user asked "Check my balance", your Level 2 bot couldn't:
- Remember which account the user has
- Ask for the account number and remember it
- Use that account number in subsequent actions
