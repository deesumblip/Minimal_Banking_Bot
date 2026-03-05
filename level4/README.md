# Level 4: Multiple Slots

**Goal:** Learn how to collect multiple pieces of information from the user before performing an action.

## What You'll Learn

- How to define multiple slots in the domain
- How to collect multiple slots in a single flow
- How to read and validate multiple slot values in actions
- How to handle multi-step conversations (amount, recipient, account_from)

## Building on Level 3

**Important:** This level builds on your Level 3 banking bot. You don't start from scratch. You use the **same virtual environment** created in Level 1 (in the **project root**). There is no new `.venv` inside `level4/`.

The **level4** folder is set up as a copy of your Level 3 bot. You add the following in the labs.

**What stays the same:** All Level 3 responses, flows, actions, and the `account` slot remain.

**What you add:** In Lab 2.1 you add slots `amount`, `recipient`, `account_from` and utter_ask_* responses and register `action_process_transfer`. In Lab 3.1 you create the action file. In Lab 4.1 you create the transfer_money flow. Your existing Level 3 banking bot continues to work; Level 4 adds multiple slot collection for the transfer flow.

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

### Running locally

- **Windows (PowerShell):** From project root, run `.venv\Scripts\Activate.ps1`, then `cd level4`. Then `python -m rasa train` and `python -m rasa inspect --debug`. Open **http://localhost:5005** (or …/inspect.html) in your browser.
- **Windows (Command Prompt):** From project root, run `.venv\Scripts\activate.bat`, then `cd level4`. Same train and inspect commands; open http://localhost:5005 in the browser.
- **macOS / Linux:** From project root, run `source .venv/bin/activate`, then `cd level4`. Same train and inspect commands; open http://localhost:5005 in the browser.

Use your actual project path. Ensure `.env` exists in the project root (or level4) with `RASA_LICENSE` and `OPENAI_API_KEY` (see Lab 0.1 / Level 1 if needed).

---

## What's New in This Level

**Additions to your Level 3 banking bot:**

- **Domain (Lab 2.1):** Slots `amount`, `recipient`, `account_from`; responses `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`; `action_process_transfer` in the actions list.
- **Action (Lab 3.1):** `actions/action_process_transfer.py` — reads the three slots and sends a transfer confirmation (and optionally validates placeholders).
- **Flow (Lab 4.1):** `data/basics/transfer_money.yml` — collect amount, recipient, account_from, then run action_process_transfer.

All Level 3 content (including check_balance flow and action_check_balance_simple) remains unchanged.

## Key Concepts

- **Multiple slot collection:** A flow can have several `collect:` steps; the bot asks for each value in order.
- **Consistent naming:** Slot names and `utter_ask_<slot_name>` in the domain must match the flow and the action's `get_slot(...)` calls.
- **Validation:** In the action you can check for placeholders or missing values and re-prompt using the appropriate utter_ask_*.

## Next Level

Once you're comfortable with multiple slots, move to **Level 5** to learn about tool calling. See **Level4_Unit6_Content_6.6_Whats-Next-Level-5-Preview.md** for a preview.
