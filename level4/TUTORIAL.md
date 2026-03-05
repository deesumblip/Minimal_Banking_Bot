# Level 4: Multiple Slots - Tutorial

**A guide to adding a transfer flow with multiple slot collection to your Level 3 banking bot.**

---

## Table of Contents

0. [Recap: What You Built in Level 3](#module-0-recap-what-you-built-in-level-3)
1. [Multiple Slots](#module-1-multiple-slots)
2. [Adding Slots and Responses](#module-2-adding-slots-and-responses)
3. [Reading Multiple Slots in Actions](#module-3-reading-multiple-slots-in-actions)
4. [Flows with Multiple Collect Steps](#module-4-flows-with-multiple-collect-steps)
5. [Training and Testing](#module-5-training-and-testing)
6. [Summary and Next Steps](#module-6-summary-and-next-steps)

---

## Module 0: Recap - What You Built in Level 3

### 0.1 Your Level 3 Banking Bot

Level 4 uses the **level4** folder, which is set up as a copy of your Level 3 bot. Everything from Level 3 remains:

- **Domain**: `account` slot, `utter_ask_account`, actions `action_bank_hours` and `action_check_balance_simple`
- **Flows**: greet, help, contact, goodbye, hours, check_balance (with collect account + action_check_balance_simple)
- **Actions**: action_bank_hours.py, action_check_balance_simple.py

### 0.2 What Level 4 Adds

Level 4 adds **multiple slot collection**: one flow that collects several pieces of information (amount, recipient, account_from) before running one action (action_process_transfer).

You will add:

- **Domain (Lab 2.1):** Slots `amount`, `recipient`, `account_from`; responses `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`; register `action_process_transfer`
- **Action (Lab 3.1):** Create `action_process_transfer.py` that reads the three slots and sends a confirmation
- **Flow (Lab 4.1):** Create `transfer_money.yml` with three `collect:` steps then `action: action_process_transfer`
- **Training and testing (Labs 5.1, 5.2):** Train from level4 and run the completion check

---

## Module 1: Multiple Slots

### 1.1 Multiple Slots

A flow can collect **multiple slots** in sequence. The bot remembers each value and uses them together (e.g. in one action). For a transfer you need amount, recipient, and source account.

### 1.2 Order of Collection

The **order of `collect:` steps** in the flow is the order in which the bot asks the user. Keep this order consistent with what your action expects (e.g. amount, then recipient, then account_from).

### 1.3 Slot Naming

Use the same naming as Level 3: slot names in the domain (e.g. `amount`, `recipient`, `account_from`), and `utter_ask_<slot_name>` for the response used when that slot is empty. The action reads slots with `tracker.get_slot("slot_name")` using the same names.

### 1.4 Test Your Knowledge

See **Level4_Unit1_Content_1.4_Test-Your-Knowledge.md** for a short quiz on Units 0–1.

---

## Module 2: Adding Slots and Responses

### 2.1 Adding Slots and Responses

In **Lab 2.1** you edit `level4/domain/basics.yml` to add:

- Under `slots:` — `amount`, `recipient`, `account_from` (each `type: text`)
- Under `responses:` — `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from` with appropriate ask text
- Under `actions:` — add `action_process_transfer` (the action file is created in Lab 3.1)

All Level 3 content (account slot, utter_ask_account, existing actions and responses) stays unchanged.

---

## Module 3: Reading Multiple Slots in Actions

### 3.1 Reading Multiple Slots

In **Lab 3.1** you create `level4/actions/action_process_transfer.py`. In `run()` you:

- Read `amount = tracker.get_slot("amount")`, and similarly for `recipient` and `account_from`
- Optionally check for placeholders and re-prompt with the appropriate `utter_ask_*`
- Send a confirmation message (e.g. "Transfer of $X from account Y to Z processed") and return `[]`

---

## Module 4: Flows with Multiple Collect Steps

### 4.1 Multiple Collect Steps

In **Lab 4.1** you create `level4/data/basics/transfer_money.yml` with a flow that has:

- Steps: `collect: amount`, then `collect: recipient`, then `collect: account_from`, then `action: action_process_transfer`

The bot will ask for each slot in that order when the slot is empty, then run the action.

---

## Module 5: Training and Testing

### 5.1 Training Level 4

From **project root**, activate the venv and run:

- `cd level4`
- `python -m rasa train`

A model is created in `level4/models/`. Use the same venv as Level 1–3 (no new venv in level4).

### 5.2 Testing Transfer

Run `python -m rasa inspect --debug` (from level4 with venv active). In Codio use the **Rasa Inspect** tab (not Tools → Ports). Trigger the transfer flow and provide amount, recipient, and account_from to confirm slot collection and the action.

**Lab 5.1** is graded (training); **Lab 5.2** is the completion check (domain + action + flow + model).

---

## Module 6: Summary and Next Steps

### 6.1 Complete Bot Walkthrough

Your Level 4 bot supports: Level 1 responses, Level 2 bank hours action, Level 3 check balance (collect account), and Level 4 transfer (collect amount, recipient, account_from then action_process_transfer).

### 6.2 What You've Learned

You added multiple slots and ask responses in the domain, an action that reads all three slots, and a flow with three collect steps and one action step. Order of collection and consistent naming (domain, flow, action) are key.

### 6.3 What's Next

See **Level4_Unit6_Content_6.3_Whats-Next.md** for possible next steps (forms, NLU, channels). See **6.6 What's Next: Level 5 Preview** for tool calling.

### 6.4 Knowledge Check

See **Level4_Unit6_Content_6.4_Knowledge-Check.md** for a short quiz on Level 4.

### 6.5 Limitations of Level 4

See **Level4_Unit6_Content_6.5_Limitations-of-Level-4.md** for what Level 4 cannot do and when to move to Level 5.

### 6.6 What's Next: Level 5 Preview

See **Level4_Unit6_Content_6.6_Whats-Next-Level-5-Preview.md** for an overview of tool calling (Level 5).

### 6.7 Course Completion Checklist

See **Level4_Unit6_Content_6.7_Course-Completion-Checklist.md** before moving to Level 5.

---

## Quick Reference

| Item | Location |
|------|----------|
| Virtual environment | Project root (same as Level 1–3). Activate from root, then `cd level4`. |
| Domain | level4/domain/basics.yml |
| Transfer flow | level4/data/basics/transfer_money.yml (you create in Lab 4.1) |
| Transfer action | level4/actions/action_process_transfer.py (you create in Lab 3.1) |
| Inspector on Codio | Use **Rasa Inspect** tab only (no port 5005 / Ports view) |

For step-by-step lab instructions and assessment setup, use the **Level4_Lab*_Content.md** and **Level4_Lab*_Assessment_Setup.md** files in level4/.
