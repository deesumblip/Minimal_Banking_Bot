# Unit 6: Training and Testing with Actions

### 6.3 Testing Your Action

This section is where you **review and use the Rasa Inspector GUI**: train your bot, start Inspector, open it in your browser, and try the questions below to confirm that your flows and actions behave as expected.

#### Questions to ask in the Inspector chat

Use these in the Inspector chat to check that the most recent implementations work:

| You ask | Expected flow | Expected action / behavior |
|--------|----------------|----------------------------|
| **"Hello"** | `greet` | Level 1 greeting |
| **"What are your hours?"** / **"When are you open?"** | `hours` | `action_bank_hours` — message varies by day (weekday vs weekend) |
| **"What are your holiday hours?"** / **"Are you open on holidays?"** / **"Are you open on Christmas?"** | `holiday_hours` | `action_holiday_hours` — message varies by whether today is a holiday (date-based) |
| **"Help"** | `help` | Level 1 help |
| **"How can I contact you?"** | `contact` | Level 1 contact |

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

5. **Test both of your actions**:
   - Ask about **regular hours** (e.g. "What are your hours?") → Should trigger `hours` flow and `action_bank_hours`
   - Ask about **holiday hours** (e.g. "What are your holiday hours?" or "Are you open on holidays?") → Should trigger `holiday_hours` flow and `action_holiday_hours`; message will vary by whether today is a holiday ("closed today") or not (general schedule)

**Key Point**: All Level 1 functionality remains, and both the example action and the action you created should work. If your new action doesn’t trigger, check that it’s registered in the domain and that its flow has a clear `description`.

**Explore how your modifications show up**: In Inspector you can see which **flow** was matched and which **action** ran for each message. Try "What are your hours?" vs "What are your holiday hours?" and observe how the selected flow and action change—that's your domain registration and flow YAML directly affecting the bot's behavior.

---
