# Level 5: Tool Calling - Comprehensive Tutorial

**A Complete Guide to Dynamic Function Selection**

---

## Table of Contents

0. [Recap: What You Built in Level 4](#module-0-recap-what-you-built-in-level-4)
1. [Introduction to Tools](#module-1-introduction-to-tools)
2. [Understanding Tools vs. Actions](#module-2-understanding-tools-vs-actions)
3. [Creating Tool Functions](#module-3-creating-tool-functions)
4. [Registering Tools](#module-4-registering-tools)
5. [Using Tools in Conversations](#module-5-using-tools-in-conversations)
6. [Training and Testing with Tools](#module-6-training-and-testing-with-tools)
7. [Putting It All Together](#module-7-putting-it-all-together)
8. [Assessment and Next Steps](#module-8-assessment-and-next-steps)

---

## Module 0: Recap - What You Built in Level 4

### 0.1 Your Level 4 Banking Bot

Before we add tool calling, let's recap what you've already built in Level 4. **All of this remains unchanged** - Level 5 builds on top of it!

#### What You Have from Level 4

**Domain File (`domain/basics.yml`)**:
- ✅ All Level 1-3 responses
- ✅ All ask responses: `utter_ask_account`, `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- ✅ All slots: `account`, `amount`, `recipient`, `account_from`
- ✅ All Level 1-3 actions
- ✅ `action_process_transfer` action (Level 4)

**Flows (`data/basics/`)**:
- ✅ All Level 1-3 flows
- ✅ `transfer_money` flow with multiple slot collection (Level 4)

**Actions (`actions/`)**:
- ✅ All Level 1-3 actions
- ✅ `action_process_transfer` that uses multiple slots

**System Patterns**: Unchanged from Level 1

**Configuration Files**: Unchanged from Level 4

#### What Level 4 Couldn't Do

Your Level 4 bot could collect multiple pieces of information, but it couldn't:
- ❌ Let the LLM dynamically choose which operations to perform
- ❌ Adapt to complex, branching scenarios
- ❌ Handle flexible operations that vary based on context
- ❌ Allow the LLM to decide which functions to call

**Example**: If a user asked complex questions like "Check my balance and then transfer $50 if I have enough", your Level 4 bot would need explicit flows for every scenario. It couldn't let the LLM decide to call `check_balance` first, then conditionally call `process_transfer`.

---

### 0.2 What Level 5 Adds

Level 5 introduces **Tool Calling** - allowing the LLM to dynamically select and call functions based on conversation context.

**Your existing Level 4 bot continues to work** - Level 5 adds dynamic tool calling on top of it!

#### What's New in Level 5

**New Files**:
- `tools/` folder - Contains tool functions
- `tools/__init__.py` - Makes the folder a Python package
- `tools/banking_tools.py` - Contains tool functions the LLM can call

**Modified Files**:
- `endpoints.yml` - Adds `tools:` section to register tools
- New action: `action_process_transfer_with_tools.py` - Demonstrates tools usage
- New flow: `transfer_money_tools.yml` - Flow that uses tool calling

**Unchanged**:
- All Level 1-4 responses remain
- All Level 1-4 flows remain
- All Level 1-4 actions remain
- All Level 1-4 slots remain

---

## Module 1: Introduction to Tools

### 1.1 What is a Tool?

A **tool** is a Python function that the LLM can dynamically call during conversations. Unlike actions (which are explicitly called in flows), tools are selected by the LLM based on the conversation context.

#### Tools vs. Actions

**Actions (`action_*`)**:
- Explicitly called in flows: `- action: action_name`
- Predictable execution order
- You control exactly when they run
- Good for: Structured workflows, required steps

**Tools**:
- Dynamically selected by the LLM
- Called based on conversation context
- LLM decides when to call them
- Good for: Flexible operations, complex multi-step tasks, adapting to user needs

#### Example: Checking Balance

**With Actions (Level 2-4)**:
```yaml
# Explicit flow
steps:
  - action: action_check_balance
```

**With Tools (Level 5)**:
```python
# LLM decides to call check_balance tool based on conversation
# No explicit flow step needed - LLM chooses dynamically
```

---

### 1.2 When to Use Tools

✅ **Use tools when**:
- You want the LLM to decide what to do
- Operations might vary based on context
- Complex, multi-step scenarios with branching
- Flexible operations that adapt to user needs

❌ **Use actions when**:
- You need guaranteed execution order
- Predictable, structured workflows
- Simple, single-purpose operations
- You want explicit control over when code runs

#### Example Scenarios

**Good for Tools**:
- "Check my balance and transfer $50 if I have enough" → LLM decides to call `check_balance`, then conditionally call `process_transfer`
- "What's my account info and balance?" → LLM calls `get_account_info` and `check_balance`
- Complex queries that require multiple operations

**Good for Actions**:
- "What are your hours?" → Simple, predictable → Use action
- "Transfer $100 to John" → Structured workflow → Use action (or tool, both work)

---

### 1.3 How Tools Work

When tools are available, the LLM:

1. **Analyzes the conversation** - Understands what the user wants
2. **Selects appropriate tools** - Decides which tools to call
3. **Calls tools dynamically** - Executes the selected tools
4. **Uses results** - Incorporates tool results into the response

**Key Point**: You don't explicitly call tools in flows - the LLM decides when to use them based on context.

---

## Module 2: Understanding Tools vs. Actions

### 2.1 Key Differences

| Feature | Actions | Tools |
|--------|---------|-------|
| **Definition** | Python classes in `actions/` | Python functions in `tools/` |
| **Registration** | In `domain/basics.yml` under `actions:` | In `endpoints.yml` under `tools:` |
| **Calling** | Explicit in flows: `- action: action_name` | Dynamic by LLM (no explicit call) |
| **Control** | You control when they run | LLM decides when to call |
| **Use Case** | Structured, predictable workflows | Flexible, context-aware operations |

---

### 2.2 When to Use Each

#### Use Actions For:

- **Structured workflows**: "Transfer money" → Collect slots → Process transfer
- **Required steps**: Steps that must always happen in a specific order
- **Simple operations**: Single-purpose, straightforward tasks
- **Explicit control**: When you need to guarantee execution

**Example**: The `transfer_money` flow uses actions because it's a structured process: collect information → process transfer.

#### Use Tools For:

- **Flexible operations**: "Check balance and transfer if possible"
- **Complex scenarios**: Multi-step tasks with branching
- **Context-dependent**: Operations that vary based on conversation
- **LLM decision-making**: When you want the LLM to choose what to do

**Example**: The `transfer_money_tools` flow uses tools because the LLM can dynamically decide which operations to perform.

---

### 2.3 Can You Use Both?

**Yes!** You can use both actions and tools in the same bot:

- **Actions** for structured, predictable workflows
- **Tools** for flexible, dynamic operations

They complement each other - use the right tool for the right job.

---

## Module 3: Creating Tool Functions

### 3.1 Tool Function Structure

Tools are simple Python functions (not classes like actions). Here's the basic structure:

```python
def tool_name(param1: type, param2: type) -> Dict[str, Any]:
    """Tool description.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Dictionary with results
    """
    # Your logic here
    return {"result": "value"}
```

**Key Requirements**:
1. Function must have a docstring (LLM uses this to understand the tool)
2. Parameters should be typed
3. Should return a dictionary
4. Must be exported in `__all__` list

---

### 3.2 Examining Banking Tools

Let's look at the actual `banking_tools.py` file:

```python
"""Banking tools for Level 5: Tool Calling.

Tools are functions that the LLM can dynamically call during conversations.
Unlike actions (which are explicitly called in flows), tools are selected
by the LLM based on the conversation context.
"""

from typing import Dict, Any


def check_balance(account: str) -> Dict[str, Any]:
    """Check the balance for a given account.
    
    This is a tool function that the LLM can call dynamically.
    
    Args:
        account: The account number to check
        
    Returns:
        A dictionary with the balance information
    """
    # Demo implementation - in real life, this would query a database
    return {
        "account": account,
        "balance": 1234.56,
        "currency": "USD",
        "status": "active"
    }


def process_transfer(amount: float, from_account: str, to_account: str) -> Dict[str, Any]:
    """Process a money transfer between accounts.
    
    This is a tool function that the LLM can call dynamically.
    
    Args:
        amount: The amount to transfer
        from_account: Source account number
        to_account: Destination account number
        
    Returns:
        A dictionary with the transfer result
    """
    # Demo implementation - in real life, this would process a real transfer
    return {
        "success": True,
        "transaction_id": "TXN-12345",
        "amount": amount,
        "from_account": from_account,
        "to_account": to_account,
        "message": "Transfer processed successfully"
    }


def get_account_info(account: str) -> Dict[str, Any]:
    """Get information about an account.
    
    This is a tool function that the LLM can call dynamically.
    
    Args:
        account: The account number
        
    Returns:
        A dictionary with account information
    """
    # Demo implementation
    return {
        "account": account,
        "type": "checking",
        "owner": "John Doe",
        "opened": "2020-01-15",
        "status": "active"
    }


# Export all tools so Rasa can discover them
__all__ = ["check_balance", "process_transfer", "get_account_info"]
```

#### Breaking Down Tool Functions

1. **Docstring**: Critical! The LLM reads this to understand what the tool does
   ```python
   """Check the balance for a given account.
   
   Args:
       account: The account number to check
   """
   ```

2. **Type Hints**: Help the LLM understand parameter types
   ```python
   def check_balance(account: str) -> Dict[str, Any]:
   ```

3. **Return Dictionary**: Tools return dictionaries with results
   ```python
   return {
       "account": account,
       "balance": 1234.56,
       "currency": "USD"
   }
   ```

4. **Export List**: Must list all tools in `__all__`
   ```python
   __all__ = ["check_balance", "process_transfer", "get_account_info"]
   ```

---

### 3.3 Step-by-Step: Creating a Tool

**Step 1: Navigate to Tools Folder**

1. Go to `tools/` folder (create it if it doesn't exist)
2. You should see `__init__.py` and `banking_tools.py`

---

**Step 2: Add a New Tool Function**

1. Open `tools/banking_tools.py`
2. Add a new function:

```python
def close_account(account: str) -> Dict[str, Any]:
    """Close an account.
    
    This tool closes a bank account.
    
    Args:
        account: The account number to close
        
    Returns:
        A dictionary with the closure result
    """
    # Demo implementation
    return {
        "account": account,
        "status": "closed",
        "message": f"Account {account} has been closed successfully."
    }
```

3. Add it to `__all__`:
```python
__all__ = ["check_balance", "process_transfer", "get_account_info", "close_account"]
```

---

**Step 3: Verify Your Tool**

Check:
- ✅ Function has a clear docstring
- ✅ Parameters are typed
- ✅ Function returns a dictionary
- ✅ Tool is listed in `__all__`
- ✅ Python syntax is correct

---

## Module 4: Registering Tools

### 4.1 Tools Registration in endpoints.yml

Tools must be registered in `endpoints.yml` so Rasa knows where to find them.

#### endpoints.yml Structure in Level 5

```yaml
action_endpoint:
  actions_module: "actions"

nlg:
  type: rephrase
  llm:
    model_group: gpt-4o-mini

# Tools registration - NEW in Level 5
tools:
  tools_module: "tools"

model_groups:
  - id: gpt-4o-mini
    models:
      - provider: openai
        model: gpt-4o-mini-2024-07-18
        temperature: 0.3
```

#### The Tools Section

```yaml
tools:
  tools_module: "tools"
```

**Breaking it down**:
- **`tools:`** - Section for tool registration
- **`tools_module: "tools"`** - Tells Rasa to look in the `tools/` folder

**How it works**:
1. Rasa looks in the `tools/` folder
2. Finds Python files (like `banking_tools.py`)
3. Looks for functions listed in `__all__`
4. Makes them available as tools the LLM can call

---

### 4.2 Step-by-Step: Registering Tools

**Step 1: Open endpoints.yml**

1. Navigate to `endpoints.yml` (root of your project)
2. Open it in your editor

**What you should see**: Existing configuration from Level 4

---

**Step 2: Add Tools Section**

1. Find the `nlg:` section
2. Add the `tools:` section after it:

```yaml
nlg:
  type: rephrase
  llm:
    model_group: gpt-4o-mini

# Tools registration - NEW in Level 5
tools:
  tools_module: "tools"

model_groups:
  # ... existing model groups
```

⚠️ **Important**:
- `tools:` is at the same indentation level as `nlg:` and `model_groups:`
- `tools_module: "tools"` is indented 2 spaces under `tools:`
- The value `"tools"` matches your `tools/` folder name

---

**Step 3: Verify Registration**

Check:
- ✅ `tools:` section exists
- ✅ `tools_module: "tools"` matches your folder name
- ✅ YAML syntax is correct
- ✅ All existing configuration remains unchanged

---

## Module 5: Using Tools in Conversations

### 5.1 How Tools Are Called

Tools are called **dynamically by the LLM** - you don't explicitly call them in flows like actions.

#### Tool Calling Process

```
User sends message
    ↓
LLM analyzes conversation
    ↓
LLM reads available tools (from tools/ folder)
    ↓
LLM decides which tools to call based on context
    ↓
LLM calls selected tools
    ↓
Tool functions execute
    ↓
LLM uses tool results in response
    ↓
Bot responds to user
```

**Key Point**: The LLM makes the decision - you just provide the tools and let the LLM choose when to use them.

---

### 5.2 Creating a Flow That Uses Tools

While tools are called dynamically, you can create flows that set up the context for tool calling.

#### Example: transfer_money_tools Flow

```yaml
flows:
  transfer_money_tools:
    name: transfer money with tools
    description: |
      Demonstrates tool calling in a flow.
      The bot collects the necessary information, then the LLM
      can dynamically decide to call tools (like check_balance
      or process_transfer) based on the conversation context.
    steps:
      - collect: amount
        description: "transfer amount"
      - collect: recipient
        description: "recipient name or account"
      - collect: account_from
        description: "source account number"
      - action: action_process_transfer_with_tools
      # Note: Tools are registered in endpoints.yml and can be called
      # dynamically by the LLM during the conversation
```

**What happens**:
1. Flow collects slots (amount, recipient, account_from)
2. Flow calls `action_process_transfer_with_tools`
3. During the conversation, the LLM can dynamically call tools
4. Tools execute and provide results
5. LLM uses tool results in the response

---

### 5.3 Tools in Action Code

Actions can work alongside tools. The LLM can call tools during the conversation, and actions can be aware of tool availability.

#### Example: action_process_transfer_with_tools

```python
class ActionProcessTransferWithTools(Action):
    """A custom action that works with tools.
    
    This demonstrates how actions can work alongside tool calling.
    The LLM can dynamically decide to call tools (like check_balance
    or process_transfer) based on the conversation context.
    """

    def name(self) -> Text:
        return "action_process_transfer_with_tools"

    def run(self, dispatcher, tracker, domain):
        # This action can work with tools registered in endpoints.yml
        # The LLM will decide when to call tools based on the conversation
        
        amount = tracker.get_slot("amount")
        recipient = tracker.get_slot("recipient")
        account_from = tracker.get_slot("account_from")
        
        # Validate slots (same as Level 4)
        if not amount or not recipient or not account_from:
            dispatcher.utter_message(
                text="I'm missing some information. Please provide amount, recipient, and source account."
            )
            return []
        
        # The LLM can call tools dynamically during the conversation
        # Tools like check_balance, process_transfer, get_account_info
        # are available and the LLM can choose to use them
        
        dispatcher.utter_message(
            text=f"(Demo with Tools) Transfer of ${amount} from account {account_from} to {recipient} has been processed successfully. Tools are available for dynamic operations."
        )
        return []
```

**Key Point**: The action doesn't explicitly call tools - it just indicates that tools are available, and the LLM decides when to use them.

---

## Module 6: Training and Testing with Tools

### 6.1 Training with Tools

Training with tools is similar to previous levels, but Rasa now also processes tool definitions.

#### Training Command

```powershell
. .\load_env.ps1
python -m rasa train
```

#### What Happens During Training

Rasa:
1. Reads tool definitions from `tools/` folder
2. Validates tool functions (checks `__all__` list)
3. Processes tool registration in `endpoints.yml`
4. Makes tools available to the LLM
5. Creates model with tool information

---

### 6.2 Testing Tool Calling

#### Basic Testing Workflow

1. **Train your bot**: `python -m rasa train`

2. **Start Inspector**: 
   ```powershell
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

3. **Test tool calling**:
   - Type "Transfer $100 to John from account 1234"
   - Bot should collect slots
   - LLM may call tools dynamically based on context
   - Bot should process transfer

4. **Test with complex queries**:
   - Type "Check my balance for account 1234 and get account info"
   - LLM should decide to call `check_balance` and `get_account_info` tools
   - Bot should provide results from both tools

5. **Verify previous levels still work**:
   - All Level 1-4 functionality should still work
   - Tools add new capabilities without breaking existing ones

---

### 6.3 Understanding Tool Execution

In Inspector debug panel, you can see:
- Which tools the LLM decided to call
- Tool execution results
- How the LLM used tool results in the response

**Key Point**: Tool calling is dynamic - the LLM makes decisions based on conversation context.

---

### 6.4 Common Issues with Tools

#### Issue: Tools Not Found

**Symptoms**: LLM doesn't call tools, or error about tools not found

**Possible Causes**:
1. Tools not registered in `endpoints.yml`
2. Tools not exported in `__all__`
3. Tool functions have syntax errors

**Solutions**:
1. Check `endpoints.yml` has `tools:` section with `tools_module: "tools"`
2. Verify all tools are listed in `__all__`
3. Check Python syntax in tool functions

---

#### Issue: LLM Not Calling Tools

**Symptoms**: Tools are registered but LLM never calls them

**Possible Causes**:
1. Tool docstrings not clear enough
2. Conversation context doesn't trigger tool usage
3. Tools not appropriate for the use case

**Solutions**:
1. Improve tool docstrings (LLM uses these to understand tools)
2. Test with queries that clearly need the tools
3. Consider if actions might be more appropriate

---

## Module 7: Putting It All Together

### 7.1 Complete Bot Walkthrough

Let's trace through a complete conversation showing how all levels work together, including tool calling.

#### Conversation Example

```
[User opens chat - new session starts]

1. pattern_session_start triggers (Level 1)
   ↓
Bot: "Hi! I'm a banking assistant. How can I help you today?"

[User types: "Check my balance for account 1234 and get the account info"]

2. LLM understands: "User wants balance and account info"
   ↓
   LLM sees available tools: check_balance, get_account_info
   ↓
   LLM decides to call both tools dynamically
   ↓
   Tool: check_balance("1234") executes
   ↓
   Tool: get_account_info("1234") executes
   ↓
   LLM uses tool results in response
   ↓
Bot: "Balance for account 1234 is $1234.56. Account type: checking, Owner: John Doe, Status: active."

[User types: "Transfer $100 to John from account 1234"]

3. LLM understands: "User wants to transfer money"
   ↓
   Flow: transfer_money_tools (Level 5)
   ↓
   Flow collects slots: amount="100", recipient="John", account_from="1234"
   ↓
   Flow calls: action_process_transfer_with_tools
   ↓
   During conversation, LLM may call process_transfer tool dynamically
   ↓
Bot: "(Demo with Tools) Transfer of $100 from account 1234 to John has been processed successfully. Tools are available for dynamic operations."

[User types: "What are your hours?"]

4. LLM understands: "User wants bank hours"
   ↓
   Flow: hours (Level 2)
   ↓
   Action: action_bank_hours
   ↓
Bot: "Our bank hours are Monday-Friday 9am-5pm..."
```

**Notice**: The bot seamlessly uses:
- Level 1 responses
- Level 2 actions
- Level 3 single slot collection
- Level 4 multiple slot collection
- Level 5 tool calling (dynamic function selection)

---

### 7.2 Your Level 5 Banking Bot: Summary

Congratulations! You've completed all five levels and built a comprehensive banking bot!

#### Your Complete Bot Structure

**Domain (`domain/basics.yml`)**:
- ✅ All responses from Levels 1-4
- ✅ All slots from Levels 3-4
- ✅ All actions from Levels 2-4

**Flows (`data/basics/`)**:
- ✅ All flows from Levels 1-4
- ✅ New `transfer_money_tools` flow (Level 5)

**Actions (`actions/`)**:
- ✅ All actions from Levels 2-4
- ✅ New `action_process_transfer_with_tools` (Level 5)

**Tools (`tools/`)**:
- ✅ `banking_tools.py` with tool functions (Level 5)

**Configuration**:
- ✅ `endpoints.yml` with tools registration (Level 5)

#### What Your Bot Can Do Now

Your Level 5 banking bot can:
- ✅ Everything from Levels 1-4
- ✅ Dynamically call functions based on conversation context
- ✅ Handle complex, branching scenarios
- ✅ Adapt to user needs flexibly
- ✅ Use LLM decision-making for tool selection

#### Complete Capabilities

- **Level 1**: Static responses
- **Level 2**: Custom Python code (actions)
- **Level 3**: Memory (single slots)
- **Level 4**: Multiple slot collection
- **Level 5**: Dynamic tool calling

You now have a fully-featured conversational banking bot!

---

### 7.3 Best Practices

#### Tool Design

1. **Clear docstrings**: LLM uses these to understand tools - make them descriptive
2. **Type hints**: Help LLM understand parameter types
3. **Return dictionaries**: Tools should return structured data
4. **Export in __all__**: Must list all tools for Rasa to discover them

#### When to Use Tools vs. Actions

**Use Tools**:
- When you want LLM to decide what to do
- For flexible, context-aware operations
- Complex scenarios with branching

**Use Actions**:
- For structured, predictable workflows
- When you need guaranteed execution order
- Simple, single-purpose operations

#### Tool Documentation

**Good tool docstring**:
```python
"""Check the balance for a given account.
    
This tool retrieves the current balance for a bank account.

Args:
    account: The account number to check (e.g., "1234")
        
Returns:
    A dictionary with:
        - account: The account number
        - balance: The current balance
        - currency: The currency code
        - status: Account status
"""
```

**Bad tool docstring**:
```python
"""Check balance."""  # Too vague - LLM won't understand when to use it
```

---

## Module 8: Assessment and Next Steps

### 8.1 Knowledge Check

#### Question 1: What is a Tool?

a) A predefined bot message  
b) A Python function the LLM can call dynamically  
c) A memory variable  
d) A conversation script

**Answer**: b) A Python function the LLM can call dynamically

**Explanation**: Tools are Python functions that the LLM can select and call based on conversation context, unlike actions which are explicitly called in flows.

---

#### Question 2: Where are Tools Registered?

a) In `domain/basics.yml` under `tools:`  
b) In `endpoints.yml` under `tools:`  
c) In flow files  
d) In action files

