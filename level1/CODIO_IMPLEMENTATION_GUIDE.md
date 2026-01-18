# Level 1: Just Responses - Complete Codio Course Guide

**Complete Course Content and Implementation Guide for Codio Platform**

**Purpose**: This document serves as both:
- **Complete course content** for students (all tutorial content integrated)
- **Implementation guide** for the Codio team (technical specifications and deployment details)

**Target Audiences**: 
- Students learning to build their first Rasa bot
- Codio team members implementing the course
- Course developers and instructional designers

**Date**: January 2025

---

## Table of Contents

### For Students
- [Course Introduction](#course-introduction)
- [Unit 0: Prerequisites and Setup](#unit-0-prerequisites-and-setup)
- [Unit 1: Introduction to Rasa Bots](#unit-1-introduction-to-rasa-bots)
- [Unit 2: Understanding the Domain File](#unit-2-understanding-the-domain-file)
- [Unit 3: Understanding Flows](#unit-3-understanding-flows)
- [Unit 4: System Patterns](#unit-4-system-patterns)
- [Unit 5: Configuration Files](#unit-5-configuration-files)
- [Unit 6: Training and Testing](#unit-6-training-and-testing)
- [Unit 7: Putting It All Together](#unit-7-putting-it-all-together)
- [Unit 8: Assessment and Next Steps](#unit-8-assessment-and-next-steps)
- [Troubleshooting Guide](#troubleshooting-guide)
- [Additional Resources](#additional-resources)
- [Glossary](#glossary)

### For Codio Team
- [Implementation Overview](#implementation-overview-for-codio-team)
- [Technical Specifications](#technical-specifications-for-codio-team)
- [Unit-by-Unit Implementation Notes](#unit-by-unit-implementation-notes)
- [Auto-Grading Specifications](#auto-grading-specifications)
- [AI Coach Configuration](#ai-coach-configuration-reference)
- [Code Playback Configuration](#code-playback-configuration)
- [Assessment Specifications](#assessment-specifications)
- [Implementation Phases](#implementation-phases)
- [Quality Assurance Checklist](#quality-assurance-checklist)

---

## Course Introduction

### Welcome to Level 1: Just Responses

**A Complete Guide to Building Your First Rasa Bot**

This course teaches you how to build your first conversational bot using Rasa Pro. By the end of this course, you'll have created a working banking assistant bot that can greet users, provide information, and handle basic conversations.

### What You'll Learn

In this course, you will:
- Understand what a Rasa bot is and how it works
- Create bot responses in the domain file
- Create flows that trigger responses
- Configure system patterns for conversation lifecycle
- Train and test a working bot

### Prerequisites

Before starting, you should:
- Have basic Python knowledge (variables, strings, lists)
- Be comfortable with command line basics
- Be able to edit text files in an IDE

### Time Commitment

This course takes **2-3 hours** to complete thoroughly. Plan to work through it without rushing.

### Course Structure

This course is organized into **8 units** (0-7), plus assessment (Unit 8):
- **Unit 0**: Prerequisites and Setup (environment verification)
- **Unit 1**: Introduction to Rasa Bots (concepts)
- **Unit 2**: Understanding the Domain File (responses)
- **Unit 3**: Understanding Flows (conversation scripts)
- **Unit 4**: System Patterns (session lifecycle)
- **Unit 5**: Configuration Files (bot architecture)
- **Unit 6**: Training and Testing (making it work)
- **Unit 7**: Putting It All Together (complete bot)
- **Unit 8**: Assessment and Next Steps (knowledge check, Level 2 preview)

---

# Unit 0: Prerequisites and Setup

## For Students

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

**Note for Codio Students**: Your environment is pre-configured! Skip to [Lab 0.1: Verify Your Environment](#lab-01-verify-your-environment) to confirm everything is set up.

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

### Lab 0.1: Verify Your Environment

**Objective**: Confirm your Codio environment is set up correctly.

**For Codio Students**: Your environment is pre-configured. This lab helps you verify everything works.

#### Steps

1. **Verify Python and Rasa Pro**
   ```bash
   python -m rasa --version
   ```
   You should see version information (no errors).

2. **Check Environment Variables**
   ```bash
   # Check .env file exists
   ls -la .env
   # or on Windows
   dir .env
   ```
   The `.env` file should exist in your project root.

3. **Verify Project Structure**
   - Check that `domain/` folder exists
   - Check that `data/` folder exists
   - Check that `config.yml`, `credentials.yml`, and `endpoints.yml` exist

4. **Test Training (Optional)**
   ```bash
   python -m rasa train
   ```
   Training should complete successfully and create a model file in `models/`.

---

### 0.5 Getting Help

**Stuck?** Here are resources:

- **Rasa Documentation**: [https://rasa.com/docs](https://rasa.com/docs)
- **Error Messages**: Check the troubleshooting section at the end of this guide
- **Common Issues**: Most setup issues are covered in the troubleshooting guide
- **AI Coach**: Ask the AI Coach in Codio for help with any questions

---

## For Codio Team: Unit 0 Implementation Notes

**Type**: Setup Lab (Pre-configured environment)

**Codio Configuration Requirements**:
- Browser-based IDE with VSCode interface
- Python 3.11 pre-installed
- Rasa Pro pre-installed and configured
- Virtual environment pre-created and activated
- Environment variables pre-configured:
  - `RASA_LICENSE` (provided by instructor/student)
  - `OPENAI_API_KEY` (provided by instructor/student)
- All project files pre-populated in IDE

**Auto-grading for Lab 0.1**:
- ✅ `python -m rasa --version` returns version info
- ✅ `.env` file exists in project root
- ✅ Virtual environment is active (Python path check)
- ✅ Project structure is correct (domain/, data/, config files exist)

**AI Coach Configuration**:
- Context: "Student is setting up Rasa Pro environment"
- Common questions to handle:
  - "How do I activate the virtual environment?" → "Your environment is already activated in Codio. You can verify by checking the Python path."
  - "Where do I put my Rasa license?" → "Your `.env` file in the project root. The file should contain `RASA_LICENSE=your-license-here`."
  - "How do I verify Rasa is installed?" → "Run `python -m rasa --version` in the terminal."

**Deliverables**:
- Pre-configured lab environment specification
- Auto-grading script requirements
- Environment variable configuration guide

---

# Unit 1: Introduction to Rasa Bots

## For Students

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

### Concept Check 1.1: Identifying Bot Capabilities

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

## For Codio Team: Unit 1 Implementation Notes

**Type**: Guided Reading + Concept Check (Auto-graded)

**Content Strategy**:
- Preserve all conceptual content from TUTORIAL.md
- Use concise explanations but maintain clarity
- Include examples and analogies

**Auto-graded Assessment: Concept Check 1.1**

**Question 1**: Multiple choice
- "What is a conversational bot?"
- Options:
  - a) A computer program that follows strict rules
  - b) A program that can have natural, human-like conversations
  - c) A database query system
  - d) A web application
- Correct answer: b
- Points: 2

**Question 2**: True/False
- "Level 1 Rasa bots can remember information from earlier in the conversation."
- Correct answer: False
- Points: 1

**Question 3**: Multiple choice
- "What makes Level 1 bots different from advanced bots?"
- Options:
  - a) Level 1 bots use AI, advanced bots don't
  - b) Level 1 bots only use predefined responses, advanced bots can execute custom code
  - c) Level 1 bots are faster
  - d) There is no difference
- Correct answer: b
- Points: 2

**Total Points**: 5

**AI Coach Configuration**:
- Context: "Student is learning Rasa bot fundamentals"
- Common questions:
  - "How is a bot different from a regular program?" → "Bots can understand natural language and have conversations. Regular programs require specific commands."
  - "What can Level 1 bots do?" → "Level 1 bots can provide predefined information. They can't remember things or execute custom code yet."
  - "What are real-world examples of bots?" → "Customer service bots, FAQ assistants, information bots for companies or products."

**Deliverables**:
- Text content (markdown format)
- Assessment questions with answer keys
- Auto-grading configuration

---

# Unit 2: Understanding the Domain File

## For Students

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

### Lab 2.1: Understanding YAML Syntax for Responses

**Objective**: Learn YAML syntax by exploring existing responses.

#### Steps

1. **Open the Domain File**
   - Navigate to `domain/basics.yml` in your IDE
   - You should see existing responses like `utter_greet`, `utter_help`, and `utter_contact`

2. **Identify Response Structure**
   - Find the `responses:` section
   - Notice how each response is indented with 2 spaces
   - Notice the `-` (dash) before `text:`
   - Notice the `metadata:` section aligned with `text:`

3. **Explore Response Variations**
   - Check if any responses have multiple variations (multiple `- text:` items)
   - Notice how variations are at the same indentation level

**AI Coach**: If you're confused about YAML syntax, ask the AI Coach: "What does the dash before text: mean?" or "Why do I need metadata: rephrase: True?"

---

### Lab 2.2: Creating Your First Response

**Objective**: Add a new `utter_goodbye` response to your bot's domain file.

#### Before You Begin

✅ **Checklist**:
- You have a text editor or IDE open
- You know where the `domain/` folder is in your project
- You understand basic YAML syntax (review Unit 0.3 if needed)

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
- `rephrase` is spelled correctly

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

### 2.3 Response Variations

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

---

### Lab 2.3: Add Response Variations

**Objective**: Add a second variation to `utter_goodbye`.

**Before You Begin**:
- ✅ You've completed Lab 2.2 (created `utter_goodbye`)
- ✅ You have `domain/basics.yml` open in your editor

#### Steps

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
4. ✅ Try training your bot (we'll learn this in Unit 6) - if training succeeds, your YAML is correct!

**What This Means**: When `utter_goodbye` is used, Rasa will randomly select one of the two variations, making your bot feel more natural.

---

## For Codio Team: Unit 2 Implementation Notes

**Type**: Guided Lab + Auto-Graded Exercises

### Lab 2.1: Understanding YAML Syntax

**Content Structure**:
- Brief YAML Primer (integrated into Unit 0.3)
- Interactive exploration of existing responses

**Auto-graded Exercises**:
- **Exercise 1**: Identify all responses
  - Student lists all `utter_*` responses in file
  - **Auto-grading**: Checks list matches file contents
  - Points: 3
  
- **Exercise 2**: Explain metadata
  - Student explains what `rephrase: True` does
  - **Auto-grading**: Text analysis or multiple choice
  - Points: 2
  
- **Exercise 3**: Count variations
  - Student counts total response variations
  - **Auto-grading**: Checks count matches file
  - Points: 1

**Deliverables**:
- Pre-populated domain file
- Exercise specifications
- Auto-grading scripts for file analysis

### Lab 2.2: Creating Your First Response

**Type**: Hands-On Lab with Auto-Grading (Rubric-based)

**Content Structure**:
- Complete step-by-step instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Add `utter_goodbye` response

**Auto-Grading Rubric**:
- ✅ Correct YAML syntax (YAML file parses) (2 points)
- ✅ Proper indentation (2 spaces, not tabs) (2 points)
- ✅ Response name follows convention (`utter_goodbye`) (1 point)
- ✅ Includes `metadata: rephrase: True` (1 point)
- ✅ Response text is non-empty (1 point)
- ✅ Response is saved in correct file (`domain/basics.yml`) (1 point)
- ✅ Response is properly structured (correct nesting) (2 points)
- **Total**: 10 points

**Auto-Grading Implementation Requirements**:
1. Parse `domain/basics.yml` and validate YAML structure
2. Check for presence of `utter_goodbye` key
3. Validate indentation (count spaces, reject tabs)
4. Verify metadata structure exists
5. Check response is in correct file location
6. Provide specific error messages for each failed criterion

**Code Playback**: Enable for this lab (review how students create responses)

**AI Coach Configuration**:
- Context: "Student is creating their first bot response"
- Common issues to help with:
  - Indentation errors → "Check that you're using exactly 2 spaces (not tabs, not 4 spaces). Use your editor's 'show whitespace' feature."
  - Missing colons/dashes → "Remember: response names end with `:`, and list items start with `-`."
  - Wrong file location → "Make sure you're editing `domain/basics.yml`, not a different file."
  - YAML syntax errors → "Check the YAML syntax. Common issues: missing colons, wrong indentation, missing dashes."

**Deliverables**:
- Lab instructions (markdown)
- Auto-grading script specification
- Rubric criteria details
- Code Playback configuration

### Lab 2.3: Response Variations

**Type**: Hands-On Lab with Auto-Grading

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Add multiple variations to `utter_goodbye`

**Auto-Grading Rubric**:
- ✅ `utter_goodbye` has at least 2 variations (2 points)
- ✅ All variations have correct YAML structure (2 points)
- ✅ All variations have `rephrase: True` (2 points)
- ✅ Variations are different text (not duplicates) (2 points)
- **Total**: 8 points

**Deliverables**:
- Lab instructions
- Auto-grading specification
- Duplicate detection logic

---

---

# Unit 3: Understanding Flows

## For Students

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

### Lab 3.1: Exploring Existing Flows

**Objective**: Understand flow structure by examining existing flows.

#### Steps

1. **Navigate to the Data Folder**
   - Open the `data/basics/` folder in your IDE
   - You should see files like `greet.yml`, `help.yml`, and `contact.yml`

2. **Examine Flow Structure**
   - Open `greet.yml` and identify:
     - The `flows:` key
     - The flow identifier (`greet:`)
     - The `name:` field
     - The `description:` field (notice how it's written!)
     - The `steps:` section

3. **Compare Flows**
   - Open `help.yml` and `contact.yml`
   - Notice they all follow the same structure
   - Compare their descriptions - how are they different?

**AI Coach**: Ask questions like "Why does every flow need a description?" or "What happens if I remove the description field?"

---

### Lab 3.2: Creating Your First Flow

**Objective**: Create a new `goodbye.yml` flow that uses the `utter_goodbye` response from Lab 2.2.

#### Before You Begin

✅ **Checklist**:
- You've completed Lab 2.2 (created `utter_goodbye` in the domain)
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

### 3.3 Multiple Steps in a Flow

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

---

### Lab 3.3: Multi-Step Flow

**Objective**: Modify `greet.yml` to have two steps.

**Before You Begin**:
- ✅ You understand how flows work
- ✅ You know where `data/basics/greet.yml` is located
- ✅ The responses `utter_greet` and `utter_help` exist in your domain

#### Steps

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
5. ✅ Try training your bot (Unit 6) - if training succeeds, your flow is correct!

**What Happens**: When a user says "hello", the bot will:
1. First greet them (`utter_greet`)
2. Then immediately show the help message (`utter_help`)
3. Flow completes

This creates a more helpful greeting experience!

---

### 3.4 Flow Descriptions and LLM Understanding

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

---

### Lab 3.4: Flow Descriptions and LLM Matching

**Objective**: Practice writing good flow descriptions.

#### Task

For each of these scenarios, write a good flow description:

1. A flow that provides bank hours
2. A flow that explains how to check balance
3. A flow that lists available services

#### Example Solutions

1. `description: "Tell the user when the bank is open and what the operating hours are."`
2. `description: "Explain the process for checking account balance, including what information is needed."`
3. `description: "List all the services and features the bot can help with."`

**Key**: Be specific about what the flow does, not how the user asks for it.

**AI Coach**: Ask "How do I write a good flow description?" or "What makes a description too vague?"

---

## For Codio Team: Unit 3 Implementation Notes

**Type**: Guided Lab + Auto-Graded Exercises

### Lab 3.1: Exploring Existing Flows

**Type**: Exploration Lab with Auto-Grading

**Content Structure**:
- Pre-populated flow files in `data/basics/` folder
- Brief explanation of flow structure (preserved from TUTORIAL.md)

**Auto-graded Exercises**:
- **Exercise 1**: Match flow descriptions
  - Show flow names: `greet`, `help`, `contact`
  - Student matches to their purposes
  - **Auto-grading**: Validates matches
  - Points: 3
  
- **Exercise 2**: Identify flow components
  - Student identifies: name, description, steps in a flow
  - **Auto-grading**: Multiple choice or checklist
  - Points: 3
  
- **Exercise 3**: Explain description field
  - Student explains why `description:` is important
  - **Auto-grading**: Text analysis or multiple choice
  - Points: 2

**Deliverables**:
- Pre-populated flow files
- Exercise specifications
- Auto-grading configuration

### Lab 3.2: Creating Your First Flow

**Type**: Hands-On Lab with Auto-Grading (Rubric-based)

**Content Structure**:
- Complete step-by-step instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Create `goodbye.yml` flow

**Auto-Grading Rubric**:
- ✅ File created in correct location (`data/basics/`) (1 point)
- ✅ File has `flows:` key at top level (1 point)
- ✅ Flow identifier matches filename (`goodbye`) (1 point)
- ✅ Includes `name:` field (1 point)
- ✅ Includes `description:` field (2 points) - CRITICAL
- ✅ Includes `steps:` section (1 point)
- ✅ Step references existing response (`utter_goodbye`) (1 point)
- ✅ Correct YAML indentation (2 spaces) (2 points)
- ✅ YAML file parses correctly (2 points)
- **Total**: 12 points

**Auto-Grading Implementation Requirements**:
1. Check file exists in `data/basics/` directory
2. Parse YAML and validate structure
3. Check for required fields (name, description, steps)
4. Validate description field exists and is non-empty (critical!)
5. Verify step references existing response
6. Check indentation (2 spaces)
7. Provide specific error messages

**Code Playback**: Enable for this lab (critical - review flow creation)

**AI Coach Configuration**:
- Context: "Student is creating their first bot flow"
- Common issues:
  - Missing `description:` field (most common!) → "Every flow needs a description field. The LLM uses it to match user messages to your flow. Add `description: [what the flow does]` under the flow identifier."
  - Wrong file location → "Make sure you're creating the file in `data/basics/`, not in `data/` root."
  - Incorrect YAML structure → "Check your YAML syntax. Remember: use 2 spaces for indentation, add `flows:` at the top, and include `name:`, `description:`, and `steps:` fields."
  - Response reference doesn't exist → "Make sure the response `utter_goodbye` exists in `domain/basics.yml`. Check the spelling matches exactly (case-sensitive)."

**Deliverables**:
- Lab instructions (markdown)
- Auto-grading script specification
- Rubric details
- Code Playback configuration

### Lab 3.3: Multiple Steps in a Flow

**Type**: Hands-On Lab with Auto-Grading

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Create flow with multiple `utter_*` steps

**Auto-Grading Rubric**:
- ✅ Flow has at least 2 steps (2 points)
- ✅ All steps reference existing responses (2 points)
- ✅ Steps execute in correct order (2 points)
- ✅ Correct YAML structure (2 points)
- **Total**: 8 points

**Deliverables**:
- Lab instructions
- Auto-grading specification

### Lab 3.4: Flow Descriptions and LLM Matching

**Type**: Hands-On Lab with Auto-Grading

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Explain how `description:` field helps LLM match user messages
- Show examples of good vs bad descriptions

**Hands-On Exercise**:
- Student improves flow descriptions
- Or writes new descriptions for flows

**Auto-Grading**:
- Validates descriptions exist and are descriptive (not empty, >10 characters)
- Checks descriptions are unique
- Points: 5

**Deliverables**:
- Lab instructions
- Auto-grading specification for text validation

---

# Unit 4: System Patterns

## For Students

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

### Lab 4.1: Understanding System Patterns

**Objective**: Explore system patterns and understand their purpose.

#### Steps

1. **Open the Patterns File**
   - Navigate to `data/system/patterns/patterns.yml`
   - You should see both `pattern_session_start` and `pattern_completed`

2. **Examine `pattern_session_start`**
   - Notice it has `nlu_trigger: - intent: session_start`
   - Notice it automatically triggers (no user message needed)
   - Notice what step it executes

3. **Examine `pattern_completed`**
   - Notice it has `noop: true` and `next: END`
   - Understand this marks the end of a conversation

**AI Coach**: Ask "When does pattern_session_start trigger?" or "What happens if I remove pattern_completed?"

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

---

### Lab 4.2: Modifying System Patterns

**Objective**: Modify `pattern_session_start` to greet the user and provide contact information.

#### Steps

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

## For Codio Team: Unit 4 Implementation Notes

### Lab 4.1: Understanding System Patterns

**Type**: Exploration Lab with Auto-Grading

**Content Structure**:
- Pre-populated `data/system/patterns/patterns.yml` file
- Brief explanation (preserved from TUTORIAL.md)

**Auto-graded Exercises**:
- **Exercise 1**: Explain `pattern_session_start`
  - Student explains purpose
  - **Auto-grading**: Text analysis or multiple choice
  - Points: 2
  
- **Exercise 2**: Explain `pattern_completed`
  - Student explains purpose
  - **Auto-grading**: Text analysis or multiple choice
  - Points: 2
  
- **Exercise 3**: Identify when patterns trigger
  - Student identifies trigger points
  - **Auto-grading**: Multiple choice
  - Points: 2

**Deliverables**:
- Pre-populated patterns file
- Exercise specifications

### Lab 4.2: Modifying System Patterns

**Type**: Hands-On Lab with Auto-Grading

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Modify greeting message in `pattern_session_start`

**Auto-Grading Rubric**:
- ✅ Changes are saved correctly (2 points)
- ✅ Response reference is valid (2 points)
- ✅ YAML structure is correct (2 points)
- **Total**: 6 points

**Code Playback**: Enable for this lab

**Deliverables**:
- Lab instructions
- Auto-grading specification

---

# Unit 5: Configuration Files

## For Students

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

### Lab 5.1: Configuration Exploration

**Objective**: Understand configuration files by exploring them.

#### Task

Answer these questions by examining the configuration files:

1. What language is the bot configured for?
2. What LLM model is being used?
3. Where would Rasa look for custom actions?
4. What does `temperature: 0.3` mean for the LLM?

#### Answers

1. English (`language: en`)
2. GPT-4o-mini (`model: gpt-4o-mini-2024-07-18`)
3. The `actions/` folder (`actions_module: "actions"`)
4. The LLM will be somewhat creative but mostly consistent (0.3 is relatively low, meaning less randomness)

---

## For Codio Team: Unit 5 Implementation Notes

**Type**: Exploration Lab with Auto-Grading

**Content Structure**:
- Pre-populated config files (`config.yml`, `credentials.yml`, `endpoints.yml`)
- Brief explanation of each file (preserved from TUTORIAL.md)

**Auto-graded Exercises**:
- **Exercise 1**: Identify file purposes
  - Student matches files to their purposes
  - **Auto-grading**: Multiple choice
  - Points: 3
  
- **Exercise 2**: Explain key sections
  - Student explains important sections in each file
  - **Auto-grading**: Multiple choice or text analysis
  - Points: 5

**Content Strategy**: 
- Minimal text - "learn by exploring"
- AI Coach available for questions

**Deliverables**:
- Pre-populated config files
- Exercise specifications

---

# Unit 6: Training and Testing

## For Students

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
1. ✅ Virtual environment is activated (for Codio: already active)
2. ✅ Environment variables are loaded (`.env` file)
3. ✅ All YAML files have correct syntax
4. ✅ All responses referenced in flows exist in domain

#### Training Command

```bash
# In Codio terminal:
python -m rasa train
```

**For Codio Students**: Your environment is pre-configured. Just run the training command.

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

**AI Coach**: Ask "How do I fix a YAML syntax error?" or "What does 'block mapping' error mean?"

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

**AI Coach**: Ask "Why is my response not found?" or "How do I check if a response exists?"

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

**For Codio Students**: This shouldn't happen - Rasa Pro is pre-installed. If you see this error, ask the AI Coach for help.

**How to fix it (if not using Codio):**

1. **Check if your virtual environment is activated:**
   ```bash
   # Your command prompt should show (.venv) at the beginning
   # If not, activate it:
   source .venv/bin/activate  # Linux/Mac
   # or
   .venv\Scripts\Activate.ps1  # Windows
   ```

2. **Verify Rasa is installed:**
   ```bash
   python -m rasa --version
   # Should show version info (not an error)
   ```

3. **If Rasa is not installed:**
   ```bash
   # Make sure venv is activated first!
   python -m pip install --no-cache-dir rasa-pro
   ```

**AI Coach**: Ask "How do I check if Rasa is installed?" or "Why do I get 'module not found' error?"

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

**For Codio Students**: The `.env` file should be pre-configured. If you see this error, check that the `.env` file exists and has real values (not placeholders).

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

**How to verify the fix:**
- Check that `.env` file exists and has real values (not placeholders)
- Try training again

**AI Coach**: Ask "Where do I put my Rasa license?" or "How do I set environment variables?"

---

### Lab 6.1: Training Your Bot

**Objective**: Train your bot and verify it works.

#### Steps

1. **Run Training Command**
   ```bash
   python -m rasa train
   ```
   Wait for training to complete.

2. **Check for Errors**
   - If training fails, read the error message
   - Common errors are explained above
   - Ask AI Coach if you're stuck

3. **Verify Model Created**
   - Check that `models/` folder contains a new `.tar.gz` file
   - The file should have a timestamp in its name

4. **What Success Looks Like**
   - You see "Successfully saved model" message
   - No error messages
   - Model file exists in `models/` folder

**AI Coach**: Ask "How do I know training succeeded?" or "What should I see when training works?"

---

### 6.3 Using Rasa Inspector

**Inspector** is Rasa's built-in testing interface. It provides a web-based chat interface where you can test your bot.

#### Starting Inspector

```bash
# After training, start Inspector
python -m rasa inspect --debug --log-file logs/logs.out
```

**Output**:
```
Starting Rasa server on http://0.0.0.0:5005
2025-01-12 12:08:17 INFO     rasa.server  - Starting Rasa server...
```

#### Opening Inspector

1. **In Codio**: Inspector should be accessible through port forwarding
2. **Navigate to**: The Inspector URL (Codio will provide the link)
3. **You should see**: A chat interface

#### Inspector Interface Overview

The Inspector interface has several sections:

1. **Chat Window** (center)
   - Where you type messages
   - Where bot responses appear
   - Shows conversation history

2. **Flow Visualization** (right side, if enabled)
   - Shows which flow is currently active
   - Shows flow steps
   - Visual representation of conversation state

3. **Debug Information** (bottom or side panel)
   - Shows which flow was triggered
   - Shows NLU predictions
   - Shows policy decisions
   - Very useful for debugging

4. **Slot Values** (if applicable)
   - Shows current slot values
   - For Level 1, this will be empty (no slots)

---

### Lab 6.2: Using Rasa Inspector

**Objective**: Start Inspector and test a simple conversation.

#### Steps

1. **Start Inspector**
   ```bash
   python -m rasa inspect --debug --log-file logs/logs.out
   ```
   Wait for the server to start.

2. **Access Inspector**
   - In Codio: Use the provided URL or port forwarding
   - You should see the Inspector chat interface

3. **Test a Simple Conversation**
   - Type "hello" and press Enter
   - The bot should respond
   - Check that the correct flow triggered

**AI Coach**: Ask "How do I access Inspector in Codio?" or "Why won't Inspector start?"

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

---

### Lab 6.3: Testing Your Bot

**Objective**: Test your bot thoroughly with multiple variations.

#### Task

Test your bot thoroughly:

1. Test the `greet` flow with 3 different greetings
2. Test the `help` flow with 3 different ways to ask for help
3. Test the `contact` flow with 3 different ways to ask for contact info
4. Test the `goodbye` flow (if you created it)

#### Documentation

For each test, note:
- What you said
- Which flow triggered
- What the bot responded
- Whether it matched your expectations

**AI Coach**: Ask "Why isn't my flow triggering?" or "How do I test if my bot works correctly?"

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

**AI Coach**: Ask "Why didn't my flow trigger?" or "How do I debug flow matching?"

---

## For Codio Team: Unit 6 Implementation Notes

### Lab 6.1: Training Your Bot

**Type**: Hands-On Lab with Auto-Grading

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Explain what training does
- Show command: `python -m rasa train`

**Hands-On Exercise**:
- Student runs training command
- Waits for completion

**Auto-Grading Rubric**:
- ✅ Training command completes successfully (3 points)
- ✅ Model file is created (`models/` directory) (2 points)
- ✅ No training errors in output (3 points)
- ✅ Training completes in reasonable time (<5 minutes) (2 points)
- **Total**: 10 points

**Auto-Grading Implementation Requirements**:
1. Execute training command in background or check if it completed
2. Verify model file exists in `models/` directory
3. Parse training output for errors
4. Time the training process

**AI Coach Configuration**:
- Context: "Student is training their Rasa bot"
- Common issues:
  - Training errors (YAML syntax issues) → "Check your YAML files for syntax errors. Common issues: wrong indentation, missing colons, missing dashes."
  - Missing files → "Make sure all your flow files are in the `data/` folder and domain file is in `domain/` folder."
  - Environment problems → "Check that your `.env` file exists and has valid values for RASA_LICENSE and OPENAI_API_KEY."

**Learning Analytics**: Track training attempts and errors

**Deliverables**:
- Lab instructions
- Auto-grading script specification
- Error detection logic
- Analytics configuration

### Lab 6.2: Using Rasa Inspector

**Type**: Guided Exercise

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Explain what Rasa Inspector is
- Show how to start it

**Hands-On Exercise**:
- Student starts Rasa Inspector
- Tests a simple conversation

**Auto-Grading**:
- ✅ Inspector starts successfully (2 points)
- ✅ Test conversation works (3 points)
- **Total**: 5 points

**Implementation Requirements**:
- Pre-configure Rasa Inspector in Codio IDE
- Provide access to web interface (port forwarding or embedded)

**Code Playback**: Enable to review conversations

**Deliverables**:
- Lab instructions
- Rasa Inspector configuration
- Port forwarding/web access setup
- Auto-grading specification

### Lab 6.3: Testing Your Bot

**Type**: Hands-On Lab with Auto-Grading (Rubric-based)

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Objective: Test all three flows (greet, help, contact)
- Explain testing process

**Hands-On Exercise**:
- Student tests each flow through Rasa Inspector
- Verifies bot responds correctly

**Auto-Grading Rubric**:
- ✅ Greet flow triggers correctly (test with "hello", "hi") (2 points)
- ✅ Help flow triggers correctly (test with "help", "what can you do") (2 points)
- ✅ Contact flow triggers correctly (test with "contact", "how to reach") (2 points)
- ✅ Bot responds with correct messages (3 points)
- ✅ All flows work independently (1 point)
- **Total**: 10 points

**Auto-Grading Implementation Requirements**:
1. Programmatic testing of bot via API or script
2. Send test messages for each flow
3. Verify correct flow is triggered
4. Verify correct response is returned

**AI Coach Configuration**:
- Context: "Student is testing their bot"
- Common issues:
  - Flows not triggering → "Check your flow descriptions. Are they clear and specific? The LLM uses descriptions to match user messages."
  - Wrong responses → "Verify the response text in your domain file. Make sure you retrained after making changes."
  - Description field issues → "Every flow needs a `description:` field. Without it, the LLM can't match user messages to your flow."

**Deliverables**:
- Lab instructions
- Auto-grading script (bot testing)
- Test cases specification
- Rubric details

---

# Unit 7: Putting It All Together

## For Students

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

### Lab 7.1: Complete Bot Walkthrough

**Objective**: Understand how all pieces work together in a complete conversation.

#### Steps

1. **Start Inspector** (if not already running)
2. **Have a Complete Conversation**
   - Open a new session (this triggers `pattern_session_start`)
   - Try asking for help
   - Try asking for contact info
   - Try ending the conversation
3. **Observe Each Step**
   - Notice which flow triggers for each message
   - Check the debug output to see LLM understanding
   - Understand how flows and responses connect

**AI Coach**: Ask "How does the bot decide which flow to trigger?" or "What happens when I start a new conversation?"

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

### Lab 7.2: Build Your Own Feature (Project)

**Objective**: Add a new feature to your banking bot (new response + new flow).

#### Task

Create a new feature for your banking bot:
1. **Create a new response** in `domain/basics.yml`
   - Think of something useful (e.g., bank hours, account info, FAQs)
   - Follow the same pattern as existing responses
   - Include `metadata: rephrase: True`

2. **Create a new flow** in `data/basics/`
   - Create a new YAML file (e.g., `hours.yml`)
   - Write a clear, specific description
   - Reference your new response in the steps

3. **Train your bot**
   - Run `python -m rasa train`
   - Make sure training succeeds

4. **Test your new feature**
   - Start Inspector
   - Test your new flow with multiple phrasings
   - Verify it works correctly

**Example Ideas**:
- Bank hours feature
- Account types information
- Branch locations
- Online banking help

**AI Coach**: Ask "How do I create a new feature?" or "What makes a good flow description?"

---

### Lab 7.3: Best Practices Application

**Objective**: Apply best practices to your existing code.

#### Task

Review your bot and apply best practices:

1. **Review Flow Descriptions**
   - Are they clear and specific?
   - Do they use action verbs?
   - Do they include context?

2. **Review Response Variations**
   - Do key responses have multiple variations?
   - Are variations different (not duplicates)?

3. **Test Thoroughly**
   - Test each flow with multiple phrasings
   - Verify all flows work correctly
   - Check for any errors in logs

**AI Coach**: Ask "How do I improve my flow descriptions?" or "What makes a good response?"

---

## For Codio Team: Unit 7 Implementation Notes

### Lab 7.1: Complete Bot Walkthrough

**Type**: Guided Demonstration

**Content Structure**:
- Step-by-step conversation walkthrough (preserved from TUTORIAL.md)
- Interactive demonstration in Rasa Inspector
- **No auto-grading** - informational only

**AI Coach**: Available for questions

**Deliverables**:
- Demonstration script/instructions
- Sample conversation flows

### Lab 7.2: Build Your Own Feature (Project)

**Type**: Comprehensive Project with Auto-Grading (Rubric-based)

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Objective: Add a new feature (new response + new flow)
- Challenge students to create something new

**Hands-On Project**:
- Student creates new response
- Student creates new flow
- Student trains bot
- Student tests new feature

**Auto-Grading Rubric**:
- ✅ New response created correctly (YAML valid, follows convention) (3 points)
- ✅ New flow created correctly (has name, description, steps) (3 points)
- ✅ Flow references new response (1 point)
- ✅ Bot can be trained successfully (2 points)
- ✅ New feature works in testing (flow triggers, response shows) (3 points)
- ✅ Code follows best practices (descriptions present, proper structure) (2 points)
- **Total**: 14 points

**Code Playback**: Enable for full project review

**AI Coach**: Available throughout project

**Deliverables**:
- Project instructions
- Comprehensive auto-grading specification
- Rubric details

### Lab 7.3: Best Practices Application

**Type**: Auto-Graded Exercise

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Explain best practices learned
- Objective: Apply to existing code

**Hands-On Exercise**:
- Student reviews their code
- Applies best practices (improve descriptions, add variations, etc.)

**Auto-Grading**:
- Validates code follows conventions
- Checks for best practices
- Points: 5

**Deliverables**:
- Lab instructions
- Auto-grading specification

---

# Unit 8: Assessment and Next Steps

## For Students

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

## For Codio Team: Unit 8 Implementation Notes

### Final Assessment

**Type**: Comprehensive Assessment (Auto-Graded)

**Content Structure**:
1. **Knowledge Check** (Auto-Graded Multiple Choice)
   - 10-15 questions covering all concepts
   - Topics: Domain files, flows, system patterns, config, training
   - **Total**: 20 points

2. **Practical Exercise** (Auto-Graded with Rubric)
   - Create complete feature from scratch
   - Similar to Lab 7.2 but graded more strictly
   - **Total**: 20 points

3. **Code Review** (Using Code Playback)
   - Instructor reviews student's final bot
   - Provides feedback
   - **Total**: 10 points

**Deliverables**:
- Assessment questions with answer keys
- Practical exercise rubric
- Code Playback configuration

### Next Steps Module

**Content Structure**:
- Brief preview of Level 2 (Actions) (preserved from TUTORIAL.md)
- Links to continue learning
- **No auto-grading** - informational only

**AI Coach**: Helps students plan next steps

---

# Troubleshooting Guide

## Common Issues and Solutions

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

**AI Coach**: Ask "Why isn't my flow triggering?" → "Check your flow description. It should be clear and specific so the LLM can match user messages. Also verify your YAML syntax is correct and you retrained after making changes."

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

**AI Coach**: Ask "How do I fix 'response not found' error?" → "Make sure the response name in your flow exactly matches the response name in `domain/basics.yml`. Check spelling (case-sensitive) and ensure it's under the `responses:` section."

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

**AI Coach**: Ask "How do I fix YAML syntax errors?" → "YAML is very sensitive to indentation. Use exactly 2 spaces (not tabs, not 4 spaces). Make sure all keys end with colons (`:`) and list items start with dashes (`-`). Check the line number mentioned in the error."

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

**AI Coach**: Ask "Why won't Inspector start?" → "First, make sure you've trained your bot (`python -m rasa train`). If the port is in use, check for other Rasa processes. Verify `credentials.yml` has the `socketio:` section."

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

**AI Coach**: Ask "Why is my bot saying the wrong thing?" → "Check which flow actually triggered using Inspector's debug output. Verify the response text in your domain file matches what you expect. Make sure you retrained after making changes."

---

# Additional Resources

## Extension Exercises

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

# Glossary

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

*[All content from TUTORIAL.md is now fully integrated. The document serves as both complete course content for students and implementation guide for Codio team.]*

---

---


## Implementation Overview for Codio Team

### Executive Summary

This guide outlines how to transform the comprehensive Level 1 Rasa Bot tutorial (currently ~1,829 lines of detailed text in TUTORIAL.md) into an interactive Codio course that leverages Codio's AI-enhanced learning features, auto-grading, Code Playback, and AI Coach capabilities.

**Key Transformation Goals**:
- Preserve all educational content from TUTORIAL.md (comprehensive explanations, examples, step-by-step tutorials)
- Convert hands-on exercises into auto-graded labs with immediate feedback
- Eliminate setup friction with pre-configured environments
- Leverage AI Coach for student support instead of extensive troubleshooting text
- Use Code Playback for instructor review and student debugging
- Implement comprehensive analytics for learning insights

**Expected Outcomes** (based on Codio research):
- 2x higher completion rates
- 15% average grade improvement
- 70% faster time to first success
- 50% reduction in support tickets

### Content Integration Strategy

**All content from TUTORIAL.md is preserved** in this integrated document:
- Full conceptual explanations (no reduction in educational content)
- Complete step-by-step tutorials
- All examples, analogies, and code samples
- All troubleshooting content (kept for reference, AI Coach handles real-time help)
- All glossary terms and definitions

**Exercises are converted to labs**:
- Step-by-step tutorials → Hands-on labs with auto-grading
- Knowledge checks → Auto-graded assessments
- Verification steps → Auto-grading checks

**AI Coach replaces extensive troubleshooting text** for real-time student support.

---

## Technical Specifications for Codio Team

### Lab Environment Configuration

**Base Environment Requirements**:
- Operating System: Linux (Ubuntu 22.04 or similar)
- Python: 3.11
- IDE: Browser-based VSCode (Codio standard)
- Terminal: Bash shell

**Pre-Installed Software**:
```bash
# Python and pip
python3.11
pip (latest version)

# Rasa Pro
rasa-pro (latest stable version)

# Git (for version control if needed)
git
```

**Pre-Configured Project Structure**:
```
project/
├── domain/
│   └── basics.yml (pre-populated with starter responses)
├── data/
│   ├── basics/
│   │   ├── greet.yml
│   │   ├── help.yml
│   │   └── contact.yml
│   └── system/
│       └── patterns/
│           └── patterns.yml
├── config.yml
├── credentials.yml
├── endpoints.yml
├── .env (template with placeholders)
└── README.md
```

**Environment Variables Configuration**:
- `.env` file template provided
- Students/instructors fill in actual values:
  - `RASA_LICENSE=...`
  - `OPENAI_API_KEY=...`
- Environment variable loading script included

**Port Configuration**:
- Rasa Inspector: Port 5005 (default)
- Ensure port forwarding or web access is configured

### Auto-Grading Script Requirements

**General Requirements**:
1. All scripts should be executable in the Codio environment
2. Scripts should provide clear error messages
3. Scripts should output results in Codio-compatible format
4. Scripts should handle edge cases gracefully

**YAML Validation**:
- Use Python `yaml` library or similar
- Validate syntax, structure, indentation
- Provide specific error messages

**File Validation**:
- Check file existence
- Check file location
- Check file contents
- Compare against expected patterns

**Bot Testing**:
- Use Rasa API or command-line interface
- Send test messages programmatically
- Verify responses and flow triggers
- Handle timeouts and errors

**Rubric Evaluation**:
- Each criterion should be independently checkable
- Provide partial credit when applicable
- Show which criteria passed/failed

### Code Playback Configuration

**Enable Code Playback For**:
- Lab 2.2: Creating Your First Response
- Lab 2.3: Response Variations
- Lab 3.2: Creating Your First Flow
- Lab 4.2: Modifying System Patterns
- Lab 7.2: Build Your Own Feature (Project)
- Final Assessment: Code Review

**Configuration Details**:
- Record keystrokes in relevant files
- Track file edits (domain/basics.yml, data/basics/*.yml)
- Allow instructor review after submission
- Allow student review of their own work

### AI Coach Configuration Reference

**Context Settings**:
Each unit should have appropriate context:
- Current learning objective
- Relevant concepts being taught
- Common mistakes to watch for
- Available resources (file locations, commands)

**Response Guidelines**:
- Provide hints, not direct answers
- Guide students to find answers themselves
- Reference relevant file locations
- Explain concepts clearly
- Avoid doing the work for students

**Common Questions Per Unit**:
- Document common questions for each unit (see Unit 0-2 examples)
- Pre-configure helpful responses
- Update based on student interactions

### Learning Analytics Configuration

**Track the Following Metrics**:
1. **Time Spent**: Per unit, per lab, total course time
2. **Attempts**: Number of attempts per lab, time between attempts, improvement over attempts
3. **Errors**: Common error types, error frequency, error resolution time
4. **Engagement**: Keystroke activity, file edits, Code Playback analysis
5. **Performance**: Lab scores, assessment scores, completion rates

**Analytics Dashboards**:
- Instructor dashboard: Class-wide performance
- Student dashboard: Individual progress
- Alert system: Flag struggling students early

### LMS Integration Requirements

**Grade Passback**:
- Auto-graded labs: Pass scores to LMS
- Rubric-based labs: Pass detailed scores to LMS
- Final assessment: Pass overall grade to LMS

**Progress Tracking**:
- Unit completion status
- Lab completion status
- Assessment completion status

**SSO Configuration**:
- Single sign-on integration
- User authentication
- Course enrollment

---

## Implementation Phases

### Phase 1: Foundation (Priority: High)
**Units**: 0-2 (Prerequisites, Introduction, Domain File)
**Timeline**: 2-3 weeks
**Deliverables**:
- Environment configuration
- Units 0-2 content
- Auto-grading for Units 0-2
- AI Coach configuration

### Phase 2: Core Concepts (Priority: High)
**Units**: 3-5 (Flows, System Patterns, Config)
**Timeline**: 2-3 weeks
**Deliverables**:
- Units 3-5 content
- Auto-grading for Units 3-5
- Code Playback configuration
- Enhanced AI Coach

### Phase 3: Application (Priority: Medium)
**Units**: 6-8 (Training, Testing, Assessment)
**Timeline**: 2-3 weeks
**Deliverables**:
- Units 6-8 content
- Comprehensive assessment
- Final analytics configuration
- LMS integration

### Phase 4: Enhancement (Priority: Low)
**Timeline**: Ongoing
**Deliverables**:
- Analytics refinement
- AI Coach improvements
- Additional practice exercises
- Student feedback integration

---

## Quality Assurance Checklist

### Content Quality
- [ ] All text is concise and clear (while preserving educational completeness)
- [ ] All TUTORIAL.md content is integrated
- [ ] Examples are relevant and helpful
- [ ] Instructions are actionable
- [ ] Visual elements support understanding

### Technical Quality
- [ ] All code examples work correctly
- [ ] Environment configuration is complete
- [ ] Auto-grading scripts are accurate
- [ ] Error messages are helpful
- [ ] Port forwarding works correctly

### Assessment Quality
- [ ] Questions test understanding, not memorization
- [ ] Rubrics are clear and fair
- [ ] Partial credit is appropriate
- [ ] Feedback is constructive
- [ ] Assessments align with learning objectives

### User Experience
- [ ] Navigation is intuitive
- [ ] Instructions are easy to follow
- [ ] AI Coach provides helpful guidance
- [ ] Code Playback works smoothly
- [ ] Analytics are accessible and useful

---

## Success Metrics

### Student Outcomes
- **Completion Rate**: Target 2x higher than text-based tutorial
- **Grade Improvement**: Target 15% average improvement
- **Time to Success**: Target 70% faster
- **Support Tickets**: Target 50% reduction

### Engagement Metrics
- **Time Spent**: Track per unit
- **Attempts**: Track per lab
- **AI Coach Usage**: Track questions asked
- **Code Playback Views**: Track review sessions

### Instructor Benefits
- **Grading Time**: Reduced by 90% (auto-grading)
- **Support Load**: Reduced by 50% (AI Coach)
- **Insights**: Real-time analytics on student progress
- **Intervention**: Early identification of struggling students

---

## Conclusion

This integrated document serves as both:
1. **Complete course content** for students - preserving all educational material from TUTORIAL.md
2. **Implementation guide** for Codio team - providing all technical specifications and deployment details

**Key Principle**: All content from TUTORIAL.md is preserved and integrated. Exercises are converted to labs with auto-grading. AI Coach handles real-time support, allowing students to learn with immediate feedback while preserving comprehensive educational content for reference.

**Next Steps**: 
1. Review this document with Codio team
2. Address questions and clarify specifications
3. Create detailed specs for Phase 1 (Units 0-2)
4. Begin implementation of Phase 1
5. Test and iterate based on feedback
6. Proceed with Phases 2 and 3
7. Continuous improvement based on analytics and feedback

---

**End of Complete Codio Course Guide**

This document fully integrates all content from TUTORIAL.md and serves as both the complete course material and implementation guide. TUTORIAL.md is now redundant as all its content is preserved here.
