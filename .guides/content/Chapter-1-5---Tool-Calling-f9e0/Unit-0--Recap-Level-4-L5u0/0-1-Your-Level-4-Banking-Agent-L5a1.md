**Why tool calling:** In Level 4, **flows** and **actions** give you predictable steps: when the dialogue reaches an **`action:`** step, that code runs. That fits **ordered** tasks—for example collect **amount**, then **recipient**, then run **`action_process_transfer`**.

Users often **mix goals** in one turn (balance plus transfer, or a detour that does not match a single fixed branch). **Tool calling** lets the **LLM** choose *which* registered Python functions to run and *when*, from context, instead of spelling out every path in YAML. Keep **flows** and **actions** where you need structure; add **tools** where you need that flexibility.

**Level 5 starting point:** This chapter adds tool calling on top of your **Level 4 banking agent** (transfer slots, **`transfer_money`**, **`endpoints.yml`**, and the rest of what you already trained). You are not starting from scratch. Activate the venv at **project root**, then **`cd level5`** for every **`python -m rasa …`** command.

**Naming:** *Level 5* is the chapter skill name; **`level5/`** is the project folder. The **lab order** is under **What you add in Level 5** below; **Unit 0.2 What Level 5 Adds** is the full checklist from baseline to done.

---

What follows is a **quick recap of Level 4 completion**. That behavior stays; Level 5 **adds** tool calling on top. Use the **same virtual environment** as in Level 4 (project root)—there is no separate venv inside **`level5/`**.

## Where Level 5 happens

Do all Level 5 work under **`level5/`**. The **lab sequence** and **deliverables table** are on **Unit 0.2 What Level 5 Adds**.

---

## What you have at Level 4 completion

### Domain (`domain/basics.yml`)

- Responses: `utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`, `utter_ask_account`, `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- Slots: `account`, `amount`, `recipient`, `account_from`
- Actions (**custom**): `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`, `action_process_transfer`
- Actions (**responses used as flow steps**): every **`utter_*`** name listed under **Responses** must also appear under **`actions:`** so Rasa can run those steps in flows.

### Flows (`data/basics/`)

- `greet`, `help`, `contact`, `goodbye`, `hours`, `holiday_hours`, `check_balance`, `transfer_money`

### Actions (`actions/`)

- `action_bank_hours.py`, `action_holiday_hours.py`, `action_check_balance_simple.py`, `action_process_transfer.py`

### Config (at Level 5 **start**)

The **`level5/`** baseline is ready to work like Level 4, with Level 5–specific choices called out here—read this before **Lab 2.0** and **Lab 3.1**.

**Files present:** **`config.yml`**, **`credentials.yml`**, **`endpoints.yml`**.

**Identity:** **`assistant_id`** is **`level5-agent`**, distinct from **`level4-agent`** (after Level 4 Lab 0.1 in **`level4/`**).

**Command generator:** The pipeline uses **`SearchReadyLLMCommandGenerator`** so **Lab 2.0** can attach **`prompt_template`**. Level 4 Lab 0.1 uses **`CompactLLMCommandGenerator`** in **`level4/config.yml`** instead—see the header comment in **`level5/config.yml`** if you compare trees.

**Before Lab 2.0:** There is **no** **`prompt_template`** in **`config.yml`** and **no** copy under **`data/prompts/`**. The template to copy is **`resources/command_prompt_v3_slot_names.jinja2`**. **Lab 2.0** copies it into **`data/prompts/`** and sets **`prompt_template`**.

**Before Lab 3.1:** **`endpoints.yml`** matches Level 4 (**`action_endpoint`**, **`nlg`**, **`model_groups`**) and has **no** **`tools:`** block yet.

**Heads-up:** At **Lab 3.1**, you **append** a **`tools:`** block without removing or renaming **`action_endpoint`**, **`nlg`**, or **`model_groups`**.

---

## What you add in Level 5

In order, you will:

- Copy the command prompt from **`resources/`** into **`data/prompts/`** and set **`prompt_template`** in **`config.yml`** (**Lab 2.0**)
- Create the **`tools/`** folder and **`banking_tools.py`** (**Lab 2.1**)
- Register tools in **`endpoints.yml`** (**Lab 3.1**)
- Add **`action_process_transfer_with_tools`**, **`transfer_money_tools.yml`**, and the **`from_llm`** domain conditions for **`transfer_money_tools`** (**Lab 4.1**)
- Train and test (**Labs 5.1** and **5.2**)

---

## How Level 5 extends Level 4

Level 4 already uses an **LLM command generator** (after Lab 0.1, **`CompactLLMCommandGenerator`** in **`level4/config.yml`**) to drive **CALM** commands. **`level5/`** uses **`SearchReadyLLMCommandGenerator`** and **`prompt_template`** from **Lab 2.0** instead—see **Config** above.

**New in Level 5:** Register Python **tools** in **`endpoints.yml`**, implement them under **`tools/`**, and add the **`transfer_money_tools`** flow with **`action_process_transfer_with_tools`** so the model can invoke tools at runtime inside that action. For motivation, see **Why tool calling** at the top of this page.