**Answer**: b) In `endpoints.yml` under `tools:`

**Explanation**: Tools are registered in `endpoints.yml` with `tools_module: "tools"`, which tells Rasa where to find tool functions.

---

#### Question 3: How Does the LLM Know When to Call Tools?

a) Tools are explicitly called in flows  
b) The LLM reads tool docstrings and decides based on context  
c) Tools are called automatically  
d) You must specify when to call tools

**Answer**: b) The LLM reads tool docstrings and decides based on context

**Explanation**: The LLM analyzes the conversation, reads available tool docstrings, and dynamically decides which tools to call based on what the user needs.

---

#### Question 4: What's the Main Difference Between Tools and Actions?

a) Tools are in Python, actions are in YAML  
b) Tools are called dynamically by LLM, actions are called explicitly in flows  
c) Tools are faster than actions  
d) There's no difference

**Answer**: b) Tools are called dynamically by LLM, actions are called explicitly in flows

**Explanation**: Actions are explicitly called in flows with `- action: action_name`, while tools are dynamically selected by the LLM based on conversation context.

---

### 8.2 What You've Learned

#### Key Concepts

1. **Tools**: Python functions the LLM can call dynamically
2. **Tool Registration**: Telling Rasa where to find tools in `endpoints.yml`
3. **Dynamic Selection**: LLM decides which tools to call based on context
4. **Tools vs. Actions**: When to use each approach

