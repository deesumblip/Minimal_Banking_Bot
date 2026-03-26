**Chapter 1.5 starting point:** This chapter assumes you **begin from the banking agent you finished at the end of Chapter 1.4**—the one reflected in **`level4/`** after those labs: multiple slots, **`transfer_money`**, **`action_process_transfer`**, and the Chapter 1.4 pipeline (**`CompactLLMCommandGenerator`**, **`endpoints.yml`** with **`action_endpoint`**, **`nlg`**, and **`model_groups`** as in the finished **`level4/`** agent). You are not starting from scratch.

**Repository note:** In this course repository, **`level5/`** is checked in as that **Chapter 1.4 completion** baseline (same general shape as the finished **`level4/`** agent: domain, flows—including **`goodbye`**, **`holiday_hours`**, **`check_balance`**, **`transfer_money`**—and **Level 2–4** actions). You still **build** Chapter 1.5 in the labs (tools folder, **`tools:`** in **`endpoints.yml`**, **`transfer_money_tools`**, **`action_process_transfer_with_tools`**). Use **`level4/`** as the reference for “Chapter 1.4 end” and **`level5/`** for “work in progress” as you add tool calling.

---

Before we add tool calling, here is a quick recap of what you have at **Chapter 1.4 completion**. All of that behavior stays in place; Chapter 1.5 **adds** tools on top.

**Naming:** *Level 5* means the outcome of Chapter 1.5. The **`level5/`** folder is where Chapter 1.5 changes go; it continues from the same agent you completed in **`level4/`**.

## Where Chapter 1.5 happens

You add the **`tools/`** module, **`endpoints.yml`** registration, the **`transfer_money_tools`** flow, and **`action_process_transfer_with_tools`** under **`level5/`**. The **next page** summarizes the lab sequence and what you will add in each step.

Use the **same virtual environment** as in Chapter 1.4 (project root); there is no new venv inside **`level5/`**.

---

## What you have at Chapter 1.4 completion

### Domain (`domain/basics.yml`)

- Responses: `utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`, `utter_ask_account`, `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- Slots: `account`, `amount`, `recipient`, `account_from`
- Actions: `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`, `action_process_transfer`

### Flows (`data/basics/`)

- greet, help, contact, goodbye, hours, holiday_hours, check_balance, transfer_money

### Actions (`actions/`)

- `action_bank_hours.py`, `action_holiday_hours.py`, `action_check_balance_simple.py`, `action_process_transfer.py`

### Config

- **`config.yml`**, **`credentials.yml`**, **`endpoints.yml`** (no **`tools:`** section until **Lab 3.1**). Config uses **`assistant_id: level5-agent`** so this assistant is distinct from **`level4-agent`**.

**Heads-up:** Until you register tools, your **`endpoints.yml`** matches the Chapter 1.4 pattern ( **`action_endpoint`**, **`nlg`**, **`model_groups`** ). When you reach the lab that registers tools, you will add a **`tools:`** block without removing or renaming those sections.

---

## What you add in Chapter 1.5

In order, you will:

- Create the **`tools/`** folder and **`banking_tools.py`** (**Lab 2.1**)
- Register tools in **`endpoints.yml`** (**Lab 3.1**)
- Add **`action_process_transfer_with_tools`** and **`transfer_money_tools.yml`** (**Lab 4.1**)
- Train and test (**Labs 5.1** and **5.2**)

---

## What Level 4 could not do

Your Chapter 1.4 agent used **actions** that flows call by name. It could not let the **LLM decide at runtime** which operations to run (for example, balance check versus transfer) based on free-form dialogue alone. Chapter 1.5 adds **tools**: functions the LLM can discover and call dynamically so the agent can adapt to the conversation.
