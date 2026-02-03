# Level 4: Multiple Slots - Complete Codio Course Guide

**Complete Course Content and Implementation Guide for Codio Platform**

**Purpose**: This document serves as both:
- **Complete course content** for students (Level 4 tutorial content integrated)
- **Implementation guide** for the Codio team (technical specifications and deployment notes)

---

## For Students (Full Tutorial Content)

**A Complete Guide to Collecting Multiple Pieces of Information**

---

## Table of Contents

0. [Recap: What You Built in Level 3](#module-0-recap-what-you-built-in-level-3)
1. [Introduction to Multiple Slots](#module-1-introduction-to-multiple-slots)
2. [Defining Multiple Slots](#module-2-defining-multiple-slots)
3. [Collecting Multiple Slots in Flows](#module-3-collecting-multiple-slots-in-flows)
4. [Validating Multiple Slots in Actions](#module-4-validating-multiple-slots-in-actions)
5. [Handling Complex Conversations](#module-5-handling-complex-conversations)
6. [Training and Testing with Multiple Slots](#module-6-training-and-testing-with-multiple-slots)
7. [Putting It All Together](#module-7-putting-it-all-together)
8. [Assessment and Next Steps](#module-8-assessment-and-next-steps)

---

## Module 0: Recap - What You Built in Level 3

### 0.1 Your Level 3 Banking Bot

Before we add multiple slots, let's recap what you've already built in Level 3. **All of this remains unchanged** - Level 4 builds on top of it!

#### What You Have from Level 3

**Domain File (`domain/basics.yml`)**:
- ✅ All Level 1 & 2 responses (`utter_greet`, `utter_help`, `utter_contact`)
- ✅ `utter_ask_account` response (Level 3)
- ✅ `slots:` section with `account` slot (Level 3)
- ✅ All Level 2 actions (`action_bank_hours`)
- ✅ `action_check_balance_simple` action (Level 3)

**Flows (`data/basics/`)**:
- ✅ All Level 1 & 2 flows (`greet`, `help`, `contact`, `hours`)
- ✅ `check_balance` flow with slot collection (Level 3)

**Actions (`actions/`)**:
- ✅ All Level 2 actions
- ✅ `action_check_balance_simple` that uses the `account` slot

**System Patterns**: Unchanged from Level 1

**Configuration Files**: Unchanged from Level 3

#### What Level 3 Couldn't Do

Your Level 3 bot could remember one piece of information, but it couldn't:
- ❌ Collect multiple pieces of information efficiently
- ❌ Handle complex forms with multiple fields
- ❌ Process actions that require multiple data points

**Example**: If a user wanted to transfer money, your Level 3 bot couldn't easily collect:
- Transfer amount
- Recipient name
- Source account number

All in one smooth flow.

---

### 0.2 What Level 4 Adds

Level 4 introduces **Multiple Slot Collection** - the ability to collect several pieces of information in sequence before performing an action.

**Your existing Level 3 bot continues to work** - Level 4 adds multiple slot collection on top of it!

#### What's New in Level 4

**New in Domain**:
- Additional slots: `amount`, `recipient`, `account_from`
- Additional ask responses: `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`

**New Files**:
- `actions/action_process_transfer.py` - Action that uses multiple slots

**New Flows**:
- `data/basics/transfer_money.yml` - Flow that collects multiple slots before processing transfer

**Unchanged**:
- All Level 3 responses remain
- All Level 3 flows remain
- All Level 3 actions remain
- All Level 3 slots remain

---

## Module 1: Introduction to Multiple Slots

### 1.1 Why Multiple Slots?

Many real-world tasks require multiple pieces of information:

**Example: Money Transfer**
- Amount: How much to transfer?
- Recipient: Who to transfer to?
- Source Account: Which account to transfer from?

**Example: Booking a Flight**
- Destination: Where to?
- Date: When?
- Passengers: How many?

**Example: Ordering Food**
- Item: What to order?
- Quantity: How many?
- Delivery Address: Where to deliver?

#### Single Slot Limitation

With Level 3, you could collect one piece of information at a time. For complex tasks, you'd need multiple separate flows, which is inefficient.

#### Multiple Slots Solution

Level 4 allows you to collect multiple slots in a single flow, making complex tasks smooth and natural.

---

### 1.2 How Multiple Slot Collection Works

When a flow has multiple `collect:` steps, Rasa collects them in order:

```yaml
steps:
  - collect: amount          # Step 1: Get amount
    description: "transfer amount"
  - collect: recipient       # Step 2: Get recipient
    description: "recipient name or account"
  - collect: account_from    # Step 3: Get source account
    description: "source account number"
  - action: action_process_transfer  # Step 4: Use all collected info
```

**Execution Flow**:
1. Flow starts
2. Collect amount:
   - If empty → Ask: "How much would you like to transfer?"
   - User provides → Store in `amount` slot
3. Collect recipient:
   - If empty → Ask: "Who would you like to transfer money to?"
   - User provides → Store in `recipient` slot
4. Collect account_from:
   - If empty → Ask: "Which account would you like to transfer from?"
   - User provides → Store in `account_from` slot
5. All slots filled → Execute action
6. Action uses all three slots to process transfer

**Key Point**: The bot collects slots **in order**, asking for each one if it's missing.

---

### 1.3 User Experience

#### Natural Conversation Flow

```
User: "I want to transfer money"
Bot: "How much would you like to transfer?"
User: "$100"
Bot: "Who would you like to transfer money to?"
User: "John Doe"
Bot: "Which account would you like to transfer from?"
User: "1234"
Bot: [All slots collected, processes transfer]
Bot: "(Demo) Transfer of $100 from account 1234 to John Doe has been processed successfully."
```

**Notice**: The bot guides the user through collecting all necessary information step by step.

#### User Provides Multiple Values at Once

Users might provide multiple pieces of information in one message:

```
User: "Transfer $100 to John from account 1234"
Bot: [LLM extracts all three values]
Bot: [Stores in slots: amount="100", recipient="John", account_from="1234"]
Bot: [All slots filled, processes transfer immediately]
Bot: "(Demo) Transfer of $100 from account 1234 to John has been processed successfully."
```

**Key Point**: The LLM can extract multiple values from a single message, making the conversation feel natural!

---

## Module 2: Defining Multiple Slots

### 2.1 Adding More Slots to the Domain

In Level 3, you had one slot (`account`). Level 4 adds more slots for the transfer functionality.

#### Domain Structure in Level 4

```yaml
version: "3.1"

slots:                    # ← Multiple slots now
  account:                # ← From Level 3 (unchanged)
    type: text
    # Account number for balance checks
  
  amount:                 # ← NEW in Level 4
    type: text
    # Transfer amount
  
  recipient:              # ← NEW in Level 4
    type: text
    # Recipient name or account for transfers
  
  account_from:           # ← NEW in Level 4
    type: text
    # Source account for transfers

responses:                # ← All previous responses + new ask responses
  # ... existing responses
  utter_ask_account:      # ← From Level 3
    - text: "What is your account number?"
  
  utter_ask_amount:       # ← NEW in Level 4
    - text: "How much would you like to transfer?"
  
  utter_ask_recipient:    # ← NEW in Level 4
    - text: "Who would you like to transfer money to?"
  
  utter_ask_account_from: # ← NEW in Level 4
    - text: "Which account would you like to transfer from?"

actions:                  # ← All previous actions + new action
  - action_bank_hours
  - action_check_balance_simple
  - action_process_transfer  # ← NEW in Level 4
```

---

### 2.2 Step-by-Step: Adding Multiple Slots

**Step 1: Open the Domain File**

1. Navigate to `domain/basics.yml`
2. Open it in your editor

**What you should see**: Your Level 3 content (slots, responses, actions)

---

**Step 2: Add Additional Slots**

1. Find the `slots:` section
2. Add the new slots after `account`:

```yaml
slots:
  account:                # ← Existing from Level 3
    type: text
    # Account number for balance checks
  
  amount:                 # ← Add this
    type: text
    # Transfer amount
  
  recipient:              # ← Add this
    type: text
    # Recipient name or account for transfers
  
  account_from:           # ← Add this
    type: text
    # Source account for transfers
```

⚠️ **Important**:
- Each slot is at the same indentation level
- Use 2 spaces for indentation
- Add comments to explain what each slot stores

---

**Step 3: Add Ask Responses**

For each new slot, add a corresponding `utter_ask_*` response:

```yaml
responses:
  # ... existing responses including utter_ask_account
  
  utter_ask_amount:       # ← Add this
    - text: "How much would you like to transfer?"
      metadata:
        rephrase: True
  
  utter_ask_recipient:    # ← Add this
    - text: "Who would you like to transfer money to?"
      metadata:
        rephrase: True
  
  utter_ask_account_from: # ← Add this
    - text: "Which account would you like to transfer from?"
      metadata:
        rephrase: True
```

**Naming convention**: `utter_ask_<slot_name>`
- Slot: `amount` → Response: `utter_ask_amount`
- Slot: `recipient` → Response: `utter_ask_recipient`
- Slot: `account_from` → Response: `utter_ask_account_from`

---

**Step 4: Verify Your Domain**

Check:
- ✅ All slots are defined (`account`, `amount`, `recipient`, `account_from`)
- ✅ All ask responses exist (`utter_ask_account`, `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`)
- ✅ All Level 3 responses remain
- ✅ All Level 3 actions remain
- ✅ YAML syntax is correct

---

## Module 3: Collecting Multiple Slots in Flows

### 3.1 Creating a Flow with Multiple Collect Steps

Let's create the `transfer_money.yml` flow that collects multiple slots.

#### Step-by-Step Tutorial

**Step 1: Navigate to Data Folder**

1. Go to `data/basics/` folder
2. You should see your Level 3 flows

---

**Step 2: Create the Transfer Money Flow**

1. Create a new file: `data/basics/transfer_money.yml`
2. Add the flow structure:

```yaml
flows:
  transfer_money:
    name: transfer money
    description: |
      Demonstrates collecting multiple slots before executing an action.
      The bot will collect: amount, recipient, and source account.
      Then it will process the transfer.
    steps:
      - collect: amount
        description: "transfer amount"
      - collect: recipient
        description: "recipient name or account"
      - collect: account_from
        description: "source account number"
      - action: action_process_transfer
```

**Complete file**:
```yaml
flows:
  transfer_money:
    name: transfer money
    description: |
      Demonstrates collecting multiple slots before executing an action.
      The bot will collect: amount, recipient, and source account.
      Then it will process the transfer.
    steps:
      - collect: amount
        description: "transfer amount"
      - collect: recipient
        description: "recipient name or account"
      - collect: account_from
        description: "source account number"
      - action: action_process_transfer
```

---

**Step 3: Understanding the Flow**

**Flow execution**:
1. User says "Transfer money" or "I want to make a transfer"
2. LLM matches to `transfer_money` flow
3. Step 1: `collect: amount`
   - Bot checks: Does `amount` slot have value?
   - **No** → Bot asks: "How much would you like to transfer?"
   - User provides: "$100"
   - Bot stores "100" in `amount` slot
4. Step 2: `collect: recipient`
   - Bot checks: Does `recipient` slot have value?
   - **No** → Bot asks: "Who would you like to transfer money to?"
   - User provides: "John Doe"
   - Bot stores "John Doe" in `recipient` slot
5. Step 3: `collect: account_from`
   - Bot checks: Does `account_from` slot have value?
   - **No** → Bot asks: "Which account would you like to transfer from?"
   - User provides: "1234"
   - Bot stores "1234" in `account_from` slot
6. Step 4: `action: action_process_transfer`
   - All slots are filled
   - Action reads all three slots
   - Action processes the transfer
   - Action responds with confirmation

**If user provides all info at once**:
- User: "Transfer $100 to John from account 1234"
- LLM extracts all three values
- Bot stores them in slots immediately
- Flow skips asking steps
- Goes directly to action

---

**Step 4: Verify the Flow**

Check:
- ✅ File is in `data/basics/` folder
- ✅ Flow has `name:`, `description:`, and `steps:`
- ✅ All three `collect:` steps exist
- ✅ Action name matches registered action
- ✅ YAML syntax is correct

---

### 3.2 Collection Order Matters

The order of `collect:` steps determines the order the bot asks for information:

```yaml
steps:
  - collect: amount        # Asked first
  - collect: recipient    # Asked second
  - collect: account_from # Asked third
```

**Why order matters**:
- Users expect logical flow (amount → recipient → account)
- Some information might depend on previous information
- Natural conversation flow

**Best practice**: Order slots logically based on the task flow.

---

### 3.3 Partial Information

Users might provide some information but not all:

```
User: "Transfer $100"
Bot: [Stores amount="100"]
Bot: "Who would you like to transfer money to?"
User: "John"
Bot: [Stores recipient="John"]
Bot: "Which account would you like to transfer from?"
User: "1234"
Bot: [Stores account_from="1234", processes transfer]
```

**Key Point**: The bot only asks for missing information. If the user provides some values, those slots are skipped.

---

## Module 4: Validating Multiple Slots in Actions

### 4.1 Why Validate Multiple Slots?

When an action uses multiple slots, you need to ensure:
1. All required slots have values
2. Values are not placeholders
3. Values are in the correct format (if needed)

---

### 4.2 Creating an Action That Uses Multiple Slots

Let's examine `action_process_transfer.py` to see how it validates multiple slots.

#### Complete Action File

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransfer(Action):
    """A custom action that processes a money transfer using multiple slots.
    
    This demonstrates:
    - Reading multiple slots from the tracker
    - Validating slot values
    - Using all collected information to perform an action
    """

    def name(self) -> Text:
        return "action_process_transfer"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Read all the slots we need
        amount = tracker.get_slot("amount")
        recipient = tracker.get_slot("recipient")
        account_from = tracker.get_slot("account_from")
        
        # Validate that we have all required information
        if not amount or not recipient or not account_from:
            dispatcher.utter_message(
                text="I'm missing some information. Please provide amount, recipient, and source account."
            )
            return []
        
        # Check for placeholder values
        placeholder_values = ["amount", "recipient", "account number", "user_account_number"]
        if (amount.lower() in [p.lower() for p in placeholder_values] or
            recipient.lower() in [p.lower() for p in placeholder_values] or
            account_from.lower() in [p.lower() for p in placeholder_values]):
            dispatcher.utter_message(
                text="I need the actual values, not placeholders. Please provide the real amount, recipient name, and account number."
            )
            return []
        
        # Process the transfer (demo - no real transfer happening)
        dispatcher.utter_message(
            text=f"(Demo) Transfer of ${amount} from account {account_from} to {recipient} has been processed successfully."
        )
        return []
```

#### Breaking Down the Validation Logic

1. **Read all slots**:
   ```python
   amount = tracker.get_slot("amount")
   recipient = tracker.get_slot("recipient")
   account_from = tracker.get_slot("account_from")
   ```
   - Gets all three slot values

2. **Check for missing values**:
   ```python
   if not amount or not recipient or not account_from:
       dispatcher.utter_message("I'm missing some information...")
       return []
   ```
   - Ensures all slots have values
   - If any are missing, ask for them and return early

3. **Check for placeholder values**:
   ```python
   placeholder_values = ["amount", "recipient", "account number", "user_account_number"]
   if (amount.lower() in [p.lower() for p in placeholder_values] or ...):
       dispatcher.utter_message("I need the actual values...")
       return []
   ```
   - Sometimes LLM extracts generic text instead of actual values
   - Check if any slot has a placeholder value
   - If so, ask for real values

4. **Use all values**:
   ```python
   dispatcher.utter_message(
       text=f"Transfer of ${amount} from account {account_from} to {recipient}..."
   )
   ```
   - All slots validated
   - Use all three values in the response

---

### 4.3 Validation Best Practices

#### Always Check for None

```python
# ✅ GOOD: Check all slots
if not amount or not recipient or not account_from:
    # Handle missing values
    pass

# ❌ BAD: Assume slots have values
dispatcher.utter_message(f"Transfer ${amount}...")  # Might be None!
```

#### Check for Placeholders

```python
# ✅ GOOD: Validate placeholder values
placeholder_values = ["amount", "recipient", "account number"]
if amount.lower() in [p.lower() for p in placeholder_values]:
    # Handle placeholder
    pass
```

#### Provide Helpful Error Messages

```python
# ✅ GOOD: Specific error message
if not amount:
    dispatcher.utter_message("I need to know how much you want to transfer.")

# ❌ BAD: Vague error message
if not amount:
    dispatcher.utter_message("Error.")  # Not helpful!
```

---

## Module 5: Handling Complex Conversations

### 5.1 Users Providing Information Out of Order

Users might provide information in different orders:

**Scenario 1: All at once**
```
User: "Transfer $100 to John from account 1234"
Bot: [Extracts all, processes immediately]
```

**Scenario 2: Partial information**
```
User: "Transfer $100 to John"
Bot: [Stores amount and recipient]
Bot: "Which account would you like to transfer from?"
User: "1234"
Bot: [Processes transfer]
```

**Scenario 3: Out of order**
```
User: "Transfer from account 1234"
Bot: [Stores account_from]
Bot: "How much would you like to transfer?"
User: "$100"
Bot: [Stores amount]
Bot: "Who would you like to transfer money to?"
User: "John"
Bot: [Processes transfer]
```

**Key Point**: The LLM and slot collection handle all these scenarios automatically!

---

### 5.2 Handling User Corrections

Users might want to change information:

```
User: "Transfer $100 to John"
Bot: "Which account would you like to transfer from?"
User: "Actually, make it $200"  # Changing amount
Bot: [Updates amount slot to "200"]
Bot: "Which account would you like to transfer from?"
```

**How it works**: The LLM can extract updated values and the bot updates the slot.

---

### 5.3 Flow Descriptions for Multiple Slots

Good flow descriptions help the LLM understand when to trigger the flow:

```yaml
description: |
  Demonstrates collecting multiple slots before executing an action.
  The bot will collect: amount, recipient, and source account.
  Then it will process the transfer.
```

**Why this works**:
- Mentions "collecting multiple slots"
- Lists what information is needed
- Explains the purpose (process transfer)

**Bad description**:
```yaml
description: Transfer money  # Too vague - doesn't mention multiple slots
```

---

## Module 6: Training and Testing with Multiple Slots

### 6.1 Training with Multiple Slots

Training is the same as previous levels, but Rasa now processes multiple slot definitions and collection steps.

#### Training Command

```powershell
. .\load_env.ps1
python -m rasa train
```

#### What Happens During Training

Rasa:
1. Reads all slot definitions (including new ones)
2. Validates all `utter_ask_*` responses exist
3. Processes flows with multiple `collect:` steps
4. Ensures actions that use slots are properly registered
5. Creates model with all slot information

---

### 6.2 Testing Multiple Slot Collection

#### Basic Testing Workflow

1. **Train your bot**: `python -m rasa train`

2. **Start Inspector**: 
   ```powershell
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

3. **Test sequential collection**:
   - Type "Transfer money"
   - Bot should ask: "How much would you like to transfer?"
   - Type "$100"
   - Bot should ask: "Who would you like to transfer money to?"
   - Type "John"
   - Bot should ask: "Which account would you like to transfer from?"
   - Type "1234"
   - Bot should process transfer and confirm

4. **Test all-at-once collection**:
   - Type "Transfer $100 to John from account 1234"
   - Bot should extract all values
   - Bot should process transfer immediately (no asking)

5. **Test partial information**:
   - Type "Transfer $100"
   - Bot should ask for recipient and account
   - Provide them
   - Bot should process transfer

6. **Verify previous levels still work**:
   - Type "Check my balance" → Should work (Level 3)
   - Type "What are your hours?" → Should work (Level 2)
   - Type "Hello" → Should work (Level 1)

---

### 6.3 Understanding Slot State

In Inspector debug panel, you can see all slot values:
- `amount: "100"`
- `recipient: "John"`
- `account_from: "1234"`
- `account: "1234"` (from Level 3)

**Key Point**: All slots persist throughout the conversation. The bot remembers all collected information.

---

### 6.4 Common Issues with Multiple Slots

#### Issue: Not All Slots Collected

**Symptoms**: Action runs but some slots are None

**Possible Causes**:
1. Missing `collect:` step in flow
2. User didn't provide all information
3. LLM didn't extract all values

**Solutions**:
1. Verify all `collect:` steps exist in flow
2. Check flow description mentions all required information
3. Test with explicit values to ensure extraction works

---

#### Issue: Wrong Collection Order

**Symptoms**: Bot asks for information in confusing order

**Possible Causes**:
1. `collect:` steps in wrong order
2. Flow description doesn't explain the sequence

**Solutions**:
1. Reorder `collect:` steps logically
2. Update flow description to explain the sequence

---

## Module 7: Putting It All Together

### 7.1 Complete Bot Walkthrough

Let's trace through a complete conversation showing how all levels work together.

#### Conversation Example

```
[User opens chat - new session starts]

1. pattern_session_start triggers (Level 1)
   ↓
Bot: "Hi! I'm a banking assistant. How can I help you today?"

[User types: "I want to transfer money"]

2. LLM understands: "User wants to transfer money"
   ↓
   Flow: transfer_money (Level 4)
   Step 1: collect: amount
   ↓
   Bot asks: "How much would you like to transfer?"

[User types: "$100"]

3. Bot stores "100" in amount slot
   ↓
   Flow continues to Step 2: collect: recipient
   ↓
   Bot asks: "Who would you like to transfer money to?"

[User types: "John Doe"]

4. Bot stores "John Doe" in recipient slot
   ↓
   Flow continues to Step 3: collect: account_from
   ↓
   Bot asks: "Which account would you like to transfer from?"

[User types: "1234"]

5. Bot stores "1234" in account_from slot
   ↓
   Flow continues to Step 4: action_process_transfer
   ↓
   Action reads all three slots: amount="100", recipient="John Doe", account_from="1234"
   ↓
   Action validates all slots have values
   ↓
   Action processes transfer
   ↓
Bot: "(Demo) Transfer of $100 from account 1234 to John Doe has been processed successfully."

[User types: "Check my balance"]

6. LLM understands: "User wants balance"
   ↓
   Flow: check_balance (Level 3)
   Step 1: collect: account
   ↓
   Bot checks: Does account slot have value? (We have account_from="1234", but not account)
   ↓
   Bot asks: "What is your account number?"

[User types: "1234"]

7. Bot stores "1234" in account slot
   ↓
   Flow continues to action_check_balance_simple
   ↓
   Action reads account slot: "1234"
   ↓
Bot: "(Demo) Balance for account 1234 is $123.45."
```

**Notice**: The bot seamlessly uses:
- Level 1 responses (greet)
- Level 2 actions (hours)
- Level 3 single slot collection (check_balance)
- Level 4 multiple slot collection (transfer_money)

---

### 7.2 Your Level 4 Banking Bot: Summary

Congratulations! You've extended your Level 3 banking bot with multiple slot collection capabilities.

#### Your Complete Bot Structure

**Domain (`domain/basics.yml`)**:
- ✅ All Level 1-3 responses
- ✅ New ask responses: `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- ✅ All slots: `account` (Level 3), `amount`, `recipient`, `account_from` (Level 4)
- ✅ All Level 1-3 actions
- ✅ New `action_process_transfer` action

**Flows (`data/basics/`)**:
- ✅ All Level 1-3 flows
- ✅ New `transfer_money` flow with multiple slot collection

**Actions (`actions/`)**:
- ✅ All Level 1-3 actions
- ✅ New `action_process_transfer` that uses multiple slots

#### What Your Bot Can Do Now

Your Level 4 banking bot can:
- ✅ Everything Level 1-3 could do
- ✅ Collect multiple pieces of information in one flow
- ✅ Handle complex forms with multiple fields
- ✅ Process actions that require multiple data points
- ✅ Guide users through multi-step processes naturally

#### What's Still Missing (Coming in Level 5)

Your Level 4 bot cannot yet:
- ❌ Use dynamic tool calling (Level 5: Tools)

But you now have comprehensive data collection capabilities!

---

### 7.3 Best Practices

#### Slot Design

1. **One slot per piece of information**: Don't try to store multiple values in one slot
2. **Logical grouping**: Group related slots together (e.g., all transfer-related slots)
3. **Clear names**: Use descriptive slot names

#### Collection Order

1. **Logical sequence**: Order slots in a way that makes sense to users
2. **Dependencies first**: If one slot depends on another, collect the dependency first
3. **Most important first**: Collect the most critical information first

#### Validation

1. **Validate all slots**: Always check all required slots have values
2. **Check for placeholders**: Validate that values aren't generic placeholders
3. **Helpful errors**: Provide clear error messages when validation fails

---

## Module 8: Assessment and Next Steps

### 8.1 Knowledge Check

#### Question 1: How Do You Collect Multiple Slots?

a) Use multiple `collect:` steps in sequence  
b) Use `collect: slot1, slot2, slot3`  
c) Define multiple slots in one `collect:` step  
d) Slots are collected automatically

**Answer**: a) Use multiple `collect:` steps in sequence

**Explanation**: Each slot gets its own `collect:` step. They execute in order, asking for each slot if it's empty.

---

#### Question 2: What Happens If a User Provides All Information at Once?

a) The bot ignores it and asks anyway  
b) The bot extracts all values and skips asking  
c) The bot only uses the first value  
d) The bot asks for confirmation

**Answer**: b) The bot extracts all values and skips asking

**Explanation**: The LLM can extract multiple values from a single message. If all slots are filled, the bot skips the asking steps and goes directly to the action.

---

#### Question 3: How Do You Validate Multiple Slots in an Action?

a) Check each slot individually with `if` statements  
b) Slots are automatically validated  
c) Use a validation function  
d) Validation isn't necessary

**Answer**: a) Check each slot individually with `if` statements

**Explanation**: You need to explicitly check each slot value in your action code to ensure all required information is present and valid.

---

### 8.2 What You've Learned

#### Key Concepts

1. **Multiple Slots**: Defining and using several slots in one flow
2. **Sequential Collection**: Collecting slots one after another
3. **Slot Validation**: Ensuring all required slots have valid values
4. **Complex Conversations**: Handling users providing information in different ways

#### Skills You've Developed

- ✅ Can define multiple slots in the domain
- ✅ Can create flows that collect multiple slots
- ✅ Can validate multiple slots in actions
- ✅ Can handle complex multi-step conversations
- ✅ Can guide users through data collection naturally

---

### 8.3 Limitations of Level 4

#### What Level 4 Cannot Do

1. **Dynamic Tool Selection**: Can't let the LLM dynamically choose which functions to call
   - Example: LLM can't decide to call different tools based on context
   - Solution: Level 5 adds tool calling

#### When Level 4 is Sufficient

Level 4 is perfect for:
- ✅ Collecting multiple pieces of information
- ✅ Complex forms and multi-step processes
- ✅ Actions that require multiple data points
- ✅ Structured workflows with clear steps

#### When You Need More

Move to Level 5 when you need:
- Dynamic function selection by the LLM
- Flexible operations that adapt to context
- Complex branching scenarios

---

### 8.4 What's Next: Level 5 Preview

⚠️ **Important: Building on Your Existing Banking Bot**

When you move to Level 5, you will **continue working on the same banking bot** you've built throughout Levels 1-4. Level 5 doesn't start from scratch - it builds on what you've already created:

- **Your existing responses** (all Level 1-4 responses) stay
- **Your existing flows** (all Level 1-4 flows) stay
- **Your existing actions** (all Level 2-4 actions) stay
- **Your existing slots** (all Level 3-4 slots) stay
- **Level 5 adds**: Tools (dynamic functions), tools registration, actions that work with tools, flows that use tool calling

**You don't start a new bot** - you extend your existing Level 4 banking bot with dynamic tool calling!

---

**Level 5: Tool Calling** introduces dynamic function selection by the LLM.

#### What Tools Enable

**Example Scenario**: User asks complex questions that require multiple operations

- **Level 4**: Actions are explicitly called in flows (predictable)
- **Level 5**: Tools are dynamically selected by the LLM (flexible)

In Level 5, you'll add:
- `tools/` folder with `banking_tools.py` containing tool functions
- Tools registration in `endpoints.yml`
- `action_process_transfer_with_tools` action that works with tools
- `transfer_money_tools` flow that uses tool calling

#### Key Concepts in Level 5

1. **Tools**: Python functions the LLM can call dynamically
2. **Tool Registration**: Telling Rasa where to find tools
3. **Dynamic Selection**: LLM decides which tools to call based on context
4. **Tools vs. Actions**: When to use each

#### When to Move to Level 5

Move to Level 5 when you need:
- The LLM to dynamically choose which operations to perform
- Flexible, context-aware function calling
- Complex scenarios where the flow depends on dynamic conditions

**Your Level 4 banking bot is the foundation** - Level 5 adds dynamic tool calling on top of it!

---

### 8.5 Course Completion Checklist

Before moving to Level 5, ensure you can:

- [ ] Define multiple slots in the domain
- [ ] Create flows that collect multiple slots in sequence
- [ ] Validate multiple slots in actions
- [ ] Handle users providing information in different orders
- [ ] Understand that Level 4 builds on Level 3 (all Level 3 content remains)

If you can check all these boxes, you're ready for Level 5!

---

## Troubleshooting Guide

### Common Issues and Solutions

#### Issue: Not All Slots Being Collected

**Symptoms**: Some slots remain None even after user provides information

**Possible Causes**:
1. Missing `collect:` step for that slot
2. LLM didn't extract the value
3. Slot name mismatch

**Solutions**:
1. Verify all required slots have `collect:` steps
2. Check flow description mentions all required information
3. Ensure slot names match exactly everywhere

---

#### Issue: Wrong Collection Order

**Symptoms**: Bot asks for information in confusing order

**Possible Causes**:
1. `collect:` steps in wrong order
2. Flow description doesn't explain sequence

**Solutions**:
1. Reorder `collect:` steps logically
2. Update flow description to clarify the sequence

---

## Conclusion

Congratulations! You've completed Level 4 and learned how to collect multiple pieces of information.

### What You Can Do Now

- Collect multiple pieces of information in one flow
- Handle complex forms and multi-step processes
- Validate multiple slot values
- Guide users through data collection naturally
- Build sophisticated conversational interfaces

### What's Coming Next

- **Level 5**: Enable dynamic tool calling for flexible, context-aware operations

### Keep Learning

- Practice by adding more slots and flows
- Experiment with different collection patterns
- Try validating slot formats (numbers, dates, etc.)
- Read the Rasa documentation on slots
- Join the Rasa community

**Happy building! 🚀**

---

## Implementation Overview for Codio Team

### Executive Summary

This document is a **combined student course + Codio implementation guide** for **Level 4: Multiple Slots**.

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
- Validate required new artifacts for Level 4 exist (e.g., new flows/actions/tools)
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