#### Skills You've Developed

- ✅ Can create tool functions
- ✅ Can register tools in endpoints.yml
- ✅ Can understand when to use tools vs. actions
- ✅ Can build bots with dynamic tool calling
- ✅ Can create comprehensive, flexible conversational interfaces

---

### 8.3 Course Completion

Congratulations! You've completed all five levels of the Rasa Pro + CALM tutorial!

#### What You've Built

You now have a complete banking bot that can:
- ✅ Provide static information (Level 1)
- ✅ Execute custom Python code (Level 2)
- ✅ Remember information (Level 3)
- ✅ Collect multiple pieces of information (Level 4)
- ✅ Dynamically call functions based on context (Level 5)

#### Your Complete Learning Journey

- **Level 1**: Responses - Predefined bot messages
- **Level 2**: Actions - Custom Python code
- **Level 3**: Slots - Conversation memory
- **Level 4**: Multiple Slots - Complex data collection
- **Level 5**: Tools - Dynamic function selection

---

### 8.4 Next Steps

#### Continue Learning

- **Advanced Rasa Features**: Explore more advanced Rasa Pro capabilities
- **Custom Integrations**: Integrate with databases, APIs, external services
- **Production Deployment**: Learn how to deploy your bot to production
- **Testing Strategies**: Learn comprehensive testing approaches
- **Performance Optimization**: Optimize your bot for scale

