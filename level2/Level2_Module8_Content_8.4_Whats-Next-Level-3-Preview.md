# Module 8: Assessment and Next Steps

### 8.4 What's Next: Level 3 Preview

⚠️ **Important: Building on Your Existing Banking Bot**

When you move to Level 3, you will **continue working on the same banking bot** you've built throughout Levels 1 and 2. Level 3 doesn't start from scratch - it builds on what you've already created:

- **Your existing responses** (`utter_greet`, `utter_help`, `utter_contact`) stay
- **Your existing flows** (`greet`, `help`, `contact`, `hours`) stay
- **Your existing actions** (`action_bank_hours`) stay
- **Level 3 adds**: Slots (memory), new responses for asking questions, new actions that use slots, new flows that collect information

**You don't start a new bot** - you extend your existing Level 2 banking bot with memory capabilities!

---

**Level 3: Slot Collection** introduces conversation memory.

#### What Slots Enable

**Example Scenario**: "Check my balance"

- **Level 2**: Bot can't remember which account the user has
- **Level 3**: Bot can:
  - Ask for account number
  - Remember it in a slot
  - Use that slot in actions
  - Check balance for that specific account

In Level 3, you'll add:
- `account` slot to store the user's account number
- `utter_ask_account` response to ask for the account
- `action_check_balance_simple` action that reads the slot
- `check_balance` flow that collects the account before checking

#### Key Concepts in Level 3

1. **Slots**: Memory variables that store information from the conversation
2. **Slot Collection**: Using `collect:` in flows to ask for and store information
3. **Reading Slots**: Using `tracker.get_slot()` in actions to access stored information
4. **Ask Responses**: `utter_ask_*` responses used when collecting slots

#### When to Move to Level 3

Move to Level 3 when you need:
- To remember information from the conversation
- To collect information from users before performing actions
- Multi-turn conversations with context
- Personalized responses based on user information

**Your Level 2 banking bot is the foundation** - Level 3 adds memory on top of it!

---
