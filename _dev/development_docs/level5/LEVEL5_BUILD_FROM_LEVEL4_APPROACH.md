# Level 5: Building from Level 4 — Setup Walkthrough

This document walks through how to set up **Level 5** so that the **starting agent is the final Level 4 bot**, and students add Level 5 content (tools folder, tools registration, `transfer_money_tools` flow and action) in guided labs.

---

## Goal

Students **start from Level 4 completion**—the same banking agent they finished at the end of **Level 4** (transfer flow, **`action_process_transfer`**, **Compact** pipeline, aligned **`endpoints.yml`**). Level 5 = that baseline **plus** tools module, **`tools:`** in **`endpoints.yml`**, **`transfer_money_tools`** flow, and **`action_process_transfer_with_tools`**; the student adds those in labs.

In this repository, **`level5/`** is maintained as that **Level 4 end state** as the default starting tree (students do **not** assemble it by copying **`level4/`** into **`level5/`** themselves). **`level4/`** remains the Level 4 reference workspace side by side.

---

## 1. Make the Level 5 starter = Level 4 completion

**level5/** in the repo should match the **final Level 4 agent**: all Level 1–4 responses, flows (including **`goodbye`**, **`holiday_hours`**, **`check_balance`**, **`transfer_money`**), and actions (**`action_bank_hours`**, **`action_holiday_hours`**, **`action_check_balance_simple`**, **`action_process_transfer`**). Do **not** pre-add Level 5–only lab deliverables in the **starter** if you want a clean “add in labs” story: no **`tools/`** folder, no **`tools:`** in **`endpoints.yml`**, no **`transfer_money_tools.yml`**, no **`action_process_transfer_with_tools`** until the student completes the corresponding labs.

*(If this repo ships reference implementations of those files for grading or demos, Unit 0 should still describe the **conceptual** baseline as Level 4 completion, then the labs.)*

### 1.1 level5/domain/basics.yml

- Include everything from **Level 4 completion**: transfer slots and **`utter_ask_*`**, **`utter_goodbye`**, actions **`action_bank_hours`**, **`action_holiday_hours`**, **`action_check_balance_simple`**, **`action_process_transfer`**.
- Add **`action_process_transfer_with_tools`** only after Lab 4.1 (or when shipping a reference tree).

### 1.2 level5/data/basics/

- Same flow files as Level 4 end: **`greet`**, **`help`**, **`contact`**, **`goodbye`**, **`hours`**, **`holiday_hours`**, **`check_balance`**, **`transfer_money`**.
- Add **`transfer_money_tools.yml`** in Lab 4.1.

### 1.3 level5/actions/

- Same as Level 4: **`action_bank_hours.py`**, **`action_holiday_hours.py`**, **`action_check_balance_simple.py`**, **`action_process_transfer.py`**, **`__init__.py`**.
- Add **`action_process_transfer_with_tools.py`** in Lab 4.1.

### 1.4 level5/endpoints.yml

- Match Level 4 (**`action_endpoint`**, **`nlg`**, **`model_groups`**). Add the **`tools:`** section in Lab 3.1.

### 1.5 level5/tools/

- Create in Lab 2.1 (**`tools/__init__.py`**, **`tools/banking_tools.py`**).

### 1.6 level5/config.yml

- Same **Compact** pipeline pattern as Level 4 completion; use **`assistant_id: level5-agent`** (or similar) so the assistant identity is distinct from **`level4-agent`**.

**Result:** **`level5/`** opens as the **final Level 4 bot**; Level 5 features are **added** in labs.

---

## 2. Unit 0 message

In Unit 0 (**0.1 Your Level 4 Banking Agent**, **0.2 What Level 5 Adds**), state clearly:

- **Level 5** begins from **Level 4 completion**; in this repo **`level5/`** is that baseline—**do all Level 5 work in `level5/`**; **`level4/`** is the Level 4 reference.
- Your job is to **add** tool calling: (1) **`tools/`** and **`banking_tools.py`**, (2) **`tools:`** registration in **`endpoints.yml`**, (3) **`transfer_money_tools`** flow and **`action_process_transfer_with_tools`**, (4) train and test.
