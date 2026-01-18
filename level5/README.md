# 🟣 Level 5: Tool Calling

**Goal:** Learn how to use tool calling, where the LLM dynamically selects and calls functions based on conversation context.

## What You'll Learn

- How to define tools (functions the LLM can call)
- How to register tools in `endpoints.yml`
- How tools differ from actions
- How the LLM dynamically chooses which tools to call
- When to use tools vs. actions

## Building on Level 4

⚠️ **Important**: This level builds on your Level 4 banking bot. You don't start from scratch!

**What stays the same:**
- All responses from Level 4
- All flows from Level 4 (`greet`, `help`, `contact`, `hours`, `check_balance`, `transfer_money`)
- All actions from Level 4 (`action_bank_hours`, `action_check_balance_simple`, `action_process_transfer`)
- All slots from Level 4 (`account`, `amount`, `recipient`, `account_from`)

**What this level adds:**
- `tools/` folder with `banking_tools.py`
- Tools registration in `endpoints.yml`
- New action `action_process_transfer_with_tools`
- New flow `data/basics/transfer_money_tools.yml`

**Your existing Level 4 banking bot continues to work** - this level adds tool calling, allowing the LLM to dynamically select and call functions!

## Quick Start

**Note**: If you're continuing from Level 4, you already have your virtual environment and Rasa Pro installed. You can skip steps 1-3 and go directly to step 4 (Train and run).

1. **Create and activate a virtual environment:**
   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   ```

2. **Install Rasa Pro:**
   ```powershell
   python -m pip install --no-cache-dir rasa-pro
   ```

3. **Create `.env` file:**
   ```text
   RASA_LICENSE=your-rasa-pro-license
   OPENAI_API_KEY=your-openai-api-key
   ```

4. **Train and run:**
   ```powershell
   . .\load_env.ps1
   python -m rasa train
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

   Or use the helper script:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
   ```

5. **Open Inspector:**
   - `http://localhost:5005/webhooks/socketio/inspect.html`

## What's New in This Level

**Additions to your Level 4 banking bot:**

### Tools Folder (`tools/`)
- **NEW:** `tools/banking_tools.py` - Contains tool functions
- Tools are Python functions that the LLM can call dynamically
- Unlike actions, tools are selected by the LLM based on context
- All Level 4 actions remain unchanged

### Tools Registration (`endpoints.yml`)
- **Added `tools:` section** - Registers the tools module
- `tools_module: "tools"` tells Rasa where to find tool functions
- All existing configuration remains unchanged

### New Action (`actions/action_process_transfer_with_tools.py`)
- Demonstrates how actions can work alongside tools
- The LLM can call tools during the conversation
- All Level 4 actions (`action_bank_hours`, `action_check_balance_simple`, `action_process_transfer`) remain unchanged

### New Flow (`data/basics/transfer_money_tools.yml`)
- Shows how to structure a flow that uses tool calling
- Tools are called dynamically by the LLM, not explicitly in the flow
- All Level 4 flows (greet, help, contact, hours, check_balance, transfer_money) remain unchanged
- All Level 4 responses and slots remain unchanged

## Key Concepts

**Tools vs. Actions:**

**Actions:**
- Explicitly called in flows (`- action: action_name`)
- Predictable execution order
- Good for: structured workflows, required steps

**Tools:**
- Dynamically selected by the LLM
- Called based on conversation context
- Good for: flexible operations, complex multi-step tasks, adapting to user needs

**Tool Calling:**
- The LLM analyzes the conversation
- Decides which tools to call and when
- Can call multiple tools in sequence
- Can handle complex, branching scenarios

**When to Use Tools:**
- When you want the LLM to decide what to do
- For complex, multi-step operations
- When the flow depends on dynamic conditions
- For operations that might vary based on user input

**When to Use Actions:**
- For predictable, structured workflows
- When you need guaranteed execution order
- For simple, single-purpose operations

## Tool Functions

The tools in `tools/banking_tools.py`:

- `check_balance(account)` - Check account balance
- `process_transfer(amount, from_account, to_account)` - Process a transfer
- `get_account_info(account)` - Get account information

Each tool:
- Has a clear docstring explaining its purpose
- Takes typed parameters
- Returns a dictionary with results
- Is exported in `__all__` so Rasa can discover it

## Exercises

1. **Add a new tool:** Create `close_account(account)` in `banking_tools.py`.
2. **Modify tool behavior:** Change `check_balance` to return different balances for different accounts.
3. **Create a tool-using flow:** Build a flow that lets the LLM decide which tools to call.

## Summary

You've now learned:
- ✅ Level 1: Responses (predefined messages)
- ✅ Level 2: Actions (custom Python code)
- ✅ Level 3: Slots (conversation memory)
- ✅ Level 4: Multiple slots (complex data collection)
- ✅ Level 5: Tool calling (dynamic function selection)

Congratulations! You now have a complete understanding of Rasa Pro + CALM fundamentals!
