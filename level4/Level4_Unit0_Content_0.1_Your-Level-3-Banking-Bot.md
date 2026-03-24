Before we add multiple slots for the transfer flow, here is a quick recap of what you built in Level 3. All of this remains unchanged. Level 4 builds on top of it.

**Naming in this chapter:** *Level 3* is the outcome of Chapter 1.3. The **`level3/`** folder is that bot; **`level4/`** is the copy where you do Chapter 1.4 work.

## Where Chapter 1.4 happens

You add the transfer flow and any Level 4 pipeline changes under **`level4/`** (a copy of your Level 3 tree). The **lab sequence** and the **full checklist**—including required **`config.yml`** / **`endpoints.yml`** differences—are on **Unit 0.2 What Level 4 Adds**. Use that page when you set up or verify `level4/`.

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

### System and config (Chapter 1.3)

In **`level3/`**, **`config.yml`** uses **`SearchReadyLLMCommandGenerator`** (Chapter 1.3 pattern). Your **`endpoints.yml`** and **`.env`** supply API keys.

**Heads-up when you open `level4/`:** Chapter 1.4 is **not** “same pipeline, new `assistant_id` only.” You will use a different command generator, add **`flow_retrieval`**, and align **`model_groups`** so multi-slot FillSlot works reliably. On **Unit 0.2 What Level 4 Adds**, read **§2** (pipeline) when you work in `level4/`; use **`level4/PIPELINE_CHAPTER_1_3_AND_4.md`** for deeper rationale.

---

## What Level 3 Couldn't Do

Your Level 3 bot could collect one piece of information (the account number) and use it in an action. It could not:

- Collect several pieces of information in one flow (e.g. amount, recipient, and source account for a transfer)
- Run an action that uses multiple slot values together

**Example.** If a user said "I want to transfer money", your Level 3 bot could not ask for the amount, then the recipient, then the source account, remember all three, and then run an action that uses them together.

Level 4 adds multiple slots and one new flow so the bot can do exactly that.
