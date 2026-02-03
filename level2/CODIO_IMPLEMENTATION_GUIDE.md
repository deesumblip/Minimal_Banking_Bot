# Level 2: Simple Actions - Complete Codio Course Guide

**Complete Course Content and Implementation Guide for Codio Platform**

**Purpose**: This document serves as both:
- **Complete course content** for students (Level 2 tutorial content integrated)
- **Implementation guide** for the Codio team (technical specifications and deployment notes)

---

## For Students (Full Tutorial Content)

**A Complete Guide to Adding Custom Python Code to Your Banking Bot**

---

## Table of Contents

0. [Recap: What You Built in Level 1](#module-0-recap-what-you-built-in-level-1)
1. [Introduction to Actions](#module-1-introduction-to-actions)
2. [Understanding the Action Class](#module-2-understanding-the-action-class)
3. [Creating Your First Action](#module-3-creating-your-first-action)
4. [Registering Actions in the Domain](#module-4-registering-actions-in-the-domain)
5. [Using Actions in Flows](#module-5-using-actions-in-flows)
6. [Training and Testing with Actions](#module-6-training-and-testing-with-actions)
7. [Putting It All Together](#module-7-putting-it-all-together)
8. [Assessment and Next Steps](#module-8-assessment-and-next-steps)

---

## Module 0: Recap - What You Built in Level 1

### 0.1 Your Level 1 Banking Bot

Before we add actions, let's recap what you've already built in Level 1. **All of this remains unchanged** - Level 2 builds on top of it!

#### What You Have from Level 1

**Domain File (`domain/basics.yml`)**:
- ✅ `utter_greet` - Greets users as a banking assistant
- ✅ `utter_help` - Lists banking services (balance, transfers, hours, contact)
- ✅ `utter_contact` - Provides bank contact information

**Flows (`data/basics/`)**:
- ✅ `greet.yml` - Greets users when they start a conversation
- ✅ `help.yml` - Explains what the bot can help with
- ✅ `contact.yml` - Provides contact information for the bank

**System Patterns (`data/system/patterns/patterns.yml`)**:
- ✅ `pattern_session_start` - Automatically greets users when conversation begins
- ✅ `pattern_completed` - Handles flow completion

**Configuration Files**:
- ✅ `config.yml` - Bot configuration (pipeline, policies)
- ✅ `credentials.yml` - Connection settings
- ✅ `endpoints.yml` - Action endpoints and LLM configuration

#### What Level 1 Couldn't Do

Your Level 1 bot was limited to **static responses** - predefined text that never changes. It couldn't:
- ❌ Execute custom Python code
- ❌ Perform calculations
- ❌ Access databases or APIs
- ❌ Return dynamic responses based on conditions
- ❌ Process data or make decisions

**Example**: If a user asked "What are your bank hours?", your Level 1 bot would need a static `utter_hours` response. It couldn't check the current day or calculate if the bank is currently open.

---

### 0.2 What Level 2 Adds

Level 2 introduces **Actions** - custom Python code that your bot can execute. This enables:

- ✅ Dynamic responses based on calculations
- ✅ Data processing and logic
- ✅ Integration with external systems
- ✅ Custom business logic

**Your existing Level 1 bot continues to work** - Level 2 adds actions on top of it!

#### What's New in Level 2

**New Files**:
- `actions/` folder - Contains Python action files
- `actions/__init__.py` - Makes the folder a Python package
- `actions/action_bank_hours.py` - Your first custom action

**Modified Files**:
- `domain/basics.yml` - Adds `actions:` section to register actions
- `data/basics/hours.yml` - New flow that uses an action instead of a response

**Unchanged Files**:
- All Level 1 responses remain
- All Level 1 flows remain
- All configuration files remain (with minor updates to endpoints.yml)

---

## Module 1: Introduction to Actions

### 1.1 What is an Action?

An **action** is custom Python code that your bot can execute. Actions allow your bot to do more than just say predefined text - they can perform calculations, access databases, call APIs, and execute any Python logic you write.

#### Actions vs. Responses

**Responses (`utter_*`)**:
- Predefined text messages
- No custom logic
- Just sends text to the user
- Defined in `domain/basics.yml` under `responses:`

**Actions (`action_*`)**:
- Custom Python code
- Can execute any logic
- Can access databases, APIs, perform calculations
- Defined in Python files in `actions/` folder
- Registered in `domain/basics.yml` under `actions:`

#### When to Use Actions

✅ **Use actions when you need**:
- Dynamic responses (e.g., "We're open today until 5pm" - changes based on current day)
- Calculations (e.g., calculating interest, fees)
- Data processing (e.g., formatting dates, validating input)
- External integrations (e.g., checking account balance from a database)
- Conditional logic (e.g., different responses based on conditions)

❌ **Don't use actions for**:
- Simple static text (use responses instead)
- Messages that never change
- Text that doesn't require any processing

#### Example: Bank Hours

**Level 1 approach** (static response):
```yaml
utter_hours:
  - text: "We're open Monday-Friday 9am-5pm, Saturday 10am-2pm."
```

**Level 2 approach** (dynamic action):
```python
def run(self, dispatcher, tracker, domain):
    # Check current day
    # Check if it's a holiday
    # Return dynamic message: "We're open today until 5pm" or "We're closed today"
```

---

### 1.2 How Actions Work

When a flow calls an action, here's what happens:

```
User sends message: "What are your hours?"
    ↓
Flow: hours is triggered
    ↓
Flow step: - action: action_bank_hours
    ↓
Rasa finds action_bank_hours in actions/ folder
    ↓
Rasa executes the action's run() method
    ↓
Action executes Python code
    ↓
Action sends message via dispatcher.utter_message()
    ↓
Bot responds with dynamic message
```

**Key Point**: Actions are Python classes that Rasa calls when needed. You write the logic, Rasa handles the execution.

---

### 1.3 The Action Class Structure

Every action is a Python class that inherits from `Action`. Here's the basic structure:

```python
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBankHours(Action):
    def name(self) -> Text:
        return "action_bank_hours"
    
    def run(self, dispatcher, tracker, domain):
        # Your custom code here
        dispatcher.utter_message("Your message here")
        return []
```

**Required Methods**:
1. **`name()`** - Returns the action name (must match what's in domain)
2. **`run()`** - Contains your custom logic

---

## Module 2: Understanding the Action Class

### 2.1 The Action Class Deep Dive

Let's examine the actual `action_bank_hours.py` file to understand how actions work.

#### Complete Action File

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A simple custom action that returns bank hours.
    
    This action doesn't use any slots (memory) - it just returns
    a hardcoded message. Perfect for learning how actions work!
    """

    def name(self) -> Text:
        """Return the name of this action.
        
        This name must match what you put in domain/basics.yml
        under the 'actions:' list.
        """
        return "action_bank_hours"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """Execute the action.
        
        Args:
            dispatcher: Used to send messages back to the user
            tracker: Contains the conversation history and slots
            domain: The bot's domain configuration
            
        Returns:
            A list of events (usually empty for simple actions)
        """
        # This is where your custom logic goes!
        # For now, we just return a hardcoded message.
        dispatcher.utter_message(
            text="Our bank hours are Monday-Friday 9am-5pm, Saturday 10am-2pm. We're closed on Sundays."
        )
        return []
```

#### Breaking Down Each Component

1. **Imports**:
   ```python
   from rasa_sdk import Action, Tracker
   from rasa_sdk.executor import CollectingDispatcher
   ```
   - `Action` - Base class all actions inherit from
   - `Tracker` - Contains conversation history and slots (we'll use this in Level 3)
   - `CollectingDispatcher` - Used to send messages to the user

2. **Class Definition**:
   ```python
   class ActionBankHours(Action):
   ```
   - Must inherit from `Action`
   - Class name should be descriptive (convention: `Action` + descriptive name)

3. **`name()` Method**:
   ```python
   def name(self) -> Text:
       return "action_bank_hours"
   ```
   - Returns the action identifier
   - **Must match** what you register in `domain/basics.yml`
   - Convention: starts with `action_`

4. **`run()` Method**:
   ```python
   def run(self, dispatcher, tracker, domain):
   ```
   - **`dispatcher`**: Use this to send messages to the user
   - **`tracker`**: Access conversation history and slots (Level 3+)
   - **`domain`**: Access domain configuration (rarely needed)
   - **Returns**: List of events (usually empty `[]` for simple actions)

5. **Sending Messages**:
   ```python
   dispatcher.utter_message(text="Your message here")
   ```
   - This is how you send text to the user
   - Can also use `dispatcher.utter_message(response="utter_xyz")` to use a response

---

### 2.2 Understanding the Parameters

#### Dispatcher

The `dispatcher` is your way to communicate with the user:

```python
# Send a simple text message
dispatcher.utter_message(text="Hello!")

# Use a response from the domain
dispatcher.utter_message(response="utter_greet")

# Send multiple messages
dispatcher.utter_message(text="First message")
dispatcher.utter_message(text="Second message")
```

#### Tracker

The `tracker` contains conversation information (we'll use this more in Level 3):

```python
# Get conversation history (Level 3+)
events = tracker.events

# Get slots (Level 3+)
account = tracker.get_slot("account")
```

For Level 2, we don't use the tracker much - it's mainly for Level 3 when we add memory.

#### Domain

The `domain` contains your bot's configuration:

```python
# Access domain (rarely needed)
responses = domain.get("responses", {})
```

For Level 2, you typically don't need to access the domain directly.

---

## Module 3: Creating Your First Action

### 3.1 Step-by-Step: Creating an Action

Let's create a simple action to practice. We'll create `action_bank_hours.py` (which already exists, but we'll understand how it was created).

#### Before You Begin

✅ **Checklist**:
- You understand basic Python syntax
- You know where the `actions/` folder is
- You have a text editor ready
- Your Level 1 bot is working

#### Step-by-Step Tutorial

**Step 1: Navigate to the Actions Folder**

1. In your project folder, navigate to the `actions/` folder
2. If it doesn't exist, create it
3. You should see `__init__.py` (if the folder exists)

**What you should see**: An `actions/` folder with `__init__.py` inside.

---

**Step 2: Create the Action File**

1. In the `actions/` folder, create a new file named `action_bank_hours.py`
2. Open it in your text editor

⚠️ **File naming**:
- Use lowercase with underscores: `action_bank_hours.py`
- Must start with `action_` (convention)
- The filename should match the action name

---

**Step 3: Add the Action Class Structure**

1. Add the imports at the top:
   ```python
   from typing import Any, Dict, List, Text
   
   from rasa_sdk import Action, Tracker
   from rasa_sdk.executor import CollectingDispatcher
   ```

2. Create the class:
   ```python
   class ActionBankHours(Action):
       def name(self) -> Text:
           return "action_bank_hours"
       
       def run(self, dispatcher, tracker, domain):
           dispatcher.utter_message(
               text="Our bank hours are Monday-Friday 9am-5pm, Saturday 10am-2pm. We're closed on Sundays."
           )
           return []
   ```

**Complete file**:
```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A simple custom action that returns bank hours."""

    def name(self) -> Text:
        return "action_bank_hours"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Our bank hours are Monday-Friday 9am-5pm, Saturday 10am-2pm. We're closed on Sundays."
        )
        return []
```

---

**Step 4: Verify Your Code**

Before saving, check:

✅ **Imports**: All required imports are present
✅ **Class name**: `ActionBankHours` (descriptive, starts with `Action`)
✅ **`name()` method**: Returns `"action_bank_hours"` (matches filename)
✅ **`run()` method**: Has correct parameters (`dispatcher`, `tracker`, `domain`)
✅ **Message sending**: Uses `dispatcher.utter_message()`
✅ **Return value**: Returns `[]` (empty list)

**Common mistakes to avoid**:
- ❌ Forgetting to inherit from `Action`
- ❌ Wrong return type in `name()` (should return string, not call it)
- ❌ Forgetting to return `[]` from `run()`
- ❌ Typos in method names (`run` not `runs`, `name` not `names`)

---

**Step 5: Save the File**

1. Save your file as `action_bank_hours.py` in the `actions/` folder
2. Your action is now created!

---

### 3.2 Understanding Action Execution

When Rasa executes your action:

1. **Rasa finds the action**: Looks for `action_bank_hours` in the `actions/` folder
2. **Rasa instantiates the class**: Creates an instance of `ActionBankHours`
3. **Rasa calls `name()`**: Verifies the action name matches
4. **Rasa calls `run()`**: Executes your custom code
5. **Your code runs**: Python executes your logic
6. **Message is sent**: `dispatcher.utter_message()` sends text to the user
7. **Action completes**: Returns empty list `[]`

**Key Point**: Rasa handles all the infrastructure - you just write the `run()` method with your logic.

---

## Module 4: Registering Actions in the Domain

### 4.1 Why Register Actions?

Actions must be registered in the domain file so Rasa knows they exist. Without registration, Rasa won't find your actions even if the Python files exist.

**File Location**: `domain/basics.yml`

**Analogy**: Registering an action is like adding a phone number to your contacts - you need to tell Rasa "this action exists and here's its name."

---

### 4.2 The Actions Section

In Level 1, your domain file only had a `responses:` section. Level 2 adds an `actions:` section.

#### Domain Structure in Level 2

```yaml
version: "3.1"

responses:              # ← From Level 1 (unchanged)
  utter_greet:
    - text: "Hi! I'm a banking assistant..."
  # ... other responses

actions:                # ← NEW in Level 2
  - action_bank_hours   # ← Register your actions here
```

#### How to Register an Action

1. **Open `domain/basics.yml`**
2. **Add `actions:` section** (if it doesn't exist):
   ```yaml
   actions:
     - action_bank_hours
   ```

3. **The action name must match**:
   - The return value of `name()` method: `"action_bank_hours"`
   - The class name (without `Action` prefix): `ActionBankHours` → `action_bank_hours`
   - Convention: lowercase with underscores

---

### 4.3 Step-by-Step: Registering Your Action

**Step 1: Open the Domain File**

1. Navigate to `domain/basics.yml`
2. Open it in your editor

**What you should see**: Your Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`)

---

**Step 2: Add the Actions Section**

1. Find the end of the `responses:` section
2. Add a blank line
3. Add the `actions:` section:

```yaml
responses:
  utter_greet:
    - text: "Hi! I'm a banking assistant. How can I help you today?"
      metadata:
        rephrase: True

  utter_help:
    - text: |
        I can help you with:
        - Checking your balance
        - Transferring money
        - Bank hours
        - Contact information
      metadata:
        rephrase: True

  utter_contact:
    - text: "You can reach us at support@bank.com or call 1-800-BANK-123."
      metadata:
        rephrase: True

actions:                # ← NEW: Add this section
  - action_bank_hours   # ← List your actions here
```

⚠️ **Important**:
- `actions:` is at the same indentation level as `responses:`
- The dash (`-`) indicates a list item
- Action name must match exactly what `name()` returns

---

**Step 3: Verify Registration**

Check:
- ✅ `actions:` section exists
- ✅ Action name matches `name()` return value exactly
- ✅ Proper YAML syntax (indentation, dashes)
- ✅ No typos in action name

**Common mistakes**:
- ❌ Wrong action name (e.g., `action_bank_hour` instead of `action_bank_hours`)
- ❌ Missing dash before action name
- ❌ Wrong indentation
- ❌ Action name doesn't match `name()` method return value

---

### 4.4 Multiple Actions

When you have multiple actions, list them all:

```yaml
actions:
  - action_bank_hours
  - action_check_balance
  - action_process_transfer
```

Each action gets its own line with a dash.

---

## Module 5: Using Actions in Flows

### 5.1 Actions vs. Responses in Flows

In Level 1, flows used `utter_*` responses. In Level 2, flows can use `action_*` actions.

#### Level 1 Flow (Response)

```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet  # ← Uses a response
```

#### Level 2 Flow (Action)

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours  # ← Uses an action
```

**Key Difference**: 
- `utter_*` = Predefined text (response)
- `action_*` = Custom Python code (action)

Both use `- action:` in the flow, but Rasa knows the difference based on the name.

---

### 5.2 Creating a Flow That Uses an Action

Let's create the `hours.yml` flow that uses `action_bank_hours`.

#### Step-by-Step Tutorial

**Step 1: Navigate to Data Folder**

1. Go to `data/basics/` folder
2. You should see your Level 1 flows: `greet.yml`, `help.yml`, `contact.yml`

---

**Step 2: Create the Hours Flow**

1. Create a new file: `data/basics/hours.yml`
2. Add the flow structure:

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours
```

**Complete file**:
```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours
```

---

**Step 3: Understanding the Flow**

- **`hours:`** - Flow identifier
- **`name: bank hours`** - Human-readable name
- **`description:`** - Critical! The LLM uses this to match user messages
- **`steps:`** - List of steps to execute
- **`- action: action_bank_hours`** - Calls your custom action

**What happens**:
1. User asks "What are your hours?"
2. LLM matches to `hours` flow (based on description)
3. Flow executes `action_bank_hours`
4. Action runs Python code
5. Action sends message via `dispatcher.utter_message()`
6. User sees: "Our bank hours are Monday-Friday 9am-5pm..."

---

**Step 4: Verify the Flow**

Check:
- ✅ File is in `data/basics/` folder
- ✅ Flow has `name:`, `description:`, and `steps:`
- ✅ Action name matches registered action exactly
- ✅ YAML syntax is correct

---

### 5.3 Mixing Responses and Actions

You can use both responses and actions in the same flow:

```yaml
flows:
  hours_and_contact:
    name: hours and contact
    description: Tell the user bank hours and provide contact information.
    steps:
      - action: action_bank_hours      # ← Action (custom code)
      - action: utter_contact          # ← Response (predefined text)
```

**Execution order**:
1. First: Action executes (returns dynamic hours)
2. Second: Response sends (static contact info)

---

## Module 6: Training and Testing with Actions

### 6.1 Training with Actions

Training with actions is the same as Level 1, but Rasa now also processes your action files.

#### Training Command

```powershell
# Make sure environment variables are loaded
. .\load_env.ps1

# Train the bot
python -m rasa train
```

#### What Happens During Training

When you run `rasa train`, Rasa:

1. **Reads all flows** from `data/` folder
   - Finds `hours.yml` with `action_bank_hours`
   - Processes all Level 1 flows (unchanged)

2. **Reads the domain** from `domain/` folder
   - Loads all responses (from Level 1)
   - Loads all actions (new in Level 2)
   - Verifies registered actions exist

3. **Validates actions**:
   - Checks that `action_bank_hours` exists in `actions/` folder
   - Verifies the `name()` method returns the registered name
   - Ensures the action class is properly structured

4. **Creates model file**:
   - Saves everything to `models/` folder
   - Includes action registration information

---

### 6.2 Common Training Errors with Actions

#### Error: Action Not Found

**What you'll see**:
```
Error: Action 'action_bank_hours' not found
```

**What this means**: Rasa can't find your action file.

**How to fix**:
1. Check the action file exists: `actions/action_bank_hours.py`
2. Check the action is registered: `domain/basics.yml` has `- action_bank_hours`
3. Check the `name()` method returns the correct name
4. Verify the file is in the `actions/` folder (not `action/` or elsewhere)

---

#### Error: Import Error

**What you'll see**:
```
ImportError: cannot import name 'Action' from 'rasa_sdk'
```

**What this means**: Rasa SDK is not installed or wrong version.

**How to fix**:
1. Make sure Rasa Pro is installed: `python -m pip install rasa-pro`
2. Check your virtual environment is activated
3. Verify Rasa SDK is included with Rasa Pro

---

#### Error: Name Mismatch

**What you'll see**:
```
Error: Action name 'action_bank_hours' in domain doesn't match class name
```

**What this means**: The action name in domain doesn't match what `name()` returns.

**How to fix**:
1. Check `domain/basics.yml`: Should have `- action_bank_hours`
2. Check `action_bank_hours.py`: `name()` should return `"action_bank_hours"`
3. Ensure they match exactly (case-sensitive!)

---

### 6.3 Testing Your Action

#### Basic Testing Workflow

1. **Train your bot**: `python -m rasa train`

2. **Start Inspector**: 
   ```powershell
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

3. **Test the action**:
   - Type "What are your hours?" or "When are you open?"
   - Should trigger `hours` flow
   - Should execute `action_bank_hours`
   - Should see: "Our bank hours are Monday-Friday 9am-5pm..."

4. **Verify Level 1 flows still work**:
   - Type "hello" → Should trigger `greet` flow (unchanged)
   - Type "help" → Should trigger `help` flow (unchanged)
   - Type "contact" → Should trigger `contact` flow (unchanged)

**Key Point**: All Level 1 functionality remains - Level 2 adds new capabilities without breaking existing ones.

---

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

## Module 7: Putting It All Together

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
   Action executes Python code
   dispatcher.utter_message() sends message
   ↓
Bot: "Our bank hours are Monday-Friday 9am-5pm, Saturday 10am-2pm. We're closed on Sundays."

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

## Module 8: Assessment and Next Steps

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

## Troubleshooting Guide

### Common Issues and Solutions

#### Issue: Action Not Found Error

**Symptoms**: Training error: "Action 'action_xyz' not found"

**Possible Causes**:
1. Action file doesn't exist in `actions/` folder
2. Action not registered in domain
3. Action name mismatch (domain vs. `name()` method)

**Solutions**:
1. Check `actions/action_xyz.py` exists
2. Verify `domain/basics.yml` has `- action_xyz` under `actions:`
3. Ensure `name()` returns exactly `"action_xyz"` (case-sensitive)

---

#### Issue: Action Executes But No Message

**Symptoms**: Action runs but user doesn't see a message

**Possible Causes**:
1. `dispatcher.utter_message()` not called
2. Python error in action (silent failure)
3. Wrong dispatcher usage

**Solutions**:
1. Check `dispatcher.utter_message()` is called in `run()` method
2. Check for Python errors (syntax, imports)
3. Verify you're using `dispatcher.utter_message(text="...")` correctly

---

#### Issue: Import Error

**Symptoms**: `ImportError: cannot import name 'Action'`

**Possible Causes**:
1. Rasa SDK not installed
2. Wrong virtual environment
3. Rasa Pro not properly installed

**Solutions**:
1. Install Rasa Pro: `python -m pip install rasa-pro`
2. Activate correct virtual environment
3. Verify installation: `python -m rasa --version`

---

## Additional Resources

### Extension Exercises

#### Exercise 1: Add More Actions

**Task**: Create additional actions for your banking bot:
- `action_account_types.py` - Returns information about account types
- `action_loan_info.py` - Returns loan information

**Goal**: Practice creating multiple actions and registering them.

---

#### Exercise 2: Dynamic Responses

**Task**: Modify `action_bank_hours.py` to:
- Check the current day of week
- Return different messages based on whether bank is currently open

**Goal**: Learn to use Python logic in actions.

---

#### Exercise 3: Action with Calculations

**Task**: Create `action_calculate_interest.py` that:
- Takes a principal amount and interest rate
- Calculates simple interest
- Returns the result

**Goal**: Practice using Python calculations in actions.

---

## Conclusion

Congratulations! You've completed Level 2 and learned how to add custom Python code to your Rasa bot.

### What You Can Do Now

- Add custom Python code to your bot
- Create dynamic responses based on logic
- Process data and perform calculations
- Integrate with external systems (with proper setup)
- Extend your Level 1 bot with new capabilities

### What's Coming Next

- **Level 3**: Add memory (slots) so the bot can remember information
- **Level 4**: Collect multiple pieces of information
- **Level 5**: Enable dynamic tool calling

### Keep Learning

- Practice by creating more actions
- Experiment with different Python logic
- Try integrating with simple APIs
- Read the Rasa SDK documentation
- Join the Rasa community

**Happy coding! 🚀**

---

## Implementation Overview for Codio Team

### Executive Summary

This document is a **combined student course + Codio implementation guide** for **Level 2: Simple Actions**.

**Key goals**:
- Preserve the complete student tutorial content (integrated above)
- Convert exercises into Codio labs with auto-grading and clear feedback
- Minimize setup friction (pre-configured environment, templates, helper scripts)
- Use Codio AI Coach for hints and troubleshooting support

### Content Integration Strategy

- The full content from `TUTORIAL.md` is included in this document (to keep the course self-contained).
- Exercises should be implemented as **auto-graded labs** wherever possible.

---

## Technical Specifications for Codio Team

### Lab Environment Configuration

**Base Environment Requirements**:
- Operating System: Linux (Ubuntu 22.04 or similar)
- Python: 3.11
- IDE: Browser-based VS Code (Codio standard)
- Terminal: Bash shell

**Pre-Installed Software**:
- Python 3.11 + pip (latest)
- `rasa-pro` (latest stable)
- `git` (optional)

**Pre-Configured Project Structure** (representative):
```
project/
├── domain/
│   └── basics.yml
├── data/
│   ├── basics/
│   │   └── *.yml
│   └── system/
│       └── patterns/
│           └── patterns.yml
├── config.yml
├── credentials.yml
├── endpoints.yml
├── .env (template with placeholders)
├── load_env.ps1 (for Windows-based local runs; optional in Codio)
└── run_inspector.ps1 (optional helper)

├── actions/
│   ├── __init__.py
│   └── action_*.py
```

**Environment Variables**:
- `RASA_LICENSE=...`
- `OPENAI_API_KEY=...`

**Port Configuration**:
- Rasa Inspector: 5005 (default)

---

## Auto-Grading Guidance (Codio Team)

**Recommended auto-grading checks**:
- Validate YAML files parse successfully and required keys exist (domain + flows + patterns)
- Validate required new artifacts for Level 2 exist (e.g., new flows/actions/tools)
- Smoke-test bot starts (`rasa inspect`) and responds to a small scripted conversation

**Implementation notes**:
- Prefer deterministic checks (file existence + YAML structure + expected strings) over LLM-output matching.
- Provide actionable error output (“Expected `actions:` section in `domain/basics.yml`”, etc.).

---

## AI Coach Configuration Reference (Codio Team)

**Guidelines**:
- Provide hints, not full solutions
- Point learners to the right file and the relevant section
- Explain why a concept matters (actions vs responses, slots, tools, etc.)
- Encourage incremental testing (train + inspect frequently)

---

## Quality Assurance Checklist (Codio Team)

- [ ] Course runs end-to-end in a clean Codio environment
- [ ] All links/anchors in the student tutorial work in Codio’s markdown renderer
- [ ] Auto-grader messages are specific and helpful
- [ ] At least one “happy-path” conversation is validated for this level’s new capability


