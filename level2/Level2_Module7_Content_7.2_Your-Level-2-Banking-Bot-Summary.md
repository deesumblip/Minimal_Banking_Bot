# Module 7: Putting It All Together

### 7.2 Your Level 2 Banking Bot: Summary

Congratulations! You've extended your Level 1 banking bot with custom Python code.

#### Your Complete Bot Structure

**Domain (`domain/basics.yml`)**:
- ✅ All Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`, `utter_goodbye`)
- ✅ New `actions:` section with `action_bank_hours` (and `action_holiday_hours` after Lab 4.1)

**Flows (`data/basics/`)**:
- ✅ All Level 1 flows (`greet`, `help`, `contact`, `goodbye`)
- ✅ Example flow (`hours`) that uses `action_bank_hours`
- ✅ Your flow (`holiday_hours`) that uses `action_holiday_hours` (the action you created in Lab 3.1)

**Actions (`actions/`)**:
- ✅ `action_bank_hours.py` - Example: returns bank hours dynamically
- ✅ `action_holiday_hours.py` - Yours: returns holiday hours (you created this in Lab 3.1)

**System Patterns**: Unchanged from Level 1

**Configuration**: Unchanged from Level 1 (except minor endpoints.yml updates)

#### What Your Bot Can Do Now

Your Level 2 banking bot can:
- ✅ Everything Level 1 could do (greet, help, contact)
- ✅ Execute custom Python code (actions) — both the example and the one you built
- ✅ Return dynamic responses based on code execution
- ✅ Process data and perform calculations
- ✅ Answer questions about regular hours and holiday hours (your action)

#### What's Still Missing (Coming in Future Levels)

Your Level 2 bot cannot yet:
- ❌ Remember information from the conversation (Level 3: Slots)
- ❌ Collect multiple pieces of information (Level 4: Multiple Slots)
- ❌ Use dynamic tool calling (Level 5: Tools)

But you have a solid foundation with custom code capabilities!

---
