# Level 2: Simple Actions - Complete Codio Course Guide

**Complete Course Content and Implementation Guide for Codio Platform**

**Purpose**: This document serves as both:
- **Complete course content** for students (Level 2 tutorial content integrated)
- **Implementation guide** for the Codio team (technical specifications and deployment notes)

---

## For Students (Full Tutorial Content)

**A Complete Guide to Adding Custom Python Code to Your Banking Agent**

---

## Table of Contents

0. [Recap - What you built in Level 1](#unit-0-recap-what-you-built-in-level-1)
1. [Introduction to Actions](#unit-1-introduction-to-actions)
2. [Understanding the Action Class](#unit-2-understanding-the-action-class)
3. [Creating Your First Action](#unit-3-creating-your-first-action)
4. [Registering Actions in the Domain](#unit-4-registering-actions-in-the-domain)
5. [Using Actions in Flows](#unit-5-using-actions-in-flows)
6. [Training and Testing with Actions](#unit-6-training-and-testing-with-actions)
7. [Putting It All Together](#unit-7-putting-it-all-together)
8. [Assessment and Next Steps](#unit-8-assessment-and-next-steps)

---

## Unit 0: Recap - What you built in Level 1

Before we add actions, let's recap what you've already built in Level 1. **All of this remains unchanged** — Level 2 builds on top of it!

#### What You Have from Level 1

**Domain File (`domain/basics.yml`)**:
- `utter_greet` - Greets users as a banking assistant
- `utter_help` - Lists banking services (balance, transfers, hours, contact)
- `utter_contact` - Provides bank contact information
- `utter_goodbye` - Says goodbye when the user ends the conversation

**Flows (`data/basics/`)**:
- `greet.yml` - Greets users when they start a conversation
- `help.yml` - Explains what the agent can help with
- `contact.yml` - Provides contact information for the bank
- `goodbye.yml` - Says goodbye when the user ends the conversation

**System Patterns (`data/system/patterns/patterns.yml`)**:
- `pattern_session_start` - Automatically greets users when conversation begins
- `pattern_completed` - Handles flow completion

**Configuration Files**:
- `config.yml` - Agent configuration (pipeline, policies)
- `credentials.yml` - Connection settings
- `endpoints.yml` - Action endpoints and LLM configuration

#### What Level 1 Couldn't Do

Your Level 1 agent was limited to **static responses** - predefined text that never changes. It couldn't:
- ❌ Execute custom Python code
- ❌ Perform calculations
- ❌ Access databases or APIs
- ❌ Return dynamic responses based on conditions
- ❌ Process data or make decisions

**Example**: If a user asked "What are your bank hours?", your Level 1 agent would need a static `utter_hours` response. It couldn't check the current day or calculate if the bank is currently open.

#### What's new in Level 2

Level 2 introduces **Actions** — custom Python code that your agent can execute. This enables:

- Dynamic responses based on calculations
- Data processing and logic
- Integration with external systems
- Custom business logic

**Your existing Level 1 agent continues to work** — Level 2 adds actions on top of it!

**Already in the project before Lab 3.1** (starter):
- `actions/` folder, `actions/__init__.py`, and `actions/action_bank_hours.py` — example action you study in Units 2–3 (the domain does not list it until **Lab 4.1**).
- No `action_holiday_hours.py` yet, no `actions:` section in `domain/basics.yml`, and no `hours.yml` / `holiday_hours.yml` — you add those in the labs below.

**What you'll build**: In **Unit 3 / Lab 3.1** you'll create your own action (**action_holiday_hours**) that uses the current date—if today is a holiday it says we're closed today, otherwise it returns the general holiday schedule. In **Lab 4.1** you'll register both actions in the domain. In **Lab 5.1** you'll create **`hours.yml`** (for the example action) and **`holiday_hours.yml`** (for your action).

**Modified Files** (as you complete the labs):
- `domain/basics.yml` — You'll add an `actions:` section and list both the example action and your action (Lab 4.1)
- `data/basics/hours.yml` — Example flow for `action_bank_hours` (Lab 5.1)
- `data/basics/holiday_hours.yml` — Flow for `action_holiday_hours` (Lab 5.1)

**Unchanged Files**:
- All Level 1 responses remain
- All Level 1 flows remain
- **Configuration** — Same **tutorial LLM** setup as Level 1 (`SearchReadyLLMCommandGenerator`, `rasa_command_generation_model`, `flow_retrieval.active: false` in `config.yml`; `https://tutorial-llm.rasa.ai` in `endpoints.yml`). Level 2’s `endpoints.yml` also defines **`action_endpoint`** so Rasa loads custom actions from the **`actions`** package.

See **`LEVEL2_STARTER_STATE.md`** for a full checklist.

---

## Unit 1: Introduction to Actions

### 1.1 What is an Action?

An **action** is custom Python code that your agent can execute. Actions allow your agent to do more than just say predefined text - they can perform calculations, access databases, call APIs, and execute any Python logic you write.

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

 **Use actions when you need**:
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
Agent responds with dynamic message
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

## Unit 2: Understanding the Action Class

### 2.1 The Action Class Deep Dive

Let's examine the actual `action_bank_hours.py` file to understand how actions work.

**Why an action (not an utter)?** This action returns a *different* message depending on the current day—Saturday, Sunday, or weekday. That requires Python logic and `datetime`. A simple `utter_*` response can't change based on when the user asks, so we need an action.

#### Complete Action File

```python
from datetime import datetime
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A custom action that returns bank hours based on the current day.
    
    Uses datetime to tailor the message—this can't be done with a simple
    utter response because the message changes depending on when the user asks.
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
        
        Returns different messages based on the current day of the week.
        """
        weekday = datetime.now().weekday()  # 0=Monday, 5=Saturday, 6=Sunday

        if weekday == 6:  # Sunday
            message = "Today is Sunday—we're closed."
        elif weekday == 5:  # Saturday
            message = "Today is Saturday—we're open 10am-2pm."
        else:  # Monday–Friday
            message = (
                "Our bank hours are Monday-Friday 9am-5pm, "
                "Saturday 10am-2pm. We're closed on Sundays."
            )

        dispatcher.utter_message(text=message)
        return []
```

#### Breaking Down Each Component

1. **Imports**:
   ```python
   from datetime import datetime
   from rasa_sdk import Action, Tracker
   from rasa_sdk.executor import CollectingDispatcher
   ```
   - `datetime` - Used to get the current day of the week
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

5. **Conditional Logic**:
   ```python
   weekday = datetime.now().weekday()  # 0=Monday, 5=Saturday, 6=Sunday
   if weekday == 6:  # Sunday
       message = "Today is Sunday—we're closed."
   elif weekday == 5:  # Saturday
       message = "Today is Saturday—we're open 10am-2pm."
   else:  # Monday–Friday
       message = "Our bank hours are..."
   ```
   - `datetime.now().weekday()` returns the current day (0=Monday through 6=Sunday)
   - Different messages for different days—this is why we need an action, not a static response

6. **Sending Messages**:
   ```python
   dispatcher.utter_message(text=message)
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

The `domain` contains your agent's configuration:

```python
# Access domain (rarely needed)
responses = domain.get("responses", {})
```

For Level 2, you typically don't need to access the domain directly.

---

## Unit 3: Creating Your First Action

### Lab 3.1 (Codio guide): Create Your Own Action

The guide no longer has a separate “3.1 Step-by-Step” page. Students use **Unit 2.1** (*The Action Class Deep Dive*) for the full **`action_bank_hours.py`** example. **Lab 3.1** is the first page in Unit 3: **Fill in the blanks** for **`action_holiday_hours`**, paste into **`level2/actions/action_holiday_hours.py`**, then the **Code Test**—same **fill-in → paste → grader** flow as Level 4 Lab 3.1.

**Codio taskIds / grader:** **`fill-in-the-blanks-201030010`** (5 pts) → **`code-output-compare-2266471391`** (8 pts). The Code Test runs **`bash …/level2_graders/lab_3.2_grader.sh`** (on-disk name; script banner says Lab 3.1).

**When creating `action_holiday_hours`, verify**: Imports (`datetime`, Rasa SDK, typing as needed); class **`ActionHolidayHours(Action)`**; **`name()`** returns **`action_holiday_hours`**; **`run()`** uses **`datetime.now()`** and date checks for holiday messages; **`dispatcher.utter_message(text=message)`**; **`return []`**.

**Common mistakes**: Forgetting to inherit from **`Action`**; wrong **`name()`** return; forgetting **`return []`** from **`run()`**.

**Execution summary (Codio guide):** The seven-step “when Rasa runs your action” list and key point appear at the **end of Lab 3.1** (no separate Unit 3.2 page).

---

## Unit 4: Registering Actions in the Domain

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
- `actions:` section exists
- Action name matches `name()` return value exactly
- Proper YAML syntax (indentation, dashes)
- No typos in action name

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

## Unit 5: Using Actions in Flows

### 5.1 Actions vs. Responses in Flows

Now that your actions are registered in the domain (Lab 4.1), you need flows that call them: the example **hours** flow and your **holiday_hours** flow. In Level 1, flows used only `utter_*` responses. In Level 2, flows can also call `action_*` custom actions.

#### Level 1 flow (response)

```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet  # ← Uses a response
```

#### Level 2 flow (action)

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours  # ← Uses an action
```

**What changes:** names starting with `utter_` refer to predefined text in the domain; names starting with `action_` refer to Python in `actions/`. In both cases you still write `- action:` under `steps:`—Rasa decides which kind of step it is from the name.

#### Mixing responses and actions in one flow

The same flow can chain both kinds of step. For example, you might run an action for dynamic content, then a response for static text:

```yaml
flows:
  hours_and_contact:
    name: hours and contact
    description: Tell the user bank hours and provide contact information.
    steps:
      - action: action_bank_hours      # ← Action (custom code)
      - action: utter_contact          # ← Response (predefined text)
```

**Execution order**

1. **`action_bank_hours`** runs first (dynamic hours message).
2. **`utter_contact`** runs next (static contact text).

---

Flow creation (`hours.yml`, `holiday_hours.yml`) is covered in **Lab 5.1**; see the lab guide for the full step-by-step.

---

## Unit 6: Training, Testing, and Level 2 Wrap-Up

**Codio guide:** Student-facing pages include **Lab 6.1** (`Lab-6-1--Training-and-Testing-with-Actions-7710.md`), **6.2**, **Lab 6.2**, **6.3**, **6.4** *See it all together* (`6-4-Level-2-Wrap-Up-d798.md` — integration, practices, knowledge check), and **6.5** *Before you continue* (`6-5-Core-Ideas-and-Level-3-Readiness-b91a.md` — short checkpoint; handoff to Level 3 Unit 0). The subsections below are the full instructor reference (including local PowerShell).

### 6.1 Training with Actions

Training with actions is the same as Level 1, but Rasa now also processes your action files.

#### Training Command

```powershell
# Make sure environment variables are loaded
. .\load_env.ps1

# Train the agent
python -m rasa train
```

#### What Happens During Training

After **Labs 3.1–5.1** (both actions registered; `hours.yml` and `holiday_hours.yml` exist), when you run `rasa train`, Rasa:

1. **Reads all flows** from `data/` folder
   - Finds `hours.yml` with `action_bank_hours` and `holiday_hours.yml` with `action_holiday_hours`
   - Processes all Level 1 flows (unchanged)

2. **Reads the domain** from `domain/` folder
   - Loads all responses (from Level 1)
   - Loads all actions registered under `actions:` (e.g. `action_bank_hours`, `action_holiday_hours`)
   - Verifies registered actions exist

3. **Validates actions**:
   - Checks that each registered action has a matching file under `actions/`
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
1. Make sure Rasa Pro is installed: `python -m pip install rasa-pro==3.16.3`
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

### 6.3 Testing and Debugging Your Action

#### Basic Testing Workflow

1. **Train your agent**: `python -m rasa train`

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

#### Check Debug Output

When testing in Inspector, check the debug panel: which flow was triggered, which action was called, and whether the action completed successfully.

#### Common Issues

1. **Action doesn't trigger**: Flow description matches user intent; action registered in domain; action file exists under `actions/`.
2. **Action executes but no message**: `dispatcher.utter_message()` is called; check for Python errors in the action.
3. **Python errors in action**: Syntax, imports, and method names.

### 6.4 See it all together

Student-facing page (`6-4-Level-2-Wrap-Up-d798`; Codio title **6.4 See it all together**): integration walkthrough, project map, best practices, **five multiple-choice Check It! assessments** (`multiple-choice-1208100001`–`0005`). Ends with a pointer to **6.5** (*Before you continue*).

#### Conversation example

Include session start, `hours` + `action_bank_hours`, `holiday_hours` + `action_holiday_hours`, and a Level 1 static flow (e.g. `contact`). Fenced `text` trace; dynamic agent lines per course.

#### Practices and knowledge check

Align **6.4** prose with `Level2_Unit6_Content_6.4_Level-2-Wrap-Up.md` / `.guides/.../6-4-Level-2-Wrap-Up-d798.md`.

### 6.5 Before you continue

Student-facing page (`6-5-Core-Ideas-and-Level-3-Readiness-b91a`; Codio title **6.5 Before you continue**): short Level 2 skills recap, one paragraph on limits (slots vs not), readiness bullets, and a pointer to **Level 3 Unit 0** for the full agent recap and Level 3 roadmap (avoid duplicating **0-1** / **0-2**). Align with `Level2_Unit6_Content_6.5_Core-Ideas-and-Level-3-Readiness.md` / `.guides/.../6-5-Core-Ideas-and-Level-3-Readiness-b91a.md`.

**Former Unit 7** page stem `7-1-Complete-Agent-Walkthrough-d798` was retired; closing material for Unit 6 is split across **6.4** and **6.5**. **Former Unit 8** content was merged into that closing pair earlier.

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
1. Install Rasa Pro: `python -m pip install rasa-pro==3.16.3`
2. Activate correct virtual environment
3. Verify installation: `python -m rasa --version`

---

## Additional Resources

### Extension Exercises

#### Exercise 1: Add More Actions

**Task**: Create additional actions for your banking agent:
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

Congratulations! You've completed Level 2 and learned how to add custom Python code to your Rasa agent.

### What You Can Do Now

- Add custom Python code to your agent
- Create dynamic responses based on logic
- Process data and perform calculations
- Integrate with external systems (with proper setup)
- Extend your Level 1 agent with new capabilities

### What's Coming Next

- **Level 3**: Add memory (slots) so the agent can remember information
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
### Content Integration Strategy

- Unit content is included in this document (to keep the course self-contained). Canonical source for narrative is also the Level2_Unit*_Content_*.md files.
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
- `rasa-pro==3.16.3` (pinned)
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
- `RASA_LICENSE=...` (required)
- LLM access uses the **tutorial** endpoint in `endpoints.yml` (`rasa_command_generation_model` / `https://tutorial-llm.rasa.ai`); students do not need `OPENAI_API_KEY` for Level 2.

**Port Configuration**:
- Rasa Inspector: 5005 (default)

---

## Auto-Grading Guidance (Codio Team)

**Recommended auto-grading checks**:
- Validate YAML files parse successfully and required keys exist (domain + flows + patterns)
- Validate required new artifacts for Level 2 exist (e.g., new flows/actions/tools)
- Smoke-test agent starts (`rasa inspect`) and responds to a small scripted conversation

**Implementation notes**:
- Prefer deterministic checks (file existence + YAML structure + expected strings) over LLM-output matching.
- Provide actionable error output (“Expected `actions:` section in `domain/basics.yml`”, etc.).

---

## Hint and troubleshooting guidelines (Codio team)

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


