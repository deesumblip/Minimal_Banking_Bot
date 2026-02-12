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
