# Level 5: Building from Level 4 - Setup Walkthrough

This document walks through how to set up **Level 5** so that the **starting agent files are the same as what the student has built at the end of Level 4**, and students add Level 5 content (tools folder, tools registration, transfer_money_tools flow and action) in guided labs.

---

## Goal

Students should **start from their Level 4 agent as the baseline** and build Level 5 themselves. Level 5 = Level 4 + tools module, endpoints tools section, one new action, and one new flow; the student does the adding.

---

## 1. Make the Level 5 starter = Level 4 end state

**level5/** in the repo should be a **true copy of the Level 4 end state**. Do **not** pre-add Level 5-only content (tools folder, tools in endpoints, transfer_money_tools flow, action_process_transfer_with_tools).

### 1.1 level5/domain/basics.yml

- Include everything from Level 4: slots (account, amount, recipient, account_from), all responses, actions: action_bank_hours, action_check_balance_simple, action_process_transfer.
- Do **not** add action_process_transfer_with_tools to the actions list; the student adds it in Lab 4.1.

### 1.2 level5/data/basics/

- Same flow files as Level 4: greet, help, contact, goodbye, hours, check_balance, transfer_money.
- Do **not** ship transfer_money_tools.yml; the student creates it in Lab 4.1.

### 1.3 level5/actions/

- Same as Level 4: action_bank_hours.py, action_check_balance_simple.py, action_process_transfer.py, __init__.py.
- Do **not** ship action_process_transfer_with_tools.py; the student creates it in Lab 4.1.

### 1.4 level5/endpoints.yml

- Match Level 4 (action_endpoint, nlg, model_groups). Do **not** add the `tools:` section; the student adds it in Lab 3.1.

### 1.5 level5/tools/

- Do **not** ship a tools folder; the student creates it in Lab 2.1 (tools/__init__.py and tools/banking_tools.py).

### 1.6 level5/config.yml

- Same structure as Level 4; change assistant_id to level5-agent (or similar) so the assistant identity is distinct.

**Result:** Opening **level5/** is "your Level 4 agent." All Level 5 content is added by the student in Labs 2.1, 3.1, 4.1, 5.1, and 5.2.

---

## 2. Unit 0 message

In Unit 0 (0.1 Your Level 4 Banking Agent, 0.2 What Level 5 Adds), state clearly:

- "Level 5 uses the **level5** folder, set up as a **copy of your Level 4 agent**. Your job is to **add** tools: (1) tools folder and banking_tools.py, (2) tools registration in endpoints.yml, (3) transfer_money_tools flow and action_process_transfer_with_tools action, (4) train and test."
- Optional: "If you built Level 4 elsewhere, copy your level4 folder to level5 so level5 matches your Level 4, then follow the labs."
