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

[User types: "What are your holiday hours?"]

3. LLM understands: "User wants holiday hours"
   ↓
   FlowPolicy matches to: holiday_hours flow (Level 2 - your flow)
   ↓
   Flow: holiday_hours
   Step: action_holiday_hours (Level 2 - the action you created in Lab 3.1!)
   ↓
   Action runs and sends message
   ↓
Bot: [Your holiday hours message]

[User types: "How can I contact you?"]

4. LLM understands: "User wants contact information"
   ↓
   FlowPolicy matches to: contact flow (Level 1)
   ↓
   Flow: contact
   Step: utter_contact (Level 1 - static response)
   ↓
Bot: "You can reach us at support@bank.com or call 1-800-BANK-123."
```

**Notice**: The bot uses Level 1 responses, the example action (`action_bank_hours`), and the action you built (`action_holiday_hours`).

---
