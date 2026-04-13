### 0.2 What Level 2 Adds

Level 2 introduces **Actions** - custom Python code that your agent can execute. This enables:

- Dynamic responses based on calculations
- Data processing and logic
- Integration with external systems
- Custom business logic

**Your existing Level 1 agent continues to work** - Level 2 adds actions on top of it!

#### What's New in Level 2

**Already in the project before Lab 3.1** (starter):
- `actions/` folder, `actions/__init__.py`, and `actions/action_bank_hours.py` — example action you study in Units 2–3 (the domain does not list it until **Lab 4.1**).
- No `action_holiday_hours.py` yet, no `actions:` section in `domain/basics.yml`, and no `hours.yml` / `holiday_hours.yml` — you add those in the labs below.

**What you'll build**: In **Unit 3 / Lab 3.1** you'll create your own action (**action_holiday_hours**) that uses the current date—if today is a holiday it says we're closed today, otherwise it returns the general holiday schedule. In **Lab 4.1** you'll register both actions in the domain. In **Lab 5.1** you'll create **`hours.yml`** (for the example action) and **`holiday_hours.yml`** (for your action).

**Modified Files** (as you complete the labs):
- `domain/basics.yml` — You'll add an `actions:` section and list both the example action and your action (Lab 4.1)
- `data/basics/hours.yml` — Example flow for `action_bank_hours` (Lab 5.1)
- `data/basics/holiday_hours.yml` — Flow for `action_holiday_hours` (Lab 5.1)

**Unchanged Files**:
- All Level 1 responses remain
- All Level 1 flows remain
- All configuration files remain (with minor updates to endpoints.yml)

---
