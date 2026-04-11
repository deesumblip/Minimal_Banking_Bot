Here is a quick recap of what you built in Level 2. In this chapter you will add **slots**, which give the agent memory across turns. None of your Level 2 work goes away. Level 3 adds new pieces on top of the same agent.

## Level 3 setup

The **level3** folder in this course is a **ready-to-use copy** of the expected end state after **Level 2** (Custom Actions): same domain shape, flows, and **both** Level 2 custom action files. You do **not** recreate `action_holiday_hours.py` in Level 3; it is **already in** `level3/actions/` so training matches the `holiday_hours` flow. If you completed Level 2 in your own repo, your files should match this starter.

In this repository, **`level2/`** is maintained as that **same** Level 2 completion snapshot: the same responses, `data/basics/` flows, and `actions/` Python files as **`level3/`**, so the runnable agent matches. The only intentional differences are **`assistant_id`** in `config.yml` (`level2-agent` vs `level3-agent`) and the comment block at the top of `domain/basics.yml` (the YAML under `version:` is the same).

In this chapter you will:

- Add slots and an ask response in the domain
- Register the new action name in the domain (you will create the Python file in Lab 4.1)
- Create the check_balance flow

Everything else stays as it was at the start of `level3/`.

---

## What is already in the Level 3 starter

### Domain (`domain/basics.yml`)

- Level 1 responses: `utter_greet`, `utter_help`, `utter_contact`, and `utter_goodbye`
- An `actions:` section with **`action_bank_hours`** and **`action_holiday_hours`** (required for the existing flows)

### Flows (`data/basics/`)

- Level 1 flows: `greet`, `help`, `contact`, `goodbye` (as in the repo)
- Level 2 flows: **`hours.yml`** and **`holiday_hours.yml`**

### Actions (`actions/`)

These Python files are **preloaded** for you at the start of Level 3:

- **`action_bank_hours.py`** (bank hours by day of week)
- **`action_holiday_hours.py`** (holiday schedule; same role as in Level 2, Lab 3.1)

You will **add** in Level 3:

- **`action_check_balance_simple.py`** in **Lab 4.1** (new file; not in the starter)

### System and config

Same pattern as Level 2: config and endpoints under `level3/`, project **`.venv`** at the **project root**.

---

## What Level 2 could not do

Your Level 2 agent could run custom Python code, but it could not:

- Remember information from the conversation
- Store user-provided data
- Use information from earlier in the conversation
- Ask for missing information and remember it

**Example.** Suppose a user says, "Check my balance." A Level 2 agent cannot remember which account they mean. It cannot ask for an account number, store that answer, and reuse it in a later turn. Slots in Level 3 fix that gap.
