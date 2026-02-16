# Level 1: Just Responses - Comprehensive Tutorial

**A Complete Guide to Building Your First Rasa Bot**

---

## Table of Contents

0. [Prerequisites and Setup](#module-0-prerequisites-and-setup)
1. [Introduction to Rasa Bots](#module-1-introduction-to-rasa-bots)
2. [Understanding the Domain File](#module-2-understanding-the-domain-file)
3. [Understanding Flows](#module-3-understanding-flows)
4. [System Patterns](#module-4-system-patterns)
5. [Configuration Files](#module-5-configuration-files)
6. [Training and Testing](#module-6-training-and-testing)
7. [Putting It All Together](#module-7-putting-it-all-together)
8. [Assessment and Next Steps](#module-8-assessment-and-next-steps)

---

## Module 0: Prerequisites and Setup

### 0.1 What You Need Before Starting

Before diving into building your first Rasa bot, let's make sure you have everything set up correctly.

#### Prerequisites Checklist

✅ **Python Knowledge**
- You should be comfortable with basic Python concepts
- You don't need to be an expert, but understanding basic syntax helps
- **If you're new to Python**: Consider learning basic syntax first (variables, strings, lists)

✅ **Command Line Familiarity**
- You'll be using PowerShell (Windows) or Terminal (Mac/Linux)
- You should know how to:
  - Navigate folders (`cd`, `ls`/`dir`)
  - Run commands
  - Activate a virtual environment

✅ **File Editing**
- You'll need a text editor or IDE (Visual Studio Code, PyCharm, etc.)
- You'll be editing YAML files (we'll explain YAML syntax below)

✅ **Rasa Pro License**
- You need a Rasa Pro license
- You need an OpenAI API key (for the LLM functionality)

✅ **Time Commitment**
- This tutorial takes 2-3 hours to complete thoroughly
- Plan to work through it without rushing

---

### 0.2 Environment Setup

Let's get your development environment ready.

#### Step 1: Create a Virtual Environment

**Why?** A virtual environment keeps your project's Python packages separate from other projects.

```powershell
# Navigate to your project folder
cd path\to\your\project

# Create a virtual environment
py -3.11 -m venv .venv

# Activate it (you'll need to do this each time you work on the project)
.\.venv\Scripts\Activate.ps1
```

**How to verify it worked**: Your command prompt should show `(.venv)` at the beginning.

#### Step 2: Install Rasa Pro

```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install Rasa Pro
python -m pip install --no-cache-dir rasa-pro
```

**How to verify it worked**: Run `python -m rasa --version` - you should see version information.

#### Step 3: Set Up Environment Variables

Create a `.env` file in your project root with:

```text
RASA_LICENSE=your-rasa-pro-license-here
OPENAI_API_KEY=your-openai-api-key-here
```

⚠️ **Important**: 
- Never commit `.env` files to version control (they contain secrets)
- Replace the placeholder values with your actual license and API key

#### Step 4: Load Environment Variables

Before running Rasa commands, load your environment variables:

```powershell
# Load environment variables
. .\load_env.ps1

# Or use the helper script that does this automatically
powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
```

---

### 0.3 Understanding YAML Syntax

**YAML** (Yet Another Markup Language) is a human-readable format for configuration files. Rasa uses YAML extensively, so understanding the basics is essential.

#### Why YAML?

YAML is designed to be easy for humans to read and write, making it perfect for configuration files. All Rasa bot files use YAML format.

#### Basic YAML Rules

1. **Indentation Matters**
   - Use **2 spaces** (not tabs, not 4 spaces)
   - Indentation shows hierarchy (what belongs to what)
   - Incorrect indentation will cause errors

2. **Key-Value Pairs**
   ```yaml
   key: value
   name: "Hello World"
   number: 42
   ```

3. **Lists (Arrays)**
   ```yaml
   # List of items (each item starts with a dash and space)
   items:
     - item1
     - item2
     - item3
   ```

4. **Colons and Dashes**
   - **Colon (`:`)** separates keys from values: `key: value`
   - **Dash (`-`)** indicates a list item: `- item`
   - Always put a space after colons and dashes

5. **Quotes**
   - Use quotes around text with special characters
   - Simple strings don't need quotes: `name: Hello`
   - But it's safer to use quotes: `name: "Hello World"`

#### YAML Examples

**✅ CORRECT Examples:**

```yaml
# Simple key-value pair
version: "3.1"

# List of items (notice the 2-space indentation)
responses:
  utter_greet:
    - text: "Hello!"        # ← 4 spaces before '-', 6 before 'text:'
      metadata:              # ← 6 spaces (same level as 'text:')
        rephrase: True       # ← 8 spaces (under 'metadata:')
```

**❌ WRONG Examples:**

```yaml
# ❌ WRONG: Missing space after colon
version:"3.1"

# ❌ WRONG: Using tabs instead of spaces
responses:
	utter_greet:
		- text: "Hello!"

# ❌ WRONG: Wrong indentation (using 4 spaces instead of 2)
responses:
    utter_greet:
        - text: "Hello!"

# ❌ WRONG: Missing dash for list item
responses:
  utter_greet:
    text: "Hello!"  # ← Should be: - text: "Hello!"
```

#### YAML Quick Reference

| Element | Syntax | Example |
|---------|--------|---------|
| Key-value | `key: value` | `name: "Hello"` |
| List item | `- item` | `- "First item"` |
| Nested structure | Indent 2 spaces | `parent:`<br>`  child: value` |
| Comments | `# comment` | `# This is a comment` |

⚠️ **Common YAML Mistakes**:
1. Using tabs instead of spaces
2. Wrong indentation (not using 2 spaces consistently)
3. Missing colons after keys
4. Missing dashes before list items
5. Mixing 2-space and 4-space indentation

**Tip**: Most modern text editors (VS Code, PyCharm) can validate YAML syntax and highlight errors.

---

### 0.4 Project File Structure

Understanding the file structure will help you navigate the codebase and understand how everything fits together.

#### Complete File Tree

```
level1/
├── config.yml              # How to build the bot (pipeline, policies)
├── credentials.yml         # How to connect (REST, Socket.IO)
├── endpoints.yml           # Where to find actions/LLMs
├── .env                    # Environment variables (secrets - not committed)
├── domain/
│   └── basics.yml          # Bot knowledge base (responses)
├── data/
│   ├── basics/             # User-facing flows (conversation scripts)
│   │   ├── greet.yml
│   │   ├── help.yml
│   │   └── contact.yml
│   └── system/
│       └── patterns/
│           └── patterns.yml # System patterns (session start, completed)
└── models/                 # Generated during training (don't edit)
```

#### File Purpose Overview

**Configuration Files** (root level):
- **`config.yml`**: Defines how Rasa builds your bot (which LLM to use, which policies, etc.)
- **`credentials.yml`**: Defines how the bot connects to chat interfaces
- **`endpoints.yml`**: Defines where to find custom actions and LLM configurations

**Domain Files** (`domain/`):
- **`domain/basics.yml`**: The bot's knowledge base - defines all responses the bot can say

**Flow Files** (`data/`):
- **`data/basics/*.yml`**: User-facing conversation scripts (flows)
- **`data/system/patterns/patterns.yml`**: System-level behaviors (session start, flow completion)

**Generated Files** (created automatically):
- **`models/`**: Compiled bot models (created when you run `rasa train`)
- **`logs/`**: Log files for debugging

#### How Files Work Together

```
User sends message
    ↓
config.yml (defines how to understand it)
    ↓
data/*.yml (flows define what to do)
    ↓
domain/basics.yml (responses define what to say)
    ↓
Bot responds
```

**Key Relationships**:
- **Flows** (in `data/`) reference **Responses** (in `domain/`)
- **Config** tells Rasa how to process everything
- **System patterns** control conversation lifecycle

---

### 0.5 Verifying Your Setup

Before starting the tutorial, verify everything works:

#### Checklist

1. **✅ Virtual Environment Active**
   ```powershell
   # Command prompt should show (.venv)
   # If not, activate it: .\.venv\Scripts\Activate.ps1
   ```

2. **✅ Rasa Pro Installed**
   ```powershell
   python -m rasa --version
   # Should show version information (no errors)
   ```

3. **✅ Environment Variables Set**
   ```powershell
   # Check .env file exists and has both RASA_LICENSE and OPENAI_API_KEY
   # Make sure values are not placeholders
   ```

4. **✅ Can Train a Bot**
   ```powershell
   . .\load_env.ps1
   python -m rasa train
   # Should complete successfully and create a model file
   ```

5. **✅ Can Start Inspector**
   ```powershell
   python -m rasa inspect --debug --log-file logs/logs.out
   # Should start server (you can stop it with Ctrl+C)
   ```

If all checks pass, you're ready to start Module 1!

---

### 0.6 Getting Help

**Stuck?** Here are resources:

- **Rasa Documentation**: [https://rasa.com/docs](https://rasa.com/docs)
- **Error Messages**: Check the troubleshooting section at the end of this tutorial
- **Common Issues**: Most setup issues are covered in the troubleshooting guide

---

## Module 1: Introduction to Rasa Bots

### 1.1 What is a Conversational Bot?

A **conversational bot** is a computer program that can have natural, human-like conversations with users. Unlike traditional programs that require specific commands, conversational bots understand natural language and respond in kind.

#### Key Characteristics

1. **Natural Language Understanding (NLU)**: The bot can understand what users mean, even when they phrase things differently. For example:
   - "What are your hours?"
   - "When are you open?"
   - "Tell me your operating hours"
   
   All three mean the same thing, and a good bot understands them all.

2. **Context Awareness**: Advanced bots can remember previous parts of the conversation. (Note: Level 1 bots don't have memory yet - that comes in Level 3.)

3. **Flow-Based Logic**: The bot follows predefined conversation paths (called "flows") that determine what happens next.

#### Types of Bots

- **Rule-Based Bots**: Follow strict if-then rules. Limited flexibility.
- **AI-Powered Bots**: Use machine learning to understand intent and respond naturally. This is what Rasa Pro provides.

#### Why Rasa Pro + CALM?

Rasa Pro with the CALM (Conversational AI Language Model) framework combines:
- **Flow-based structure**: Easy to understand and maintain
- **LLM-powered understanding**: Natural language comprehension
- **Flexible architecture**: Can handle simple to complex conversations

**Analogy**: Think of a Rasa bot like a helpful assistant that follows a script, but can understand when you ask questions in different ways.

---

### 1.2 The Simplest Bot Possible

Level 1 represents the **absolute minimum** a functional Rasa bot needs. We intentionally start simple to build a solid foundation.

#### What Level 1 Includes

- **Responses**: Predefined messages the bot can say
- **Flows**: Simple conversation scripts that use those responses
- **Basic configuration**: Files that tell Rasa how to build the bot

#### What Level 1 Does NOT Include

- **Slots (Memory)**: The bot cannot remember information from earlier in the conversation
- **Actions (Custom Code)**: The bot cannot execute Python code or perform calculations
- **Dynamic Responses**: All responses are static - they don't change based on context

#### Why Start Here?

1. **Minimal Cognitive Load**: You only need to understand one concept: responses
2. **Quick Wins**: You can build a working bot in minutes
3. **Real-World Validity**: Many production bots are exactly this simple
4. **Foundation**: Everything else builds on this base

**Analogy**: Level 1 is like a FAQ page that can understand questions. It provides information, but doesn't do anything complex.

---

### 1.3 Real-World Use Cases

Level 1 bots are perfect for:

- **Company Information**: "What are your hours?", "Where are you located?"
- **Product FAQs**: "What features does this product have?", "How do I get started?"
- **Contact Information**: "How can I reach support?", "What's your email?"
- **Simple Help Systems**: "What can you help me with?", "I need assistance"

**Example Conversation:**
```
User: "Hello"
Bot: "Hi! I'm a banking assistant. How can I help you today?"

User: "What can you do?"
Bot: "I can help you with:
      - Checking your balance
      - Transferring money
      - Bank hours
      - Contact information"

User: "How do I contact you?"
Bot: "You can reach us at support@bank.com or call 1-800-BANK-123."
```

Notice: The bot provides information but doesn't remember anything or perform any actions.

---

### Exercise 1.1: Identifying Bot Capabilities

**Question**: Which of these scenarios can be handled by a Level 1 bot (responses only)?

1. Providing company contact information
2. Checking account balance (requires account number)
3. Listing product features
4. Processing a payment (requires payment details and processing)
5. Explaining how to use a feature
6. Remembering user preferences

**Answer Key**:
- ✅ **Can handle**: 1, 3, 5 (just providing information)
- ❌ **Cannot handle**: 2, 4, 6 (require memory, code, or both)

**Explanation**:
- Checking balance needs the account number (memory/slots - Level 3)
- Processing payment needs code to actually transfer money (actions - Level 2)
- Remembering preferences needs memory (slots - Level 3)

---

## Module 2: Understanding the Domain File

### 2.1 What is a Domain?

The **domain file** is the bot's knowledge base. It defines everything the bot "knows":
- What it can say (responses)
- What it can remember (slots) - not in Level 1
- What code it can run (actions) - not in Level 1

**File Location**: `domain/basics.yml`

**Analogy**: The domain is like a dictionary that defines all the words (responses) the bot can use.

#### Domain Structure

The domain file has three main sections (but Level 1 only uses `responses:`):

```yaml
version: "3.1"        # Rasa version (always "3.1" for current Rasa Pro)

responses:            # ← Level 1: We use this section
  # All predefined messages go here

slots:                # ← Level 3: Memory variables (not used in Level 1)
  # Memory variables go here

actions:              # ← Level 2: Custom Python code (not used in Level 1)
  # Custom Python code goes here
```

⚠️ **For Level 1**: We only use the `responses:` section. The `slots:` and `actions:` sections are empty (we'll learn about them in later levels).

---

### 2.2 Understanding Responses

A **response** is a predefined message the bot can send to users. Responses are defined in the domain file and used in flows.

#### Response Structure

Let's examine a real response from `domain/basics.yml`:

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
    metadata:
      rephrase: True
```

**Breaking it down**:

1. **`utter_greet`**: The response name
   - Must start with `utter_` (Rasa convention)
   - `greet` is the descriptive part
   - This is how you reference the response in flows

2. **`- text: "..."`**: The actual message
   - The dash (`-`) means this is a list item
   - `text:` is the field name
   - The quoted string is what the bot will say

3. **`metadata: rephrase: True`**: Optional configuration
   - Tells the LLM it can vary the wording
   - Makes the bot feel more natural
   - The bot might say "Hello!" instead of "Hi!" sometimes

⚠️ **Important**: `rephrase: True` allows the LLM to vary the wording while keeping the same meaning. This makes conversations feel more natural - users notice when a bot says the exact same thing every time!

**Why this matters**: Real conversations aren't repetitive. Without `rephrase: True`, your bot will always say exactly the same thing. With it enabled, the bot can say "Hello!" one time and "Hi there!" another time, while meaning the same thing.

#### Why a List?

Responses are defined as lists because you can have multiple variations:

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
  - text: "Hello! How can I help you?"
  - text: "Welcome! I'm here to assist you."
```

Rasa will randomly select one of these when the response is used, making the bot feel more natural.

---

### 2.3 Creating Your First Response

Let's add a new response to practice. This hands-on exercise will help you understand how responses work.

#### Before You Begin

✅ **Checklist**:
- You have a text editor or IDE open
- You know where the `domain/` folder is in your project
- You understand basic YAML syntax (review Module 0.3 if needed)

#### Step-by-Step Tutorial

**Step 1: Navigate to the Domain File**

1. In your project folder, navigate to the `domain/` folder
2. Open the file named `basics.yml` in your text editor
3. You should see a file that starts with `version: "3.1"` followed by a `responses:` section

**What you should see**: The file should contain existing responses like `utter_greet`, `utter_help`, and `utter_contact`.

---

**Step 2: Locate the Responses Section**

1. Scroll to find the `responses:` section (it should be near the top, after `version: "3.1"`)
2. You'll see existing responses like:
   ```yaml
   responses:
     utter_greet:
       - text: "Hi! I'm a banking assistant. How can I help you today?"
         metadata:
           rephrase: True
     
     utter_help:
       - text: |
           I can help you with:
           ...
     
     utter_contact:
       - text: "You can reach us at support@bank.com or call 1-800-BANK-123."
         metadata:
           rephrase: True
   ```

**What you should see**: Multiple responses, each with the `utter_` prefix, indented properly with 2 spaces.

---

**Step 3: Add Your New Response**

1. Find the `utter_contact` response (the last one in the list)
2. After `utter_contact`, add a blank line
3. Add your new response using this exact pattern:
   ```yaml
   utter_goodbye:
     - text: "Goodbye! Have a great day!"
       metadata:
         rephrase: True
   ```

⚠️ **Important**: Pay attention to indentation:
- `utter_goodbye:` should be at the same level as `utter_contact:` (2 spaces from the left)
- `- text:` should be indented 2 more spaces (4 spaces total)
- `metadata:` should be at the same level as `text:` (6 spaces from the start of the line)
- `rephrase: True` should be indented 2 more spaces under `metadata:` (8 spaces total)

**Why add it here?** The order doesn't matter for functionality, but keeping responses organized helps with readability.

---

**Step 4: Verify Your Syntax**

Before saving, double-check:

✅ **Indentation**: 
- Use exactly 2 spaces (not tabs, not 4 spaces)
- Use your editor's "show whitespace" feature if available

✅ **Structure**:
- Response name ends with `:` (colon)
- `-` (dash) before `text:`
- `metadata:` is aligned with `text:`
- `rephrase: True` is under `metadata:`

✅ **Spelling**: 
- `utter_goodbye` is spelled correctly
- `rephrase` is spelled correctly (not "rephrase" vs "rephrase")

**Common mistakes to avoid**:
- ❌ Missing dash: `text: "..."` instead of `- text: "..."`
- ❌ Wrong indentation: Using tabs or wrong number of spaces
- ❌ Missing colon: `utter_goodbye` instead of `utter_goodbye:`
- ❌ Wrong metadata indentation: `metadata:` aligned with `-` instead of `text:`

---

**Step 5: Save the File**

1. Save your changes (Ctrl+S or Cmd+S)
2. Your file should now have the new `utter_goodbye` response

#### Complete Example

Your `responses:` section should now look like:

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

  utter_goodbye:
    - text: "Goodbye! Have a great day!"
      metadata:
        rephrase: True
```

#### Common Mistakes

1. **Missing dash**: Forgetting the `-` before `text:` causes YAML parsing errors
2. **Wrong indentation**: YAML is very sensitive to spacing - use 2 spaces consistently
3. **Missing colon**: The response name must end with `:`
4. **Forgetting `utter_` prefix**: While not strictly required, it's a strong convention

---

### 2.4 Response Variations

Having multiple variations of the same response makes your bot feel more natural and less robotic.

#### When to Use Variations

✅ **Good for**:
- Greetings (various ways to say hello)
- Confirmations (different ways to say "yes")
- General information (can be phrased differently)

❌ **Not good for**:
- Critical information (account numbers, error codes)
- Legal disclaimers (must be exact)
- Step-by-step instructions (clarity is more important than variety)

#### Example: Multiple Variations

```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
  - text: "Hello! I'm here to help with your banking needs."
  - text: "Welcome! How can I assist you today?"
    metadata:
      rephrase: True
```

When `utter_greet` is called, Rasa randomly selects one of these three options.

#### Exercise 2.1: Add Variations

**Task**: Add a second variation to `utter_goodbye`.

**Before You Begin**:
- ✅ You've completed the previous exercise (created `utter_goodbye`)
- ✅ You have `domain/basics.yml` open in your editor

**Steps**:
1. Find `utter_goodbye` in `domain/basics.yml` (it should be at the end of the responses section)
2. Add a second `- text:` item with a different farewell message
   - The second `- text:` should be at the same indentation level as the first
   - Use a different farewell phrase (e.g., "See you later!", "Take care!", "Have a great day!")
3. Keep the `metadata:` section (it can be under the last text item)

**Example Solution**:
```yaml
utter_goodbye:
  - text: "Goodbye! Have a great day!"
  - text: "See you later! Take care!"
    metadata:
      rephrase: True
```

**How to Verify**:
1. ✅ Check that both `- text:` items are at the same indentation level (4 spaces from the left)
2. ✅ Check that `metadata:` is aligned with `text:` (6 spaces from the left)
3. ✅ Check that `rephrase: True` is under `metadata:` (8 spaces from the left)
4. ✅ Try training your bot (we'll learn this in Module 6) - if training succeeds, your YAML is correct!

**What This Means**: When `utter_goodbye` is used, Rasa will randomly select one of the two variations, making your bot feel more natural.

---

## Module 3: Understanding Flows

### 3.1 What is a Flow?

A **flow** is a conversation script - a step-by-step plan for how the bot should handle a particular conversation path.

**File Location**: `data/basics/*.yml` (one file per flow, or multiple flows per file)

**Analogy**: A flow is like a recipe. It has:
- A name (what recipe is this?)
- A description (what does this recipe make?)
- Steps (what do I do, in order?)

#### Flow Execution

When a flow is triggered, Rasa executes each step in order:

```
User says "hello"
    ↓
Flow: greet is triggered
    ↓
Step 1: utter_greet
    ↓
Bot responds: "Hi! I'm a banking assistant..."
    ↓
Flow completes
```

---

### 3.2 Flow Structure Deep Dive

Let's examine a real flow from `data/basics/greet.yml`:

```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet
```

#### Breaking Down Each Component

1. **`flows:`**: Top-level key
   - Indicates this file contains flow definitions
   - All flows in this file go under this key

2. **`greet:`**: Flow name
   - This is the identifier used to reference the flow
   - Must be unique within the bot
   - Convention: lowercase, descriptive

3. **`name: say hello`**: Human-readable name
   - Used in logs and debugging
   - Helps humans understand what the flow does
   - Can be different from the flow identifier

4. **`description: ...`**: What the flow does
   - **Critical**: The LLM uses this to match user messages to flows
   - Should be clear and specific
   - Example: "Greet the user when they start a conversation" helps the LLM understand this flow should trigger on "hello", "hi", "hey", etc.

⚠️ **Critical**: Flow descriptions are **essential**! The LLM reads flow descriptions to understand what each flow does. Without a good description, the LLM won't know when to trigger your flow. Always write clear, specific descriptions.

**Example of good vs bad descriptions**:
- ❌ **Bad**: "Say hello" (too vague - when? why?)
- ✅ **Good**: "Greet the user when they start a conversation" (clear context and purpose)

5. **`steps:`**: The actual steps to execute
   - A list of actions to perform in order
   - Each step is indented with a dash (`-`)

6. **`- action: utter_greet`**: A single step
   - `action:` indicates this is an action step
   - `utter_greet` is the response to use (must be defined in domain)

---

### 3.3 Creating Your First Flow

Let's create a flow that uses the `utter_goodbye` response we added earlier. This will connect a user message to a bot response.

#### Before You Begin

✅ **Checklist**:
- You've completed the previous exercise (created `utter_goodbye` in the domain)
- You know where the `data/basics/` folder is
- You have a text editor ready

#### Step-by-Step Tutorial

**Step 1: Navigate to the Data Folder**

1. In your project folder, navigate to the `data/` folder
2. Open the `basics/` subfolder
3. You should see files like `greet.yml`, `help.yml`, and `contact.yml`

**What you should see**: Multiple YAML files, each containing flow definitions.

---

**Step 2: Create the New Flow File**

1. In the `data/basics/` folder, create a new file
2. Name it exactly: `goodbye.yml` (all lowercase, `.yml` extension)
3. Make sure the file is saved in `data/basics/` (not in `data/` root)

⚠️ **File naming tips**:
- Use lowercase letters
- Use underscores for multi-word names (e.g., `check_balance.yml`)
- Always use `.yml` extension (not `.yaml`)

---

**Step 3: Add the Flow Structure**

1. Open `goodbye.yml` in your editor (it will be empty)
2. Add this exact structure:

```yaml
flows:
  goodbye:
    name: say goodbye
    description: Farewell the user when they end the conversation.
    steps:
      - action: utter_goodbye
```

⚠️ **Pay attention to indentation**:
- `flows:` is at the start (no indentation)
- `goodbye:` is indented 2 spaces under `flows:`
- `name:`, `description:`, and `steps:` are indented 2 spaces under `goodbye:`
- `- action: utter_goodbye` is indented 4 spaces (under `steps:`)

**What each part does**:
- `flows:` - Top-level key (tells Rasa this file contains flows)
- `goodbye:` - Flow identifier (how you reference it internally)
- `name: say goodbye` - Human-readable name (for logs/debugging)
- `description: ...` - **Critical!** The LLM uses this to match user messages
- `steps:` - List of actions to execute
- `- action: utter_goodbye` - The action to perform (uses the response we created)

---

**Step 4: Verify the Structure**

Before saving, check:

✅ **Required fields present**:
- `flows:` at the top
- Flow identifier (`goodbye:`) with colon
- `name:` field (human-readable name)
- `description:` field (what the flow does - very important!)
- `steps:` section
- At least one step (`- action: ...`)

✅ **Indentation correct**:
- Use 2 spaces consistently
- `goodbye:` aligned under `flows:`
- `name:`, `description:`, `steps:` aligned under `goodbye:`
- `- action:` indented under `steps:`

✅ **Response exists**:
- The response `utter_goodbye` exists in `domain/basics.yml`
- Spelling matches exactly (case-sensitive!)

**Common mistakes to avoid**:
- ❌ Missing `flows:` at the top
- ❌ Missing `description:` field (this is critical - flows won't match without it!)
- ❌ Wrong indentation
- ❌ Response name typo (e.g., `utter_goodby` instead of `utter_goodbye`)
- ❌ Missing colon after flow name (`goodbye` instead of `goodbye:`)

---

**Step 5: Save and Verify**

1. Save the file (Ctrl+S or Cmd+S)
2. Your file should now contain a complete flow definition

#### Complete File

`data/basics/goodbye.yml`:
```yaml
flows:
  goodbye:
    name: say goodbye
    description: Farewell the user when they end the conversation.
    steps:
      - action: utter_goodbye
```

#### How Rasa Finds Flows

Rasa automatically searches the `data/` folder (and subfolders) for `.yml` files containing flows. You can organize flows however you like:
- One flow per file (recommended for clarity)
- Multiple flows per file (okay for related flows)
- Nested folders (good for organization)

---

### 3.4 Multiple Steps in a Flow

Flows can have multiple steps, executed in order. This is useful for:
- Providing context before answering
- Giving multiple pieces of information
- Creating multi-part responses

#### Example: Greet Then Help

```yaml
flows:
  greet_and_help:
    name: greet and show help
    description: Greet the user and then show what the bot can do.
    steps:
      - action: utter_greet
      - action: utter_help
```

**Execution Order**:
1. Bot says the greet message
2. Bot says the help message
3. Flow completes

#### Exercise 3.1: Multi-Step Flow

**Task**: Modify `greet.yml` to have two steps:
1. First: `utter_greet`
2. Second: `utter_help`

**Before You Begin**:
- ✅ You understand how flows work
- ✅ You know where `data/basics/greet.yml` is located
- ✅ The responses `utter_greet` and `utter_help` exist in your domain

**Steps**:
1. Open `data/basics/greet.yml` in your editor
2. Find the `steps:` section (it should have one step: `- action: utter_greet`)
3. Add a second step: `- action: utter_help`
   - Make sure it's at the same indentation level as the first step
   - Use a dash (`-`) before `action:`
4. Save the file

**Expected Result**:
```yaml
flows:
  greet:
    name: say hello
    description: Greet the user when they start a conversation.
    steps:
      - action: utter_greet
      - action: utter_help
```

**How to Verify**:
1. ✅ Both steps are at the same indentation level (4 spaces from the left)
2. ✅ Both steps start with `- action:`
3. ✅ Both response names exist in your domain file
4. ✅ YAML syntax is correct (no errors when you save)
5. ✅ Try training your bot - if training succeeds, your flow is correct!

**What Happens**: When a user says "hello", the bot will:
1. First greet them (`utter_greet`)
2. Then immediately show the help message (`utter_help`)
3. Flow completes

This creates a more helpful greeting experience!

---

### 3.5 Flow Descriptions and LLM Understanding

The `description` field is **critical** because the LLM uses it to match user messages to flows.

#### How It Works

1. User sends a message: "I need help"
2. LLM reads all flow descriptions
3. LLM matches the message to the best-fitting description
4. Rasa triggers that flow

#### Writing Good Descriptions

✅ **Good descriptions**:
- Clear and specific: "Greet the user when they start a conversation"
- Action-oriented: "Provide contact information for the bank"
- Context-aware: "Explain what the bot can help with"

❌ **Bad descriptions**:
- Too vague: "Help user" (what kind of help?)
- Too specific: "Respond when user says exactly 'hello'" (misses "hi", "hey")
- Missing context: "Say hello" (when? why?)

#### Example: Matching Process

**Flow Description**: "Greet the user when they start a conversation"

**User Messages That Match**:
- "hello"
- "hi"
- "hey there"
- "good morning"
- "greetings"

**Why**: The LLM understands all these are greetings that start conversations.

#### Exercise 3.2: Writing Descriptions

**Task**: For each of these flows, write a good description:

1. A flow that provides bank hours
2. A flow that explains how to check balance
3. A flow that lists available services

**Example Solutions**:

1. `description: "Tell the user when the bank is open and what the operating hours are."`
2. `description: "Explain the process for checking account balance, including what information is needed."`
3. `description: "List all the services and features the bot can help with."`

**Key**: Be specific about what the flow does, not how the user asks for it.

---

## Module 4: System Patterns

### 4.1 What are System Patterns?

**System patterns** are special flows that Rasa uses internally to manage conversation lifecycle. They're not user-facing flows, but rather system-level behaviors.

**File Location**: `data/system/patterns/patterns.yml`

**Analogy**: System patterns are like the operating system of your bot - they handle the "behind the scenes" stuff.

#### Two Key Patterns

1. **`pattern_session_start`**: What happens when a conversation begins
2. **`pattern_completed`**: What happens when a flow finishes

---

### 4.2 Session Start Pattern

The `pattern_session_start` flow automatically triggers when a new conversation begins.

#### How It Works

```yaml
flows:
  pattern_session_start:
    description: Start the conversation with a greeting
    name: pattern session start
    nlu_trigger:
      - intent: session_start
    steps:
      - action: utter_greet
```

#### Breaking It Down

1. **`pattern_session_start`**: Special name Rasa recognizes
   - Must be exactly this name
   - Rasa automatically triggers this on new conversations

2. **`nlu_trigger: - intent: session_start`**: When to trigger
   - `session_start` is a special intent Rasa generates
   - Triggers automatically when conversation begins
   - No user message needed

3. **`steps: - action: utter_greet`**: What to do
   - Executes when pattern triggers
   - In this case, greets the user

#### Conversation Flow

```
User opens chat
    ↓
Rasa detects new session
    ↓
pattern_session_start triggers automatically
    ↓
Bot says utter_greet
    ↓
User sees: "Hi! I'm a banking assistant..."
```

**Key Point**: The user doesn't need to say anything - the bot greets them automatically.

---

### 4.3 Pattern Completed

The `pattern_completed` flow handles what happens when a flow finishes.

```yaml
flows:
  pattern_completed:
    description: A flow has been completed and there is nothing else to be done
    steps:
      - noop: true
        next: END
```

#### Breaking It Down

1. **`pattern_completed`**: Special name Rasa recognizes
   - Must be exactly this name
   - Triggers when a flow completes

2. **`- noop: true`**: No operation
   - `noop` means "no operation" - do nothing
   - Just a placeholder step

3. **`next: END`**: End the conversation
   - Tells Rasa the conversation is complete
   - Bot waits for next user message

#### When It Triggers

After any flow completes, if there's nothing else to do, `pattern_completed` runs and the conversation ends (waits for next input).

---

### 4.4 Modifying System Patterns

You can customize system patterns to change default behavior.

#### Example: Enhanced Session Start

Instead of just greeting, you might want to greet AND show help:

```yaml
flows:
  pattern_session_start:
    description: Start the conversation with a greeting
    name: pattern session start
    nlu_trigger:
      - intent: session_start
    steps:
      - action: utter_greet
      - action: utter_help
```

**Result**: When a user opens the chat, they see both the greeting and the help message.

#### Exercise 4.1: Customize Session Start

**Task**: Modify `pattern_session_start` to greet the user and provide contact information.

**Steps**:
1. Open `data/system/patterns/patterns.yml`
2. Find `pattern_session_start`
3. Add a second step: `- action: utter_contact`
4. Save and test

**Expected Result**:
```yaml
pattern_session_start:
  description: Start the conversation with a greeting
  name: pattern session start
  nlu_trigger:
    - intent: session_start
  steps:
    - action: utter_greet
    - action: utter_contact
```

**What Happens**: New conversations start with greeting, then contact info.

---

## Module 5: Configuration Files

### 5.1 The config.yml File

The `config.yml` file tells Rasa **how to build your bot**. It's like the blueprint that defines the bot's architecture.

**File Location**: `config.yml` (root of your bot folder)

#### Complete config.yml Breakdown

```yaml
recipe: default.v1
language: en
assistant_id: level1-bot

pipeline:
  - name: SearchReadyLLMCommandGenerator
    llm:
      model_group: gpt-4o-mini

policies:
  - name: FlowPolicy
```

#### Section-by-Section Explanation

1. **`recipe: default.v1`**
   - Which Rasa recipe to use
   - `default.v1` is the standard Rasa Pro recipe
   - Recipes define the default configuration

2. **`language: en`**
   - The language your bot speaks
   - `en` = English
   - Change to `es` for Spanish, `fr` for French, etc.

3. **`assistant_id: level1-bot`**
   - Unique identifier for this bot
   - Used in logs and tracking
   - Should be unique if you have multiple bots

4. **`pipeline:`**
   - Defines how Rasa understands user messages
   - `SearchReadyLLMCommandGenerator`: Uses an LLM to understand natural language
   - `model_group: gpt-4o-mini`: Which LLM to use (OpenAI's GPT-4o-mini)

5. **`policies:`**
   - Defines how Rasa decides what to do next
   - `FlowPolicy`: Uses the flows you defined to decide responses
   - This is what makes your flows actually work

#### Simplified Mental Model

```
config.yml = "How to build this bot"
  ├── recipe: "Use Rasa Pro standard recipe"
  ├── language: "English"
  ├── assistant_id: "level1-bot (unique name)"
  ├── pipeline: "Use LLM to understand messages"
  └── policies: "Use flows to decide responses"
```

---

### 5.2 credentials.yml

The `credentials.yml` file defines **how the bot connects to chat interfaces**.

**File Location**: `credentials.yml` (root of your bot folder)

#### Complete credentials.yml Breakdown

```yaml
rest:

socketio:
  bot_message_evt: bot_uttered
  session_persistence: true
  user_message_evt: user_uttered
```

#### Section-by-Section Explanation

1. **`rest:`** (empty)
   - Enables REST API access
   - Allows programmatic access to the bot
   - Empty means "use defaults"

2. **`socketio:`**
   - Enables Socket.IO interface
   - This is what Inspector uses for testing
   - Required for the web-based testing interface

3. **`bot_message_evt: bot_uttered`**
   - Event name when bot sends a message
   - Technical detail - usually don't need to change

4. **`session_persistence: true`**
   - Keeps conversation state between messages
   - Required for multi-turn conversations
   - Should always be `true`

5. **`user_message_evt: user_uttered`**
   - Event name when user sends a message
   - Technical detail - usually don't need to change

#### When You'd Modify This

- **Add Slack**: Add a `slack:` section with your Slack credentials
- **Add Teams**: Add a `msteams:` section
- **Add custom channel**: Add your custom channel configuration

For Level 1, you typically don't need to modify this file.

---

### 5.3 endpoints.yml

The `endpoints.yml` file defines **where Rasa can find actions, tools, and LLM configuration**.

**File Location**: `endpoints.yml` (root of your bot folder)

#### Complete endpoints.yml Breakdown

```yaml
action_endpoint:
  actions_module: "actions"

nlg:
  type: rephrase
  llm:
    model_group: gpt-4o-mini

model_groups:
  - id: gpt-4o-mini
    models:
      - provider: openai
        model: gpt-4o-mini-2024-07-18
        temperature: 0.3
```

#### Section-by-Section Explanation

1. **`action_endpoint:`**
   - Tells Rasa where to find custom actions
   - `actions_module: "actions"` means "look in the `actions/` folder"
   - For Level 1, this folder is empty (no actions yet)

2. **`nlg:`** (Natural Language Generation)
   - Defines how responses are generated
   - `type: rephrase`: Allows LLM to rephrase responses
   - This is why `rephrase: True` in responses works
   - `model_group: gpt-4o-mini`: Which LLM to use for rephrasing

3. **`model_groups:`**
   - Defines LLM configurations
   - `id: gpt-4o-mini`: Name of this model group
   - `provider: openai`: Which LLM provider to use
   - `model: gpt-4o-mini-2024-07-18`: Specific model version
   - `temperature: 0.3`: How creative the LLM should be (0.0 = deterministic, 1.0 = very creative)

#### Understanding `actions_module`

When you write `actions_module: "actions"`, Rasa:
1. Looks for a folder named `actions/`
2. Looks for Python files in that folder
3. Looks for classes that inherit from `Action`
4. Makes those available as actions in your flows

For Level 1, the `actions/` folder doesn't exist yet (we'll create it in Level 2).

---

### Exercise 5.1: Configuration Exploration

**Task**: Answer these questions by examining the configuration files:

1. What language is the bot configured for?
2. What LLM model is being used?
3. Where would Rasa look for custom actions?
4. What does `temperature: 0.3` mean for the LLM?

**Answers**:
1. English (`language: en`)
2. GPT-4o-mini (`model: gpt-4o-mini-2024-07-18`)
3. The `actions/` folder (`actions_module: "actions"`)
4. The LLM will be somewhat creative but mostly consistent (0.3 is relatively low, meaning less randomness)

---

## Module 6: Training and Testing

### 6.1 What is Training?

**Training** is the process of building your bot's "brain" - converting your flows, domain, and configuration into a runnable model.

#### What Happens During Training

When you run `rasa train`, Rasa:

1. **Reads all flows** from `data/` folder
   - Scans for `.yml` files
   - Parses flow definitions
   - Builds a flow graph

2. **Reads the domain** from `domain/` folder
   - Loads all responses
   - Loads all slots (none in Level 1)
   - Loads all actions (none in Level 1)

3. **Applies configuration** from `config.yml`
   - Sets up the pipeline (LLM for understanding)
   - Sets up policies (FlowPolicy for decision-making)
   - Configures language and other settings

4. **Creates a model file**
   - Saves everything to `models/` folder
   - File name includes timestamp: `20250112-120817-descent-lard.tar.gz`
   - This is the "compiled" version of your bot

**Analogy**: Training is like compiling code. Your flows/domain are source code, training creates the executable.

---

### 6.2 How to Train Your Bot

#### Prerequisites

Before training, ensure:
1. ✅ Virtual environment is activated
2. ✅ Environment variables are loaded (`.env` file)
3. ✅ All YAML files have correct syntax
4. ✅ All responses referenced in flows exist in domain

#### Training Command

```powershell
# Option 1: Manual training
python -m rasa train

# Option 2: Using the helper script (recommended)
powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
# (This script trains AND starts Inspector)
```

#### What You'll See

When training starts, you'll see output like:

```
Training Core model...
2025-01-12 12:08:17 INFO     rasa.core.training  - Training FlowPolicy...
2025-01-12 12:08:17 INFO     rasa.core.training  - FlowPolicy training completed.
2025-01-12 12:08:17 INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'.
```

#### Understanding the Output

- **"Training Core model"**: Building the conversation logic
- **"Training FlowPolicy"**: Processing your flows
- **"Successfully saved model"**: Training completed, model saved

#### Common Training Errors

When training fails, the error message usually tells you what went wrong. Here are the most common errors and how to fix them.

---

**1. YAML Syntax Error**

**What you'll see:**
```
Error: while parsing a block mapping
expected <block end>, but found '<block mapping start>'
  in "<unicode string>", line 5, column 3
```

**What this means (plain language):**
Rasa couldn't understand your YAML file because the syntax is wrong. Usually this means incorrect indentation, missing colons, or missing dashes.

**Why it happens:**
- You used tabs instead of spaces
- You used 4 spaces instead of 2 spaces
- You forgot a colon after a key
- You forgot a dash before a list item
- You mixed different indentation styles

**How to fix it:**

1. **Check the line number mentioned in the error** (e.g., "line 5, column 3")
   - Go to that line in your file
   - Check the indentation and syntax

2. **Verify indentation:**
   - Use exactly 2 spaces (not tabs, not 4 spaces)
   - Enable "show whitespace" in your editor if possible
   - Make sure all levels are consistent

3. **Common fixes:**
   ```yaml
   # ❌ WRONG: Missing colon
   utter_greet
     - text: "Hello"
   
   # ✅ CORRECT: Has colon
   utter_greet:
     - text: "Hello"
   ```

   ```yaml
   # ❌ WRONG: Missing dash
   steps:
     action: utter_greet
   
   # ✅ CORRECT: Has dash
   steps:
     - action: utter_greet
   ```

   ```yaml
   # ❌ WRONG: Wrong indentation (4 spaces)
   responses:
       utter_greet:
   
   # ✅ CORRECT: Correct indentation (2 spaces)
   responses:
     utter_greet:
   ```

**How to verify the fix:**
- Save your file
- Try training again
- If the error persists, check the line number mentioned

---

**2. Response Not Found Error**

**What you'll see:**
```
Error: Response 'utter_xyz' not found in domain
```

**What this means (plain language):**
A flow is trying to use a response called `utter_xyz`, but that response doesn't exist in your domain file.

**Why it happens:**
- You referenced a response in a flow that you haven't created yet
- You made a typo in the response name (e.g., `utter_greet` vs `utter_greets`)
- You forgot to define the response in the domain file
- The response exists but in a different file

**How to fix it:**

1. **Find where the response is referenced:**
   - Search your `data/` folder for `utter_xyz`
   - Find which flow is trying to use it

2. **Check if the response exists:**
   - Open `domain/basics.yml`
   - Search for `utter_xyz`
   - Verify the spelling matches exactly (case-sensitive!)

3. **Two options to fix:**
   
   **Option A: Add the missing response** (if you intended to use it)
   ```yaml
   # In domain/basics.yml, add:
   utter_xyz:
     - text: "Your message here"
       metadata:
         rephrase: True
   ```
   
   **Option B: Fix the flow** (if you made a typo)
   ```yaml
   # In your flow file, change:
   - action: utter_xyz  # ❌ Wrong name
   
   # To:
   - action: utter_greet  # ✅ Correct name
   ```

**How to verify the fix:**
- Check that the response name in the flow exactly matches the response name in the domain
- Try training again
- The error should disappear

---

**3. Import Error / Module Not Found**

**What you'll see:**
```
Error: No module named 'rasa'
```
or
```
ModuleNotFoundError: No module named 'rasa'
```

**What this means (plain language):**
Python can't find the Rasa library. This usually means Rasa isn't installed, or you're not using the correct Python environment.

**Why it happens:**
- You haven't installed Rasa Pro yet
- Your virtual environment isn't activated
- You're using the wrong Python interpreter
- Rasa was installed in a different environment

**How to fix it:**

1. **Check if your virtual environment is activated:**
   ```powershell
   # Your command prompt should show (.venv) at the beginning
   # If not, activate it:
   .\.venv\Scripts\Activate.ps1
   ```

2. **Verify Rasa is installed:**
   ```powershell
   python -m rasa --version
   # Should show version info (not an error)
   ```

3. **If Rasa is not installed:**
   ```powershell
   # Make sure venv is activated first!
   python -m pip install --no-cache-dir rasa-pro
   ```

4. **If using an IDE (VS Code, PyCharm):**
   - Make sure the IDE is using the correct Python interpreter
   - Select the Python interpreter from your `.venv` folder
   - Restart the IDE if needed

**How to verify the fix:**
- Run `python -m rasa --version` - should show version info
- Try training again - should work now

---

**4. Environment Variable Error**

**What you'll see:**
```
Error: RASA_LICENSE environment variable not set
```
or
```
Error: OPENAI_API_KEY not found
```

**What this means (plain language):**
Rasa needs your license and API keys, but it can't find them.

**Why it happens:**
- You haven't created a `.env` file
- You haven't loaded the environment variables
- The `.env` file has the wrong format
- The environment variables have placeholder values

**How to fix it:**

1. **Check if `.env` file exists:**
   - Should be in the root of your project folder
   - Should contain: `RASA_LICENSE=...` and `OPENAI_API_KEY=...`

2. **Verify the format:**
   ```text
   # ✅ CORRECT format:
   RASA_LICENSE=your-actual-license-here
   OPENAI_API_KEY=sk-your-actual-api-key-here
   
   # ❌ WRONG format:
   RASA_LICENSE="your-actual-license-here"  # No quotes needed
   RASA_LICENSE=your-rasa-pro-license  # Placeholder value
   ```

3. **Load the environment variables:**
   ```powershell
   # Before running Rasa commands:
   . .\load_env.ps1
   
   # Or use the helper script that does this automatically:
   powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
   ```

**How to verify the fix:**
- Check that `.env` file exists and has real values (not placeholders)
- Load environment variables before running Rasa commands
- Try training again

---

### 6.3 Using Rasa Inspector

**Inspector** is Rasa's built-in testing interface. It provides a web-based chat interface where you can test your bot.

#### Starting Inspector

```powershell
# After training, start Inspector
python -m rasa inspect --debug --log-file logs/logs.out
```

**Output**:
```
Starting Rasa server on http://0.0.0.0:5005
2025-01-12 12:08:17 INFO     rasa.server  - Starting Rasa server...
```

#### Opening Inspector

1. **Open your browser**
2. **Navigate to**: `http://localhost:5005/webhooks/socketio/inspect.html`
3. **You should see**: A chat interface

#### Inspector Interface Overview

Inspector opens in your browser with four main panes. Layout may vary (e.g. Chat on the left, debug panes on the right or below). Use them to see which flow and step run for each message and to debug when the bot doesn’t behave as expected.

1. **Chat Widget** (main chat area)
   - **Purpose:** Talk to your assistant and see its replies.
   - Type messages in the input box and send; the bot’s responses appear in the thread.
   - Full conversation history is shown in order.
   - The other panes update in real time as you send messages, so you can see which flow and step were chosen for each turn.

2. **Flow View** (flow diagram)
   - **Purpose:** See the currently active flow and which step the bot is on.
   - Shows the active flow as a flowchart and highlights the latest step.
   - You can click rows in the Stack View (see below) to jump to flows that were active at earlier points in the conversation.
   - **Restart conversation:** A button at the bottom (or in the pane) clears the conversation and starts a new one—useful for testing from a clean state.

3. **Stack View** (flow stack)
   - **Purpose:** See which flows are active and in what order (bottom-up, chronological).
   - Lists activated flows and their latest steps. The **topmost** row is the currently active flow step the bot is trying to complete; flows below it are paused until the one above finishes.
   - Each row typically shows: **Step ID** (matches your flow YAML), **Flow** (flow name from your flows), and **ID** (unique frame id).
   - Helps you confirm that the right flow ran for a given user message (e.g. “help” vs “contact”).

4. **Slots, End-2-End Test, and Tracker State** (data and debug)
   - **Slots:** Shows current slot values (conversation memory). **For Level 1 this is empty**—Level 1 has no slots. In later levels you’ll see collected values here.
   - **End-2-End Test:** Renders the current chat in Rasa’s end-to-end test format so you can copy it into a test file and turn the conversation into an automated test case.
   - **Tracker State:** Detailed event log: user messages, the command (flow/step) the model predicted, slots set, any repair patterns, and actions executed. Use this to debug when the wrong flow runs or an action doesn’t fire.

---

### 6.4 Testing Your Bot

#### Basic Testing Workflow

1. **Start Inspector** (see above)

2. **Test each flow**:
   - Type "hello" → Should trigger `greet` flow
   - Type "help" → Should trigger `help` flow
   - Type "contact" → Should trigger `contact` flow

3. **Observe the behavior**:
   - Does the correct flow trigger?
   - Does the bot say the expected response?
   - Are there any errors?

#### Example Test Session

```
You: hello
Bot: Hi! I'm a banking assistant. How can I help you today?

You: what can you do?
Bot: I can help you with:
     - Checking your balance
     - Transferring money
     - Bank hours
     - Contact information

You: how do I contact you?
Bot: You can reach us at support@bank.com or call 1-800-BANK-123.
```

#### Understanding Flow Triggers

The LLM uses flow descriptions to match user messages. For example:

- **Flow**: `greet` with description "Greet the user when they start a conversation"
- **User says**: "hello", "hi", "hey", "good morning"
- **Result**: All trigger the `greet` flow because the LLM understands they're greetings

#### Exercise 6.1: Comprehensive Testing

**Task**: Test your bot thoroughly:

1. Test the `greet` flow with 3 different greetings
2. Test the `help` flow with 3 different ways to ask for help
3. Test the `contact` flow with 3 different ways to ask for contact info
4. Test the `goodbye` flow (if you created it)

**Documentation**: For each test, note:
- What you said
- Which flow triggered
- What the bot responded
- Whether it matched your expectations

---

### 6.5 Understanding Bot Behavior

#### How the Bot Decides What to Do

Here's the complete flow of what happens when a user sends a message:

```
1. User sends message: "hello"
   ↓
2. Pipeline (LLM) processes message
   - Understands: "This is a greeting"
   - Extracts intent: greeting
   ↓
3. FlowPolicy searches flows
   - Reads all flow descriptions
   - Matches: "Greet the user when they start a conversation"
   - Selects: greet flow
   ↓
4. Flow executes
   - Step 1: utter_greet
   - Looks up response in domain
   - Finds: "Hi! I'm a banking assistant..."
   ↓
5. Bot responds
   - Sends message to user
   - Updates conversation state
   ↓
6. Flow completes
   - pattern_completed triggers
   - Conversation ends (waits for next input)
```

#### Visual Flow Diagram

```
User Message
    ↓
LLM Understanding (Pipeline)
    ↓
Flow Matching (FlowPolicy)
    ↓
Flow Execution
    ↓
Response Lookup (Domain)
    ↓
Bot Response
```

#### Why Flows Might Not Trigger

1. **Description doesn't match**: Flow description is too vague or specific
2. **LLM misunderstanding**: LLM doesn't recognize the user's intent
3. **No matching flow**: No flow exists for that type of request

#### Debugging Tips

1. **Check flow descriptions**: Are they clear and specific?
2. **Check debug output**: What did the LLM understand?
3. **Try different phrasings**: Does the flow trigger with other wordings?
4. **Check logs**: `logs/logs.out` contains detailed information

---

## Module 7: Putting It All Together

### 7.1 Complete Bot Walkthrough

Let's trace through a complete conversation from start to finish, showing how all the pieces fit together.

#### Conversation Example

```
[User opens chat - new session starts]

1. pattern_session_start triggers automatically
   ↓
   Flow: pattern_session_start
   Step: utter_greet
   ↓
Bot: "Hi! I'm a banking assistant. How can I help you today?"

[User types: "what can you help me with?"]

2. LLM understands: "User wants to know capabilities"
   ↓
   FlowPolicy matches to: help flow
   (Description: "Explain what the bot can do")
   ↓
   Flow: help
   Step: utter_help
   ↓
Bot: "I can help you with:
      - Checking your balance
      - Transferring money
      - Bank hours
      - Contact information"

[User types: "how do I contact support?"]

3. LLM understands: "User wants contact information"
   ↓
   FlowPolicy matches to: contact flow
   (Description: "Provide contact information for the bank")
   ↓
   Flow: contact
   Step: utter_contact
   ↓
Bot: "You can reach us at support@bank.com or call 1-800-BANK-123."

[User types: "thanks"]

4. LLM understands: "User is ending conversation"
   ↓
   FlowPolicy: No specific flow matches
   ↓
   Flow completes
   pattern_completed triggers
   ↓
   Conversation ends, waits for next input
```

#### File-by-File Trace

**When user says "hello"**:

1. **`data/system/patterns/patterns.yml`**
   - `pattern_session_start` triggers
   - Executes `utter_greet`

2. **`domain/basics.yml`**
   - Looks up `utter_greet` in `responses:`
   - Finds the text: "Hi! I'm a banking assistant..."

3. **`config.yml`**
   - Pipeline (LLM) understands the greeting
   - FlowPolicy selects the pattern

4. **Bot responds** with the greeting

**When user says "help"**:

1. **`data/basics/help.yml`**
   - Flow `help` is triggered
   - Description matches user intent

2. **`domain/basics.yml`**
   - Looks up `utter_help` in `responses:`
   - Finds the help text

3. **Bot responds** with help information

---

### 7.2 Your Level 1 Banking Bot: Summary

Congratulations! You've built a complete Level 1 banking bot. Let's review what you have:

#### Your Banking Bot Structure

**Domain (`domain/basics.yml`)**:
- `utter_greet` - Greets users as a banking assistant
- `utter_help` - Lists banking services (balance, transfers, hours, contact)
- `utter_contact` - Provides bank contact information

**Flows (`data/basics/`)**:
- `greet.yml` - Greets users when they start a conversation
- `help.yml` - Explains what the bot can help with
- `contact.yml` - Provides contact information for the bank

**System Patterns (`data/system/patterns/patterns.yml`)**:
- `pattern_session_start` - Automatically greets users when conversation begins
- `pattern_completed` - Handles flow completion

#### What Your Bot Can Do

Your Level 1 banking bot can:
- Greet users when they start a conversation
- Explain what services are available (balance checking, transfers, hours, contact)
- Provide bank contact information (email and phone)

#### Testing Your Bot

Try these conversations with your bot:
- "Hello" or "Hi" → Should trigger the greet flow
- "What can you do?" or "Help" → Should trigger the help flow
- "How can I contact you?" or "Contact" → Should trigger the contact flow

**Your bot is working correctly when**:
- Each flow triggers on appropriate user messages
- The bot responds with the correct messages
- All three flows work independently

#### What's Missing (Coming in Future Levels)

Your Level 1 bot cannot yet:
- Execute custom Python code (Level 2: Actions)
- Remember information from the conversation (Level 3: Slots)
- Collect multiple pieces of information (Level 4: Multiple Slots)
- Use dynamic tool calling (Level 5: Tools)

But you have a solid foundation! In Level 2, you'll add custom Python code (actions) to your existing banking bot.

---

### 7.3 Best Practices

#### Organizing Your Bot

1. **One flow per file**: Makes it easier to find and modify flows
2. **Descriptive names**: Use clear, descriptive flow and response names
3. **Group related flows**: Use folders to organize (e.g., `data/basics/`, `data/advanced/`)

#### Writing Good Responses

1. **Be clear and concise**: Users want information quickly
2. **Use variations**: Make the bot feel more natural
3. **Include context**: Help users understand what to do next

#### Writing Good Flow Descriptions

1. **Be specific**: "Provide contact information" not "Help user"
2. **Use action verbs**: "Tell", "Provide", "Explain"
3. **Include context**: What information does this flow provide?

#### Testing Strategy

1. **Test each flow individually**: Make sure each one works
2. **Test with variations**: Try different ways to ask for the same thing
3. **Test the full conversation**: Make sure flows work together
4. **Check for errors**: Look at logs if something doesn't work

---

## Module 8: Assessment and Next Steps

### 8.1 Knowledge Check

Test your understanding with these questions:

#### Question 1: What is a Flow?

a) A predefined bot message  
b) A conversation script with steps  
c) A Python function  
d) A configuration file

**Answer**: b) A conversation script with steps

**Explanation**: A flow is a step-by-step plan for how the bot should handle a conversation path. It contains steps (like `utter_*` actions) that execute in order.

---

#### Question 2: Where are Responses Defined?

a) `data/basics/*.yml`  
b) `domain/basics.yml`  
c) `config.yml`  
d) `actions/*.py`

**Answer**: b) `domain/basics.yml`

**Explanation**: Responses are defined in the domain file under the `responses:` section. Flows (in `data/`) reference these responses, but don't define them.

---

#### Question 3: What Triggers `pattern_session_start`?

a) User says "hello"  
b) A flow completes  
c) A new conversation begins  
d) User asks for help

**Answer**: c) A new conversation begins

**Explanation**: `pattern_session_start` is a special system pattern that automatically triggers when a new conversation session begins. The user doesn't need to say anything - it happens automatically.

---

#### Question 4: What Does `rephrase: True` Do?

a) Makes the bot remember previous messages  
b) Allows the LLM to vary the wording of responses  
c) Forces the bot to use exact text  
d) Enables custom Python code

**Answer**: b) Allows the LLM to vary the wording of responses

**Explanation**: `rephrase: True` in the metadata tells the LLM it can rephrase the response text while keeping the same meaning. This makes the bot feel more natural.

---

#### Question 5: What is the Purpose of Flow Descriptions?

a) They're just comments for developers  
b) The LLM uses them to match user messages to flows  
c) They're required for YAML syntax  
d) They're displayed to users

**Answer**: b) The LLM uses them to match user messages to flows

**Explanation**: Flow descriptions are critical because the LLM reads them to understand what each flow does. When a user sends a message, the LLM matches it to the best-fitting flow description.

---

### 8.2 What You've Learned

#### Key Concepts

1. **Responses**: Predefined messages the bot can say, defined in the domain file
2. **Flows**: Conversation scripts that use responses, defined in data files
3. **Domain**: The bot's knowledge base (responses, slots, actions)
4. **System Patterns**: Special flows that handle conversation lifecycle
5. **Configuration**: Files that tell Rasa how to build and run the bot
6. **Training**: The process of building the bot's model from your files
7. **Testing**: Using Inspector to verify the bot works correctly

#### Skills You've Developed

- ✅ Can create responses in the domain file
- ✅ Can create flows that use responses
- ✅ Can understand how flows and responses connect
- ✅ Can train a bot from your files
- ✅ Can test a bot using Inspector
- ✅ Can debug when things don't work
- ✅ Can build a simple information bot from scratch

---

### 8.3 Limitations of Level 1

Level 1 bots have clear limitations:

#### What Level 1 Cannot Do

1. **Remember Information**: The bot cannot remember what the user said earlier
   - Example: User says "My account is 1234" → Bot forgets immediately

2. **Perform Calculations**: The bot cannot do math or calculations
   - Example: "What's 5 + 3?" → Bot cannot answer

3. **Access Databases**: The bot cannot look up information from databases
   - Example: "What's my balance?" → Bot cannot check a database

4. **Make API Calls**: The bot cannot call external services
   - Example: "What's the weather?" → Bot cannot call weather API

5. **Dynamic Responses**: All responses are static
   - Example: "What time is it?" → Bot cannot give current time

#### When Level 1 is Sufficient

Level 1 is perfect for:
- ✅ Static information bots (FAQs, contact info)
- ✅ Simple help systems
- ✅ Information-only assistants
- ✅ Basic routing bots

#### When You Need More

Move to Level 2 when you need:
- Custom Python code (actions)
- Dynamic responses
- Calculations or data processing

Move to Level 3 when you need:
- Memory (slots)
- Remembering user information
- Multi-turn conversations with context

---

### 8.4 What's Next: Level 2 Preview

⚠️ **Important: Building on Your Existing Banking Bot**

When you move to Level 2, you will **continue working on the same banking bot** you've built throughout Level 1. Level 2 doesn't start from scratch - it builds on what you've already created:

- **Your existing responses** (`utter_greet`, `utter_help`, `utter_contact`) stay in the domain
- **Your existing flows** (`greet`, `help`, `contact`) stay in `data/basics/`
- **Level 2 adds**: Custom Python actions, new flows that use actions, and action registration in the domain

**You don't start a new bot** - you extend your existing Level 1 banking bot with new capabilities!

---

**Level 2: Simple Actions** introduces custom Python code.

#### What Actions Enable

**Example Scenario**: "What are your bank hours?"

- **Level 1**: Bot would need a static `utter_hours` response (not implemented in Level 1)
- **Level 2**: Bot runs Python code (`action_bank_hours`) that:
  - Returns dynamic bank hours information
  - Can calculate or process data
  - Can integrate with external systems

In Level 2, you'll add `action_bank_hours` - a custom Python action that returns bank hours dynamically.

#### Key Concepts in Level 2

1. **Actions**: Python classes that execute custom code
2. **Action Registration**: Telling Rasa about your actions in the domain (`actions:` section)
3. **Action Execution**: How actions are called from flows (like `utter_*`, but with custom logic)
4. **Action Structure**: The `Action` class and `run()` method

#### Example Action You'll Create

In Level 2, you'll create `action_bank_hours.py`:

```python
class ActionBankHours(Action):
    def name(self) -> Text:
        return "action_bank_hours"
    
    def run(self, dispatcher, tracker, domain):
        # Custom Python code here
        dispatcher.utter_message("Our bank hours are...")
        return []
```

You'll also create a new flow `data/basics/hours.yml` that uses this action.

#### What You'll Learn in Level 2

- How to create custom Python actions
- How to register actions in `domain/basics.yml` under `actions:`
- How to call actions from flows (similar to `utter_*` but with custom code)
- The difference between responses (`utter_*`) and actions (`action_*`)

#### When to Move to Level 2

Move to Level 2 when you're ready to:
- Add custom Python code to your banking bot
- Create dynamic responses (beyond static text)
- Execute calculations or data processing
- Integrate with external systems

**Your Level 1 banking bot is the foundation** - Level 2 adds actions on top of it!

---

### 8.5 Course Completion Checklist

Before moving to Level 2, ensure you can:

- [ ] Explain what a response is and where it's defined
- [ ] Create a new response in the domain file
- [ ] Explain what a flow is and how it works
- [ ] Create a new flow that uses a response
- [ ] Understand how flows and responses connect
- [ ] Explain what system patterns do
- [ ] Understand the purpose of config.yml, credentials.yml, and endpoints.yml
- [ ] Successfully train a bot
- [ ] Test a bot in Inspector
- [ ] Debug when flows don't trigger correctly
- [ ] Understand how your Level 1 banking bot works

If you can check all these boxes, you're ready for Level 2!

---

## Troubleshooting Guide

### Common Issues and Solutions

#### Issue: Flow Not Triggering

**Symptoms**: User says something, but no flow executes.

**Possible Causes**:
1. Flow description doesn't match user intent
2. YAML syntax error in flow file
3. Flow not saved or not in correct location

**Solutions**:
1. Check flow description - make it more specific
2. Verify YAML syntax (indentation, colons)
3. Ensure flow file is in `data/` folder
4. Retrain the bot after making changes

---

#### Issue: Response Not Found Error

**Symptoms**: Training error: "Response 'utter_xyz' not found in domain"

**Possible Causes**:
1. Response not defined in domain
2. Typo in response name (flow vs domain)
3. Response defined but in wrong section

**Solutions**:
1. Check `domain/basics.yml` - is the response defined?
2. Verify spelling matches exactly (case-sensitive)
3. Ensure response is under `responses:` section

---

#### Issue: YAML Syntax Error

**Symptoms**: Training fails with "while parsing a block mapping" error

**Possible Causes**:
1. Incorrect indentation
2. Missing colons
3. Missing dashes in lists

**Solutions**:
1. Use 2 spaces for indentation (not tabs)
2. Ensure all keys end with colons
3. Ensure list items start with dashes
4. Use a YAML validator to check syntax

---

#### Issue: Inspector Won't Start

**Symptoms**: `rasa inspect` command fails or browser shows error

**Possible Causes**:
1. Port 5005 already in use
2. Model not trained
3. Credentials.yml misconfigured

**Solutions**:
1. Check if another process is using port 5005
2. Train the bot first: `rasa train`
3. Verify `credentials.yml` has `socketio:` section
4. Check logs for specific error messages

---

#### Issue: Bot Says Wrong Thing

**Symptoms**: Bot responds, but not with the expected response

**Possible Causes**:
1. Wrong flow triggered
2. Response text is wrong in domain
3. Multiple responses with similar names

**Solutions**:
1. Check which flow actually triggered (use debug output)
2. Verify response text in domain file
3. Check for duplicate response names
4. Ensure you retrained after making changes

---

## Additional Resources

### Extension Exercises

#### Exercise 1: Add More Response Variations

**Task**: Add 3 variations to each response in your domain file.

**Goal**: Make the bot feel more natural and less repetitive.

**Example**:
```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
  - text: "Hello! I'm here to help with your banking needs."
  - text: "Welcome! How can I assist you today?"
```

---

#### Exercise 2: Create Multi-Step Flows

**Task**: Create flows that have 2-3 steps each.

**Goal**: Learn how to chain multiple responses together.

**Example**:
```yaml
flows:
  welcome:
    name: welcome new user
    description: Welcome the user and show them what the bot can do.
    steps:
      - action: utter_greet
      - action: utter_help
      - action: utter_contact
```

---

#### Exercise 3: Build a Complex Information Bot

**Task**: Build a bot for a topic you're interested in (sports, movies, hobbies, etc.).

**Requirements**:
- At least 5 different responses
- At least 5 different flows
- Clear, descriptive flow descriptions
- Test all flows work correctly

**Goal**: Apply everything you've learned in a real project.

---

### Real-World Examples

#### Example 1: Company FAQ Bot

A simple bot that answers common questions:
- "What are your hours?"
- "Where are you located?"
- "How can I contact you?"
- "What services do you offer?"

**Perfect for**: Small businesses, customer service, information desks.

---

#### Example 2: Product Information Bot

A bot that provides product information:
- Product features
- Pricing information
- Availability
- Specifications

**Perfect for**: E-commerce, product support, sales assistance.

---

#### Example 3: Event Information Bot

A bot that provides event information:
- Event schedule
- Location and directions
- Ticket information
- Contact for questions

**Perfect for**: Conferences, festivals, community events.

---

## Conclusion

Congratulations! You've completed Level 1 and learned the fundamentals of building Rasa bots.

### What You Can Do Now

- Build simple information bots
- Create flows and responses
- Train and test bots
- Debug common issues
- Understand the basic Rasa architecture

### What's Coming Next

⚠️ **Important: Each Level Builds on the Previous**

Each level builds **recursively** on your existing banking bot:

- **Level 2**: Adds custom Python code (actions) to your existing Level 1 banking bot
- **Level 3**: Adds memory (slots) to your existing Level 2 banking bot  
- **Level 4**: Handles complex multi-step conversations in your existing Level 3 banking bot
- **Level 5**: Enables dynamic tool calling in your existing Level 4 banking bot

**You keep the same banking bot** throughout all levels - each level adds new capabilities without starting from scratch!

### Keep Learning

- Practice by building more bots
- Experiment with different flow structures
- Try different response variations
- Read the Rasa documentation
- Join the Rasa community

---

## Glossary

Quick reference for key terms used in this tutorial.

### A-D

**Action** (Level 2+): Custom Python code that the bot can execute. Actions are defined in Python files and can perform calculations, API calls, database queries, etc.

**CALM**: Conversational AI Language Model framework. Rasa Pro uses CALM to provide LLM-powered understanding and generation.

**Domain**: The bot's knowledge base. The domain file (`domain/basics.yml`) defines all responses, slots, and actions the bot can use.

**Flow**: A conversation script that defines step-by-step how the bot should handle a particular conversation path. Flows are defined in YAML files in the `data/` folder.

**Flow Description**: A text description that explains what a flow does. The LLM uses flow descriptions to match user messages to the correct flow.

**FlowPolicy**: The policy that Rasa uses to decide which flow to trigger based on user messages and flow descriptions.

---

### I-P

**Inspector**: Rasa's built-in web-based testing interface. Inspector allows you to test your bot in a chat interface.

**LLM** (Large Language Model): The AI model (like GPT-4o-mini) that understands user messages and generates responses.

**Metadata**: Optional configuration for responses. The `rephrase: True` setting in metadata allows the LLM to vary response wording.

**NLU** (Natural Language Understanding): The bot's ability to understand what users mean, even when they phrase things differently.

**Pattern**: Special system-level flows that handle conversation lifecycle:
- `pattern_session_start`: Triggers when a new conversation begins
- `pattern_completed`: Triggers when a flow completes

**Pipeline**: The sequence of components Rasa uses to process user messages (e.g., LLM for understanding).

**Policy**: The component that decides what the bot should do next (e.g., which flow to trigger).

---

### R-T

**Response**: A predefined message the bot can send to users. Responses are defined in the domain file under the `responses:` section.

**Rephrase**: A metadata setting (`rephrase: True`) that allows the LLM to vary the wording of responses while keeping the same meaning.

**Slot** (Level 3+): A memory variable that stores information from the conversation (e.g., user's name, account number).

**Step**: A single action within a flow. Steps execute in order. In Level 1, steps are typically `- action: utter_*` actions.

**System Pattern**: Special flows that Rasa uses internally to manage conversation lifecycle (e.g., `pattern_session_start`, `pattern_completed`).

**Training**: The process of building your bot's model from your flows, domain, and configuration files. Running `rasa train` creates a model file in the `models/` folder.

---

### U-Y

**`utter_*`**: The naming convention for responses. All responses start with `utter_` (e.g., `utter_greet`, `utter_help`). The `utter_` prefix is a Rasa convention.

**YAML**: Yet Another Markup Language. A human-readable format for configuration files. All Rasa bot files use YAML format.

---