#### Practice Projects

- Build bots for different domains (customer service, e-commerce, etc.)
- Integrate with real APIs and databases
- Add more sophisticated validation and error handling
- Experiment with different tool and action patterns

#### Resources

- Rasa Documentation: [https://rasa.com/docs](https://rasa.com/docs)
- Rasa Community: Join forums and discussions
- Rasa Examples: Explore example bots and patterns
- Rasa Training: Advanced training courses

---

### 8.5 Final Checklist

You've mastered Rasa Pro + CALM fundamentals if you can:

- [ ] Build bots with responses, actions, slots, and tools
- [ ] Understand when to use each approach
- [ ] Create flows that collect information
- [ ] Write actions that use slots
- [ ] Create tools for dynamic operations
- [ ] Debug and test your bots effectively
- [ ] Understand that each level builds on previous levels

**You're now ready to build production-ready Rasa bots! 🎉**

---

## Troubleshooting Guide

### Common Issues and Solutions

#### Issue: Tools Not Being Called

**Symptoms**: Tools are registered but LLM never calls them

**Possible Causes**:
1. Tool docstrings not descriptive enough
2. Conversation doesn't clearly need the tools
3. Tools not appropriate for the use case

**Solutions**:
1. Improve tool docstrings - be very descriptive
2. Test with queries that clearly need the tools
3. Consider if actions might be better for this use case

---

#### Issue: Tool Registration Error

**Symptoms**: Error about tools not found or tools_module error

**Possible Causes**:
1. `tools:` section missing in endpoints.yml
2. `tools_module` value doesn't match folder name
3. Tools not exported in `__all__`

**Solutions**:
1. Check `endpoints.yml` has `tools:` section
2. Verify `tools_module: "tools"` matches your folder name
3. Ensure all tools are in `__all__` list

---

## Conclusion

Congratulations! You've completed all five levels and have a complete understanding of Rasa Pro + CALM!

### What You Can Do Now

- Build comprehensive conversational bots
- Use responses, actions, slots, and tools effectively
- Create flexible, context-aware conversations
- Handle complex multi-step interactions
- Deploy production-ready bots

### Your Complete Banking Bot

You've built a banking bot that demonstrates:
- ✅ Static information (Level 1)
- ✅ Dynamic code execution (Level 2)
- ✅ Conversation memory (Level 3)
- ✅ Multiple data collection (Level 4)
- ✅ Dynamic tool calling (Level 5)

### Keep Learning

- Practice by building more bots
- Experiment with different patterns
- Integrate with real systems
- Read advanced Rasa documentation
- Join the Rasa community
- Share your bots and learn from others

**You're now a Rasa Pro + CALM expert! 🚀**

**Happy building!**
