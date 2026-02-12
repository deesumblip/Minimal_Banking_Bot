# Unit 6: Training and Testing with Actions

### 6.4 Debugging Actions

#### Check Debug Output

When testing in Inspector, check the debug panel:
- Which flow was triggered?
- Which action was called?
- Did the action execute successfully?

#### Common Issues

1. **Action doesn't trigger**:
   - Check flow description matches user intent
   - Verify action is registered in domain
   - Check action file exists and is correct

2. **Action executes but no message**:
   - Check `dispatcher.utter_message()` is called
   - Verify the message text is correct
   - Check for Python errors in the action

3. **Python errors in action**:
   - Check Python syntax
   - Verify all imports are correct
   - Check for typos in method names

---
