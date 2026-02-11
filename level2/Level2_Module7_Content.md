# Module 7: Putting It All Together

### 7.1 Complete Bot Walkthrough

Let's trace through a complete conversation showing how Level 1 and Level 2 work together.

#### Conversation Example

```
[User opens chat - new session starts]

1. pattern_session_start triggers automatically (Level 1)
   ↓
   Flow: pattern_session_start
   Step: utter_greet
   ↓
Bot: "Hi! I'm a banking assistant. How can I help you today?"

[User types: "What are your hours?"]

2. LLM understands: "User wants to know bank hours"
   ↓
   FlowPolicy matches to: hours flow (Level 2)
   (Description: "Tell the user when the bank is open")
   ↓
   Flow: hours
   Step: action_bank_hours (Level 2 - custom Python code!)
   ↓
   Action executes Python code (checks current day via datetime)
   dispatcher.utter_message() sends message
   ↓
Bot: [Dynamic message—e.g., "Today is Saturday—we're open 10am-2pm." or full schedule on weekdays]

[User types: "How can I contact you?"]

3. LLM understands: "User wants contact information"
   ↓
   FlowPolicy matches to: contact flow (Level 1)
   ↓
   Flow: contact
   Step: utter_contact (Level 1 - static response)
   ↓
Bot: "You can reach us at support@bank.com or call 1-800-BANK-123."
```

**Notice**: The bot seamlessly uses both Level 1 responses and Level 2 actions!

---

### 7.2 Your Level 2 Banking Bot: Summary

Congratulations! You've extended your Level 1 banking bot with custom Python code.

#### Your Complete Bot Structure

**Domain (`domain/basics.yml`)**:
- ✅ All Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`)
- ✅ New `actions:` section with `action_bank_hours`

**Flows (`data/basics/`)**:
- ✅ All Level 1 flows (`greet`, `help`, `contact`)
- ✅ New flow (`hours`) that uses an action

**Actions (`actions/`)**:
- ✅ `action_bank_hours.py` - Returns bank hours dynamically

**System Patterns**: Unchanged from Level 1

**Configuration**: Unchanged from Level 1 (except minor endpoints.yml updates)

#### What Your Bot Can Do Now

Your Level 2 banking bot can:
- ✅ Everything Level 1 could do (greet, help, contact)
- ✅ Execute custom Python code (actions)
- ✅ Return dynamic responses based on code execution
- ✅ Process data and perform calculations

#### What's Still Missing (Coming in Future Levels)

Your Level 2 bot cannot yet:
- ❌ Remember information from the conversation (Level 3: Slots)
- ❌ Collect multiple pieces of information (Level 4: Multiple Slots)
- ❌ Use dynamic tool calling (Level 5: Tools)

But you have a solid foundation with custom code capabilities!

---

### 7.3 Best Practices

#### Organizing Actions

1. **One action per file**: Makes it easier to find and modify actions
2. **Descriptive names**: Use clear, descriptive action names
3. **Group related actions**: Keep related actions in the same folder

#### Writing Good Actions

1. **Keep actions focused**: Each action should do one thing well
2. **Handle errors gracefully**: Check for None values, validate input
3. **Use clear messages**: Make sure users understand what happened
4. **Add comments**: Explain complex logic

#### Action Naming Conventions

- ✅ **Good**: `action_bank_hours`, `action_check_balance`, `action_process_transfer`
- ❌ **Bad**: `action1`, `hours`, `do_stuff`

**Convention**: `action_` + descriptive_name (lowercase, underscores)

---
