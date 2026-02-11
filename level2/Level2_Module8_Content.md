# Module 8: Assessment and Next Steps

### 8.1 Knowledge Check

Test your understanding with these questions:

#### Question 1: What is an Action?

a) A predefined bot message  
b) Custom Python code the bot can execute  
c) A conversation script  
d) A configuration file

**Answer**: b) Custom Python code the bot can execute

**Explanation**: Actions are Python classes that execute custom code. They allow the bot to do more than just send static text - they can perform calculations, access databases, and execute any Python logic.

---

#### Question 2: Where are Actions Defined?

a) In `domain/basics.yml` under `responses:`  
b) In Python files in the `actions/` folder  
c) In flow files in `data/basics/`  
d) In `config.yml`

**Answer**: b) In Python files in the `actions/` folder

**Explanation**: Actions are Python classes defined in `.py` files in the `actions/` folder. They must also be registered in `domain/basics.yml` under `actions:`, but the actual code is in Python files.

---

#### Question 3: What Method Must Every Action Have?

a) `execute()`  
b) `run()`  
c) `perform()`  
d) `do()`

**Answer**: b) `run()`

**Explanation**: Every action class must have a `run()` method that contains the custom logic. This is the method Rasa calls when the action is executed.

---

#### Question 4: How Do You Send a Message from an Action?

a) `print("message")`  
b) `dispatcher.utter_message(text="message")`  
c) `return "message"`  
d) `send_message("message")`

**Answer**: b) `dispatcher.utter_message(text="message")`

**Explanation**: The `dispatcher` parameter in the `run()` method is used to send messages to the user. Use `dispatcher.utter_message(text="...")` to send text.

---

#### Question 5: What's the Difference Between `utter_*` and `action_*`?

a) There's no difference  
b) `utter_*` are responses (static text), `action_*` are actions (custom code)  
c) `utter_*` are actions, `action_*` are responses  
d) They're the same thing

**Answer**: b) `utter_*` are responses (static text), `action_*` are actions (custom code)

**Explanation**: `utter_*` responses are predefined text messages in the domain file. `action_*` actions are custom Python code that can execute any logic. Both can be called from flows using `- action:`, but they work differently.

---

### 8.2 What You've Learned

#### Key Concepts

1. **Actions**: Custom Python code that the bot can execute
2. **Action Class**: Python class that inherits from `Action`
3. **Action Registration**: Telling Rasa about actions in the domain file
4. **Dispatcher**: Used to send messages from actions
5. **Action Execution**: How Rasa calls and runs your custom code

#### Skills You've Developed

- ✅ Can create custom Python actions
- ✅ Can register actions in the domain file
- ✅ Can call actions from flows
- ✅ Can understand the difference between responses and actions
- ✅ Can debug action-related issues
- ✅ Can extend your Level 1 bot with custom code

---

### 8.3 Limitations of Level 2

Level 2 bots have clear limitations:

#### What Level 2 Cannot Do

1. **Remember Information**: The bot cannot remember what the user said earlier
   - Example: User says "My account is 1234" → Bot forgets immediately
   - Solution: Level 3 adds slots (memory)

2. **Use Previous Context**: Actions can't access conversation history effectively
   - Example: "Check my balance" → Bot doesn't know which account
   - Solution: Level 3 adds slots to remember account numbers

3. **Collect Multiple Pieces of Information**: Can't gather multiple data points
   - Example: "Transfer money" → Bot can't collect amount, recipient, and account
   - Solution: Level 4 adds multiple slot collection

#### When Level 2 is Sufficient

Level 2 is perfect for:
- ✅ Dynamic responses based on calculations
- ✅ Data processing and formatting
- ✅ Simple integrations (APIs, databases)
- ✅ Conditional logic that doesn't need memory

#### When You Need More

Move to Level 3 when you need:
- Memory (slots) to remember user information
- Multi-turn conversations with context
- Collecting information from users

---

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

### 8.5 Course Completion Checklist

Before moving to Level 3, ensure you can:

- [ ] Explain what an action is and how it differs from a response
- [ ] Create a new action in Python
- [ ] Register an action in the domain file
- [ ] Create a flow that uses an action
- [ ] Understand how actions are executed
- [ ] Debug when actions don't work
- [ ] Understand that Level 2 builds on Level 1 (all Level 1 content remains)

If you can check all these boxes, you're ready for Level 3!

---
