# Level 3: Slot Collection - Comprehensive Tutorial

**A Complete Guide to Adding Memory to Your Banking Bot**

---

## Table of Contents

0. [Recap: What You Built in Level 2](#module-0-recap-what-you-built-in-level-2)
1. [Introduction to Slots](#module-1-introduction-to-slots)
2. [Understanding Slot Types](#module-2-understanding-slot-types)
3. [Defining Slots in the Domain](#module-3-defining-slots-in-the-domain)
4. [Collecting Slots in Flows](#module-4-collecting-slots-in-flows)
5. [Reading Slots in Actions](#module-5-reading-slots-in-actions)
6. [Training and Testing with Slots](#module-6-training-and-testing-with-slots)
7. [Putting It All Together](#module-7-putting-it-all-together)
8. [Assessment and Next Steps](#module-8-assessment-and-next-steps)

---

## Module 0: Recap - What You Built in Level 2

### 0.1 Your Level 2 Banking Bot

Before we add slots (memory), let's recap what you've already built in Level 2. **All of this remains unchanged** - Level 3 builds on top of it!

#### What You Have from Level 2

**Domain File (`domain/basics.yml`)**:
- All Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`)
- `actions:` section with `action_bank_hours` registered

**Flows (`data/basics/`)**:
- All Level 1 flows (`greet`, `help`, `contact`)
- New Level 2 flow (`hours`) that uses `action_bank_hours`

**Actions (`actions/`)**:
- `action_bank_hours.py` - Returns bank hours dynamically

**System Patterns**: Unchanged from Level 1

**Configuration Files**: Unchanged from Level 2

#### What Level 2 Couldn't Do

Your Level 2 bot could execute custom Python code, but it couldn't:
- ❌ Remember information from the conversation
- ❌ Store user-provided data
- ❌ Use information from earlier in the conversation
- ❌ Ask for missing information and remember it

**Example**: If a user asked "Check my balance", your Level 2 bot couldn't:
- Remember which account the user has
- Ask for the account number and remember it
- Use that account number in subsequent actions

---

### 0.2 What Level 3 Adds

Level 3 introduces **Slots** - the bot's memory. This enables:

- Remembering information from the conversation
- Storing user-provided data (like account numbers)
- Asking for missing information
- Using stored information in actions

**Your existing Level 2 bot continues to work** - Level 3 adds memory on top of it!

#### What's New in Level 3

**New in Domain**:
- `slots:` section - Defines what the bot remembers
- `account` slot - Stores the user's account number
- New response `utter_ask_account` - Used when asking for account number

**New Files**:
- `actions/action_check_balance_simple.py` - Action that reads the `account` slot

**New Flows**:
- `data/basics/check_balance.yml` - Flow that collects account number before checking balance

**Unchanged**:
- All Level 2 responses remain
- All Level 2 flows remain
- All Level 2 actions remain

---

## Module 1: Introduction to Slots

### 1.1 What is a Slot?

A **slot** is a memory variable that stores information from the conversation. Slots allow your bot to remember what users tell it and use that information later.

#### Slots = Bot Memory

Think of slots like a form that the bot fills out during the conversation:
- User provides information → Bot stores it in a slot
- Bot needs information → Bot asks user and stores answer in slot
- Action needs information → Bot reads it from the slot

#### Example: Account Number

**Without slots (Level 2)**:
```
User: "Check my balance"
Bot: "I need your account number" (but forgets immediately)
User: "1234"
Bot: "What account number?" (forgot it!)
```

**With slots (Level 3)**:
```
User: "Check my balance"
Bot: "What is your account number?"
User: "1234"
Bot: [Stores "1234" in account slot]
Bot: "Balance for account 1234 is $123.45"
[Later in conversation]
User: "What's my balance?"
Bot: [Remembers account 1234 from slot]
Bot: "Balance for account 1234 is $123.45"
```

---

### 1.2 How Slots Work

Slots work in three steps:

1. **Define the slot** in `domain/basics.yml`:
   ```yaml
   slots:
     account:
       type: text
   ```

2. **Collect the slot** in a flow:
   ```yaml
   steps:
     - collect: account
       description: "account number"
   ```

3. **Read the slot** in an action:
   ```python
   account = tracker.get_slot("account")
   ```

---

### 1.3 Slot Collection

When a flow has a `collect:` step:

- **If slot is empty**: Bot asks for it (using `utter_ask_*` response)
- **If slot has value**: Flow continues immediately (no asking)
- **User provides value**: Bot stores it in the slot

**Example Flow**:
```yaml
steps:
  - collect: account        # Step 1: Get account number
    description: "account number"
  - action: action_check_balance_simple  # Step 2: Use it
```

**What happens**:
1. Flow starts
2. Bot checks: Does `account` slot have a value?
   - **No** → Bot asks: "What is your account number?" (using `utter_ask_account`)
   - **Yes** → Skip to step 2
3. User provides account number
4. Bot stores it in `account` slot
5. Flow continues to step 2
6. Action reads `account` slot and uses it

---

## Module 2: Understanding Slot Types

### 2.1 Slot Types

Slots can have different types. For Level 3, we use the simplest type: `text`.

#### Text Slots

```yaml
slots:
  account:
    type: text
```

**Text slots**:
- Store any text value
- Most flexible type
- Good for: names, account numbers, descriptions, any text input

**Example values**:
- `"1234"` (account number)
- `"John Doe"` (name)
- `"checking"` (account type)

#### Other Slot Types (Advanced)

For Level 3, we only use `text` slots. Other types exist (like `bool`, `float`, `list`) but are covered in advanced tutorials.

---

### 2.2 Slot Naming

**Good slot names**:
- `account` - Clear and descriptive
- `user_name` - Descriptive
- `transfer_amount` - Clear purpose

**Bad slot names**:
- ❌ `a` - Too vague
- ❌ `slot1` - Not descriptive
- ❌ `data` - Too generic

**Convention**: Use lowercase, descriptive names. Use underscores for multi-word names.

---

## Module 3: Defining Slots in the Domain

### 3.1 The Slots Section

Slots are defined in the domain file, just like responses and actions.

#### Domain Structure in Level 3

```yaml
version: "3.1"

slots:                    # ← NEW in Level 3
  account:
    type: text

responses:                # ← From Level 1 & 2 (unchanged)
  utter_greet:
    - text: "Hi! I'm a banking assistant..."
  # ... other responses
  utter_ask_account:      # ← NEW: Used when collecting account slot
    - text: "What is your account number?"

actions:                  # ← From Level 2 (unchanged)
  - action_bank_hours
  - action_check_balance_simple  # ← NEW: Uses the account slot
```

---

### 3.2 Step-by-Step: Defining a Slot

**Step 1: Open the Domain File**

1. Navigate to `domain/basics.yml`
2. Open it in your editor

**What you should see**: Your Level 2 content (responses and actions)

---

**Step 2: Add the Slots Section**

1. Add the `slots:` section at the top (before `responses:`):

```yaml
version: "3.1"

slots:                    # ← Add this section
  account:                # ← Slot name
    type: text            # ← Slot type

responses:
  # ... existing responses
```

⚠️ **Important**:
- `slots:` is at the same indentation level as `responses:` and `actions:`
- `account:` is indented 2 spaces under `slots:`
- `type: text` is indented 2 spaces under `account:`

---

**Step 3: Add the Ask Response**

When collecting a slot, Rasa needs a response to ask for it. Add `utter_ask_account`:

```yaml
responses:
  utter_greet:
    - text: "Hi! I'm a banking assistant. How can I help you today?"
      metadata:
        rephrase: True

  # ... other responses

  utter_ask_account:      # ← NEW: Used when collecting account slot
    - text: "What is your account number?"
      metadata:
        rephrase: True
```

**Naming convention**: `utter_ask_<slot_name>`
- Slot: `account` → Response: `utter_ask_account`
- Slot: `name` → Response: `utter_ask_name`

---

**Step 4: Verify Your Domain**

Check:
- `slots:` section exists with `account` slot
- `utter_ask_account` response exists
- All Level 2 responses remain
- All Level 2 actions remain
- YAML syntax is correct

---

## Module 4: Collecting Slots in Flows

### 4.1 The Collect Step

The `collect:` step in a flow tells Rasa: "Get this slot value before continuing."

#### Collect Step Structure

```yaml
steps:
  - collect: account
    description: "account number"
```

**Breaking it down**:
- **`collect: account`** - Which slot to collect
- **`description:`** - Helps the LLM understand what to extract (optional but recommended)

---

### 4.2 Creating a Flow with Slot Collection

Let's create the `check_balance.yml` flow that collects the account number.

#### Step-by-Step Tutorial

**Step 1: Navigate to Data Folder**

1. Go to `data/basics/` folder
2. You should see your Level 2 flows: `greet.yml`, `help.yml`, `contact.yml`, `hours.yml`

---

**Step 2: Create the Check Balance Flow**

1. Create a new file: `data/basics/check_balance.yml`
2. Add the flow structure:

```yaml
flows:
  check_balance:
    name: check a balance (demo)
    description: |
      Demonstrates a flow with slot collection.
      The bot will ask for an account number if not provided,
      then call the action to check the balance.
    steps:
      - collect: account
        description: "account number"
      - action: action_check_balance_simple
```

**Complete file**:
```yaml
flows:
  check_balance:
    name: check a balance (demo)
    description: |
      Demonstrates a flow with slot collection.
      The bot will ask for an account number if not provided,
      then call the action to check the balance.
    steps:
      - collect: account
        description: "account number"
      - action: action_check_balance_simple
```

---

**Step 3: Understanding the Flow**

**Flow execution**:
1. User says "Check my balance" or "What's my balance?"
2. LLM matches to `check_balance` flow
3. Flow step 1: `collect: account`
   - Bot checks: Does `account` slot have a value?
   - **No** → Bot asks: "What is your account number?" (uses `utter_ask_account`)
   - User provides: "1234"
   - Bot stores "1234" in `account` slot
4. Flow step 2: `action: action_check_balance_simple`
   - Action reads `account` slot (gets "1234")
   - Action checks balance for account 1234
   - Action responds with balance

**If slot already has value**:
- User already provided account number earlier
- Flow skips the asking step
- Goes directly to action (which uses the stored value)

---

**Step 4: Verify the Flow**

Check:
- File is in `data/basics/` folder
- Flow has `name:`, `description:`, and `steps:`
- `collect: account` step exists
- Action name matches registered action
- YAML syntax is correct

---

### 4.3 How Collection Works

#### Collection Process

```
Flow starts
    ↓
Step 1: collect: account
    ↓
Does account slot have a value?
    ├─ NO → Bot asks: "What is your account number?"
    │        ↓
    │   User provides: "1234"
    │        ↓
    │   Bot stores "1234" in account slot
    │        ↓
    └─ YES → Skip asking (use existing value)
            ↓
Step 2: action_check_balance_simple
    ↓
Action reads account slot
    ↓
Action uses the value
```

**Key Point**: The bot only asks if the slot is empty. If it already has a value, it uses that value immediately.

---

## Module 5: Reading Slots in Actions

### 5.1 Accessing Slots in Actions

To use slot values in your actions, you read them from the `tracker` parameter.

#### Reading a Slot

```python
def run(self, dispatcher, tracker, domain):
    # Read the slot value
    account = tracker.get_slot("account")
    
    # Use the slot value
    if account:
        dispatcher.utter_message(f"Balance for account {account} is $123.45")
    else:
        dispatcher.utter_message("I don't have your account number.")
    
    return []
```

---

### 5.2 Understanding the Tracker

The `tracker` contains all conversation information:

```python
# Get a slot value
account = tracker.get_slot("account")

# Slot might be None if not set yet
if account is None:
    # Handle missing slot
    pass
```

**Important**: Slots can be `None` if they haven't been set yet. Always check!

---

### 5.3 Creating an Action That Uses Slots

Let's examine `action_check_balance_simple.py` to see how it uses slots.

#### Complete Action File

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalanceSimple(Action):
    """A custom action that reads a slot and returns a balance.
    
    This demonstrates:
    - How to read slots (conversation memory) from the tracker
    - How to handle placeholder values that the LLM might extract incorrectly
    - How to re-prompt the user if needed
    """

    def name(self) -> Text:
        return "action_check_balance_simple"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Read the 'account' slot from conversation memory
        account = tracker.get_slot("account") or "<missing>"
        
        # Check if the account is a placeholder value
        # Sometimes the LLM extracts "account number" or "user_account_number"
        # as the value, which isn't a real account number
        placeholder_values = ["account number", "user_account_number", "<missing>"]
        if account.lower() in [p.lower() for p in placeholder_values]:
            # Ask for the account number instead
            dispatcher.utter_message(response="utter_ask_account")
            return []
        
        # If we have a real account number, show the balance
        dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")
        return []
```

#### Breaking Down the Logic

1. **Read the slot**:
   ```python
   account = tracker.get_slot("account") or "<missing>"
   ```
   - Gets the slot value
   - Uses `"<missing>"` as default if slot is `None`

2. **Check for placeholder values**:
   ```python
   placeholder_values = ["account number", "user_account_number", "<missing>"]
   if account.lower() in [p.lower() for p in placeholder_values]:
   ```
   - Sometimes the LLM extracts generic text like "account number" instead of the actual number
   - We check if the value is a placeholder

3. **Re-prompt if needed**:
   ```python
   dispatcher.utter_message(response="utter_ask_account")
   return []
   ```
   - If it's a placeholder, ask again
   - Use the `utter_ask_account` response

4. **Use the real value**:
   ```python
   dispatcher.utter_message(text=f"Balance for account {account} is $123.45.")
   ```
   - If we have a real account number, use it

---

### 5.4 Handling Missing Slots

Always check if a slot has a value before using it:

```python
# GOOD: Check for None
account = tracker.get_slot("account")
if account:
    # Use the account
    dispatcher.utter_message(f"Balance: {account}")
else:
    # Handle missing value
    dispatcher.utter_message("I need your account number.")

# ❌ BAD: Don't assume slot has value
account = tracker.get_slot("account")
dispatcher.utter_message(f"Balance: {account}")  # Might be None!
```

---

## Module 6: Training and Testing with Slots

### 6.1 Training with Slots

Training with slots is similar to Level 2, but Rasa now also processes slot definitions.

#### Training Command

```powershell
. .\load_env.ps1
python -m rasa train
```

#### What Happens During Training

Rasa:
1. Reads slot definitions from `domain/basics.yml`
2. Validates slot types and structure
3. Processes flows with `collect:` steps
4. Ensures `utter_ask_*` responses exist for collected slots
5. Creates model with slot information

---

### 6.2 Testing Slot Collection

#### Basic Testing Workflow

1. **Train your bot**: `python -m rasa train`

2. **Start Inspector**: 
   ```powershell
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

3. **Test slot collection**:
   - Type "Check my balance"
   - Bot should ask: "What is your account number?"
   - Type "1234"
   - Bot should respond with balance for account 1234

4. **Test slot persistence**:
   - Type "What's my balance?" again
   - Bot should remember account 1234 (no asking)
   - Bot should respond immediately

5. **Verify Level 2 flows still work**:
   - Type "What are your hours?" → Should work (Level 2)
   - Type "Hello" → Should work (Level 1)

---

### 6.3 Understanding Slot State

In Inspector, you can see slot values in the debug panel:
- **Before collection**: `account: null`
- **After user provides**: `account: "1234"`
- **In action**: Action can read `account: "1234"`

**Key Point**: Slots persist throughout the conversation until the session ends.

---

### 6.4 Common Issues with Slots

#### Issue: Slot Not Collected

**Symptoms**: Bot doesn't ask for slot value

**Possible Causes**:
1. Slot not defined in domain
2. `collect:` step missing or incorrect
3. `utter_ask_*` response missing

**Solutions**:
1. Check `slots:` section in domain
2. Verify `collect: account` step exists in flow
3. Ensure `utter_ask_account` response exists

---

#### Issue: Slot Always None in Action

**Symptoms**: Action reads slot but gets `None`

**Possible Causes**:
1. Slot not collected before action runs
2. User didn't provide value
3. Slot name mismatch

**Solutions**:
1. Ensure `collect:` step comes before action in flow
2. Check user actually provided a value
3. Verify slot name matches exactly (case-sensitive)

---

## Module 7: Putting It All Together

### 7.1 Complete Bot Walkthrough

Let's trace through a complete conversation showing how Levels 1, 2, and 3 work together.

#### Conversation Example

```
[User opens chat - new session starts]

1. pattern_session_start triggers (Level 1)
   ↓
Bot: "Hi! I'm a banking assistant. How can I help you today?"

[User types: "Check my balance"]

2. LLM understands: "User wants to check balance"
   ↓
   Flow: check_balance (Level 3)
   Step 1: collect: account
   ↓
   Bot checks: Does account slot have value? NO
   ↓
   Bot asks: "What is your account number?" (utter_ask_account)
   
[User types: "1234"]

3. Bot stores "1234" in account slot
   ↓
   Flow continues to Step 2: action_check_balance_simple
   ↓
   Action reads account slot: "1234"
   ↓
   Action checks balance for account 1234
   ↓
Bot: "(Demo) Balance for account 1234 is $123.45."

[User types: "What's my balance?"]

4. LLM understands: "User wants balance again"
   ↓
   Flow: check_balance (Level 3)
   Step 1: collect: account
   ↓
   Bot checks: Does account slot have value? YES ("1234")
   ↓
   Flow skips asking, goes directly to Step 2
   ↓
   Action reads account slot: "1234" (remembers from before!)
   ↓
Bot: "(Demo) Balance for account 1234 is $123.45."

[User types: "What are your hours?"]

5. LLM understands: "User wants bank hours"
   ↓
   Flow: hours (Level 2)
   Step: action_bank_hours
   ↓
Bot: "Our bank hours are Monday-Friday 9am-5pm..."
```

**Notice**: The bot seamlessly uses:
- Level 1 responses (greet)
- Level 2 actions (hours)
- Level 3 slots (remembering account number)

---

### 7.2 Your Level 3 Banking Bot: Summary

Congratulations! You've extended your Level 2 banking bot with memory capabilities.

#### Your Complete Bot Structure

**Domain (`domain/basics.yml`)**:
- All Level 1 & 2 responses
- New `utter_ask_account` response
- `slots:` section with `account` slot
- All Level 2 actions
- New `action_check_balance_simple` action

**Flows (`data/basics/`)**:
- All Level 1 & 2 flows
- New `check_balance` flow with slot collection

**Actions (`actions/`)**:
- All Level 2 actions
- New `action_check_balance_simple` that uses slots

#### What Your Bot Can Do Now

Your Level 3 banking bot can:
- Everything Level 1 & 2 could do
- Remember information from the conversation (slots)
- Ask for missing information
- Use remembered information in actions
- Have multi-turn conversations with context

#### What's Still Missing (Coming in Future Levels)

Your Level 3 bot cannot yet:
- ❌ Collect multiple pieces of information in one flow (Level 4: Multiple Slots)
- ❌ Use dynamic tool calling (Level 5: Tools)

But you now have memory - a huge step forward!

---

### 7.3 Best Practices

#### Slot Design

1. **One slot per piece of information**: Don't try to store multiple values in one slot
2. **Descriptive names**: Use clear slot names (`account` not `a`)
3. **Appropriate types**: Use `text` for Level 3 (other types come later)

#### Slot Collection

1. **Always provide descriptions**: Help the LLM understand what to extract
2. **Collect before using**: Make sure `collect:` comes before actions that need the slot
3. **Handle missing values**: Always check if slot is `None` in actions

#### Ask Responses

1. **Clear questions**: Make `utter_ask_*` responses clear and specific
2. **Consistent naming**: Use `utter_ask_<slot_name>` convention
3. **Helpful context**: Tell users why you need the information

---

## Module 8: Assessment and Next Steps

### 8.1 Knowledge Check

#### Question 1: What is a Slot?

a) A predefined bot message  
b) A memory variable that stores conversation information  
c) Custom Python code  
d) A conversation script

**Answer**: b) A memory variable that stores conversation information

**Explanation**: Slots are the bot's memory - they store information the user provides so the bot can remember and use it later.

---

#### Question 2: How Do You Collect a Slot in a Flow?

a) `- action: collect_account`  
b) `- collect: account`  
c) `- slot: account`  
d) `- remember: account`

**Answer**: b) `- collect: account`

**Explanation**: Use `collect: <slot_name>` in a flow step to collect a slot value before continuing.

---

#### Question 3: How Do You Read a Slot in an Action?

a) `slot.get("account")`  
b) `tracker.get_slot("account")`  
c) `domain.get_slot("account")`  
d) `dispatcher.get_slot("account")`

**Answer**: b) `tracker.get_slot("account")`

**Explanation**: The `tracker` parameter in the `run()` method provides access to slots via `tracker.get_slot()`.

---

#### Question 4: What Response is Used When Collecting a Slot?

a) `utter_account`  
b) `utter_ask_account`  
c) `utter_collect_account`  
d) `utter_get_account`

**Answer**: b) `utter_ask_account`

**Explanation**: The convention is `utter_ask_<slot_name>`. When collecting the `account` slot, Rasa uses `utter_ask_account`.

---

### 8.2 What You've Learned

#### Key Concepts

1. **Slots**: Memory variables that store conversation information
2. **Slot Collection**: Using `collect:` in flows to ask for and store information
3. **Reading Slots**: Using `tracker.get_slot()` in actions to access stored values
4. **Ask Responses**: `utter_ask_*` responses used when collecting slots

#### Skills You've Developed

- Can define slots in the domain file
- Can collect slots in flows
- Can read slots in actions
- Can handle missing or placeholder slot values
- Can create multi-turn conversations with memory

---

### 8.3 Limitations of Level 3

#### What Level 3 Cannot Do

1. **Collect Multiple Slots Efficiently**: Can only collect one slot at a time easily
   - Example: "Transfer money" needs amount, recipient, and account
   - Solution: Level 4 adds multiple slot collection

2. **Complex Validation**: Limited validation of slot values
   - Example: Can't easily validate account format
   - Solution: Can be handled in actions, but Level 4 makes it easier

#### When Level 3 is Sufficient

Level 3 is perfect for:
- Single piece of information (account number, name)
- Simple multi-turn conversations
- Remembering one key piece of data

#### When You Need More

Move to Level 4 when you need:
- To collect multiple pieces of information
- Complex forms with multiple fields
- Validating multiple slot values together

---

### 8.4 What's Next: Level 4 Preview

⚠️ **Important: Building on Your Existing Banking Bot**

When you move to Level 4, you will **continue working on the same banking bot** you've built throughout Levels 1, 2, and 3. Level 4 doesn't start from scratch - it builds on what you've already created:

- **Your existing responses** (all Level 1-3 responses) stay
- **Your existing flows** (all Level 1-3 flows) stay
- **Your existing actions** (all Level 2-3 actions) stay
- **Your existing slots** (`account`) stay
- **Level 4 adds**: More slots, more ask responses, actions that use multiple slots, flows that collect multiple slots

**You don't start a new bot** - you extend your existing Level 3 banking bot with multiple slot collection!

---

**Level 4: Multiple Slots** introduces collecting multiple pieces of information.

#### What Multiple Slots Enable

**Example Scenario**: "Transfer $100 to John from account 1234"

- **Level 3**: Can only easily collect one piece of information at a time
- **Level 4**: Can collect:
  - Amount: $100
  - Recipient: John
  - Source account: 1234
  - All in one flow, in order

In Level 4, you'll add:
- Additional slots: `amount`, `recipient`, `account_from`
- Additional ask responses: `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- `action_process_transfer` action that uses all three slots
- `transfer_money` flow that collects all three slots before processing

#### Key Concepts in Level 4

1. **Multiple Slot Collection**: Collecting several slots in sequence
2. **Slot Validation**: Ensuring all required slots have valid values
3. **Complex Conversations**: Handling users providing information in different orders

#### When to Move to Level 4

Move to Level 4 when you need:
- To collect multiple pieces of information before performing an action
- Complex forms or multi-step data collection
- Actions that require multiple data points

**Your Level 3 banking bot is the foundation** - Level 4 adds multiple slot collection on top of it!

---

### 8.5 Course Completion Checklist

Before moving to Level 4, ensure you can:

- Explain what a slot is and how it differs from a response or action
- Define a slot in the domain file
- Create a flow that collects a slot
- Read a slot value in an action
- Handle missing or placeholder slot values
- Understand that Level 3 builds on Level 2 (all Level 2 content remains)

If you can do all of the above, you're ready for Level 4!

---

## Troubleshooting Guide

### Common Issues and Solutions

#### Issue: Slot Not Being Collected

**Symptoms**: Bot doesn't ask for slot value, or slot is always None

**Possible Causes**:
1. Slot not defined in domain
2. `collect:` step missing in flow
3. `utter_ask_*` response missing

**Solutions**:
1. Check `slots:` section exists in `domain/basics.yml`
2. Verify flow has `- collect: account` step
3. Ensure `utter_ask_account` response exists

---

#### Issue: Slot Always None in Action

**Symptoms**: `tracker.get_slot("account")` returns `None` even after user provided value

**Possible Causes**:
1. Slot name mismatch (domain vs. flow vs. action)
2. Slot not collected before action runs
3. User didn't actually provide value

**Solutions**:
1. Verify slot name matches exactly everywhere (case-sensitive)
2. Ensure `collect:` step comes before action in flow
3. Check user actually provided a value (test in Inspector)

---

## Conclusion

Congratulations! You've completed Level 3 and learned how to add memory to your Rasa bot.

### What You Can Do Now

- Remember information from conversations
- Ask for missing information
- Use remembered information in actions
- Create multi-turn conversations with context
- Build more intelligent, personalized bots

### What's Coming Next

- **Level 4**: Collect multiple pieces of information
- **Level 5**: Enable dynamic tool calling

### Keep Learning

- Practice by adding more slots
- Experiment with different slot collection patterns
- Try validating slot values
- Read the Rasa documentation on slots
- Join the Rasa community

**Happy building! 🚀**
