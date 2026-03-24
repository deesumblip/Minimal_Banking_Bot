# 🟡 Level 2: Simple Actions

**Goal:** Learn how to write custom Python code (actions) that the agent can execute.

## What You'll Learn

- How to create custom actions in Python
- How to register actions in the domain
- How to call actions from flows
- The difference between `utter_*` (responses) and `action_*` (custom code)

## Building on Level 1

⚠️ **Important**: This level builds on your Level 1 banking agent. You don't start from scratch!

**Repo note (Chapter 1.2 end state):** The **`level2/`** folder in this repository is the **completed** Chapter 1.2 agent: same responses, flows, and both custom actions as the **`level3/`** starter used in Chapter 1.3 (aside from `assistant_id` in `config.yml` and the header comments in `domain/basics.yml`). If you follow the labs from a minimal tree, you will **build** the holiday action and flows in order; if you clone the repo to study, you already have the full Level 2 agent here.

**What stays the same:**
- All responses from Level 1 (`utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`)
- All flows from Level 1 (`greet`, `help`, `contact`, `goodbye`)
- All configuration files (`config.yml`, `credentials.yml`, `endpoints.yml`)

**What this level adds (conceptually; labs walk you through creating and wiring pieces):**
- An **example** action and flow (`action_bank_hours`, `hours.yml`) so you can see how actions work.
- **Lab 3.1** — create **`action_holiday_hours`**. **Labs 4.1 and 5.1** — register it in the domain and add **`holiday_hours.yml`**.

**Your existing Level 1 banking agent continues to work** — this level adds custom Python code (actions) on top of it, and you build and wire in your own action.

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

**Additions to your Level 1 banking agent:**

### Actions Folder (`actions/`)
- `__init__.py` - Makes the folder a Python package
- `action_bank_hours.py` - **Example** action (bank hours by day)
- `action_holiday_hours.py` - Holiday schedule (you create this in **Lab 3.1** when working through the course from scratch; it is already present in this repo’s `level2/` as the Chapter 1.2 completion)

### Domain (`domain/basics.yml`)
- **`actions:` section** — Registers `action_bank_hours` and `action_holiday_hours` (Lab 4.1 covers registering actions when you add them yourself)
- All Level 1 responses remain unchanged

### Flows that use actions
- **hours.yml** - Example flow using `action_bank_hours`
- **holiday_hours.yml** - Flow for `action_holiday_hours` (you create this in **Lab 5.1** when building step by step; present in this repo for parity with **`level3/`**)
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

1. **Modify your action:** Edit `actions/action_holiday_hours.py` to return different holiday messages or add simple logic (e.g. different message by month).
2. **Add another action:** Create a new action (e.g. `action_faq`) and register it in the domain.
3. **Add a flow for it:** Create a new flow file that uses your new action.

## Next Level

Once you're comfortable with actions, move to **Level 3** to learn about slots (memory)!
