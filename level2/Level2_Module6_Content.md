# Module 6: Training and Testing with Actions

### 6.1 Training with Actions

Training with actions is the same as Level 1, but Rasa now also processes your action files.

#### Training Command

**In Codio**:
```bash
cd level2
source .venv/bin/activate
python -m rasa train
```

**Running locally**:
```powershell
# Make sure environment variables are loaded
. .\load_env.ps1

# Train the bot
python -m rasa train
```

#### What Happens During Training

When you run `rasa train`, Rasa:

1. **Reads all flows** from `data/` folder
   - Finds `hours.yml` with `action_bank_hours`
   - Processes all Level 1 flows (unchanged)

2. **Reads the domain** from `domain/` folder
   - Loads all responses (from Level 1)
   - Loads all actions (new in Level 2)
   - Verifies registered actions exist

3. **Validates actions**:
   - Checks that `action_bank_hours` exists in `actions/` folder
   - Verifies the `name()` method returns the registered name
   - Ensures the action class is properly structured

4. **Creates model file**:
   - Saves everything to `models/` folder
   - Includes action registration information

---

### 6.2 Common Training Errors with Actions

#### Error: Action Not Found

**What you'll see**:
```
Error: Action 'action_bank_hours' not found
```

**What this means**: Rasa can't find your action file.

**How to fix**:
1. Check the action file exists: `actions/action_bank_hours.py`
2. Check the action is registered: `domain/basics.yml` has `- action_bank_hours`
3. Check the `name()` method returns the correct name
4. Verify the file is in the `actions/` folder (not `action/` or elsewhere)

---

#### Error: Import Error

**What you'll see**:
```
ImportError: cannot import name 'Action' from 'rasa_sdk'
```

**What this means**: Rasa SDK is not installed or wrong version.

**How to fix**:
1. Make sure Rasa Pro is installed: `python -m pip install rasa-pro`
2. Check your virtual environment is activated
3. Verify Rasa SDK is included with Rasa Pro

---

#### Error: Name Mismatch

**What you'll see**:
```
Error: Action name 'action_bank_hours' in domain doesn't match class name
```

**What this means**: The action name in domain doesn't match what `name()` returns.

**How to fix**:
1. Check `domain/basics.yml`: Should have `- action_bank_hours`
2. Check `action_bank_hours.py`: `name()` should return `"action_bank_hours"`
3. Ensure they match exactly (case-sensitive!)

---

### 6.3 Testing Your Action

#### Basic Testing Workflow

1. **Train your bot**: `python -m rasa train`

2. **Start Inspector**: 
   ```bash
   python -m rasa inspect --debug --log-file logs/logs.out
   ```
   
   **In Codio**: After starting Inspector, open it in your browser:
   - Open the **Ports** view: **Tools** → **Ports**, or **Preview** menu, or a **Ports** tab at the bottom
   - Find **port 5005** and click its URL (or "Open in browser")
   - Or use the direct URL: `https://your-project-5005.codio.io` (replace `your-project` with your Codio project subdomain)
   - Inspector opens in a new browser tab

3. **Test the action**:
   - Type "What are your hours?" or "When are you open?"
   - Should trigger `hours` flow
   - Should execute `action_bank_hours`
   - Should see a message that varies by day—e.g., "Today is Saturday—we're open 10am-2pm." or the full schedule on weekdays

4. **Verify Level 1 flows still work**:
   - Type "hello" → Should trigger `greet` flow (unchanged)
   - Type "help" → Should trigger `help` flow (unchanged)
   - Type "contact" → Should trigger `contact` flow (unchanged)

**Key Point**: All Level 1 functionality remains - Level 2 adds new capabilities without breaking existing ones.

---

### 6.4 Debugging Actions

#### Check Debug Output

When testing in Inspector, check the debug panel:
- Which flow was triggered?
- Which action was called?
- Did the action execute successfully?

#### Common Issues

1. **Action doesn't trigger**:
   - Check flow description matches user intent
   - Verify action is registered in domain
   - Check action file exists and is correct

2. **Action executes but no message**:
   - Check `dispatcher.utter_message()` is called
   - Verify the message text is correct
   - Check for Python errors in the action

3. **Python errors in action**:
   - Check Python syntax
   - Verify all imports are correct
   - Check for typos in method names

---
