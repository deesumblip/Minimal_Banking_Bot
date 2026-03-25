# Level 4: Multiple Slots

**Goal:** Learn how to collect multiple pieces of information from the user before performing an action.

**Starting point:** Chapter 1.4 **assumes** you begin from the **final banking agent at the end of Chapter 1.3** (your finished agent in **`level3/`**). Labs add transfer slots, **`action_process_transfer`**, and **`transfer_money.yml`**, then training and testing. See **Unit 0** (`Level4_Unit0_Content_0.1` and `0.2`). After **Lab 5.1**, **`level4/models/`** holds your trained model for **Lab 5.2**.

**Repository vs pedagogy:** The **narrative** is always “Chapter 1.3 end state → apply Chapter 1.4 labs in **`level4/`**.” **In this repo**, the **`level4/`** folder is the **completed** Chapter 1.4 agent, checked in so **Codio** and **graders** can be tested end-to-end. It is **not** a minimal starter; **Unit 0** and the labs define the **delta** from **`level3/`**.

## What You'll Learn

- How to define multiple slots in the domain
- How to collect multiple slots in a single flow
- How to read and validate multiple slot values in actions
- How to handle multi-step conversations (amount, recipient, account_from)

## Building on Level 3

**Important:** This level builds on your Level 3 banking agent. You don't start from scratch. You use the **same virtual environment** created in Level 1 (in the **project root**). There is no new `.venv` inside `level4/`.

**Pipeline:** Chapter 1.3 (`level3`) still uses **`SearchReadyLLMCommandGenerator`**. Chapter 1.4 (`level4`) uses **`CompactLLMCommandGenerator`** for reliable multi-slot / free-text collection (same **`FlowPolicy`**). **`endpoints.yml`** keeps the **`gpt-4o-mini`** group **id** but maps it to **`gpt-4o-2024-11-20`** at **`temperature: 0.1`** so **FillSlot** on names behaves—see **`level4/endpoints.yml`** and **Unit 0.2**. **Level 3 is not modified.** Details: **`PIPELINE_CHAPTER_1_3_AND_4.md`**.

**Full delta (Ch 1.3 end → Ch 1.4 end):** **`Level4_Unit0_Content_0.2_What-Level-4-Adds.md`** (pipeline, labs, summary in one place). **File checklist:** **`LEVEL3_TO_LEVEL4_FILE_DELTA.md`**.

In the labs you **add** the following in **`level4/`** (on top of the **final banking agent at the end of Chapter 1.3**—your **`level3/`** project).

**What stays the same:** All Level 3 responses, flows, actions, and the `account` slot remain.

**What you add:** In Lab 2.1 you add slots `amount`, `recipient`, `account_from` and utter_ask_* responses and register `action_process_transfer`. In Lab 3.1 you create the action file. In Lab 4.1 you create the transfer_money flow. Your existing Level 3 banking agent continues to work; Level 4 adds multiple slot collection for the transfer flow.

---

## Quick Start

**Setup:** Use the virtual environment in the **project root** (the folder that contains `level1`, `level2`, `level3`, `level4`, and `.guides`). Activate it from there, then go into `level4`.

### In Codio

1. Open a terminal (it opens at `~/workspace`, i.e. project root).
2. Activate the virtual environment: `source .venv/bin/activate`. Your prompt should show `(.venv)`.
3. Go to Level 4: `cd level4`.
4. Train: `python -m rasa train`. Wait for "Successfully saved model".
5. Start Inspector: `python -m rasa inspect --debug --log-file logs/logs.out`. Leave the terminal open.
6. Open the chat: In the top menu bar, click the **Rasa Inspect** tab. (Do not use Tools → Ports or port 5005.)
7. **Test the transfer flow** using the **scripted turns** in **Lab 5.2** (amount → recipient → account → `(Demo) Transfer of $…`).

### Running locally

- **Windows (PowerShell):** From project root, run `.venv\Scripts\Activate.ps1`, then `cd level4` **once** (if your prompt already shows `...\level4>`, skip `cd level4`—a second `cd level4` fails). Train, then inspect: `python -m rasa train` then `python -m rasa inspect --debug --log-file logs/logs.out`. The repo includes a `logs/` folder so that path works; or run `.\run_inspector.ps1` (creates `logs/` if missing, then trains and starts Inspector). Open **http://localhost:5005** (or …/inspect.html) in your browser.
- **Windows (Command Prompt):** From project root, run `.venv\Scripts\activate.bat`, then `cd level4`. Same train and inspect commands; open http://localhost:5005 in the browser.
- **macOS / Linux:** From project root, run `source .venv/bin/activate`, then `cd level4`. Same train and inspect commands; open http://localhost:5005 in the browser.

Use your actual project path. Ensure `.env` exists in the project root (or level4) with `RASA_LICENSE` and `OPENAI_API_KEY` (see Lab 0.1 / Level 1 if needed).

---

## What's New in This Level

**Additions to your Level 3 banking agent:**

- **Domain (Lab 2.1):** Slots `amount`, `recipient`, `account_from`; responses `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`; **append** `action_process_transfer` to `actions:` **without removing** Level 3 action names (`action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`).
- **Action (Lab 3.1):** `actions/action_process_transfer.py` — reads the three slots and sends a transfer confirmation (and optionally validates placeholders).
- **Flow (Lab 4.1):** `data/basics/transfer_money.yml` — collect amount, recipient, account_from, then run action_process_transfer.

All Chapter 1.3 content (including **`check_balance`**, **`holiday_hours`**, and the existing actions) remains in place; you add the transfer pieces alongside it.

## Key Concepts

- **Multiple slot collection:** A flow can have several `collect:` steps; the agent asks for each value in order.
- **Consistent naming:** Slot names and `utter_ask_<slot_name>` in the domain must match the flow and the action's `get_slot(...)` calls.
- **Validation:** In the action you can check for placeholders or missing values and re-prompt using the appropriate utter_ask_*.

## Next Level

Once you're comfortable with multiple slots, move to **Level 5** to learn about tool calling. See **Level4_Unit6_Content_6.6_Whats-Next-Level-5-Preview.md** for a preview.
