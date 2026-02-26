Before we add multiple slots for the transfer flow, here is a quick recap of what you built in Level 3. All of this remains unchanged. Level 4 builds on top of it.

## Level 4 Setup

The **level4** folder is set up as a copy of your Level 3 bot. In this chapter you will:

- Add three new slots and three ask responses in the domain (Lab 2.1)
- Register and create the new action `action_process_transfer` (Labs 4.1 and 4.2)
- Create the transfer_money flow that collects all three slots (Lab 4.1)
- Train and test (Labs 4.4 and 4.5)

Everything else is your Level 3 content.

---

## What You Have from Level 3

### Domain (`domain/basics.yml`)

- Responses: `utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`, `utter_ask_account`
- A `slots:` section with the `account` slot (type text)
- An `actions:` section with `action_bank_hours` and `action_check_balance_simple`

### Flows (`data/basics/`)

- Level 1 flows: `greet`, `help`, `contact`, `goodbye`
- Level 2 flow: `hours` (uses `action_bank_hours`)
- Level 3 flow: `check_balance` (collects `account`, then runs `action_check_balance_simple`)

### Actions (`actions/`)

- `action_bank_hours.py`
- `action_check_balance_simple.py` (reads the `account` slot and returns a demo balance)

### System and config

Unchanged from Level 3. Config uses `assistant_id: level4-bot`.

---

## What Level 3 Couldn't Do

Your Level 3 bot could collect one piece of information (the account number) and use it in an action. It could not:

- Collect several pieces of information in one flow (e.g. amount, recipient, and source account for a transfer)
- Run an action that uses multiple slot values together

**Example.** If a user said "I want to transfer money", your Level 3 bot could not ask for the amount, then the recipient, then the source account, remember all three, and then run an action that uses them together.

Level 4 adds multiple slots and one new flow so the bot can do exactly that.
