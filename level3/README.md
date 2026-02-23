# Level 3: Slot Collection

**Goal:** Learn how to collect and use information from the user (slots = conversation memory).

## What You'll Learn

- How to define slots in the domain
- How to collect slots in flows using `collect:`
- How to read slots in actions
- How to handle placeholder values that the LLM might extract incorrectly

## Building on Level 2

**Important:** This level builds on your Level 2 banking bot. You don't start from scratch. You use the **same virtual environment** created in Level 1 (in the **project root**). There is no new `.venv` inside `level3/`.

The **level3** folder is set up as a copy of your Level 2 bot. You add the following in the labs.

**What stays the same:** All Level 2 responses, flows, and actions remain.

**What you add:** In Lab 3.1 you add the `slots:` section (with `account` slot), the `utter_ask_account` response, and you register the new action `action_check_balance_simple` in the domain (the action file is provided). In Lab 4.1 you explore how that action uses the slot. In Lab 5.1 you create the flow `data/basics/check_balance.yml`. Your existing Level 2 banking bot continues to work; Level 3 adds memory (slots) so the bot can remember information.

---

## Quick Start

**Setup:** Use the virtual environment in the **project root** (the folder that contains `level1`, `level2`, `level3`, and `.guides`). Activate it from there, then go into `level3`.

### In Codio

1. Open a terminal (it opens at `~/workspace`, i.e. project root).
2. Activate the virtual environment: `source .venv/bin/activate`. Your prompt should show `(.venv)`.
3. Go to Level 3: `cd level3`.
4. Train: `python -m rasa train`. Wait for "Successfully saved model".
5. Start Inspector: `python -m rasa inspect --debug --log-file logs/logs.out`. Leave the terminal open.
6. Open the chat: In the top menu bar, click the **Rasa Inspect** tab. (Do not use Tools → Ports or port 5005.)

### Running locally

- **Windows (PowerShell):** From project root, run `.venv\Scripts\Activate.ps1`, then `cd level3`. Then `python -m rasa train` and `python -m rasa inspect --debug`. Open **http://localhost:5005** (or …/inspect.html) in your browser.
- **Windows (Command Prompt):** From project root, run `.venv\Scripts\activate.bat`, then `cd level3`. Same train and inspect commands; open http://localhost:5005 in the browser.
- **macOS / Linux:** From project root, run `source .venv/bin/activate`, then `cd level3`. Same train and inspect commands; open http://localhost:5005 in the browser.

Use your actual project path (e.g. `C:\Users\You\Minimal_Banking_Bot` or `~/Minimal_Banking_Bot`). Ensure `.env` exists in the `level3` folder with `RASA_LICENSE` and `OPENAI_API_KEY` (see Lab 0.1 / Unit 0 if needed).

---

## What's New in This Level

**Additions to your Level 2 banking bot:**

### Slots (`domain/basics.yml`)
- **Added `slots:` section** – Defines what the bot remembers
- `account` slot stores the user's account number
- All Level 2 responses and actions remain unchanged

### New Action (`actions/action_check_balance_simple.py`)
- Reads the `account` slot from the tracker
- Handles placeholder values (if the LLM extracts "account number" instead of a real number)
- Re-prompts the user if needed

### New Flow (`data/basics/check_balance.yml`)
- Uses `collect: account` to ask for and store the account number
- Then calls `action_check_balance_simple` to use that information

### New Response (`utter_ask_account`)
- Used by the `collect:` step to ask for the account number

## Key Concepts

**Slots:** The bot's memory. They store information the user provides and are defined in `domain/basics.yml` under `slots:`.

**Collect step:** `collect: account` in a flow means "get this slot value before continuing." If the slot is empty, the bot asks (using `utter_ask_*`); if it has a value, the flow continues.

**Reading slots in actions:** Use `tracker.get_slot("slot_name")` to read slot values. Always check for `None` or placeholder values.

## Exercises

1. **Add a new slot:** Create a `name` slot and a flow that collects it.
2. **Modify the action:** Change `action_check_balance_simple.py` to return different balances based on the account number.
3. **Add validation:** Check if the account number is a valid format (e.g. 4 digits).

## Next Level

Once you're comfortable with single slots, move to **Level 4** to learn about multiple slots.
