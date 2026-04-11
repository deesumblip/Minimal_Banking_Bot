# 🟡 Level 2: Simple Actions

**Goal:** Learn how to write custom Python code (actions) that the agent can execute.

## What You'll Learn

- How to create custom actions in Python
- How to register actions in the domain
- How to call actions from flows
- The difference between `utter_*` (responses) and `action_*` (custom code)

## Building on Level 1

⚠️ **Important**: This level builds on your Level 1 banking agent. You don't start from scratch!

**Repo note (starter vs completion):** The **`level2/`** folder is the **Level 2 entry** state: end of Level 1 (responses + Level 1 flows), plus the **example** `actions/action_bank_hours.py` for Units 2–3. It does **not** include `action_holiday_hours.py`, an `actions:` block in the domain, or `hours.yml` / `holiday_hours.yml`—students add those in Labs 3.1, 4.1, and 5.1. The **`level3/`** folder in this repo remains a **completed** Level 2 baseline (both actions + flows) for Level 3. See **`LEVEL2_STARTER_STATE.md`** for a full file checklist and the **post–Level 2** end state.

**What stays the same:**
- All responses from Level 1 (`utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`)
- All flows from Level 1 (`greet`, `help`, `contact`, `goodbye`)
- All configuration files (`config.yml`, `credentials.yml`, `endpoints.yml`)

**What this level adds (conceptually; labs walk you through creating and wiring pieces):**
- An **example** action file (`action_bank_hours.py`) to study before you write your own.
- **Lab 3.1** — create **`action_holiday_hours.py`**. **Lab 4.1** — add an **`actions:`** section and register **`action_bank_hours`** and **`action_holiday_hours`**. **Lab 5.1** — create **`hours.yml`** and **`holiday_hours.yml`**.

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
- `action_bank_hours.py` - **Example** action (bank hours by day); you register it in **Lab 4.1**
- `action_holiday_hours.py` - You **create** this file in **Lab 3.1** (not present in the starter)

### Domain (`domain/basics.yml`)
- **`responses:`** — Same as Level 1 end state (including `utter_goodbye`)
- **`actions:`** — You add this section in **Lab 4.1** and list both custom actions

### Flows that use actions
- **`hours.yml`** and **`holiday_hours.yml`** — You create both in **Lab 5.1**
- All Level 1 flows (`greet`, `help`, `contact`, `goodbye`) remain as in Level 1

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
