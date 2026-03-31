**Starting point:** Chapter 1.5 adds **tool calling** on top of your **Chapter 1.4 banking agent**—transfer slots and **`transfer_money`**, **`endpoints.yml`** (**`action_endpoint`**, **`nlg`**, **`model_groups`**), and the other flows you already trained. You are not starting from scratch.

Activate the venv at **project root**, then **`cd level5`** for every **`python -m rasa …`** command.

**Repository layout:** When we say **“Level 4”** in Unit 0 (for example **0.1 Your Level 4 Banking Agent**), we mean your **Chapter 1.4 skills and bot**, not the **`level4/`** folder as checked into git—that tree is the **Chapter 1.3** starter. **`level5/`** is this course’s **Chapter 1.4–complete** baseline for tool calling. If **`level5/`** differs slightly from files you kept in **`level4/`**, read the comment headers at the top of **`level5/config.yml`**, **`level5/domain/basics.yml`**, and **`level5/data/basics/check_balance.yml`**.

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
- Actions (**custom**): `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`, `action_process_transfer`
- Actions (**responses used as flow steps**): every **`utter_*`** name listed under **Responses** must also appear under **`actions:`** so Rasa can run those steps in flows.

### Flows (`data/basics/`)

- greet, help, contact, goodbye, hours, holiday_hours, check_balance, transfer_money

### Actions (`actions/`)

- `action_bank_hours.py`, `action_holiday_hours.py`, `action_check_balance_simple.py`, `action_process_transfer.py`

### Config (at Chapter 1.5 **start**)

- **`config.yml`**, **`credentials.yml`**, and **`endpoints.yml`** ship with the baseline.
- **`assistant_id`** in **`level5/`** is **`level5-agent`**, so it does not collide with **`level4-agent`** (after Chapter 1.4 Lab 0.1 in **`level4/`**).
- **`SearchReadyLLMCommandGenerator`** is in **`pipeline`** so **Lab 2.0** can set **`prompt_template`** where graders expect. Chapter 1.4 Lab 0.1 uses **`CompactLLMCommandGenerator`** in **`level4/config.yml`** instead; see the header comment in **`level5/config.yml`** if you merge trees.
- Before **Lab 2.0**, there is **no** **`prompt_template`** in **`config.yml`** and **no** copy under **`data/prompts/`**. The template to copy lives at **`resources/command_prompt_v3_slot_names.jinja2`**. **Lab 2.0** (first lab in Unit 2) copies it into **`data/prompts/`** and wires **`prompt_template`** in **`config.yml`**.
- **`endpoints.yml`** matches Chapter 1.4 (**`action_endpoint`**, **`nlg`**, **`model_groups`**) and has **no** **`tools:`** block until **Lab 3.1**.

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

## What Chapter 1.5 adds beyond Chapter 1.4

Chapter 1.4 already uses an **LLM command generator** (after Lab 0.1, **`CompactLLMCommandGenerator`** in **`level4/config.yml`**) to produce **CALM commands**: flows, **FillSlot**, and steps that run **actions** you listed in YAML.

Chapter 1.5 keeps that pattern in **`level5/`**, using **`SearchReadyLLMCommandGenerator`** and **`prompt_template`** from **Lab 2.0** (see **Unit 0.1** and **`level5/config.yml`**). It adds **tools**: Python functions the model may **invoke by name** at runtime (registered in **`endpoints.yml`**), especially inside steps such as **`action_process_transfer_with_tools`**.
