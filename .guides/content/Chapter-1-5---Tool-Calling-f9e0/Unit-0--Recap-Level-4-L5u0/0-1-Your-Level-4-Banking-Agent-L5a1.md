**Starting point:** Chapter 1.5 extends the **banking agent you finished in Chapter 1.4**—same idea as **`level4/`** (CALM stack with **`SearchReadyLLMCommandGenerator`**, **`endpoints.yml`** with **`action_endpoint`**, **`nlg`**, **`model_groups`**, slots, **`transfer_money`**, and related flows). You are **not** starting from scratch.

**Where to work:** Activate the venv at **project root**, then **`cd level5`** for every command (**`python -m rasa …`**).

**What you add in 1.5:** In order, the labs have you add **`prompt_template`** / **`data/prompts/`**, **`tools/`**, **`tools:`** in **`endpoints.yml`**, **`transfer_money_tools`**, and **`action_process_transfer_with_tools`**. *Level 5* names the Chapter 1.5 skill; **`level5/`** is where those files live.

---

What follows is a **quick recap of Chapter 1.4 completion**. That behavior stays; Chapter 1.5 **adds** tool calling on top.

## Where Chapter 1.5 happens

All of the above lives under **`level5/`** as you work through the labs. The **next page** spells out the lab order step by step.

Use the **same virtual environment** as in Chapter 1.4 (project root); there is no separate venv inside **`level5/`**.

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

### Config (at Chapter 1.5 **start**)

- **`config.yml`**, **`credentials.yml`**, **`endpoints.yml`**. The **`level5/`** project sets **`assistant_id: level5-agent`** so it does not collide with the **`level4/`** assistant id (**`level4-agent`** in this repository’s **`level4/config.yml`**).
- **`SearchReadyLLMCommandGenerator`** is already in **`pipeline`** (same idea as Chapter 1.4). The canonical command prompt template ships as **`resources/command_prompt_v3_slot_names.jinja2`**; before **Lab 2.0** you have **no** **`prompt_template`** in **`config.yml`** and **no** copy under **`data/prompts/`**—**Lab 2.0** has you copy from **`resources/`** into **`data/prompts/`** and set **`prompt_template`** in **`config.yml`** (first lab in Unit 2).
- **`endpoints.yml`** matches the Chapter 1.4 pattern (**`action_endpoint`**, **`nlg`**, **`model_groups`**) and has **no** **`tools:`** section until **Lab 3.1**.

**Heads-up:** When you reach **Lab 3.1**, you will **add** a **`tools:`** block without removing or renaming **`action_endpoint`**, **`nlg`**, or **`model_groups`**.

---

## What you add in Chapter 1.5

In order, you will:

- Copy the command prompt from **`resources/`** into **`data/prompts/`** and set **`prompt_template`** in **`config.yml`** (**Lab 2.0**)
- Create the **`tools/`** folder and **`banking_tools.py`** (**Lab 2.1**)
- Register tools in **`endpoints.yml`** (**Lab 3.1**)
- Add **`action_process_transfer_with_tools`**, **`transfer_money_tools.yml`**, and the **`from_llm`** domain conditions for **`transfer_money_tools`** (**Lab 4.1**)
- Train and test (**Labs 5.1** and **5.2**)

---

## What Chapter 1.4 did not cover

In Chapter 1.4, **actions** are whatever the flow names at each step—the runtime does not pick between them. The **LLM** does not freely choose “balance check now” versus “transfer” from raw dialogue alone. Chapter 1.5 adds **tools**: functions the model can select and call as the conversation unfolds.
