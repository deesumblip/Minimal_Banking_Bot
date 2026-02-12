# Unit 0: Recap - What You Built in Level 1

### 0.2 What Level 2 Adds

Level 2 introduces **Actions** - custom Python code that your bot can execute. This enables:

- ✅ Dynamic responses based on calculations
- ✅ Data processing and logic
- ✅ Integration with external systems
- ✅ Custom business logic

**Your existing Level 1 bot continues to work** - Level 2 adds actions on top of it!

#### What's New in Level 2

**Example (already in the project)**:
- `actions/` folder, `actions/__init__.py`, `actions/action_bank_hours.py` - Example action (bank hours by day)
- `data/basics/hours.yml` - Example flow that uses that action

**What you'll build**: In **Unit 3 / Lab 3.1** you'll create your own action (**action_holiday_hours**). In **Labs 4.1 and 5.1** you'll register it in the domain and add a flow for it.

**Modified Files** (as you complete the labs):
- `domain/basics.yml` - You'll add an `actions:` section (or add to it) and list both the example action and your action
- You'll add `data/basics/holiday_hours.yml` for your action (Lab 5.1)

**Unchanged Files**:
- All Level 1 responses remain
- All Level 1 flows remain
- All configuration files remain (with minor updates to endpoints.yml)

---
