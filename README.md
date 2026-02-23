# Minimal Banking Bot - Rasa Pro + CALM Learning Course

A progressive, hands-on course for learning Rasa Pro + CALM from absolute beginner to advanced tool calling.

## 🎯 Course Overview

This repository contains **5 levels** of increasing complexity, each building on the previous one:

- **🟢 Level 1: Just Responses** - Learn the basics of flows and predefined messages
- **🟡 Level 2: Simple Actions** - Add custom Python code to your bot
- **🟠 Level 3: Slot Collection** - Store and use information from users
- **🔴 Level 4: Multiple Slots** - Handle complex multi-step conversations
- **🟣 Level 5: Tool Calling** - Enable dynamic function selection by the LLM

Each level is a **complete, runnable bot** that you can train and test independently.

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+** installed
- **Rasa Pro license** (get one at [rasa.com](https://rasa.com))
- **OpenAI API key** (for LLM features)

### Setup (One Time)

1. **Choose a level** to start with (we recommend starting at Level 1):
   ```powershell
   cd level1
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   ```

3. **Install Rasa Pro:**
   ```powershell
   python -m pip install --no-cache-dir rasa-pro
   ```

4. **Create `.env` file** in the level folder:
   ```text
   RASA_LICENSE=your-rasa-pro-license
   OPENAI_API_KEY=your-openai-api-key
   ```

5. **Train and run:**
   ```powershell
   . .\load_env.ps1
   python -m rasa train
   python -m rasa inspect --debug --log-file logs/logs.out
   ```

   Or use the helper script:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
   ```

6. **Open Inspector:**
   - Navigate to: `http://localhost:5005/webhooks/socketio/inspect.html`
   - Start chatting with your bot!

---

## 📚 Course Structure

### Level 1: Just Responses 🟢

**Goal:** Build the simplest possible bot using only predefined responses.

**What you'll learn:**
- How to define bot responses in the domain
- How to create simple flows
- The basic structure of a Rasa bot

**Files:**
- `domain/basics.yml` - Only responses (no slots, no actions)
- `data/basics/*.yml` - Simple flows with `utter_*` actions

**Start here:** `level1/README.md`

---

### Level 2: Simple Actions 🟡

**Goal:** Learn how to write custom Python code (actions) that the bot can execute.

**What you'll learn:**
- How to create custom actions in Python
- How to register actions in the domain
- How to call actions from flows

**Files:**
- `actions/action_bank_hours.py` - Your first custom action
- `domain/basics.yml` - Adds `actions:` section

**Start here:** `level2/README.md`

---

### Level 3: Slot Collection 🟠

**Goal:** Learn how to collect and use information from the user (slots = conversation memory).

**What you'll learn:**
- How to define slots in the domain
- How to collect slots in flows using `collect:`
- How to read slots in actions
- How to handle placeholder values

**Files:**
- `actions/action_check_balance_simple.py` - You write this in Lab 4.1 (reads slots and handles placeholders)
- `domain/basics.yml` - Adds `slots:` section
- `data/basics/check_balance.yml` - Flow with slot collection

**Start here:** `level3/README.md`

---

### Level 4: Multiple Slots 🔴

**Goal:** Learn how to collect multiple pieces of information before performing an action.

**What you'll learn:**
- How to define multiple slots
- How to collect multiple slots in a single flow
- How to validate multiple slot values
- How to handle complex multi-step conversations

**Files:**
- `actions/action_process_transfer.py` - Action using multiple slots
- `domain/basics.yml` - Multiple slots defined
- `data/basics/transfer_money.yml` - Flow with multiple `collect:` steps

**Start here:** `level4/README.md`

---

### Level 5: Tool Calling 🟣

**Goal:** Learn how to use tool calling, where the LLM dynamically selects and calls functions.

**What you'll learn:**
- How to define tools (functions the LLM can call)
- How to register tools in `endpoints.yml`
- How tools differ from actions
- When to use tools vs. actions

**Files:**
- `tools/banking_tools.py` - Tool functions
- `endpoints.yml` - Tools registration
- `data/basics/transfer_money_tools.yml` - Flow demonstrating tool calling

**Start here:** `level5/README.md`

---

## 🛠️ Troubleshooting

### `ModuleNotFoundError: No module named 'randomname'` or `'pypred'`

On some Windows setups, `pip` can end up with only metadata installed.

**Fix:**
```powershell
.\.venv\Scripts\python.exe -m pip install --no-cache-dir --force-reinstall randomname==0.2.1 pypred==0.4.0
python -m rasa --version
```

### Virtual Environment Issues

If you encounter permission errors or conflicts:

1. Deactivate any active virtual environment
2. Delete the `.venv` folder: `Remove-Item -Recurse -Force .\.venv`
3. Create a fresh venv: `py -3.11 -m venv .venv`
4. Activate and reinstall: `.\.venv\Scripts\Activate.ps1` then `python -m pip install --no-cache-dir rasa-pro`

---

## 📖 Learning Path

**Recommended progression:**

1. **Start with Level 1** - Get comfortable with the basics
2. **Complete all exercises** in each level before moving on
3. **Experiment** - Try modifying the code to see what happens
4. **Move to the next level** only when you understand the current one

**Each level includes:**
- ✅ Complete, runnable bot code
- ✅ Detailed README with explanations
- ✅ Step-by-step setup instructions
- ✅ Exercises to practice what you learned
- ✅ Clear explanation of new concepts

---

## 🎓 Key Concepts (Quick Reference)

| Concept | What It Is | Where It Lives |
|---------|-----------|----------------|
| **Flow** | Step-by-step conversation plan | `data/*.yml` |
| **Response** | Predefined bot message | `domain/basics.yml` → `responses:` |
| **Action** | Custom Python code | `actions/*.py` |
| **Slot** | Conversation memory | `domain/basics.yml` → `slots:` |
| **Tool** | Dynamic function the LLM can call | `tools/*.py` |

---

## 📝 Notes

- **Each level is independent** - You can work on any level without the others
- **All levels use the same setup** - Virtual environment, Rasa Pro, `.env` file
- **Code is heavily annotated** - Every file includes comments explaining what's happening
- **Progressive complexity** - Each level builds naturally on the previous one

---

## 🚦 Ready to Start?

1. Navigate to `level1/`
2. Read `level1/README.md`
3. Follow the setup instructions
4. Start building!

**Happy learning! 🎉**
