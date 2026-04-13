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
