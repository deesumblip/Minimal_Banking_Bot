# Unit 6: Training and Testing with Actions

### 6.3 Testing Your Action

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
   - Ask about **holiday hours** (e.g. "What are your holiday hours?" or "Are you open on holidays?") → Should trigger `holiday_hours` flow and `action_holiday_hours`

**Key Point**: All Level 1 functionality remains, and both the example action and the action you created should work. If your new action doesn’t trigger, check that it’s registered in the domain and that its flow has a clear `description`.

---
