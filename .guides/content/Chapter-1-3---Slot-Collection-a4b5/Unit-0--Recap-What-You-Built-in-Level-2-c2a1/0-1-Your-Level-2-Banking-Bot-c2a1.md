Before we add slots—the bot's memory—here is a quick recap of what you built in Level 2. All of this remains unchanged. Level 3 builds on top of it.

## Level 3 Setup

The **level3** folder is set up as a copy of your Level 2 bot. In this chapter you will:

- Add slots and an ask response in the domain
- Register the new action (the action file is already in the project)
- Create the check_balance flow

Everything else is your Level 2 content.

---

## What You Have from Level 2

### Domain (`domain/basics.yml`)

- Level 1 responses: `utter_greet`, `utter_help`, `utter_contact`, and often `utter_goodbye`
- An `actions:` section with `action_bank_hours` registered
- If you did Level 2, your domain may also list `action_holiday_hours`

### Flows (`data/basics/`)

- Level 1 flows: `greet`, `help`, `contact`
- Level 2 flow: `hours` (uses `action_bank_hours`)
- If you did Level 2 Lab 5.1: `holiday_hours` as well

### Actions (`actions/`)

- `action_bank_hours.py`
- If you built it in Level 2: `action_holiday_hours.py`
- **Provided for Level 3:** `action_check_balance_simple.py` — you will register it in the domain in Lab 3.1

### System and config

Unchanged from Level 2.

---

## What Level 2 Couldn't Do

Your Level 2 bot could run custom Python code, but it could not:

- Remember information from the conversation
- Store user-provided data
- Use information from earlier in the conversation
- Ask for missing information and remember it

**Example.** If a user said "Check my balance", your Level 2 bot could not remember which account they have, ask for the account number and remember it, or use that account number in a later reply.
