Here is a quick recap of what you built in Level 2. In this chapter you will add **slots**, which give the bot memory across turns. None of your Level 2 work goes away. Level 3 adds new pieces on top of the same bot.

## Level 3 Setup

The **level3** folder is set up as a copy of your Level 2 bot. In this chapter you will:

- Add slots and an ask response in the domain
- Register the new action name in the domain (you will create the action file in Lab 4.1)
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
- **Level 3.** In Lab 3.1 you register **action_check_balance_simple** in the domain. In Lab 4.1 you **write** `action_check_balance_simple.py`.

### System and config

Unchanged from Level 2.

---

## What Level 2 Couldn't Do

Your Level 2 bot could run custom Python code, but it could not:

- Remember information from the conversation
- Store user-provided data
- Use information from earlier in the conversation
- Ask for missing information and remember it

**Example.** Suppose a user says, "Check my balance." A Level 2 bot cannot remember which account they mean. It cannot ask for an account number, store that answer, and reuse it in a later turn. Slots in Level 3 fix that gap.
