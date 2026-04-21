**Starting point:** Level 5 adds **tool calling** on top of your **Level 4 banking agent**—multiple slots, **`transfer_money`**, **`action_process_transfer`**, and **`endpoints.yml`** (**`action_endpoint`**, **`nlg`**, **`model_groups`**). You are not starting from scratch. Do **not** edit **`level4/`** for this chapter; activate the venv at **project root**, then **`cd level5`** for every change and every **`python -m rasa …`**.

**Repository layout:** **“Level 4”** in Unit 0 (including **0.1 Your Level 4 Banking Agent**) means your **Level 4** work, not the **`level4/`** folder in git—that snapshot is **Level 3**. **`level5/`** is the **Level 4–complete** baseline here. If **`level5/`** differs from files you saved in **`level4/`**, see the comment headers in **`level5/config.yml`**, **`level5/domain/basics.yml`**, and **`level5/data/basics/check_balance.yml`**. You still complete Level 5 in the labs (**`tools/`**, **`tools:`** in **`endpoints.yml`**, **`transfer_money_tools`**, **`action_process_transfer_with_tools`**).

---

Before we add tool calling, here is a quick recap of what you have at **Level 4 completion**. All of that behavior stays in place; Level 5 **adds** tools on top.

**Naming:** *Level 5* means the outcome of Level 5. The **`level5/`** folder is where Level 5 changes go; it continues from the same agent you completed in **`level4/`**.

## Where Level 5 happens

You add the **`tools/`** module, **`endpoints.yml`** registration, the **`transfer_money_tools`** flow, and **`action_process_transfer_with_tools`** under **`level5/`**. The **next page** summarizes the lab sequence and what you will add in each step.

Use the **same virtual environment** as in Level 4 (project root); there is no new venv inside **`level5/`**.

---

## What you have at Level 4 completion

### Domain (`domain/basics.yml`)

- Responses: `utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`, `utter_ask_account`, `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- Slots: `account`, `amount`, `recipient`, `account_from`
- Actions: `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`, `action_process_transfer`

### Flows (`data/basics/`)

- greet, help, contact, goodbye, hours, holiday_hours, check_balance, transfer_money

### Actions (`actions/`)

- `action_bank_hours.py`, `action_holiday_hours.py`, `action_check_balance_simple.py`, `action_process_transfer.py`

### Config

- **`config.yml`**, **`credentials.yml`**, **`endpoints.yml`** (no **`tools:`** section until **Lab 3.1**). **`assistant_id`** is **`level5-agent`** ( **`level4-agent`** after Level 4 Lab 0.1 in **`level4/`** ). **`level5/config.yml`** uses **`SearchReadyLLMCommandGenerator`** so **Lab 2.0** can attach **`prompt_template`** where graders expect; **Level 4** has you finish **`level4/`** with **`CompactLLMCommandGenerator`**—see the top of **`level5/config.yml`**.

**Heads-up:** Until you register tools, your **`endpoints.yml`** matches the Level 4 pattern ( **`action_endpoint`**, **`nlg`**, **`model_groups`** ). When you reach the lab that registers tools, you will add a **`tools:`** block without removing or renaming those sections.

---

## What you add in Level 5

In order, you will:

- Copy the command prompt into **`data/prompts/`** and set **`prompt_template`** in **`config.yml`** (**Lab 2.0**)
- Create the **`tools/`** folder and **`banking_tools.py`** (**Lab 2.1**)
- Register tools in **`endpoints.yml`** (**Lab 3.1**)
- Add **`action_process_transfer_with_tools`** and **`transfer_money_tools.yml`** (**Lab 4.1**)
- Train and test (**Labs 5.1** and **5.2**)

---

## What Level 5 adds beyond Level 4

Level 4 already uses an **LLM command generator** (after Lab 0.1, **`CompactLLMCommandGenerator`** in **`level4/config.yml`**) for **CALM commands**—flows, **FillSlot**, and **actions** named in YAML. Level 5 uses **`SearchReadyLLMCommandGenerator`** and **`prompt_template`** in **`level5/`** (**Lab 2.0**) and adds **tools**: Python functions the model may **invoke by name** (registered in **`endpoints.yml`**), especially in steps such as **`action_process_transfer_with_tools`**. See the top of **`level5/config.yml`** for how this differs from your finished **`level4/`** pipeline.
