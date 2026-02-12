# Module 0: Recap - What You Built in Level 1

### 0.2 What Level 2 Adds

Level 2 introduces **Actions** - custom Python code that your bot can execute. This enables:

- ✅ Dynamic responses based on calculations
- ✅ Data processing and logic
- ✅ Integration with external systems
- ✅ Custom business logic

**Your existing Level 1 bot continues to work** - Level 2 adds actions on top of it!

#### What's New in Level 2

**New Files**:
- `actions/` folder - Contains Python action files
- `actions/__init__.py` - Makes the folder a Python package
- `actions/action_bank_hours.py` - Your first custom action

**Modified Files**:
- `domain/basics.yml` - Adds `actions:` section to register actions
- `data/basics/hours.yml` - New flow that uses an action instead of a response

**Unchanged Files**:
- All Level 1 responses remain
- All Level 1 flows remain
- All configuration files remain (with minor updates to endpoints.yml)

---
