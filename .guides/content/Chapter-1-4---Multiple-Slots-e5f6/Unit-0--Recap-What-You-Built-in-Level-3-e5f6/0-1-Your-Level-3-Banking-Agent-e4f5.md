**Chapter 1.4 starting point:** Everything in this chapter assumes you **begin from the final banking agent at the end of Chapter 1.3**—the agent you finished in **`level3/`** after Chapter 1.3 labs. You are **not** starting from scratch. **`level4/`** is the folder where you do Chapter 1.4 work (typically a copy of your Level 3 tree).

**Repository note:** The **`level4/`** folder in this repository is initialized to the **Chapter 1.3 completion** state (same idea as **`level3/`**: SearchReady pipeline placeholders, Level 3 endpoints, **`account`** + check-balance pieces, **no** transfer flow or **`action_process_transfer`** yet). You **add** everything in Chapter 1.4 through the labs. **Lab 0.1** has you **fill in the blanks** and **paste** into **`config.yml`** / **`endpoints.yml`** (then the code test). Graders that validate the **finished** Level 4 agent may expect a completed tree after you finish the labs. Compare **`level3/`** and **`level4/`** to see “Chapter 1.3 end” vs “your Chapter 1.4 work in progress.”

---

Before we add multiple slots for the transfer flow, here is a quick recap of what you have at **Chapter 1.3 completion**. All of this stays in place; Level 4 adds transfer pieces on top.

**Naming:** *Level 3* means the outcome of Chapter 1.3. The **`level3/`** folder is that agent; **`level4/`** is where Chapter 1.4 changes go.

## Where Chapter 1.4 happens

You add the transfer flow and Chapter 1.4 pipeline settings under **`level4/`**. The **lab sequence** and the **full checklist** are on **Unit 0.2 What Level 4 Adds**.

---

## What you have at Chapter 1.3 completion

### Domain (`domain/basics.yml`)

- Responses: `utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`, `utter_ask_account`
- A `slots:` section with the `account` slot (type text)
- An `actions:` section listing **`action_bank_hours`**, **`action_holiday_hours`**, and **`action_check_balance_simple`**

### Flows (`data/basics/`)

- Level 1 flows: `greet`, `help`, `contact`, `goodbye`
- Level 2 flows: `hours` (uses `action_bank_hours`); `holiday_hours` (uses `action_holiday_hours`)
- Level 3 flow: `check_balance` (collects `account`, then runs `action_check_balance_simple`)

### Actions (`actions/`)

- `action_bank_hours.py`
- `action_holiday_hours.py`
- `action_check_balance_simple.py` (reads the `account` slot and returns a demo balance)

### System and config (Chapter 1.3)

In **`level3/`**, **`config.yml`** uses **`SearchReadyLLMCommandGenerator`** (Chapter 1.3 pattern). Your **`endpoints.yml`** and **`.env`** supply API keys.

**Heads-up when you configure `level4/`:** Chapter 1.4 is **not** “same pipeline, new `assistant_id` only.” You will use a different command generator, add **`flow_retrieval`**, and align **`model_groups`** so multi-slot FillSlot works reliably. On **Unit 0.2 What Level 4 Adds**, read **section 2** (pipeline). Use **`level4/PIPELINE_CHAPTER_1_3_AND_4.md`** for rationale.

**File-level reference:** **`LEVEL3_TO_LEVEL4_FILE_DELTA.md`**

---

## What Level 3 could not do

Your Chapter 1.3 agent could collect one piece of information (the account number) and use it in an action. It could not:

- Collect several pieces of information in one flow (e.g. amount, recipient, and source account for a transfer)
- Run an action that uses multiple slot values together

**Example.** If a user said "I want to transfer money", your Level 3 agent could not ask for the amount, then the recipient, then the source account, remember all three, and then run an action that uses them together.

Chapter 1.4 adds multiple slots and one new flow so the agent can do exactly that, in **`level4/`**, through the labs.
