# 🟠 Level 3: Slot Collection

**Goal:** Learn how to collect and use information from the user (slots = conversation memory).

## What You'll Learn

- How to define slots in the domain
- How to collect slots in flows using `collect:`
- How to read slots in actions
- How to handle placeholder values that the LLM might extract incorrectly

## Building on Level 2

⚠️ **Important**: This level builds on your Level 2 banking bot. You don't start from scratch!

**What stays the same:**
- All responses from Level 2 (`utter_greet`, `utter_help`, `utter_contact`)
- All flows from Level 2 (`greet`, `help`, `contact`, `hours`)
- All actions from Level 2 (`action_bank_hours`)

**What this level adds:**
- `slots:` section in `domain/basics.yml` (with `account` slot)
- New response `utter_ask_account`
- New action `action_check_balance_simple`
- New flow `data/basics/check_balance.yml`

**Your existing Level 2 banking bot continues to work** - this level adds memory (slots) so the bot can remember information!

## Quick Start

**Note**: If you're continuing from Level 2, you already have your virtual environment and Rasa Pro installed. You can skip steps 1-3 and go directly to step 4 (Train and run).

1. **Create and activate a virtual environment:**
   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   ```

2. **Install Rasa Pro:**
   ```powershell
   python -m pip install --no-cache-dir rasa-pro
   ```

3. **Create `.env` file:**
   ```text
   RASA_LICENSE=your-rasa-pro-license
   OPENAI_API_KEY=your-openai-api-key
   ```

4. **Train and run:**
   ```powershell
   . .\load_env.ps1
   python -m rasa train
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

   Or use the helper script:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
   ```

5. **Open Inspector:**
   - `http://localhost:5005/webhooks/socketio/inspect.html`

## What's New in This Level

**Additions to your Level 2 banking bot:**

### Slots (`domain/basics.yml`)
- **Added `slots:` section** - Defines what the bot remembers
- `account` slot stores the user's account number
- All Level 2 responses remain unchanged
- All Level 2 actions remain unchanged

### New Action (`actions/action_check_balance_simple.py`)
- Reads the `account` slot from the tracker
- Handles placeholder values (if LLM extracts "account number" instead of actual number)
- Re-prompts user if needed
- All Level 2 actions (`action_bank_hours`) remain unchanged

### New Flow (`data/basics/check_balance.yml`)
- Uses `collect: account` to ask for and store the account number
- Then calls `action_check_balance_simple` to use that information
- All Level 2 flows (greet, help, contact, hours) remain unchanged

### New Response (`utter_ask_account`)
- Used by the `collect:` step to ask for the account number
- All Level 2 responses remain unchanged

## Key Concepts

**Slots:**
- The bot's memory
- Store information the user provides
- Defined in `domain/basics.yml` under `slots:`

**Collect Step:**
- `collect: account` in a flow means "get this slot value before continuing"
- If the slot is empty, the bot will ask for it (using `utter_ask_*`)
- If the slot has a value, the flow continues

**Reading Slots in Actions:**
- Use `tracker.get_slot("slot_name")` to read slot values
- Always check for `None` or placeholder values

## Exercises

1. **Add a new slot:** Create a `name` slot and a flow that collects it.
2. **Modify the action:** Change `action_check_balance_simple.py` to return different balances based on the account number.
3. **Add validation:** Check if the account number is a valid format (e.g., 4 digits).

## Next Level

Once you're comfortable with single slots, move to **Level 4** to learn about multiple slots!
