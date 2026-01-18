# 🔴 Level 4: Multiple Slots

**Goal:** Learn how to collect multiple pieces of information from the user before performing an action.

## What You'll Learn

- How to define multiple slots in the domain
- How to collect multiple slots in a single flow
- How to validate multiple slot values in actions
- How to handle complex multi-step conversations

## Building on Level 3

⚠️ **Important**: This level builds on your Level 3 banking bot. You don't start from scratch!

**What stays the same:**
- All responses from Level 3 (including `utter_ask_account`)
- All flows from Level 3 (`greet`, `help`, `contact`, `hours`, `check_balance`)
- All actions from Level 3 (`action_bank_hours`, `action_check_balance_simple`)
- All slots from Level 3 (`account`)

**What this level adds:**
- Additional slots: `amount`, `recipient`, `account_from`
- Additional ask responses: `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- New action `action_process_transfer`
- New flow `data/basics/transfer_money.yml`

**Your existing Level 3 banking bot continues to work** - this level adds the ability to collect multiple pieces of information before performing an action!

## Quick Start

**Note**: If you're continuing from Level 3, you already have your virtual environment and Rasa Pro installed. You can skip steps 1-3 and go directly to step 4 (Train and run).

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

**Additions to your Level 3 banking bot:**

### Multiple Slots (`domain/basics.yml`)
- **Added more slots:** `amount`, `recipient`, `account_from`
- Each slot stores a different piece of information
- All Level 3 slots (`account`) remain unchanged
- All Level 3 responses remain unchanged

### New Action (`actions/action_process_transfer.py`)
- Reads multiple slots: `amount`, `recipient`, `account_from`
- Validates that all slots have real values (not placeholders)
- Uses all collected information to process a transfer
- All Level 3 actions (`action_bank_hours`, `action_check_balance_simple`) remain unchanged

### New Flow (`data/basics/transfer_money.yml`)
- **Multiple `collect:` steps** - Collects amount, then recipient, then account_from
- The bot will ask for each piece of information in order
- Only proceeds to the action when all slots are filled
- All Level 3 flows (greet, help, contact, hours, check_balance) remain unchanged

### New Responses
- `utter_ask_amount` - Asks for transfer amount
- `utter_ask_recipient` - Asks for recipient
- `utter_ask_account_from` - Asks for source account
- All Level 3 responses (including `utter_ask_account`) remain unchanged

## Key Concepts

**Multiple Slot Collection:**
- Flows can have multiple `collect:` steps
- The bot collects them in order
- Each `collect:` step will ask for that slot if it's empty

**Validation in Actions:**
- Always check that all required slots have values
- Check for placeholder values that the LLM might extract
- Provide helpful error messages if information is missing

**Complex Conversations:**
- Users might provide multiple pieces of information at once
- Users might provide information out of order
- The bot handles both cases gracefully

## Exercises

1. **Add a confirmation step:** After collecting all slots, ask the user to confirm before processing.
2. **Add validation:** Check that the amount is a valid number and not negative.
3. **Add a new slot:** Create a `transfer_date` slot and collect it in the transfer flow.

## Next Level

Once you're comfortable with multiple slots, move to **Level 5** to learn about tool calling!
