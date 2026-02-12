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
   - Finds `hours.yml` with `action_bank_hours` and `holiday_hours.yml` with `action_holiday_hours`
   - Processes all Level 1 flows (unchanged)

2. **Reads the domain** from `domain/` folder
   - Loads all responses (from Level 1)
   - Loads all actions (new in Level 2: action_bank_hours, action_holiday_hours)
   - Verifies registered actions exist

3. **Validates actions**:
   - Checks that each registered action (e.g. `action_bank_hours`, `action_holiday_hours`) exists in the `actions/` folder
   - Verifies the `name()` method returns the registered name
   - Ensures the action class is properly structured

4. **Creates model file**:
   - Saves everything to `models/` folder
   - Includes action registration information

After training, you can test the bot in the **Rasa Inspector GUI** using the questions in section 6.3.

---
