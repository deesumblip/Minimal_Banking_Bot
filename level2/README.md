# 🟡 Level 2: Simple Actions

**Goal:** Learn how to write custom Python code (actions) that the bot can execute.

## What You'll Learn

- How to create custom actions in Python
- How to register actions in the domain
- How to call actions from flows
- The difference between `utter_*` (responses) and `action_*` (custom code)

## Building on Level 1

⚠️ **Important**: This level builds on your Level 1 banking bot. You don't start from scratch!

**What stays the same:**
- All responses from Level 1 (`utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`)
- All flows from Level 1 (`greet`, `help`, `contact`, `goodbye`)
- All configuration files (`config.yml`, `credentials.yml`, `endpoints.yml`)

**What this level adds:**
- `actions/` folder with `action_bank_hours.py`
- `actions:` section in `domain/basics.yml`
- New flow `data/basics/hours.yml` that uses the action

**Your existing Level 1 banking bot continues to work** - this level adds custom Python code (actions) on top of it!

## Quick Start

**Note**: If you're continuing from Level 1, you already have your virtual environment and Rasa Pro installed. You can skip steps 1-3 and go directly to step 4 (Train and run).

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

**Additions to your Level 1 banking bot:**

### Actions Folder (`actions/`)
- `__init__.py` - Makes the folder a Python package
- `action_bank_hours.py` - A simple custom action that returns bank hours

### Domain (`domain/basics.yml`)
- **Added `actions:` section** - Lists all custom actions
- All Level 1 responses remain unchanged
- Actions must be registered here to be used

### New Flow (`data/basics/hours.yml`)
- Uses `action_bank_hours` instead of `utter_*`
- Demonstrates calling custom Python code
- All Level 1 flows (greet, help, contact, goodbye) remain unchanged

## Key Concepts

**Responses (`utter_*`):**
- Predefined messages in the domain
- No custom logic
- Just text that gets sent to the user

**Actions (`action_*`):**
- Custom Python code
- Can do anything: calculations, API calls, database queries
- Must be registered in `domain/basics.yml` under `actions:`

## Exercises

1. **Modify the action:** Edit `actions/action_bank_hours.py` to return different hours.
2. **Add a new action:** Create `action_holiday_hours.py` that returns holiday hours.
3. **Use the new action:** Add it to the domain and create a flow that uses it.

## Next Level

Once you're comfortable with actions, move to **Level 3** to learn about slots (memory)!
