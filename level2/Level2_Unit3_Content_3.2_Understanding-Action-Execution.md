# Unit 3: Creating Your First Action

### 3.2 Understanding Action Execution

When Rasa executes your action:

1. **Rasa finds the action**: Looks for the action in the `actions/` folder
2. **Rasa instantiates the class**: Creates an instance of your action class
3. **Rasa calls `name()`**: Verifies the action name matches what's registered
4. **Rasa calls `run()`**: Executes your custom code
5. **Your code runs**: Python executes your logic
6. **Message is sent**: `dispatcher.utter_message()` sends text to the user
7. **Action completes**: Returns empty list `[]`

**Key Point**: Rasa handles all the infrastructure—you just write the `run()` method with your logic.

**Next**: Complete Lab 3.1 to create `action_holiday_hours.py` following the pattern from Unit 3.1.

---
