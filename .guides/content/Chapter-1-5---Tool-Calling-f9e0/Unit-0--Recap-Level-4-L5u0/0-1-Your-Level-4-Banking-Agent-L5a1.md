**Chapter 1.5 starting point:** This chapter assumes you **begin from the banking agent you finished at the end of Chapter 1.4** (Level 4): multiple slots, **`transfer_money`**, **`action_process_transfer`**, and the Chapter 1.4 pipeline (**`CompactLLMCommandGenerator`**, **`endpoints.yml`** aligned with **Unit 0.2**). You are not starting from scratch.

**Repository note:** In this course repo, **`level5/`** is maintained as that **Chapter 1.4 completion** baseline (same domain shape, flows, and **Level 3–4** actions as **`level4/`** after the Chapter 1.4 labs—including **`goodbye`**, **`holiday_hours`**, **`check_balance`**, **`transfer_money`**). You **add** tool calling in the labs below. **`level4/`** stays the Chapter 1.4 reference tree; **do all Chapter 1.5 work in `level5/`**.

Before we add tool calling, here is a quick recap of what you built in Level 4. All of that behavior stays in place; Level 5 **adds** tools on top.

## What you do in Chapter 1.5

Use the **same virtual environment** as Level 4 (project root); there is no new venv inside `level5`. In this chapter you will:

- Create the `tools/` folder and `banking_tools.py` (Lab 2.1)
- Register tools in `endpoints.yml` (Lab 3.1)
- Add the `action_process_transfer_with_tools` action and `transfer_money_tools` flow (Lab 4.1)
- Train and test (Labs 5.1 and 5.2)

---

## What you have from Chapter 1.4 (Level 4)

### Domain (`domain/basics.yml`)

- Responses: `utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`, `utter_ask_account`, `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- Slots: `account`, `amount`, `recipient`, `account_from`
- Actions: `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`, `action_process_transfer`

### Flows (`data/basics/`)

- greet, help, contact, goodbye, hours, holiday_hours, check_balance, transfer_money

### Actions (`actions/`)

- `action_bank_hours.py`, `action_holiday_hours.py`, `action_check_balance_simple.py`, `action_process_transfer.py`

### Config

- Config, credentials, endpoints (no **`tools:`** section until Lab 3.1). Config uses **`assistant_id: level5-agent`** (distinct from **`level4-agent`**).

---

## What Level 4 Couldn't Do

Your Level 4 agent used **actions** that are explicitly called in flows. It could not let the **LLM decide at runtime** which operations to perform (e.g. check balance vs. transfer) based on what the user said. Level 5 adds **tools**: functions the LLM can discover and call dynamically, so the agent can adapt to the conversation.
