# Level 1: Just Responses - Complete Codio Course Guide (OPTIMIZED VERSION)

**Complete Course Content and Implementation Guide for Codio Platform**

**⭐ OPTIMIZED VERSION**: This guide includes verified Codio optimizations that can reduce implementation time from **13.5-20.5 hours to 9-14.5 hours**, making the 2-day target easily achievable. See "Quick Start: Optimized Implementation Path" section for details.

**Purpose**: This document serves as both:
- **Complete course content** for students (all tutorial content integrated)
- **Implementation guide** for the Codio team (technical specifications and deployment details)
- **Optimized implementation path** using verified Codio features (Assessment Library, Starter Packs, Bulk Configuration)

**Target Audiences**: 
- Students learning to build their first Rasa bot
- Codio team members implementing the course
- Course developers and instructional designers

**Date**: January 2025  
**Version**: Optimized (includes verified Codio feature optimizations)

**Split content (Level 2 style)**: Student-facing content and lab instructions are also available as separate markdown files in this folder, aligned with Level 2 naming. Use **Level1_Course_Outline.md** for structure, **Level1_Implementation_Overview.md** for Codio team guidance, **Level1_UnitN_Content_*.md** for unit sections, **Level1_LabX.Y_Content.md** for lab instructions, and **Level1_LabX.Y_Assessment_Setup.md** for assessment setup. This single guide remains the full reference; the split files are for copy-paste into Codio and for consistency with Level 2.

---

### 📊 Implementation at a Glance (Path A)

| | First Course (Ground Zero) | Future Courses |
|---|---|---|
| **Total Time** | **13.5–18 hours** | **9–11 hours** |
| **Flow** | Pre-Implementation (1–2h) → Day 1 (7–9h) → Day 2 (5–7h) | Import from Library + Starter Pack |
| **Key Entry** | [Quick Start](#quick-start) → [Path A Checklist](#path-a) → [Adding Guide Content](#adding-guide-content) | Same, but import assessments |

---

### 📋 Before You Start: Dependencies

**You need:**
- Codio account with instructor/admin access
- Assessment Library access (org admin may need to create; see Optimization 1)
- Rasa Pro license and OpenAI API key (for testing the course)

**Codio features this guide assumes:** Assessment Library, Starter Packs, Bulk Virtual Coach CSV, LLM Rubric Autograde, Sandboxed Terminal (for venv). If a feature is unavailable, see each optimization's Fallback section.

---

### ✅ What's Included / Not Included

| Included (copy-paste ready) | Not Included |
|---|---|
| All guide content (main units + labs) | Codio account setup |
| Assessment questions, answers, rubrics | Rasa Pro license procurement |
| Configurations (commands, settings, fail messages) | Codio org/admin configuration |
| Virtual Coach prompts per unit | Starter Pack creation (steps provided) |

---

## ⚠️ CRITICAL: Document Structure for Codio Implementers

**This document contains TWO types of content that MUST be kept separate:**

### 📚 Student-Facing Content (COPY TO CODIO)
- **Sections marked `## For Students`** → Copy these to Codio's Guide Editor
- **Markdown code blocks in Step 0.5 sections** → These contain clean student-facing content ready to copy
- **What students see**: Only the content from `## For Students` sections and the markdown code blocks

### 🛠️ Implementation Instructions (DO NOT COPY TO CODIO)
- **Sections marked `## For Codio Team`** → These are for YOUR reference only
- **Step 0.5 sections** → The instructions BEFORE the markdown code block are for you
- **Troubleshooting sections** → Marked "FOR IMPLEMENTERS ONLY" - never copy to Codio
- **Assessment creation steps** → Marked "FOR IMPLEMENTERS ONLY" - never copy to Codio

### ✅ How to Identify What to Copy

**For Main Unit Content:**
1. Find `## For Students` section
2. Copy everything from that heading down to (but NOT including) the first `### Lab X.X:` heading
3. **STOP** when you see `## For Codio Team` or `### Lab X.X:`

**For Lab Content:**
1. Find the lab's `#### Step 0.5: Add Lab X.X Guide Content to Codio` section
2. Look for the heading `**📋 Copy This Markdown for Lab X.X:**`
3. Find the visual marker `⬇️ START COPYING HERE ⬇️`
4. Copy ALL content from that marker until you see `⬆️ STOP COPYING HERE ⬆️`
5. **DO NOT copy** the markers themselves or anything after `⬆️ STOP COPYING HERE ⬆️` (troubleshooting, Step 1, etc.)

### 🚫 What NEVER to Copy
- ❌ Any section starting with `## For Codio Team`
- ❌ Any troubleshooting section (marked "FOR IMPLEMENTERS ONLY")
- ❌ Any assessment creation steps (marked "FOR IMPLEMENTERS ONLY")
- ❌ The visual markers (`⬇️ START COPYING HERE ⬇️` and `⬆️ STOP COPYING HERE ⬆️`)
- ❌ Implementation notes, time estimates, or "What you're doing" explanations

### 📋 Visual Guide

```
# Unit 2: Understanding the Domain File

## For Students                    ← ✅ START COPYING HERE
  ### 2.1 What is a Domain?        ← ✅ COPY THIS
  ### 2.2 Understanding Responses  ← ✅ COPY THIS
  ### Lab 2.1: ...                 ← ✅ COPY THIS (lab content)
  
## For Codio Team                  ← ❌ STOP COPYING - DON'T COPY THIS
  ### Step 0.5: Add Lab 2.1...     ← ❌ Implementation instructions (for you only)
    **📋 Copy This Markdown**:     ← ✅ Look for this heading
    ⬇️ START COPYING HERE ⬇️      ← ✅ START COPYING HERE
    ### Lab 2.1: ...               ← ✅ COPY THIS (student content)
    ⬆️ STOP COPYING HERE ⬆️        ← ✅ STOP COPYING HERE
    **💡 Troubleshooting**...      ← ❌ DON'T COPY (for implementers)
    #### Step 1: Create...        ← ❌ DON'T COPY (for implementers)
```

**Note**: In Cursor's preview mode, the copyable content will render as formatted Markdown (headings, code blocks, etc.). This is intentional - you're copying the rendered Markdown content, not a code block. Just select from `⬇️ START COPYING HERE ⬇️` to `⬆️ STOP COPYING HERE ⬆️` (excluding the markers themselves).

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

### For Codio Team (Implementer Quick Navigation)
| Task | Section |
|------|---------|
| Start here | [Quick Start: Optimized Implementation Path](#quick-start) |
| Day-by-day workflow | [PATH A: Step-by-Step Guide](#path-a) |
| Add student content | [Adding Guide Content](#adding-guide-content) |
| Create assessments | [Codio Native Assessment Features](#codio-assessment-features) |
| AI shortcuts | [Codio AI-Powered Time Savers](#codio-ai-savers) |
| Reference | [Technical Specifications](#technical-specifications), [Implementation Overview](#implementation-overview) |
| Templates | [Assessment Templates Library](#assessment-templates) |
| QA | [Quality Assurance Checklist](#quality-assurance) |

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

### 0.2 Project Structure

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

### Lab 0.1: Create Virtual Environment and Install Rasa Pro

**Objective**: Create a virtual environment, install Rasa Pro in it, and verify the installation is successful.

**Important**: This is your first step! You must create a virtual environment and install Rasa Pro before you can proceed with any other exercises.

**Before you start**: Open a terminal in Codio. Run `cd level1` so you are in the `level1` folder. All commands in this lab should be run from there.

#### Steps

1. **Create a Virtual Environment**
   
   In the terminal, first check that Python 3.11 is installed correctly:
   ```bash
   python3.11 -V
   ```
   Then type:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```
   
   **What to expect**: Your command prompt should show `(.venv)` at the beginning, indicating the virtual environment is active.

2. **Install Rasa Pro**
   
   With the virtual environment activated, run:
   ```bash
   pip install --no-cache-dir rasa-pro
   ```
   
   **What to expect**:
   - Installation will take 2-5 minutes
   - You'll see progress messages as packages are downloaded and installed
   - At the end, you should see "Successfully installed rasa-pro-x.x.x" along with a list of dependencies

3. **Verify Installation**
   
   Once installation completes, verify Rasa Pro is installed correctly:
   ```bash
   rasa --version
   ```
   
   **Expected output**: You should see version information like "Rasa 3.x.x" (no errors).
   
   **If you see an error**: The installation may not have completed successfully. Review any error messages from Step 1 and try installing again.

4. **Check Project Structure** *(After installation)*
   ```bash
   # Check that project folders exist
   ls -la domain/
   ls -la data/
   ```
   Confirm:
   - The `domain/` folder exists
   - The `data/` folder exists

   ```bash
   # Check that the following .yml files exist
   ls -la config.yml credentials.yml endpoints.yml
   ```

5. **Check Environment Variables**

   **Codio**: Credentials are pre-configured. To verify they're loaded, run:
   ```bash
   [ -n "$RASA_LICENSE" ] && echo "RASA_LICENSE is set" || echo "RASA_LICENSE is not set"
   [ -n "$OPENAI_API_KEY" ] && echo "OPENAI_API_KEY is set" || echo "OPENAI_API_KEY is not set"
   ```
   Both should report "is set". If not, ask your instructor.
   
   **Local setup**: The .env file should exist in your project root. Run **ls -la .env** to confirm. If it doesn't, create it using the instructions in section 0.1.

**✅ Success Criteria**: Once you can run `rasa --version` successfully and see version information, you're ready to move on to the next exercises. You can then run the assessment for this lab to confirm your setup.

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

### 0.4 Getting Help

**Stuck?** Here are resources:

- **Rasa Documentation**: [https://rasa.com/docs](https://rasa.com/docs)
- **Error Messages**: Check the troubleshooting section at the end of this guide
- **Common Issues**: Most setup issues are covered in the troubleshooting guide
- **AI Coach**: Ask the AI Coach in Codio for help with any questions

---

<a id="quick-start"></a>
## 🚀 Quick Start: Optimized Implementation Path

**Key Icons**: ⏱️ Time estimate | 💡 Tip | ✅ Done | ❌ Error | ⚠️ Warning | 📋 Checklist | 🔍 Troubleshooting

**How to Use This Guide**:
- **Beginners**: Follow Path A (below) step-by-step. This guide defaults to Path A.
- **Experienced**: Skip to Master Checklist; use Templates Library and Time-Saving Strategies for reference.

**⏱️ Time Savings: 4-6 hours** (Verified with Codio Official Documentation)

This section provides **verified optimizations** that leverage Codio's native features to dramatically reduce implementation time. These methods are officially supported by Codio and can reduce your total implementation time from 13.5-20.5 hours to **9-14.5 hours**, making the 2-day target easily achievable.

### 🎯 Three Major Optimizations

1. **Assessment Library** (saves 2-3 hours on future courses) - Create assessments once, save to library, then reuse for future courses
2. **Starter Pack Project Template** (saves 30-60 min on future courses) - Create project once, convert to pack, then reuse for future courses
3. **Bulk Virtual Coach Configuration** (saves 1-2 hours) - Configure all units at once via CSV

**🎯 THIS GUIDE IS OPTIMIZED FOR PATH A** - All instructions below assume you're using Path A (all optimizations). This is the fastest, most transparent approach.

**Path A: Optimized Path** (This Guide's Default) → **9-11 hours total**
- ✅ Use Starter Pack for project setup
- ✅ Import assessments from Assessment Library
- ✅ Configure Virtual Coach via Bulk CSV
- ✅ Use Enhanced AI Prompts

**Alternative Paths** (if optimizations unavailable):
- **Path B: Hybrid Path** - Use some optimizations → **11-14 hours total** (see fallback instructions in each optimization section)
- **Path C: Manual Path** - Create everything manually → **13.5-20.5 hours total** (see unit-by-unit implementation notes)

---

### 📚 Optimization 1: Assessment Library Import

**⏱️ Time Saved: 2-3 hours**  
**📖 Official Documentation**: https://docs.codio.com/instructors/setupcourses/library/assessmentslibrary.html

#### What This Does

**For Your First Course (Starting from Ground Zero)**:
1. Create assessments manually as you implement each unit (follow unit-by-unit notes)
2. Save each assessment to the Assessment Library as you create it
3. This creates a reusable library for future courses

**For Future Courses**:
1. Import assessments from the library (30-45 minutes instead of 6-8 hours)
2. Review and customize as needed

#### Prerequisites

- An **organization Assessment Library** must be created first (by an Admin)
- Assessments must be saved to the library with appropriate tags

#### Step-by-Step: Creating Assessment Library (Starting from Ground Zero)

**Since you're starting from ground zero, you'll create the Assessment Library as part of the implementation process.**

1. **Create Organization Assessment Library** (Admin required):
   - Contact your Codio organization admin to create an Assessment Library
   - Or if you're an admin: Go to Organization Settings → Assessment Library → Create New Library
   - Name it: "Rasa Banking Bot - Level 1"

2. **Create Assessments** (as you implement each unit):
   - Follow the manual creation process in this guide for each assessment
   - Create all Level 1 assessments unit by unit

3. **Save to Library** (after creating each assessment):
   - After creating and testing an assessment, click **Save in Library** (bottom right of assessment editor)
   - Select your organization's Assessment Library
   - Add metadata tags:
     - `Course: Level 1`
     - `Unit: X` (where X is unit number)
     - `Lab: X.X` (where X.X is lab number)
     - `Type: Multiple Choice` or `Type: LLM Rubric` etc.

4. **Future Use**:
   - Once all assessments are saved, you can import from library for future courses
   - Reuse for Levels 2-5 (with modifications)

**⏱️ Initial Setup**: 6-8 hours (create all assessments and save to library)  
**⏱️ Future Courses**: 30-45 minutes (import from library and customize)

#### Benefits

- ✅ **Consistency**: All courses use same assessment structure
- ✅ **Speed**: Import 30+ assessments in 30-45 minutes
- ✅ **Reusability**: Use for multiple courses/levels
- ✅ **Quality**: Pre-validated assessments reduce errors

#### Fallback

If Assessment Library is not available, use the manual creation process described in the unit-by-unit implementation notes.

---

### 🎁 Optimization 2: Starter Pack Project Template

**⏱️ Time Saved: 30-60 minutes**  
**📖 Official Documentation**: https://docs.codio.com/develop/develop/packs/packs.html

#### What This Does

Instead of manually setting up the Codio project each time (30-60 minutes), you can:
1. Create a Starter Pack once from a configured project
2. Use the pack to create new projects instantly (5 minutes)
3. Configure `.env` file and start working

#### Prerequisites

- Starter Pack must be created first (one-time setup)
- Pack must include: Ubuntu base, Stack (Python 3.11, Rasa Pro), project structure

#### Step-by-Step: Creating Starter Pack (Starting from Ground Zero)

**Since you're starting from ground zero, you'll create the Starter Pack as part of the implementation process.**

1. **Prepare Project** (first, create a project with all Level 1 setup):
   - Create a Codio project with all Level 1 setup:
     - Python 3.11 verified (available in stack)
     - Rasa Pro NOT installed (students will install it in Lab 0.1)
     - Project structure created (`domain/`, `data/`, etc.)
     - `.env.template` file included
     - `.codio` file configured (for Run/Preview buttons)
     - `README.md` with instructions
   - Follow Unit 0 implementation notes for detailed setup instructions

2. **Create Pack** (after project is ready):
   - Click **Starter Packs** in navigation pane
   - Click **New Pack** on Starter Packs page
   - Choose workspace source: **Codio project** (select your prepared project)
   - Specify Stack (if custom components installed)
   - Enter name: "Rasa Banking Bot - Level 1"
   - Enter description: "Pre-configured project for Level 1 Rasa bot course"
   - Add tags: `rasa`, `python`, `banking-bot`, `level-1`
   - Set visibility: **Private** (for organization) or **Public** (after testing)
   - Click **Create**

3. **Test Pack**:
   - Use the pack to create a test project
   - Verify everything works correctly
   - Update pack if needed

**⏱️ Initial Setup**: 1-2 hours (create project, then create and test pack)  
**⏱️ Future Courses**: 5 minutes (use pack to create new projects)

#### Benefits

- ✅ **Speed**: Instant project setup (5 min vs. 30-60 min)
- ✅ **Consistency**: All students get identical environment
- ✅ **Reduced Errors**: Pre-validated setup reduces configuration issues
- ✅ **Student Experience**: Faster onboarding

#### Fallback

If Starter Pack is not available, use the manual project setup process described in Unit 0.

---

### ⚙️ Optimization 3: Bulk Virtual Coach Configuration

**⏱️ Time Saved: 1-2 hours**  
**📖 Official Documentation**: https://docs.codio.com/instructors/setupcourses/bulk-assignment-update.html

#### What This Does

Instead of configuring Virtual Coach settings for each unit individually (1-2 hours), you can:
1. Download CSV template with all assignment settings
2. Configure Virtual Coach settings for all units in one CSV file
3. Upload CSV to apply settings to all assignments at once

#### Prerequisites

- Assignments must be created first (can be empty/draft assignments)
- Course must be set up with all units/assignments

#### Step-by-Step: Bulk Virtual Coach Configuration

1. **Download CSV Template**:
   - Go to your course → **Bulk Settings** area
   - Click **Download Assignment Information** (in Assignment settings section)
   - CSV file downloads with all current assignment settings

2. **Configure Virtual Coach Settings**:
   - Open CSV in Excel/Google Sheets
   - For each assignment (row), configure these columns:
     - **Summarize Prompt**: `true` or `false` (enable/disable)
     - **Error Augmentation**: `true` or `false` (enable/disable)
     - **Next Steps Hint**: `true` or `false` (enable/disable)
   - **Example CSV Structure**:
     ```csv
     Assignment Name,Assignment ID,Summarize Prompt,Error Augmentation,Next Steps Hint
     Unit 0: Prerequisites,ASSIGN_001,true,true,true
     Unit 1: Introduction,ASSIGN_002,true,true,true
     Unit 2: Domain File,ASSIGN_003,true,true,true
     ...
     ```

3. **Upload CSV**:
   - Go back to **Bulk Settings** → **Assignment settings**
   - Click **Upload** or **Import**
   - Select your updated CSV file
   - Review changes preview
   - Click **Apply** or **Save**

4. **Verify Settings**:
   - Check a few assignments to verify Virtual Coach settings applied correctly
   - Test Virtual Coach in student preview mode

**⏱️ Estimated Time**: 15-20 minutes (vs. 1-2 hours manual configuration)

#### CSV Template Guidelines

- **Header names must match exactly** (case-insensitive)
- **Leave fields empty** if you don't want to update that setting
- **Identify assignments** by name, Assignment ID, or LTI Integration URL
- **Empty fields** = no update to that setting

#### Benefits

- ✅ **Speed**: Configure all units in 15-20 minutes vs. 1-2 hours
- ✅ **Consistency**: All units get same Virtual Coach configuration
- ✅ **Easy Updates**: Modify CSV and re-upload to update all assignments
- ✅ **Bulk Operations**: Also supports dates, due dates, penalties in same CSV

#### Fallback

If bulk update is not available, use the manual Virtual Coach configuration process described in each unit's implementation notes.

---

### 🤖 Enhanced AI Assessment Generation Templates

**⏱️ Time Saved: 1-2 hours** (additional savings beyond basic AI use)  
**📖 Official Documentation**: https://docs.codio.com/instructors/authoring/assessments/ai-assessment-generation.html

#### What This Does

Provides pre-written AI prompts optimized for each assessment type, reducing trial-and-error and improving AI-generated assessment quality.

#### Supported Assessment Types

- ✅ Multiple Choice
- ✅ Fill in the Blanks
- ✅ Free Text
- ✅ Standard Code Test
- ✅ Parsons Puzzle

#### Pre-Written AI Prompts

**For Multiple Choice Questions**:
```
Create a multiple choice question about [TOPIC] with 4 options. 
The question should test understanding of [CONCEPT]. 
Include one correct answer and three plausible distractors.
Base the question on the content in the first paragraph of this guide page.
```

**For Fill in the Blanks**:
```
Create a fill-in-the-blank question about [TOPIC]. 
The question should test knowledge of [SPECIFIC CONCEPT]. 
Include 3-5 blanks with clear context clues.
Base the question on the content in the second paragraph of this guide page.
```

**For Standard Code Test**:
```
Create a standard code test that verifies students can [TASK].
The test should:
- Check that [FILE] exists
- Verify that [COMMAND] runs successfully
- Validate that output contains [EXPECTED_TEXT]
Provide clear instructions for students.
```

**For LLM Rubric (using Generate Rubrics button)**:
```
Validate that the student's [FILE] contains:
- [REQUIREMENT 1]
- [REQUIREMENT 2]
- [REQUIREMENT 3]
Check for proper YAML syntax and indentation.
Provide helpful feedback if requirements are not met.
```

#### How to Use

1. **Create Empty Assessment**:
   - Add assessment to guide page
   - Select assessment type

2. **Click Generate**:
   - Click **Generate** button (bottom right)
   - Generation Prompt opens

3. **Use Pre-Written Prompt**:
   - Copy appropriate prompt from above
   - Customize [TOPIC], [CONCEPT], etc. with specific details
   - Paste into Generation Prompt field

4. **Generate and Review**:
   - Click **Generate Using AI**
   - Review generated assessment
   - Click **Regenerate** if needed (creates new version)
   - Click **Apply** when satisfied

5. **Refine**:
   - Edit assessment as needed
   - Review Execution and Grading tab settings
   - Test in preview mode

#### Benefits

- ✅ **Better Results**: Pre-optimized prompts produce higher quality assessments
- ✅ **Faster**: Less trial-and-error with prompt writing
- ✅ **Consistency**: All assessments follow same quality standards
- ✅ **Time Savings**: 1-2 hours saved vs. writing prompts from scratch

---

### 📊 Optimization Summary

| Optimization | Time Saved | One-Time Setup | Per-Course Time |
|--------------|------------|----------------|-----------------|
| Assessment Library | 2-3 hours | 6-8 hours | 30-45 min |
| Starter Pack | 30-60 min | 1-2 hours | 5 min |
| Bulk Virtual Coach | 1-2 hours | 15-20 min | 15-20 min |
| Enhanced AI Prompts | 1-2 hours | 0 (use templates) | Included in creation |
| **TOTAL** | **4-6 hours** | **8-11 hours** | **50-70 min** |

**First Course**: 8-11 hours setup + 9-11 hours implementation = **17-22 hours** (still within 2 days)  
**Future Courses**: 50-70 min setup + 9-11 hours implementation = **10-12 hours** (well within 1 day)

---

### ⚡ Quick Reference: Common Codio Operations

**🔍 What You'll See**: When you click these menu paths, Codio will show specific panels or dialogs. Don't worry if the exact wording differs slightly - Codio updates their UI occasionally.

**Navigation Shortcuts** (exact menu paths):
- **Guides Editor**: 
  - Click `Tools` in top menu → Click `Guides` → Click `Edit` button
  - **OR** Look for "Edit" button directly in the Guides panel (if visible)
  - **Expected Result**: Guide editor opens, showing all unit sections
  
- **Assessment Creation**: 
  - In Guide editor, find your unit section (e.g., "Unit 1: Introduction")
  - Scroll to bottom of that section
  - Click `+` button (usually at bottom right of section)
  - Select assessment type from dropdown (Code Test, Multiple Choice, etc.)
  - **Expected Result**: Assessment editor/code box appears
  
- **Virtual Coach**: 
  - Click `Education` in top menu → Click `Settings` → Click `Virtual Coach` tab
  - **Expected Result**: Settings panel with Virtual Coach configuration options
  
- **Code Playback**: 
  - Click `Education` in top menu → Click `Monitoring` → Click `Code Playback`
  - **Expected Result**: Panel showing tracked files and playback controls
  
- **Terminal**: 
  - Click `Tools` → Click `Terminal`
  - **OR** Press `Ctrl+Shift+` ` (backtick key)
  - **Expected Result**: Terminal window opens at bottom of screen

**Standard Assessment Settings** (use these defaults):

| Assessment Type | Points | Timeout | Language | Show Explanations | Max Attempts |
|----------------|--------|---------|----------|-------------------|--------------|
| Code Test (Simple) | 10 | 30s | Python 3 | N/A | 3 |
| Code Test (Complex) | 12-14 | 60s | Python 3 | N/A | 3 |
| Multiple Choice | 2 | N/A | N/A | ✓ | 3 |
| Multiple Choice (Set) | 5-8 | N/A | N/A | ✓ | 3 |

**Common Configuration Values** (copy-paste ready):

```yaml
# Virtual Coach - Summarize Prompt (add to all units)
Unit X Context:
- [Unit-specific key concepts]
- [Common patterns]

# Virtual Coach - Error Augmentation (reusable)
YAMLError → "Check YAML syntax: missing colons, wrong indentation, or missing dashes. Use exactly 2 spaces per indent level."
IndentationError → "Use exactly 2 spaces for indentation (not tabs, not 4 spaces). Enable 'show whitespace' in your editor."
FileNotFoundError → "Check file path. Ensure file is in correct location and name matches exactly (case-sensitive)."
```

### ⚡ ONE-PAGE QUICK REFERENCE CARD

**📋 Copy this to a notepad or second tab - saves 30+ minutes of searching:**

**Essential Menu Paths** (copy to notepad):
```
Guides Editor: Tools → Guides → Edit
Assessment Settings: [Gear icon] on assessment code box
Virtual Coach: Education → Settings → Virtual Coach
Code Playback: Education → Monitoring → Code Playback
Terminal: Tools → Terminal (or Ctrl+Shift+`)
Preview Mode: [Eye icon] in Guide editor
```

**Standard Settings** (copy-paste these values):
```
Code Test (Simple): Points=10, Timeout=30s, Language=Python 3
Code Test (Complex): Points=12-14, Timeout=60s, Language=Python 3
Multiple Choice: Points=2, Show Explanations=✓, Max Attempts=3
```

**File Paths** (use these exact paths in scripts):
```
Project root: /home/codio/workspace/level1
Domain file: /home/codio/workspace/level1/domain/basics.yml
Flow files: /home/codio/workspace/level1/data/basics/*.yml
Patterns: /home/codio/workspace/level1/data/system/patterns/patterns.yml
```

**Common Commands** (terminal):
```bash
python3.11 -V                    # Check Python version
python3.11 -m rasa --version     # Check Rasa version
python3.11 -m rasa train         # Train bot
python3.11 -m rasa run --enable-api  # Start server for testing
```

**Template Quick Reference**:
- Multiple Choice → Template 3 (or use **AI Generate** + **Duplicate**—see "Codio AI-Powered Time Savers")
- YAML Validation → Template 1 (LLM Rubric Autograde)—use Generate Rubrics first
- Response Check → Template 4 (LLM Rubric Autograde)
- Flow Check → Template 5 (LLM Rubric Autograde)
- Simple Facts → Fill in the Blanks (use <<<answer>>> notation)
- Virtual Coach → Template 6

### 📋 Pre-Filled Configuration Values (Copy-Paste Ready)

**Use these exact values to save time when creating assessments:**

#### Standard Code Test Settings
```
Points: 10
Timeout: 30 seconds
Language: Python 3 (or Bash for file checks)
Working Directory: /home/codio/workspace/level1
Command: [varies by assessment - see unit instructions]
Expected Output: [varies by assessment - see unit instructions]
Fail Message: [see unit instructions for specific fail messages]
```

#### LLM Rubric Autograde Settings
```
Points: 10-14 (varies by lab complexity)
Instructions: [copy from lab's Step 0.5 section or unit instructions]
Solution File: /home/codio/workspace/level1/[file path - see unit instructions]
Files to Check: /home/codio/workspace/level1/[file path - see unit instructions]
Rubric: [use "Generate Rubrics" button first, then refine - see unit instructions]
```

#### Multiple Choice Settings
```
Points: 2 per question
Show Explanations: ✓ (checked)
Max Attempts: 3
Randomize Options: ✓ (recommended)
```

#### Fill in the Blanks Settings
```
Points: 1 per blank
Case Sensitive: ✗ (unchecked - unless testing exact spelling)
Show Hints: ✓ (optional, but helpful for students)
```

### 🔄 Common Workflow Templates

**Use these workflows to implement units efficiently:**

#### Workflow 1: Adding a Complete Unit (Content + Assessments + Coach)

**⏱️ Estimated Time**: 1-1.5 hours per unit

**Steps**:
1. **Add Main Unit Content** (10-15 min)
   - Open Codio Guide Editor
   - Create unit section
   - Copy main unit content from this guide (`## For Students` to first lab)
   - Paste and save

2. **Add All Lab Content** (20-30 min)
   - For each lab in the unit:
     - Navigate to lab's Step 0.5 section
     - Copy Markdown from code block
     - Paste into Codio after main content
   - Save once after all labs

3. **Create Assessments** (30-45 min)
   - Follow unit's implementation notes
   - Use Codio AI features where possible
   - Create assessments in order (Lab 1, Lab 2, etc.)

4. **Configure Virtual Coach** (10-15 min)
   - Add unit-specific hints
   - Test with sample questions

5. **Test Everything** (10-15 min)
   - Preview guide content
   - Run each assessment
   - Verify Virtual Coach responses

**✅ Checkpoint**: Unit is complete, tested, and ready for students.

#### Workflow 2: Batch Creating Similar Assessments

**⏱️ Estimated Time**: 15-20 minutes for 5-10 similar assessments

**Example**: Creating 10 Multiple Choice questions for Unit 8 Knowledge Check

**Steps**:
1. **Create First Question** (5 min)
   - Add Multiple Choice assessment
   - Write question, options, correct answer
   - Configure settings (Points: 2, Show Explanations: ✓)
   - Save

2. **Duplicate and Modify** (1-2 min per question)
   - Click "Duplicate and Save" on first question
   - Edit question text
   - Edit options (keep same structure)
   - Change correct answer
   - Save

3. **Repeat** for remaining questions

**Time Saved**: 30-45 minutes vs. creating each from scratch

#### Workflow 3: Quick Testing Workflow

**⏱️ Estimated Time**: 5-10 minutes per unit

**Steps**:
1. **Preview Guide Content** (2 min)
   - Switch to Preview mode
   - Scroll through unit
   - Check formatting, headings, code blocks

2. **Test Each Assessment** (2-5 min)
   - Click "Run Assessment" for each lab
   - Verify pass/fail works correctly
   - Check error messages are helpful

3. **Test Virtual Coach** (1-2 min)
   - Ask sample questions
   - Verify responses are relevant

**✅ Checkpoint**: Unit is tested and working correctly.

**💡 Decision Trees**: Search for "🗺️ Decision Trees" for assessment type, UI navigation, and troubleshooting flows.

### ⚡ Parallel Work Opportunities

**Do these tasks simultaneously to save time:**

#### While Waiting for Training/Installation:
- ✅ Add guide content for next unit
- ✅ Review and plan next unit's assessments
- ✅ Update tracking checklist

#### While Testing One Unit:
- ✅ Start adding content for next unit (in separate tab)
- ✅ Review Virtual Coach responses for previous units
- ✅ Document any issues found

#### Batch Operations (Do Together):
- ✅ Add all guide content for Units 0-2 in one session
- ✅ Create all Multiple Choice questions for Unit 8 in one session
- ✅ Configure Virtual Coach for multiple units in one session
- ✅ Test all assessments for a unit in one session

**Time Saved**: 1-2 hours total by working in parallel

### ✅ Enhanced Testing Checklist (Per Unit)

**Use this checklist after completing each unit:**

#### Guide Content Testing
- [ ] Main unit content renders correctly (headings, code blocks, lists)
- [ ] All lab content renders correctly
- [ ] Code blocks have syntax highlighting
- [ ] Links work (if any)
- [ ] Images display (if any)
- [ ] Content flows logically (main content → labs)

#### Assessment Testing
- [ ] All assessments appear in Preview mode
- [ ] Each assessment runs without errors
- [ ] Pass conditions work correctly (test with correct solution)
- [ ] Fail conditions work correctly (test with incorrect solution)
- [ ] Error messages are helpful and specific
- [ ] Points are configured correctly
- [ ] Timeouts are appropriate (not too short/long)

#### Virtual Coach Testing
- [ ] Coach responds to unit-specific questions
- [ ] Responses are accurate and helpful
- [ ] Hints guide students without giving answers
- [ ] Coach handles common errors appropriately

#### Code Playback Testing (if enabled)
- [ ] Code Playback is enabled for relevant files
- [ ] Files are tracked correctly
- [ ] Playback works in student view

**⏱️ Testing Time**: 10-15 minutes per unit  
**Time Saved**: Prevents hours of debugging later

### 🚫 Common Mistakes to Avoid (Saves Hours of Debugging)

**These mistakes waste the most time - avoid them:**

1. **❌ DON'T**: Modify code templates without understanding what they do
   - **✅ DO**: Copy templates exactly, test, THEN modify if needed
   - **Time Saved**: 30-60 minutes per assessment

2. **❌ DON'T**: Create assessments in wrong unit section
   - **✅ DO**: Always verify you're in correct unit before creating
   - **Time Saved**: 10-15 minutes per mistake

3. **❌ DON'T**: Forget to save Guide after creating assessments
   - **✅ DO**: Save Guide immediately after each assessment
   - **Time Saved**: 5-10 minutes per lost assessment

4. **❌ DON'T**: Use wrong file paths in scripts
   - **✅ DO**: Copy paths from Quick Reference Card above
   - **Time Saved**: 15-20 minutes per debugging session

5. **❌ DON'T**: Skip testing assessments after creation
   - **✅ DO**: Test immediately - catch errors early
   - **Time Saved**: Hours of debugging later

6. **❌ DON'T**: Create assessments one-by-one for similar types
   - **✅ DO**: Batch create all multiple choice, then all code tests
   - **Time Saved**: 1-2 hours total

7. **❌ DON'T**: Guess at assessment settings
   - **✅ DO**: Use Standard Settings from Quick Reference Card
   - **Time Saved**: 5-10 minutes per assessment

8. **❌ DON'T**: Ignore error messages - they're usually accurate
   - **✅ DO**: Read error messages carefully - they tell you exactly what's wrong
   - **Time Saved**: 20-30 minutes per debugging session

### 📋 Pre-Implementation Checklist (Do This First!)

**Before starting ANY unit, verify these are ready:**

- [ ] **Codio account access** - Can log in and see dashboard

**🆕 For Total Codio Newbies (Highly Recommended - Saves 30-60 min):**

- [ ] **Demo Guides and Assessments Starter Pack** - Load Codio's built-in examples to see how assessments work
  - **How to do it**: In Codio, click **Starter Packs** in the left navigation
  - Search for **"Demo Guides and Assessments"**
  - Click **Use Pack** → **Create** to install it to your account
  - **Why**: Shows live examples of ALL assessment types (Multiple Choice, Code Test, Fill in the Blanks, etc.)
  - **Time**: Spend 15-20 minutes browsing the examples - you'll understand the Codio UI much faster
  - **Expected Result**: You'll see how assessments look, where settings are, and how students experience them
- [ ] **Project created** - `BankingBot-Level1` project exists
- [ ] **Python 3.11 verified** - `python3.11 -V` works (Rasa Pro installed by students in Lab 0.1)
- [ ] **Project files visible** - Can see `level1/` folder in file tree
- [ ] **Guide editor accessible** - `Tools` → `Guides` → `Edit` opens
- [ ] **Terminal accessible** - `Tools` → `Terminal` opens
- [ ] **Quick Reference Card open** - Keep it in second tab/window

**⏱️ Time to complete**: 5 minutes | **Time saved by doing this**: 30-60 minutes (prevents setup issues)

---

<a id="codio-ai-savers"></a>
### 🤖 Codio AI-Powered Time Savers (No Coding Required!)

**📖 What This Is**: Codio has built-in AI features that can generate assessments and content for you. These save 2-5 hours total and require **zero coding**—just review and approve.

**🎯 For Total Newbies**: If you're new to Codio, use these features! They're designed to be simple: click a button, review the result, approve or edit.

#### 1. AI Assessment Generation (Saves 40-100 min for Multiple Choice)

**What it does**: Codio can **auto-generate** Multiple Choice, Fill in the Blanks, Free Text, Standard Code Test, and Parsons Puzzle assessments from your guide page content.

**How to use it (step-by-step)**:
1. Add an **empty** assessment (click `+`, select **Multiple Choice** or another type)
2. Make sure the guide **page content** above the assessment explains the topic (AI uses this as context)
3. Look for the **Generate** button (usually bottom right of the assessment editor)
4. Click **Generate** → **Generate Using AI**
5. Codio creates a draft question using the page content
6. **Review carefully**—AI can make mistakes! Check the question, options, and correct answer
7. Edit anything that's wrong
8. Click **Apply** then **Create**

**💡 Time-Saving Tip**: For Unit 1, 3, 4, 5, 8—write the instructional content first, then use **Generate** for each Multiple Choice question. Review and refine. Saves 2-5 min per question.

**⚠️ Important**: Always review AI-generated assessments for correctness before deploying.

#### 2. Duplicate Assessment (Saves 5-10 min per copy)

**What it does**: Create one assessment, then **duplicate it** to make copies. Edit only what changes (e.g., question text, options).

**📋 UI Label Variations**: Codio's UI may use different names. Look for: **Duplicate and Save**, **Copy Assessment**, **Clone**, or **Duplicate**—usually in the assessment editor when you click Edit next to an assessment. If you don't see it, try right-clicking the assessment or looking in the Assessments list for a Duplicate option.

**How to use it (step-by-step)**:
1. Create your **first** assessment (e.g., one Multiple Choice question for Unit 1)
2. In the Guide Editor, click **Assessments** button (or Edit next to the assessment)
3. Select the assessment you want to copy
4. Click **Duplicate and Save** button
5. A copy appears—edit the copy (change question, options, correct answer)
6. Repeat for more questions

**💡 Time-Saving Tip**: Create one "template" Multiple Choice for Unit 1, duplicate it 2 more times, then just change the question text and options. Much faster than creating from scratch.

#### 3. LLM Rubric "Generate Rubrics" Button (Saves 10-15 min per LLM assessment)

**What it does**: For **LLM Rubric Autograde** assessments, Codio can **auto-generate** the rubric items from your instructions and guide content.

**📋 UI Label Variations**: Codio's UI may use different names. Look for: **Generate Rubrics**, **Generate Using AI**, **AI Grader**, **Rubric Generator**, or **Create Rubric**—usually in the **Grading** tab of the LLM Rubric assessment editor. The button may be at the top or bottom of the Grading section.

**How to use it (step-by-step)**:
1. Add **LLM Rubric Autograde** assessment
2. Fill in **Instructions** (what student should do)
3. Add **Solution File** path (path to correct/example file) if you have one
4. Go to the **Grading** tab
5. Look for **Generate Rubrics** or **Generate Using AI** button
6. Click it—Codio creates rubric items from your instructions + guide page + solution file
7. **Review and refine**—add or remove criteria, make requirements more specific
8. Save

**💡 Time-Saving Tip**: Use Generate Rubrics first, then refine. Don't write the full rubric from scratch. The manual rubrics in this guide are your **backup** if AI output needs heavy editing.

#### 4. AI Content Generation - Generate Content Wand (Saves 10-20 min per page)

**What it does**: Codio can **auto-generate** guide page content (instructional text) from a page title and optional requirements.

**How to use it (step-by-step)**:
1. Add a new page (or select existing page) in the Guide Editor
2. **Name the page clearly** (e.g., "Understanding YAML Syntax")—AI uses this as context
3. Click **Generate Content** button in the editor ribbon (looks like a magic wand ✨)
4. In the right panel, add **Optional Requirements** (topics to include, tone, learner level)
5. Click **Generate**—Codio creates a draft page
6. **Review carefully**—AI can make mistakes! Edit as needed
7. Click **Approve** to apply to your page

**💡 Time-Saving Tip**: Use for pages that need expansion. Generate first, then edit to match your learning objectives.

#### 5. Fill in the Blanks (Alternative to Multiple Choice for Simple Facts)

**What it does**: For factual recall (e.g., "Use exactly _____ spaces for indentation"), **Fill in the Blanks** can be faster than Multiple Choice. Supports AI generation.

**How to use it**: Add **Fill in the Blanks** assessment. Use chevron notation: `<<<answer>>>` for correct answers. Example: "Use exactly <<<2>>> spaces for YAML indentation."

**💡 When to use**: Simple facts like "The response name must start with <<<utter_>>>" or "Rasa uses <<<YAML>>> for configuration."

#### 6. Bulk Assessment Update

**What it does**: Codio allows updating assessment settings (points, timeout, etc.) **in bulk** across many assessments at once.

**How to use it**: From the course dashboard, find **Bulk Assessment Update** (or similar) in the course/module settings. Select assessments and update settings in one step.

**💡 When to use**: After creating all assessments, if you need to adjust points or timeouts across many at once.

#### 7. Assessment Libraries (For Future Levels)

**What it does**: Save assessments to a **library** and reuse them across courses or assignments. Useful when building Levels 2-5.

**How to use it**: After creating and testing an assessment, add it to your Assessment Library. When building Level 2+, pull from the library instead of recreating.

---

### 🎯 Unit-Specific Pre-Checklists

**Before Unit 0**: (Already covered above - this is your starting point)

**Before Unit 1**: 
- [ ] Unit 0 completed and tested
- [ ] Guide editor working
- [ ] Know how to create Multiple Choice assessment

**Before Unit 2**:
- [ ] Unit 1 completed
- [ ] Template 3 (Multiple Choice) understood
- [ ] Ready to create Code Tests

**Before Unit 3**:
- [ ] Unit 2 completed
- [ ] Template 4 (Response Validation) understood
- [ ] Ready to create Flow validators

**Before Unit 6**:
- [ ] Units 0-5 completed
- [ ] Port forwarding understood (for Inspector)
- [ ] Ready to test with API

**Before Unit 8**:
- [ ] Units 0-7 completed
- [ ] All assessment types mastered
- [ ] Ready for final comprehensive assessment

### ⚡ Copy-Paste Ready: Complete Assessment Configurations

**These are 100% ready to use - no modifications needed:**

**Lab 0.1 Configuration** (Standard Code Test):
```
Type: Standard Code Test (or Code Test)
Command: bash -c 'cd /home/codio/workspace/level1 && source .venv/bin/activate && rasa --version'
Expected Output: Rasa 3.
Working Directory: /home/codio/workspace/level1 (if field exists; otherwise cd is in the command)
Points: 10
Timeout: 30 seconds
Fail Message: [Copy from Unit 0 Step 2 instructions - includes virtual environment creation steps]
```

**Unit 1 Configuration** (Multiple Choice Set):
```
Type: Multiple Choice
Total Questions: 3
Points per Question: 2
Total Points: 6
Show Explanations: ✓
Max Attempts: 3
Randomize Order: Optional

🤖 Time-Saving: Use AI Generate—add empty Multiple Choice, click Generate, review, Apply. Or create one, Duplicate and Save, edit the copy.
```

**Lab 2.2 Configuration** (LLM Rubric Autograde):
```
Type: LLM Rubric Autograde
Points: 10
Timeout: 60 seconds
Instructions: [Copy from Lab 2.2 unit instructions]
Rubric: [Copy from Lab 2.2 unit instructions, OR use Generate Rubrics button]
Solution File: /home/codio/workspace/level1/domain/basics.yml
Files to Check: /home/codio/workspace/level1/domain/basics.yml

🤖 Time-Saving: Use Generate Rubrics button first—Codio creates rubric from instructions + guide content. Review and refine.
```

**Virtual Coach Base Configuration** (All Units):
```
Enabled: ✓
Summarize Prompt: [Unit-specific - see each unit]
Error Augmentation: [Copy from Template 6]
Next Steps: [Unit-specific - see each unit]
```

### 🔄 Workflow Optimization: The 5-Minute Rule

**If something takes more than 5 minutes to figure out, use this workflow:**

1. **Check Quick Reference Card** (30 seconds)
   - Is the answer there? → Use it
   - Not there? → Continue

2. **Check Decision Trees** (1 minute)
   - Does your problem match a tree? → Follow it
   - Not there? → Continue

3. **Check Troubleshooting Section** (2 minutes)
   - Is your error listed? → Follow fix
   - Not there? → Continue

4. **Check Templates Library** (1 minute)
   - Is there a template for this? → Use it
   - Not there? → Continue

5. **Check Unit Instructions** (30 seconds)
   - Re-read the specific unit section
   - Still stuck? → Document the issue and move on (come back later)

**⏱️ Total Time**: 5 minutes max | **Time Saved**: Prevents 30+ minute rabbit holes

### 📊 Testing Shortcuts

**Test multiple assessments quickly:**

**Batch Test Method**:
1. Create 3-5 assessments (don't test yet)
2. Save Guide
3. Open Preview mode
4. Test all assessments in sequence
5. Note all errors
6. Fix all errors in one batch
7. Test again

**⏱️ Time Saved**: 10-15 minutes per batch vs. testing individually

**Quick Validation Checklist** (run after each assessment):
- [ ] Code pasted correctly (no missing lines)
- [ ] Settings match Quick Reference Card
- [ ] File paths are correct
- [ ] Assessment appears in preview
- [ ] "Run Assessment" button works
- [ ] Assessment runs (even if it fails - that's OK, we'll fix it)

**⏱️ Time**: 30 seconds per assessment | **Time Saved**: Catches 90% of errors before testing

### 🎓 Learning Curve Acceleration

**If you're new to Codio, follow this learning path:**

**Hour 1**: Complete Unit 0 only
- This teaches you ALL the basics
- Don't rush - understand each step
- **Result**: You'll be comfortable with Codio

**Hour 2**: Complete Units 1-2
- Apply what you learned
- Use templates for first time
- **Result**: You'll see the pattern

**Hour 3+**: Complete remaining units
- You'll move much faster now
- Use batch creation strategies
- **Result**: Efficient implementation

**⏱️ Total Learning Time**: 3 hours | **Time Saved**: Prevents confusion and mistakes later

### 📝 Implementation Log Template (Optional but Helpful)

**Keep a simple log as you work - helps track time and catch patterns:**

```markdown
## Implementation Log - Level 1

### Day 1 Morning
- 9:00 AM - Started Unit 0
- 9:45 AM - Completed Unit 0 (45 min)
- 10:00 AM - Started Unit 1
- 10:30 AM - Completed Unit 1 (30 min)
- 10:30 AM - Started Unit 2
- 12:30 PM - Completed Unit 2 (2 hours)
- **Total**: 3 hours 15 minutes

### Day 1 Afternoon
- 1:00 PM - Started Unit 3
- [Continue logging...]

### Notes/Issues:
- Unit 2 took longer - Lab 2.2 was complex
- Had to debug YAML validation script
- Will batch create multiple choice next time
```

**⏱️ Time to log**: 1 minute per session | **Time Saved**: Helps identify bottlenecks, improves future estimates

### 🎯 Success Criteria: How to Know You're Done

**You're ready to move to next unit when:**

✅ **All assessments created**
- Every lab/exercise has its assessment
- All assessments appear in Guide editor
- All assessments saved

✅ **All assessments tested**
- Each assessment runs without errors
- Correct answers pass
- Incorrect answers fail with helpful messages

✅ **Virtual Coach configured**
- Enabled in Features
- Unit-specific context added
- Error augmentation configured
- Tested in preview (ask a question)

✅ **Code Playback enabled** (if applicable)
- Tracked files added
- Enabled for unit

✅ **Master Checklist updated**
- Unit marked complete
- Time logged
- Notes added if needed

**⏱️ Verification Time**: 2-3 minutes per unit | **Time Saved**: Prevents incomplete work, reduces rework

### 🚀 Speed Run Mode (For Experienced Users)

**If you've done this before or are very comfortable with Codio:**

1. **Skip detailed instructions** - Use Quick Reference Card only
2. **Use templates directly** - Copy-paste, modify minimally
3. **Batch create everything** - All multiple choice first, then all code tests
4. **Test at end** - Create all assessments, then test all at once
5. **Use Master Checklist** - As roadmap, not detailed guide

**⏱️ Estimated Time**: 8-10 hours (vs 12-16 hours for beginners)

**⚠️ Warning**: Only use this if you're confident. Beginners should follow full instructions.

<a id="path-a"></a>
## 🚀 PATH A: Complete Step-by-Step Implementation Guide

**⏱️ Total Time: 9-11 hours** | **Target: Complete in 2 days**

This section provides a complete, transparent workflow for Path A (Optimized Path). Follow these steps in order for the fastest implementation.

### 📋 Prerequisites Check (Before Starting)

**Before Day 1, you will need**:
- [ ] **Assessment Library** - Create empty organization Assessment Library container (Admin required, takes 5 minutes)
- [ ] Codio account access
- [ ] Organization Admin access (required for Library creation)

**Note**: You'll create the Starter Pack AFTER completing your first project (in Day 1 Step 1). You'll create the Bulk Virtual Coach CSV AFTER creating all assignments (in Day 2 Step 16).

**⏱️ First Course Time**: 13.5-18 hours (creating everything from scratch, but saving to library for future reuse)
**⏱️ Future Courses Time**: 9-11 hours (importing from library - much faster!)

---

### 📋 Master Implementation Checklist (Path A - Optimized)

**🎯 Path A Workflow**: This checklist uses all optimizations (Starter Pack, Assessment Library, Bulk Virtual Coach).

---

#### Pre-Implementation: One-Time Setup (Required - Starting from Ground Zero)

**📖 "Ground Zero" means**: No pre-existing Codio materials for this course. You'll CREATE the project, assessments, and guides from scratch (using this guide's copy-paste content). You'll SAVE to Assessment Library and Starter Pack as you go—so future courses only need to import.

**⏱️ Estimated Time**: 1-2 hours (just creating containers/templates)

**Assessment Library Setup**:
- [ ] Create organization Assessment Library (Admin required)
  - Contact your Codio organization admin, or if you're an admin: Go to Organization Settings → Assessment Library → Create New Library
  - Name it: "Rasa Banking Bot - Level 1"
  - **Note**: This is just an empty container. You'll create and save assessments to it as you implement each unit.

**Starter Pack Setup** (Do this AFTER creating your first project in Day 1):
- [ ] After completing Step 1 (Project Setup) in Day 1 Morning, you'll have a configured project
- [ ] Convert that project to a Starter Pack:
  - Click **Starter Packs** in navigation pane
  - Click **New Pack** → Choose workspace source: **Codio project** (select your project)
  - Enter name: "Rasa Banking Bot - Level 1"
  - Enter description: "Pre-configured project for Level 1 Rasa bot course"
  - Add tags: `rasa`, `python`, `banking-bot`, `level-1`
  - Set visibility: **Private** (for organization)
  - Click **Create**
- [ ] Test Starter Pack (create test project, verify everything works)

**Bulk Virtual Coach CSV Template** (Do this AFTER creating all assignments):
- [ ] After creating all assignments in Day 1-2, download CSV template from Codio (Bulk Settings → Download Assignment Information)
- [ ] Prepare CSV with Virtual Coach settings for all units (see Optimization 3)

**✅ Checkpoint**: Assessment Library container created. Ready to start implementing.

---

#### Day 1 Morning (3.5-4.5 hours): Foundation Setup

**Step 1: Project Setup** (30-60 minutes) ⚡ **FIRST TIME SETUP**

**Ground Zero**: Create project manually; convert to Starter Pack when done (see Pre-Implementation).

- [ ] **Create Codio Project**: Follow Unit 0 implementation notes to create project manually:
  - Create new Codio project (`BankingBot-Level1`, Ubuntu 22.04)
  - Verify Python 3.11 is available (but DO NOT install Rasa Pro - students will install it in Lab 0.1)
  - Create project structure (`domain/`, `data/`, etc.)
  - Create `.env.template` file
  - Create `.codio` file (for Run/Preview buttons)
  - Create `README.md` with instructions
- [ ] **Configure Environment**: Open `.env.template` → Copy to `.env` → Add Rasa license and OpenAI API key
- [ ] **Verify Structure**: Check that `domain/`, `data/`, `config.yml` exist
- [ ] **Create Starter Pack** (for future courses): After project is working, convert to Starter Pack (see Pre-Implementation section)

**⏱️ Time**: 30-60 minutes (first time only; future courses: 5 minutes using Starter Pack)

**Step 2: Add Guide Content - Units 0-2** (1-1.5 hours)

- [ ] **Unit 0**: Add main content + Lab 0.1 content (see "Adding Guide Content" section)
- [ ] **Unit 1**: Add main content
- [ ] **Unit 2**: Add main content + Labs 2.1, 2.2, 2.3 content
- [ ] **Verify**: Preview each unit to ensure content renders correctly

**⏱️ Time**: 1-1.5 hours

**Step 3: Create and Save Assessments - Units 0-2** (2-3 hours) ⚡ **OPTIMIZED WORKFLOW**

**Ground Zero**: Create assessments (not import); save each to Assessment Library.

- [ ] **Create Lab 0.1 assessment**: Follow Unit 0 implementation notes → Save to Library with tags `Course: Level 1`, `Unit: 0`, `Lab: 0.1`
- [ ] **Create Unit 1 assessments**: Follow Unit 1 implementation notes → Create 3 multiple choice questions → Save each to Library with tags `Course: Level 1`, `Unit: 1`
- [ ] **Create Unit 2 assessments**: Follow Unit 2 implementation notes → Create Labs 2.1, 2.2, 2.3 assessments → Save each to Library with tags `Course: Level 1`, `Unit: 2`, `Lab: X.X`
- [ ] **Review**: Test each assessment in preview mode, adjust points/timeouts if needed

**⏱️ Time**: 2-3 hours (creating from scratch, but saving to library for future reuse)

**Step 4: Configure Code Playback** (10 minutes)

- [ ] Enable Code Playback for `domain/basics.yml`
- [ ] Verify tracking is active

**⏱️ Time**: 10 minutes

**Step 5: Test Units 0-2** (30-45 minutes)

- [ ] Test Lab 0.1 assessment
- [ ] Test Unit 1 assessments (3 questions)
- [ ] Test Unit 2 assessments (3 labs)
- [ ] Fix any issues found

**⏱️ Time**: 30-45 minutes

**✅ Checkpoint**: Units 0-2 complete. Foundation established.

**Estimated Time**: 3.5-4.5 hours (first course - creating from scratch)

---

#### Day 1 Afternoon (3.5-4.5 hours): Core Content

**Step 6: Add Guide Content - Units 3-5** (1-1.5 hours)

- [ ] **Unit 3**: Add main content + Labs 3.1, 3.2, 3.3, 3.4 content
- [ ] **Unit 4**: Add main content + Labs 4.1, 4.2 content
- [ ] **Unit 5**: Add main content + Lab 5.1 content
- [ ] **Verify**: Preview each unit

**⏱️ Time**: 1-1.5 hours

**Step 7: Create and Save Assessments - Units 3-5** (2-3 hours) ⚡ **OPTIMIZED WORKFLOW**

**Ground Zero**: Create (not import); save each to Assessment Library.

- [ ] **Create Unit 3 assessments**: Follow Unit 3 implementation notes → Create Labs 3.1, 3.2, 3.3 assessments → Save each to Library with tags `Course: Level 1`, `Unit: 3`, `Lab: X.X`
- [ ] **Create Unit 4 assessments**: Follow Unit 4 implementation notes → Create Labs 4.1, 4.2 assessments → Save each to Library with tags `Course: Level 1`, `Unit: 4`, `Lab: X.X`
- [ ] **Create Unit 5 assessments**: Follow Unit 5 implementation notes → Create Lab 5.1 assessments (6 questions) → Save each to Library with tags `Course: Level 1`, `Unit: 5`, `Lab: 5.1`
- [ ] **Review**: Test each assessment in preview mode, adjust points/timeouts if needed

**⏱️ Time**: 2-3 hours (creating from scratch, but saving to library for future reuse)

**Step 8: Configure Code Playback - Units 3-5** (10 minutes)

- [ ] Enable Code Playback for `data/basics/*.yml`
- [ ] Enable Code Playback for `data/system/patterns/patterns.yml`
- [ ] Verify tracking

**⏱️ Time**: 10 minutes

**Step 9: Test Units 3-5** (45-60 minutes)

- [ ] Test all Unit 3 assessments
- [ ] Test all Unit 4 assessments
- [ ] Test all Unit 5 assessments
- [ ] Fix any issues

**⏱️ Time**: 45-60 minutes

**✅ Checkpoint**: Units 3-5 complete. Core content done.

**Estimated Time**: 3.5-4.5 hours (first course - creating from scratch)

---

#### Day 2 Morning (3-4 hours): Training & Testing

**Step 10: Add Guide Content - Units 6-7** (1 hour)

- [ ] **Unit 6**: Add main content + Labs 6.1, 6.2, 6.3 content
- [ ] **Unit 7**: Add main content + Labs 7.1, 7.2 content (Lab 7.3 removed)
- [ ] **Verify**: Preview each unit

**⏱️ Time**: 1 hour

**Step 11: Create and Save Assessments - Units 6-7** (1.5-2 hours) ⚡ **OPTIMIZED WORKFLOW**

**Ground Zero**: Create (not import); save each to Assessment Library.

- [ ] **Create Unit 6 assessments**: Follow Unit 6 implementation notes → Create Labs 6.1, 6.2, 6.3 assessments → Save each to Library with tags `Course: Level 1`, `Unit: 6`, `Lab: X.X`
- [ ] **Create Unit 7 assessments**: Follow Unit 7 implementation notes → Create Lab 7.2 assessment (Lab 7.1 has no assessment) → Save to Library with tags `Course: Level 1`, `Unit: 7`, `Lab: 7.2`
- [ ] **Review**: Test each assessment in preview mode, adjust points/timeouts if needed

**⏱️ Time**: 1.5-2 hours (creating from scratch, but saving to library for future reuse)

**Step 12: Configure Port Forwarding & Code Playback** (10-15 minutes)

- [ ] Configure port forwarding for Rasa Inspector (port 5005)
- [ ] Enable Code Playback for terminal/API testing
- [ ] Enable Learning Analytics

**⏱️ Time**: 10-15 minutes

**Step 13: Test Units 6-7** (45-60 minutes)

- [ ] Test all Unit 6 assessments (requires Rasa server running)
- [ ] Test Lab 7.2 assessment
- [ ] Fix any issues

**⏱️ Time**: 45-60 minutes

**✅ Checkpoint**: Units 6-7 complete. Training & testing done.

**Estimated Time**: 3-4 hours (first course - creating from scratch)

---

#### Day 2 Afternoon (2.5-3 hours): Final Assessment & Bulk Configuration

**Step 14: Add Guide Content - Unit 8** (15-20 minutes)

- [ ] **Unit 8**: Add main content
- [ ] **Verify**: Preview unit

**⏱️ Time**: 15-20 minutes

**Step 15: Create and Save Assessments - Unit 8** (1.5-2 hours) ⚡ **OPTIMIZED WORKFLOW**

**Ground Zero**: Create (not import); save each to Assessment Library.

- [ ] **Create Unit 8 assessments**: Follow Unit 8 implementation notes → Create Knowledge Check and Practical Exercise assessments → Save each to Library with tags `Course: Level 1`, `Unit: 8`
- [ ] **Note**: Code Review is manual grading only (no assessment to create)
- [ ] **Review**: Test each assessment in preview mode, adjust points/timeouts if needed

**⏱️ Time**: 1.5-2 hours (creating from scratch, but saving to library for future reuse)

**Step 16: Bulk Virtual Coach Configuration** (15-20 minutes) ⚡ **OPTIMIZED**

- [ ] **Upload CSV**: Go to Bulk Settings → Assignment settings → Upload CSV
- [ ] **Verify**: Check a few assignments to confirm Virtual Coach settings applied
- [ ] **Test**: Test Virtual Coach in student preview mode for a few units

**⏱️ Time**: 15-20 minutes (vs. 1-2 hours manual per-unit configuration)

**Step 17: Final Quality Assurance** (1-1.5 hours)

- [ ] Test complete student walkthrough (preview mode)
- [ ] Verify all assessments work correctly
- [ ] Check Virtual Coach responses for all units
- [ ] Verify Code Playback enabled for all tracked files
- [ ] Review and fix any broken assessments
- [ ] Document any customizations

**⏱️ Time**: 1-1.5 hours

**✅ Checkpoint**: Complete course ready for deployment!

**Estimated Time**: 2.5-3 hours (first course - creating from scratch)

---

### 📊 Path A Time Summary

**For Your First Course (Starting from Ground Zero)**:

| Phase | Time | What You're Doing |
|-------|------|-------------------|
| **Pre-Implementation** | 1-2 hours | Create empty Assessment Library container only |
| **Day 1 Morning** | 3.5-4.5 hours | Create project manually + Create and save assessments for Units 0-2 |
| **Day 1 Afternoon** | 3.5-4.5 hours | Create and save assessments for Units 3-5 |
| **Day 2 Morning** | 3-4 hours | Create and save assessments for Units 6-7 |
| **Day 2 Afternoon** | 2.5-3 hours | Create and save assessments for Unit 8 + Bulk Virtual Coach |
| **TOTAL (First Course)** | **13.5-18 hours** | Creating everything from scratch, saving to library as you go |

**For Future Courses** (after first course is complete):

| Phase | Time | What You're Doing |
|-------|------|-------------------|
| **Day 1 Morning** | 2.5-3.5 hours | Use Starter Pack + Import assessments for Units 0-2 |
| **Day 1 Afternoon** | 2.5-3.5 hours | Import assessments for Units 3-5 |
| **Day 2 Morning** | 2-3 hours | Import assessments for Units 6-7 |
| **Day 2 Afternoon** | 1.5-2 hours | Import assessments for Unit 8 + Bulk Virtual Coach |
| **TOTAL (Future Courses)** | **9-11 hours** | Importing from library (much faster!) |

---

### 🔄 Alternative: Manual Implementation Checklist

**If optimizations are not available**, see the unit-by-unit implementation notes for manual creation steps (Path C - 13.5-20.5 hours).

### 💡 Time-Saving Strategies

**Start with**: Optimizations 1-4 (above) and Codio AI features (Generate, Duplicate, Generate Rubrics). See "Codio AI-Powered Time Savers" section.

**Additional tips**:
- **Batch create**: All Multiple Choice for Units 1, 3, 4, 5, 8 in one session; create one, Duplicate and edit
- **Template reuse**: Lab 2.2 → duplicate for Lab 3.2; Lab 2.3 → Lab 3.3 (or import from Assessment Library)
- **Test in batches**: All Unit 2, then Unit 3, etc.; fix errors immediately
- **Bulk Assessment Update**: Adjust points/timeouts across many assessments at once (course settings)

### 🐛 Common Errors & Quick Fixes

**🔍 How to Diagnose**: Each error includes what you'll see, what it means, and exactly how to fix it.

**Error**: "Assessment not appearing in Guide"
- **What You'll See**: Created assessment but can't see it in student preview
- **What It Means**: Assessment wasn't saved or is in wrong section
- **Step-by-Step Fix**:
  1. Go back to Guide editor (`Tools` → `Guides` → `Edit`)
  2. Verify you're in the correct unit section (scroll to find it)
  3. Check if assessment code box is visible (if not, click `+` again)
  4. Click `Save` button (top right of Guide editor)
  5. Click `Preview` button to verify it appears
- **Time saved**: 5-10 minutes per occurrence

**Error**: "Python script fails with 'module not found'"
- **What You'll See**: Assessment runs but shows error like `ModuleNotFoundError: No module named 'yaml'`
- **What It Means**: Assessment language is wrong or Python path is incorrect
- **Step-by-Step Fix**:
  1. Open assessment settings (gear icon or settings button)
  2. Find "Language" dropdown
  3. Select "Python 3" (NOT "Python 2" or "Bash")
  4. Verify "Python Path" is set to `python3.11` or `python3` (if option exists)
  5. Save and test again
- **Time saved**: 10-15 minutes per occurrence

**Error**: "YAML validation fails unexpectedly"
- **What You'll See**: Assessment says YAML is invalid, but file looks correct
- **What It Means**: Hidden characters (tabs) or wrong indentation
- **Step-by-Step Fix**:
  1. Open the YAML file in Codio editor
  2. Enable "Show Whitespace" (usually in View menu or editor settings)
  3. Look for tab characters (shown as arrows →) instead of spaces
  4. Replace ALL tabs with 2 spaces (use Find & Replace: `\t` → `  `)
  5. Verify indentation: each level = 2 more spaces
  6. Save and test again
- **Time saved**: 10-20 minutes per occurrence

**Error**: "Assessment times out"
- **What You'll See**: Assessment runs but stops with "Timeout" error before completing
- **What It Means**: Script takes longer than allowed timeout
- **Step-by-Step Fix**:
  1. Open assessment settings
  2. Find "Timeout" field
  3. Increase value: 30s → 60s (for complex scripts)
  4. For very complex scripts, try 120s
  5. Save and test again
- **Time saved**: 5 minutes per occurrence

**Error**: "Virtual Coach not responding"
- **What You'll See**: Click Virtual Coach icon but nothing happens or error message
- **What It Means**: Virtual Coach isn't enabled or configured
- **Step-by-Step Fix**:
  1. Go to `Education` → `Settings` → `Features`
  2. Find "Virtual Coach" toggle
  3. Turn it ON (toggle should be green/checked)
  4. Click `Save`
  5. Go to `Education` → `Settings` → `Virtual Coach` tab
  6. Verify settings are configured (see Unit 0 for example)
  7. Test in preview mode
- **Time saved**: 5-10 minutes per occurrence

**Error**: "Can't find assessment type dropdown"
- **What You'll See**: Clicked `+` button but don't see assessment type options
- **What It Means**: You might be in wrong view or Codio UI differs
- **Step-by-Step Fix**:
  1. Verify you're in Guide editor (`Tools` → `Guides` → `Edit`)
  2. Look for `+` button at bottom of unit section (not top)
  3. If no `+` button, look for "Add Assessment" or "Add Exercise" button
  4. If still can't find, try right-clicking in the unit section
  5. Alternative: Check Codio documentation for latest UI changes
- **Time saved**: 5-10 minutes per occurrence

### 📊 Progress Tracking

**Use this to track your daily progress**:

| Day | Target Units | Target Time | Actual Time | Status |
|-----|--------------|-------------|-------------|--------|
| Day 1 AM | Units 0-2 | 3-4 hours | ___ hours | ⬜ Not Started / ⏳ In Progress / ✅ Complete |
| Day 1 PM | Units 3-5 | 3-4 hours | ___ hours | ⬜ Not Started / ⏳ In Progress / ✅ Complete |
| Day 2 AM | Units 6-7 | 3-4 hours | ___ hours | ⬜ Not Started / ⏳ In Progress / ✅ Complete |
| Day 2 PM | Unit 8 + QA | 2-3 hours | ___ hours | ⬜ Not Started / ⏳ In Progress / ✅ Complete |

**Total Target**: 12-16 hours | **Actual Total**: ___ hours

### 📖 Codio Terminology Glossary

**Quick reference for Codio-specific terms used in this guide**:

- **Guide**: The main instructional content students see. Contains text, code examples, and assessments.
- **Guide Editor**: The interface for creating/editing Guides. Access via `Tools` → `Guides` → `Edit`.
- **Assessment**: An auto-graded exercise (Code Test, Multiple Choice, etc.) embedded in a Guide.
- **Code Test**: An assessment type where students' code or files are validated by a script (Python/Bash).
- **Multiple Choice**: An assessment type with predefined answer options (one or more correct).
- **Virtual Coach**: AI-powered help system that answers student questions. Configured per unit.
- **Code Playback**: Feature that records and replays how students wrote code. Useful for review.
- **Preview Mode**: View of how students will see the Guide (read-only, can test assessments).
- **Stack**: The base operating system and pre-installed software (e.g., Ubuntu 22.04).
- **Port Forwarding**: Method to access web services (like Rasa Inspector) running in Codio.
- **Learning Analytics**: Dashboard showing student progress, attempts, completion rates.

**Common UI Elements**:
- **`+` button**: Usually means "Add" - click to add new items (assessments, files, etc.)
- **Gear icon ⚙️**: Usually means "Settings" - click to configure options
- **Eye icon 👁️**: Usually means "Preview" - click to see student view
- **Save button**: Usually top-right, saves current work
- **File tree**: Left sidebar showing project files and folders

### 🗺️ Decision Trees: Quick Problem Solving

**Use these when you're stuck - follow the path that matches your situation:**

**Problem: "I can't find where to create an assessment"**
```
Start → Are you in Guide Editor? (Tools → Guides → Edit)
  ├─ NO → Go to Tools → Guides → Edit, then continue
  └─ YES → Are you in the correct unit section?
      ├─ NO → Scroll/find the unit section (e.g., "Unit 1: Introduction")
      └─ YES → Scroll to bottom of that section
          ├─ Do you see a "+" button?
          │   ├─ YES → Click it, select assessment type
          │   └─ NO → Try right-clicking in the section, look for "Add Assessment"
          └─ Still can't find? → Check Codio documentation for latest UI
```

**Problem: "Assessment code doesn't work"**
```
Start → What error do you see?
  ├─ "Module not found" → Check assessment language is "Python 3" (not Bash)
  ├─ "Permission denied" → Check script starts with #!/bin/bash or #!/usr/bin/env python3
  ├─ "Timeout" → Increase timeout in settings (30s → 60s)
  ├─ "Syntax error" → Check code copied correctly (no missing lines)
  └─ "File not found" → Check file paths use /home/codio/workspace/level1/...
```

**Problem: "Virtual Coach doesn't respond"**
```
Start → Is Virtual Coach enabled?
  ├─ NO → Education → Settings → Features → Turn ON Virtual Coach
  └─ YES → Are settings configured?
      ├─ NO → Education → Settings → Virtual Coach → Add context/errors
      └─ YES → Try in preview mode (not edit mode)
          ├─ Works? → Good!
          └─ Still doesn't work? → Check Codio documentation or support
```

**Problem: "I don't know which template to use"**
```
Start → What are you creating?
  ├─ Multiple Choice question → Use Template 3
  ├─ YAML file validation → Use Template 1 (Python) or Template 2 (Bash)
  ├─ Response validation → Use Template 4
  ├─ Flow validation → Use Template 5
  ├─ Virtual Coach config → Use Template 6
  └─ Not sure? → Read the unit instructions - they specify which template
```

**Problem: "Guide content doesn't render correctly"**
```
Content looks wrong → What's the issue?
  ├─ Headings too large/small → Check Markdown heading levels (# vs ##)
  ├─ Code blocks show as plain text → Verify triple backticks (```) preserved
  ├─ Lists not bulleted → Check dashes/spaces in Markdown
  ├─ Formatting broken → Verify Edit mode (not Preview)
  └─ Content missing → Check you copied entire section (including headers)
```

### 📸 Visual Guide: What Codio Looks Like

**While we can't include screenshots, here's what you'll see:**

**Codio Dashboard**:
- Left sidebar: List of your projects
- Top menu: Tools, Education, etc.
- Main area: Project cards or list view
- **Look for**: "New Project" or "+" button (usually green, top right)

**Project View (after opening)**:
- **Left sidebar**: File tree showing folders and files (like Windows Explorer)
- **Top area**: Tabs for open files, menu bar
- **Main area**: Code editor (if file open) or welcome screen
- **Bottom area**: Terminal (can be opened/closed)
- **Look for**: File tree should show `level1/` folder with subfolders

**Guide Editor**:
- **Left sidebar**: Outline of all units (collapsible sections)
- **Main area**: Content editor for selected section
- **Top bar**: Save, Preview, Settings buttons
- **Look for**: Unit sections (Unit 0, Unit 1, etc.) - click to expand

**Assessment Creation**:
- **Code box**: Appears below unit content when you add Code Test
- **Settings panel**: Opens when you click gear icon
- **Look for**: Code editor with syntax highlighting, settings fields below

**Preview Mode**:
- **Looks like**: Student view - clean, read-only
- **Has**: "Run Assessment" buttons at bottom of units
- **Look for**: Eye icon or "Preview" tab to switch to this view

---

<a id="codio-assessment-features"></a>
## 🎯 Codio Native Assessment Features Guide

**📖 Purpose**: This section explains Codio's built-in assessment features and when/how to use them. **Read this before creating any assessments** to save time and avoid unnecessary custom coding.


**🎯 Goal**: Use Codio's native features instead of writing custom grading scripts wherever possible. This reduces development time from 20-25 hours to 8-12 hours.

---

### Overview: Four Assessment Types

Codio provides **four main assessment types**. Choose the right one based on what you're testing:

1. **Standard Code Test** → Simple command/file checks (fastest to set up)
2. **Advanced Code Test** → Custom scripts for complex logic (use sparingly)
3. **Multiple Choice** → Knowledge checks (built-in, no coding)
4. **LLM Rubric Autograde** → AI-powered grading for code/structure validation (most powerful, replaces most custom scripts)

**💡 Decision Tree**: 
- **Testing a command works?** → Standard Code Test
- **Testing YAML structure/code quality?** → LLM Rubric Autograde
- **Testing knowledge/concepts?** → Multiple Choice
- **Testing API calls/complex logic?** → Advanced Code Test

---

### Assessment Type 1: Standard Code Test

**🎯 When to Use**:
- Verifying a command runs successfully (e.g., `python3.11 -m rasa --version`)
- Checking if a file or directory exists
- Simple output comparison (exact match)
- Environment verification

**⏱️ Setup Time**: 5-10 minutes per assessment

**✅ Advantages**:
- Fastest to set up (no coding required)
- Built-in UI for configuration
- Automatic pass/fail based on command output
- Works great for environment checks

**❌ Limitations**:
- Only checks exact command output
- Can't do complex validation logic
- Limited to single command execution

**📋 How to Set Up (Step-by-Step)**:

1. **Navigate to Guide Editor**:
   - In Codio, click **Tools** → **Guides** → **Edit**
   - Find the unit section where you want the assessment
   - Scroll to the bottom of that section

2. **Add Standard Code Test**:
   - Click the **`+`** button (usually at bottom right of section)
   - **Expected Result**: Dropdown menu appears
   - Select **"Code Test"** or **"Standard Code Test"** from dropdown
   - **Expected Result**: A code editor box appears with a settings panel below

3. **Configure the Test**:
   - **In the code editor box**: Type the command to run (e.g., `python3.11 -m rasa --version`)
   - **OR leave empty** if you'll configure via settings panel
   
   - **Find Settings Panel**: Look below the code editor for settings fields, or click gear icon ⚙️
   - **Set "Command" field**: Type the exact command (e.g., `python3.11 -m rasa --version`)
   - **Set "Expected Output" field**: Type what successful output should contain (e.g., `Rasa 3.` or `Python 3.11`)
   - **Set "Points"**: Type number (e.g., `10`)
   - **Set "Timeout"**: Type seconds (e.g., `30`)
   - **Set "Working Directory"** (if needed): Type path (e.g., `/home/codio/workspace/level1`)
   - **Set "Fail Message"**: Type helpful message (e.g., `Make sure Rasa Pro is installed. Run: python3.11 -m pip install --no-cache-dir rasa-pro`)

4. **Test the Assessment**:
   - Click **Preview** button (eye icon) to switch to preview mode
   - Scroll to your assessment
   - Click **"Run Assessment"** button
   - **Expected Result**: Assessment runs, shows pass/fail
   - If it fails, go back to Edit mode and adjust settings

5. **Save**:
   - Click **Save** button (top right of Guide editor)
   - **Expected Result**: Changes saved, no error messages

**📸 What You'll See**:
- **In Edit Mode**: Code editor box with command, settings panel with fields below
- **In Preview Mode**: Clean student view with "Run Assessment" button
- **When Student Runs**: Command executes, output shown, pass/fail displayed

**💡 Example Use Cases**:
- **Unit 0 Lab 0.1**: Verify virtual environment exists and Rasa Pro is installed (`bash -c 'cd /home/codio/workspace/level1 && source .venv/bin/activate && rasa --version'`)
- **Unit 6 Lab 6.1**: Verify `python3.11 -m rasa train` completes successfully
- **Any unit**: Check if required file exists (`test -f domain/basics.yml`)

**⚠️ Common Mistakes**:
- **Mistake**: Writing bash script in code editor when simple command check would work
- **Fix**: Use Standard Code Test with command + expected output
- **Mistake**: Not setting working directory, so command runs in wrong folder
- **Fix**: Always set "Working Directory" to `/home/codio/workspace/level1`

---

### Assessment Type 2: Advanced Code Test

**🎯 When to Use**:
- Complex validation logic (multiple checks, loops, conditionals)
- API testing (HTTP requests, responses)
- Unit tests (running pytest, unittest)
- Custom Python/Bash scripts that can't be done with Standard Code Test

**⏱️ Setup Time**: 20-40 minutes per assessment (requires writing script)

**✅ Advantages**:
- Full control over validation logic
- Can run complex tests (API calls, file parsing, etc.)
- Supports Python, Bash, and other languages
- Can provide detailed feedback

**❌ Limitations**:
- Requires coding knowledge
- Takes longer to develop and test
- More prone to errors
- Harder to maintain

**📋 How to Set Up (Step-by-Step)**:

1. **Navigate to Guide Editor**:
   - Click **Tools** → **Guides** → **Edit**
   - Find the unit section
   - Scroll to bottom

2. **Add Advanced Code Test**:
   - Click **`+`** button
   - Select **"Advanced Code Test"** or **"Code Test"** (if Standard/Advanced option appears, choose Advanced)
   - **Expected Result**: Code editor appears with syntax highlighting

3. **Write Your Script**:
   - **Choose language**: Usually Bash (`#!/bin/bash`) or Python (`#!/usr/bin/env python3`)
   - **Write script** that:
     - Checks what you need (files, commands, API responses)
     - Prints `✅ PASS` or `❌ FAIL` messages
     - Exits with code 0 (success) or 1 (failure)
   - **Example structure**:
     ```bash
     #!/bin/bash
     set -e  # Exit on error
     cd /home/codio/workspace/level1
     
     # Your checks here
     if [ condition ]; then
         echo "✅ PASS: Check passed"
     else
         echo "❌ FAIL: Check failed - reason"
         exit 1
     fi
     ```

4. **Configure Settings**:
   - **Points**: Set point value
   - **Timeout**: Set timeout (e.g., `60` seconds for API calls)
   - **Fail Message**: Provide helpful guidance
   - **Language**: Select Bash or Python (if option available)

5. **Test Thoroughly**:
   - Switch to Preview mode
   - Run assessment multiple times with different scenarios
   - Fix any bugs in script

**💡 Example Use Cases**:
- **Unit 6 Lab 6.3**: Test API endpoint (`curl` requests, check responses)
- **Complex validation**: Multiple file checks, YAML parsing with custom logic

**⚠️ When NOT to Use**:
- **Don't use** for simple command checks → Use Standard Code Test
- **Don't use** for YAML/structure validation → Use LLM Rubric Autograde (much faster)

---

### Assessment Type 3: Multiple Choice

**🎯 When to Use**:
- Testing conceptual knowledge
- Quiz questions about Rasa concepts
- Understanding vs. implementation checks

**⏱️ Setup Time**: 2-5 minutes per question (or 30-60 seconds with AI Generation)

**✅ Advantages**:
- Fastest to create (no coding)
- Built-in UI, just fill in fields
- Automatic grading
- Can provide explanations
- **Supports AI Generation** (Codio can auto-generate from guide page content)
- **Supports Duplicate** (create one, duplicate and edit for more)

**❌ Limitations**:
- Only tests knowledge, not implementation
- Students can guess
- Limited to multiple choice format

**🤖 Time-Saving: Use AI Generation First (Saves 2-5 min per question)**:
1. Add an **empty** Multiple Choice assessment
2. Ensure the guide **page content above** explains the topic
3. Look for the **Generate** button (bottom right of assessment editor)
4. Click **Generate** → **Generate Using AI**
5. Codio creates a draft question—**review carefully** (AI can make mistakes)
6. Edit question, options, and correct answer as needed
7. Click **Apply** then **Create**

**🤖 Time-Saving: Use Duplicate for Similar Questions (Saves 5-10 min per copy)**:
1. Create your **first** Multiple Choice question
2. Click **Assessments** (or Edit next to the assessment)
3. Select the assessment → Click **Duplicate and Save**
4. Edit the copy (change question, options, correct answer)
5. Repeat for more questions—much faster than creating from scratch

**📋 How to Set Up (Step-by-Step)** (Manual method):

1. **Navigate to Guide Editor**:
   - Click **Tools** → **Guides** → **Edit**
   - Find unit section
   - Scroll to bottom

2. **Add Multiple Choice**:
   - Click **`+`** button
   - Select **"Multiple Choice"** or **"Quiz"**
   - **Expected Result**: Form appears with fields for question, options, etc.

3. **Fill in Fields** (or use AI Generate + review):
   - **Question**: Type your question (e.g., `What does "rephrase: True" in metadata do?`)
   - **Points**: Set point value (e.g., `2`)
   - **Options**: Add each answer choice:
     - Type option text
     - Check **"Correct"** checkbox for correct answer(s)
     - Click **"Add Option"** to add more choices
   - **Explanation** (optional): Type explanation shown after student answers
   - **Shuffle Options** (optional): Check if you want random order

4. **Save and Test**:
   - Click **Save**
   - Switch to Preview mode
   - Answer the question yourself to verify it works

**💡 Example Use Cases**:
- **Unit 2 Lab 2.1**: "What does rephrase: True do?"
- **Unit 3**: "What is a flow?"
- **Unit 4**: "When does pattern_session_start run?"

---

### Assessment Type 3B: Fill in the Blanks (Optional Alternative)

**🎯 When to Use**:
- Simple factual recall (e.g., "Use exactly _____ spaces for YAML indentation")
- When you want students to type the answer (not select)
- Alternative to Multiple Choice for specific facts

**⏱️ Setup Time**: 2-4 minutes per question (supports AI Generation)

**✅ Advantages**:
- Fast to create (no coding)
- Supports AI Generation from guide content
- Good for factual recall
- Use chevron notation: `<<<answer>>>` for correct answers

**📋 How to Use**:
1. Add **Fill in the Blanks** assessment (from assessment type dropdown)
2. Type your question with blanks: "Use exactly <<<2>>> spaces for YAML indentation"
3. Or use AI Generate (click **Generate** button) to create from guide content
4. Review and edit—ensure correct answer is in chevrons

**💡 Example Use Cases**:
- "The response name must start with <<<utter_>>>"
- "Rasa uses <<<YAML>>> for configuration files"
- "Use exactly <<<2>>> spaces for indentation (not tabs)"

---

### Assessment Type 4: LLM Rubric Autograde ⭐ **RECOMMENDED FOR MOST CASES**

**🎯 When to Use**:
- **YAML file structure validation** (domain files, flow files, config files)
- **Code quality checks** (proper formatting, required elements)
- **Response validation** (checking if responses exist, have correct structure)
- **Flow validation** (checking if flows are structured correctly)
- **Any assessment where you'd normally write a custom Python/Bash validator**

**⏱️ Setup Time**: 10-15 minutes per assessment (much faster than writing custom scripts)

**✅ Advantages**:
- **Saves 2-4 hours per assessment** vs. writing custom scripts
- Uses AI to understand code structure (not just exact matches)
- Can provide detailed, contextual feedback
- Handles variations in student code (different formatting, etc.)
- No coding required - just describe what to check

**❌ Limitations**:
- Requires clear instructions/rubric
- May need refinement based on test results
- Requires LLM access (usually included in Codio)

**📋 How to Set Up (Step-by-Step)**:

1. **Navigate to Guide Editor**:
   - Click **Tools** → **Guides** → **Edit**
   - Find unit section (e.g., Unit 2, Lab 2.2)
   - Scroll to bottom

2. **Add LLM Rubric Assessment**:
   - Click **`+`** button
   - Look for **"LLM Rubric"**, **"Autograde"**, **"AI Grader"**, or **"Rubric Grader"** option
   - **If you don't see it**: Check Codio documentation or look in assessment type dropdown for AI/LLM options
   - Select it
   - **Expected Result**: Form appears with fields for instructions, rubric, solution file, etc.

**🤖 Time-Saving: Use "Generate Rubrics" First (Saves 10-15 min)**:
- Before filling in the rubric manually, look for a **Generate Rubrics** or **Generate Using AI** button (usually in the Grading tab)
- **📋 UI Note**: If you don't see "Generate Rubrics," look for **AI Grader**, **Rubric Generator**, **Create Rubric**, or **Generate Using AI**—Codio may use different labels in your version
- Click it—Codio creates rubric items from your instructions, guide content, and solution file
- **Review and refine** the generated rubric (add/remove criteria, make more specific)
- The manual rubric below is your **backup** if you prefer to write from scratch or if Generate needs heavy editing

3. **Configure the Assessment** (Fill in all fields, OR use Generate Rubrics above):

   **a. Assessment Instructions** (What student should do):
   - **Field Name**: "Instructions" or "Task Description"
   - **What to type**: Clear description of what student should accomplish
   - **Example**: `Add a new response called "utter_goodbye" to domain/basics.yml with at least 2 text variations. The response should include metadata with rephrase: True.`

   **b. Rubric/Requirements** (What to check):
   - **Field Name**: "Rubric", "Requirements", or "Grading Criteria"
   - **What to type**: Detailed list of what must be present/correct
   - **Example**:
     ```
     Requirements:
     1. File domain/basics.yml exists and is valid YAML
     2. Response "utter_goodbye" exists in responses section
     3. Response has at least 2 text variations
     4. Response includes metadata with rephrase: True
     5. YAML syntax is correct (proper indentation, no syntax errors)
     ```

   **c. Solution File** (Optional but recommended):
   - **Field Name**: "Solution File" or "Reference File"
   - **What to type**: Path to example/correct version (e.g., `/home/codio/workspace/level1/domain/basics.yml`)
   - **Purpose**: Helps LLM understand expected structure

   **d. Files to Check**:
   - **Field Name**: "Files to Grade" or "Student Files"
   - **What to type**: Path(s) to file(s) student should modify (e.g., `/home/codio/workspace/level1/domain/basics.yml`)
   - **Multiple files**: Separate with commas or newlines

   **e. Guide Content Context** (Optional):
   - **Field Name**: "Guide Content" or "Context"
   - **What to type**: Copy relevant section from guide that explains the task
   - **Purpose**: Helps LLM understand learning objectives

   **f. Points**:
   - **Field Name**: "Points" or "Max Score"
   - **What to type**: Total points (e.g., `10`)

   **g. Timeout**:
   - **Field Name**: "Timeout"
   - **What to type**: Seconds (e.g., `60` for LLM processing)

4. **Test the Assessment**:
   - **Create test scenario**: Make the file with correct content
   - Switch to Preview mode
   - Run assessment
   - **Expected Result**: Assessment passes, shows feedback
   - **If it fails**: Refine rubric/instructions to be more specific

5. **Refine Based on Results**:
   - Run with intentionally incorrect student work
   - Verify it catches errors appropriately
   - Adjust rubric if needed

**📸 What You'll See**:
- **In Edit Mode**: Form with multiple fields (instructions, rubric, files, etc.)
- **In Preview Mode**: Student sees task description, can submit work
- **When Student Runs**: LLM analyzes their code, provides detailed feedback

**💡 Example Use Cases** (Replace custom scripts with LLM Rubric):
- **Unit 2 Lab 2.2**: Validate domain file structure (responses exist, correct YAML, metadata present)
- **Unit 3 Lab 3.2**: Validate flow file (flows exist, correct structure, triggers present)
- **Unit 4 Lab 4.2**: Validate system patterns (pattern_session_start exists, correct format)
- **Unit 7 Lab 7.2**: Validate complete bot structure (all files present, correct structure)

**⚠️ Common Mistakes**:
- **Mistake**: Writing vague rubric ("check if file is correct")
- **Fix**: Be specific ("Response utter_X exists, has 2+ text variations, includes metadata")
- **Mistake**: Not providing solution file or guide context
- **Fix**: Always include solution file path and relevant guide content
- **Mistake**: Testing with perfect code only
- **Fix**: Test with incorrect code to verify it catches errors

**🎯 Pro Tips**:
- **Start specific**: List exact requirements (file paths, key names, structure)
- **Include examples**: Reference solution file or provide example in rubric
- **Test iteratively**: Run assessment, refine rubric, test again
- **Use guide content**: Copy relevant guide sections to help LLM understand context

---

### Quick Reference: Which Assessment Type to Use?

| Task | Assessment Type | Setup Time |
|------|----------------|------------|
| Verify command works (`rasa --version`) | Standard Code Test | 5-10 min |
| Check file exists | Standard Code Test | 5-10 min |
| Validate YAML structure | LLM Rubric Autograde | 10-15 min |
| Check response exists in domain file | LLM Rubric Autograde | 10-15 min |
| Validate flow structure | LLM Rubric Autograde | 10-15 min |
| Test API endpoint | Advanced Code Test | 20-40 min |
| Knowledge quiz question | Multiple Choice | 2-5 min |
| Simple factual recall ("Use ___ spaces") | Fill in the Blanks | 2-4 min |
| Complex multi-file validation | LLM Rubric Autograde | 15-20 min |

**💡 Rule of Thumb**: If you're about to write a Python/Bash script to validate YAML or code structure, **use LLM Rubric Autograde instead**. It's faster and more flexible.

**🤖 Codio AI Features**: Multiple Choice, Fill in the Blanks, Standard Code Test, Free Text, and Parsons Puzzle all support **AI Generation**—click **Generate** to auto-create from guide content. Always review AI output before deploying.

---

### Migration Guide: Replacing Custom Scripts

**Before** (Custom Python Script - 30-60 minutes):
```python
#!/usr/bin/env python3
import yaml
import sys
# ... 50+ lines of validation code ...
```

**After** (LLM Rubric - 10-15 minutes):
- Instructions: "Add utter_goodbye response to domain/basics.yml"
- Rubric: "Response exists, has 2+ variations, includes metadata"
- Solution file: `/home/codio/workspace/level1/domain/basics.yml`
- Files to check: `/home/codio/workspace/level1/domain/basics.yml`

**Time Saved**: 20-45 minutes per assessment × 5-8 assessments = **2-6 hours saved**

---

<a id="adding-guide-content"></a>
## 📝 Adding Guide Content to Codio: Complete Instructions

**🎯 Purpose**: How to add all student-facing content (main unit + labs) to Codio's Guide Editor.

**📋 Copy rules**: See "⚠️ CRITICAL: Document Structure" at the top. Content uses Markdown and is copy-paste ready.

### Understanding Guide Content Structure

Each unit has **two types of content** that need to be added to Codio:

1. **Main Unit Content**: Everything from `## For Students` to the first lab (concepts, explanations, examples)
2. **Lab Content**: Individual lab instructions (each lab has its own Step 0.5 section with explicit Markdown)

**Example Structure**:
```
Unit 2: Understanding the Domain File
├── Main Unit Content (concepts, explanations)
│   ├── 2.1 What is a Domain?
│   ├── 2.2 Understanding Responses
│   └── 2.3 Response Variations (concept explanation)
└── Lab Content (hands-on exercises)
    ├── Lab 2.1: Understanding YAML Syntax
    ├── Lab 2.2: Creating Your First Response
    └── Lab 2.3: Add Response Variations
```

### Step-by-Step: Adding Main Unit Content

**⏱️ Estimated Time**: 10-15 minutes per unit

**What you're doing**: Adding the conceptual content (explanations, examples, theory) that students read before doing labs.

**How to do it**:

1. **Open Codio's Guide Editor**:
   - In Codio, click **Tools** → **Guides** → **Edit**
   - **Expected Result**: Guide editor opens, showing all unit sections in a left sidebar

2. **Create or Find Unit Section**:
   - **If unit doesn't exist**: Click "+" or "Add Section" → Name it (e.g., "Unit 2: Understanding the Domain File")
   - **If unit exists**: Click on it in the left sidebar
   - **Expected Result**: Unit section is selected and visible in the main editing area

3. **Identify Main Unit Content**:
   - In this guide, find the unit (e.g., `# Unit 2: Understanding the Domain File`)
   - Find `## For Students` section
   - **Copy everything** from `## For Students` down to (but NOT including) the first `### Lab X.X:` heading
   - **Example for Unit 2**: Copy from `## For Students` → `### 2.1 What is a Domain?` → `### 2.2 Understanding Responses` → `### 2.3 Response Variations` → Stop before `### Lab 2.1:`

4. **Paste into Codio**:
   - Click in the Unit section's content area in Codio
   - Paste the content (Ctrl+V / Cmd+V)
   - **Expected Result**: All main unit content appears in the editor

5. **Verify and Save**:
   - Check formatting (headings, code blocks, lists)
   - Save (Ctrl+S / Cmd+S)
   - Preview to ensure it renders correctly

**✅ Checkpoint**: Main unit content is visible, saved, and renders correctly in Preview mode.

**💡 Time-Saving Tip**: You can add all main unit content for multiple units in one session. Open multiple tabs of this guide, copy-paste each unit's main content sequentially.

### Step-by-Step: Adding Lab Content

**⏱️ Estimated Time**: 5-10 minutes per lab

**What you're doing**: Adding the hands-on exercise instructions for each lab.

**How to do it**:

Each lab has a **Step 0.5** section in the "For Codio Team" implementation notes that contains:
- Detailed instructions (for YOU, the implementer)
- Exact Markdown to copy-paste (marked with `⬇️ START COPYING HERE ⬇️` and `⬆️ STOP COPYING HERE ⬆️` visual markers)
- Troubleshooting tips (for YOU, NOT for students)

**Process**:
1. Navigate to the lab's Step 0.5 section (see table below)
2. Copy from `⬇️ START COPYING HERE ⬇️` to `⬆️ STOP COPYING HERE ⬆️` (exclude markers)
3. Paste into Codio Guide Editor in the unit section, after main content
4. Do NOT copy troubleshooting or Step 1+ content—implementers only

### 🚀 Batch Operations: Adding All Guide Content Efficiently

**⏱️ Estimated Time**: 1-2 hours total (vs. 2-3 hours doing individually)

**🎯 Purpose**: Add all guide content in one efficient session to save time.

**Strategy**: Work unit-by-unit, adding both main content and all labs for each unit before moving to the next.

**How to do it**:

1. **Prepare Your Workspace**:
   - Open Codio Guide Editor (Tools → Guides → Edit)
   - Open this guide in a separate tab/window
   - Have a notepad ready for tracking progress

2. **For Each Unit (0-8)**:
   - **Step A**: Add main unit content (see instructions above)
   - **Step B**: Add all lab content for that unit (use Step 0.5 sections)
   - **Step C**: Save and preview to verify
   - **Step D**: Check off in your tracking list

3. **Time-Saving Techniques**:
   - **Use multiple tabs**: Keep Codio Guide Editor open in one tab, this guide in another
   - **Copy-paste sequence**: Copy main content → paste → copy Lab 1 → paste → copy Lab 2 → paste, etc.
   - **Batch save**: Add content for entire unit, then save once (not after each paste)
   - **Preview once per unit**: Preview after completing all content for a unit, not after each lab

**Expected Time Savings**: 30-60 minutes total vs. adding content individually

**✅ Checkpoint**: All guide content for all units is added, saved, and renders correctly.

### 📋 Quick Reference: Step 0.5 Locations

**Use this table to quickly find where each lab's copy-paste Markdown is located:**

| Unit | Lab | Step 0.5 Section Location | Estimated Time |
|------|-----|---------------------------|----------------|
| 0 | 0.1 | Unit 0 Implementation Notes → Step 1.5 | 5-10 min |
| 2 | 2.1 | Unit 2 Implementation Notes → Lab 2.1 → Step 0.5 | 5-10 min |
| 2 | 2.2 | Unit 2 Implementation Notes → Lab 2.2 → Step 0.5 | 10-15 min |
| 2 | 2.3 | Unit 2 Implementation Notes → Lab 2.3 → Step 0.5 | 5-10 min |
| 3 | 3.1 | Unit 3 Implementation Notes → Lab 3.1 → Step 0.5 | 5-10 min |
| 3 | 3.2 | Unit 3 Implementation Notes → Lab 3.2 → Step 0.5 | 10-15 min |
| 3 | 3.3 | Unit 3 Implementation Notes → Lab 3.3 → Step 0.5 | 5-10 min |
| 3 | 3.4 | Unit 3 Implementation Notes → Lab 3.4 → Step 0.5 | 5-10 min |
| 4 | 4.1 | Unit 4 Implementation Notes → Lab 4.1 → Step 0.5 | 5-10 min |
| 4 | 4.2 | Unit 4 Implementation Notes → Lab 4.2 → Step 0.5 | 5-10 min |
| 5 | 5.1 | Unit 5 Implementation Notes → Lab 5.1 → Step 0.5 | 5-10 min |
| 6 | 6.1 | Unit 6 Implementation Notes → Lab 6.1 → Step 0.5 | 5-10 min |
| 6 | 6.2 | Unit 6 Implementation Notes → Lab 6.2 → Step 0.5 | 5-10 min |
| 6 | 6.3 | Unit 6 Implementation Notes → Lab 6.3 → Step 0.5 | 5-10 min |
| 7 | 7.1 | Unit 7 Implementation Notes → Lab 7.1 → Step 0.5 | 5-10 min |
| 7 | 7.2 | Unit 7 Implementation Notes → Lab 7.2 → Step 0.5 | 5-10 min |
| 7 | 7.3 | Unit 7 — 7.3 Best Practices (content only; Lab 7.3 removed) | — |

**Total Labs**: 17 labs  
**Total Estimated Time for All Lab Content**: 1.5-2.5 hours  
**Total Estimated Time for All Main Unit Content**: 1.5-2 hours  
**Combined Total**: 3-4.5 hours (can be done in one session)

### 🔍 Troubleshooting Guide Content Issues

**Problem**: Content doesn't paste correctly
- **Solution**: Make sure you're in Edit mode (not Preview mode) in Codio Guide Editor
- **Verify**: You should see editing toolbar/buttons, not just read-only view

**Problem**: Formatting looks wrong after pasting
- **Solution**: Codio uses Markdown - the content is already formatted. Try:
  1. Refresh Preview mode
  2. Check that triple backticks (```) are preserved
  3. Verify you copied the entire code block (including backticks)

**Problem**: Can't find where to paste content
- **Solution**: 
  1. Make sure you've created the unit section first
  2. Click in the unit section's content area
  3. If unit is empty, click at the top; if it has content, scroll to bottom and click

**Problem**: Content is too long and hard to manage
- **Solution**: Use batch operations - add all content for one unit at once, then move to next unit

**Problem**: Not sure what content to copy for main unit
- **Solution**: Copy from `## For Students` to the line before the first `### Lab X.X:` heading. If unsure, check the "For Codio Team" section - it starts right after the student content ends.

### 💡 Best Practices

1. **Add main unit content first**, then labs (logical flow for students)
2. **Save frequently** (after each unit, not after each lab)
3. **Preview after each unit** to catch formatting issues early
4. **Use batch operations** for efficiency (add all content for a unit in one session)
5. **Keep this guide open** in a separate tab for easy reference

### 📚 Official Codio Documentation References

**This guide is designed to align with Codio's official documentation and best practices.**

**Codio Guide Editor Documentation**:
- **Official Docs**: https://docs.codio.com/guides/ (or search "Codio Guides" in Codio documentation)
- Codio Guides use **Markdown format** (as documented in Codio's official guide editor documentation)
- Content can be added via the Guide Editor interface (**Tools** → **Guides** → **Edit**)
- Preview mode shows how students will see the content
- **Markdown Support**: Codio supports standard Markdown syntax (headings, code blocks, lists, links)

**Codio Assessment Documentation**:
- **Official Docs**: https://docs.codio.com/assessments/ (or search "Codio Assessments" in Codio documentation)
- **Assessment Types**: Standard Code Test, Advanced Code Test, Multiple Choice, LLM Rubric Autograde, Fill in the Blanks
- **AI Features**: Codio's AI Assessment Generation and LLM Rubric features are documented in Codio's assessment documentation
- **Port Forwarding**: https://docs.codio.com/ports/ (for Rasa Inspector access)

**Codio Virtual Coach Documentation**:
- **Official Docs**: https://docs.codio.com/virtual-coach/ (or search "Virtual Coach" in Codio documentation)
- Virtual Coach can be configured per unit with custom hints and responses

**Codio Code Playback Documentation**:
- **Official Docs**: https://docs.codio.com/code-playback/ (or search "Code Playback" in Codio documentation)
- Code Playback tracks student code changes for instructor review

**For More Information**:
- **Codio Documentation Home**: https://docs.codio.com/
- **Search**: Use Codio's documentation search for specific features
- **Support**: Contact Codio support if UI differs from this guide (Codio may update interfaces)

**Note**: This guide reflects Codio's features as of the guide's creation date. If Codio's UI or features have changed, refer to the latest official documentation.

---

## For Codio Team: Unit 0 Implementation Notes

**Type**: Setup Lab (Installation required)

**📋 IMPORTANT: Add Guide Content First**

**Before creating assessments**, you must add the student-facing content to Codio's Guide Editor:

1. **Add Main Unit Content**: Copy content from `## For Students` (line 94) to before `### Lab 0.1` (line 351). See "Adding Guide Content to Codio" section above for detailed instructions.

2. **Add Lab Content**: Use Step 1.5 below for Lab 0.1 content.

**⏱️ Estimated Time for Guide Content**: 15-20 minutes  
**Why First**: Students need to see the content before they can complete assessments.

---

### Step 0: Enable Sandboxed Terminal (Required for Virtual Environment)

**⏱️ Estimated Time**: 5-10 minutes

**💡 Why This Matters**: Codio's sandboxed terminal allows students to create and use virtual environments safely. This is required for Lab 0.1 where students will create a virtual environment and install Rasa Pro.

**📋 Checkpoint**: After completing this step, students will be able to create virtual environments in the terminal.

**What you're doing**: Enabling Codio's sandboxed terminal feature so students can create virtual environments.

**🔍 Before You Start**: You need Codio admin/instructor access to configure course settings.

**How to do it**:

1. **Access Course Settings**:
   - Log into Codio dashboard
   - Navigate to your course (or create a new course)
   - Click on the course name to open it
   - Look for **Settings** or **Course Settings** (usually in left sidebar or top menu)
   - Click **Settings**

2. **Enable Sandboxed Terminal**:
   - In Settings, look for **Features** or **Terminal** section
   - Find **"Sandboxed Terminal"** or **"Isolated Terminal"** option
   - **Toggle it ON** (should show as enabled/checked)
   - **If you don't see this option**: Look for **"Terminal Settings"** or **"Environment Settings"**
   - Some Codio versions may have this under **"Security"** or **"Permissions"** settings

3. **Verify Terminal Access**:
   - Go to your project in Codio
   - Click **Tools** → **Terminal** (or press `Ctrl+Shift+` `)
   - Terminal should open at bottom of screen
   - **Expected Result**: Terminal prompt appears, ready for commands

4. **Test Virtual Environment Creation** (Optional but recommended):
   - In the terminal, run:
     ```bash
     python3.11 -m venv test_venv
     ```
   - **Expected Result**: Virtual environment folder `test_venv` is created (no errors)
   - **Clean up**: Run `rm -rf test_venv` to remove test environment
   - **If this fails**: Check that Python 3.11 is available (`python3.11 -V`) and that sandboxed terminal is enabled

**✅ Checkpoint**: Sandboxed terminal is enabled. Students can now create virtual environments.

**Troubleshooting**:
- **Can't find Sandboxed Terminal setting**: Check Codio documentation or contact Codio support - feature name may vary by version
- **Terminal not opening**: Verify you have proper permissions (instructor/admin access)
- **Virtual environment creation fails**: Ensure Python 3.11 is installed in the Codio stack

---

### Step 1: Configure Codio Workspace (One-Time Setup)

**⏱️ Estimated Time**: 30-45 minutes

**💡 Time-Saving Tip**: Do this setup once at the beginning. All subsequent units will use this workspace.

**📋 Checkpoint**: After completing this step, you should have a Codio project with Python 3.11 and all project files ready. Students will create a virtual environment and install Rasa Pro themselves in Lab 0.1.

**What you're doing**: Setting up the Codio project structure. Students will create a virtual environment and install Rasa Pro themselves in Lab 0.1.

**🔍 Before You Start**: Make sure you have:
- Codio account access
- Sandboxed terminal enabled (Step 0 above)
- Git repository URL (if importing from Git) OR zip file of `level1/` folder
- Rasa Pro license key (for later)
- OpenAI API key (for later)

**How to do it**:

1. **Create the Codio project**:
   - Log into Codio dashboard (you should see your projects list)
   - Click **Projects** button (usually top menu or left sidebar)
   - Click **New Project** button (usually green "+" or "Create" button)
   - **Choose import method**:
     - **Option A (Recommended)**: Choose **Import from Git**
       - Paste your Git repository URL
       - Codio will clone the repository
     - **Option B**: Choose **Upload** or **Import**
       - Upload a zip file of the `level1/` folder
   - **Name the project**: Type `BankingBot-Level1` in the name field
   - **Select stack**: Choose **Ubuntu 22.04** from the stack dropdown
   - Click **Create** or **Import** button
   - **Expected Result**: Codio opens your project in a new tab, showing file tree on left and main editor area
   
   **✅ Checkpoint**: You should see the project files in the left sidebar (file tree). If you see an empty project, the import didn't work - try again.

2. **Verify Python 3.11 is available** (DO NOT install Rasa Pro or create virtual environment - students will do this in Lab 0.1):
   - After project opens, click **Tools** → **Terminal** (or press `Ctrl+Shift+` `)
   - **Expected Result**: Terminal window opens at bottom of screen, showing command prompt
   - **Run this command**:
     ```bash
     python3.11 -V  # Verify Python 3.11 is available
     ```
     **Expected Output**: Should show `Python 3.11.x` (version number)
   
   **⚠️ IMPORTANT**: Do NOT install Rasa Pro or create a virtual environment here. Students will do this themselves in Lab 0.1 as their first exercise. This ensures they:
   - Learn how to create a virtual environment
   - Learn the installation process
   - Understand their environment setup
   - Experience the full setup workflow
   
   **✅ Checkpoint**: Python 3.11 is available. If you see errors, check:
   - Python 3.11 is installed in the Codio stack
   - You may need to select a different stack or configure Python 3.11
   - Sandboxed terminal is enabled (from Step 0)

3. **Create `.env.template` file**:
   - In Codio file tree (left sidebar), find the `level1/` folder
   - **Right-click** on `level1/` folder (or click folder name, then look for menu)
   - Select **New File** from context menu (might say "Create File" or "Add File")
   - **Name the file**: Type exactly `.env.template` (including the dot at the beginning)
   - **Expected Result**: New file appears in file tree, editor opens with empty file
   - **Paste this content** (select all, delete, then paste):
     ```text
     RASA_LICENSE=YOUR_LICENSE_KEY_HERE
     OPENAI_API_KEY=YOUR_OPENAI_KEY_HERE
     ```
   - **Save**: Press `Ctrl+S` (or `Cmd+S` on Mac) OR click Save button
   - **Expected Result**: File shows as saved (no asterisk * next to filename)
   
   **✅ Checkpoint**: File `.env.template` exists in `level1/` folder and contains the two lines above.

4. **Verify project structure**:
   - Confirm these folders/files exist in `/home/codio/workspace/level1/`:
     - `domain/basics.yml`
     - `data/basics/` (with greet.yml, help.yml, contact.yml)
     - `data/system/patterns/patterns.yml`
     - `config.yml`, `credentials.yml`, `endpoints.yml`

### Step 1.5: Add Lab 0.1 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 0.1 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 0.1 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you completed Step 1 (workspace setup). You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**:
   - In Codio, click **Tools** in the top menu bar
   - Click **Guides** from the dropdown menu
   - Click **Edit** button (usually visible in the Guides panel, or look for an "Edit" icon)
   - **Expected Result**: Guide editor opens, showing all unit sections in a left sidebar (outline view) and main editing area

2. **Create or Find Unit 0 Section**:
   - **If Unit 0 doesn't exist**: Look for a "+" button or "Add Section" option (usually at the top of the left sidebar)
     - Click it to create a new section
     - Name it: **Unit 0: Prerequisites and Setup**
   - **If Unit 0 already exists**: Click on it in the left sidebar to select it
   - **Expected Result**: Unit 0 section is selected and visible in the main editing area

3. **Add Lab 0.1 Subsection**:
   - **Scroll down** in Unit 0's content area (or click at the end of existing content)
   - **Click** in the content editing area where you want Lab 0.1 to appear
   - **OR** look for an "Add Subsection" or "+" button within Unit 0
   - **Expected Result**: Cursor is positioned where you'll paste the content

4. **Copy and Paste the Markdown Content**:
   - **Select ALL the text** in the code block below (from `### Lab 0.1` to the `---` line)
   - **Copy it** (Ctrl+C / Cmd+C)
   - **Paste it** into Codio's Guide Editor at the location you selected (Ctrl+V / Cmd+V)
   - **Expected Result**: The Markdown content appears in the editor

5. **Verify the Content**:
   - **Check formatting**: You should see headings, code blocks, and lists formatted correctly
   - **Save**: Click **Save** button (usually top right of Guide editor, or Ctrl+S / Cmd+S)
   - **Preview**: Click **Preview** button (eye icon 👁️) or switch to Preview tab
   - **Expected Result**: Content displays nicely formatted with proper headings, code blocks with syntax highlighting, and bulleted lists

**✅ Checkpoint**: Lab 0.1 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode (headings are large, code blocks have gray background, lists are bulleted).

**📋 Copy This Markdown for Lab 0.1**:

⬇️ START COPYING HERE ⬇️

### Lab 0.1: Create Virtual Environment and Install Rasa Pro

**Objective**: Create a virtual environment, install Rasa Pro in it, and verify the installation is successful.

**Important**: This is your first step! You must create a virtual environment and install Rasa Pro before you can proceed with any other exercises.

**Before you start**: Open a terminal in Codio. Run `cd level1` so you are in the `level1` folder. All commands in this lab should be run from there.

#### Steps

1. **Create a Virtual Environment**
   
   In the terminal, first check that Python 3.11 is installed correctly:
   ```bash
   python3.11 -V
   ```
   Then type:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```
   
   **What to expect**: Your command prompt should show `(.venv)` at the beginning, indicating the virtual environment is active.

2. **Install Rasa Pro**
   
   With the virtual environment activated, run:
   ```bash
   pip install --no-cache-dir rasa-pro
   ```
   
   **What to expect**:
   - Installation will take 2-5 minutes
   - You'll see progress messages as packages are downloaded and installed
   - At the end, you should see "Successfully installed rasa-pro-x.x.x" along with a list of dependencies

3. **Verify Installation**
   
   Once installation completes, verify Rasa Pro is installed correctly:
   ```bash
   rasa --version
   ```
   
   **Expected output**: You should see version information like "Rasa 3.x.x" (no errors).
   
   **If you see an error**: The installation may not have completed successfully. Review any error messages from Step 1 and try installing again.

4. **Check Project Structure** *(After installation)*
   ```bash
   # Check that project folders exist
   ls -la domain/
   ls -la data/
   ```
   Confirm:
   - The `domain/` folder exists
   - The `data/` folder exists

   ```bash
   # Check that the following .yml files exist
   ls -la config.yml credentials.yml endpoints.yml
   ```

5. **Check Environment Variables**

   **Codio**: Credentials are pre-configured. To verify they're loaded, run:
   ```bash
   [ -n "$RASA_LICENSE" ] && echo "RASA_LICENSE is set" || echo "RASA_LICENSE is not set"
   [ -n "$OPENAI_API_KEY" ] && echo "OPENAI_API_KEY is set" || echo "OPENAI_API_KEY is not set"
   ```
   Both should report "is set". If not, ask your instructor.
   
   **Local setup**: The .env file should exist in your project root. Run **ls -la .env** to confirm. If it doesn't, create it using the instructions in section 0.1.

**✅ Success Criteria**: Once you can run `rasa --version` successfully and see version information, you're ready to move on to the next exercises. You can then run the assessment for this lab to confirm your setup.

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 1.5 Complete**: You've copied the student-facing content for Lab 0.1. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If you can't find Guide Editor**: Check Codio's top menu - it might be under "Education" → "Guides" instead of "Tools" → "Guides"

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

### Step 2: Create Lab 0.1 Assessment (Auto-Graded Verification)

**⏱️ Estimated Time**: 10-15 minutes (reduced from 20-30 minutes using Standard Code Test)

**💡 Time-Saving Tip**: Using Standard Code Test instead of Advanced Code Test saves 10-15 minutes. No script writing needed - just configure fields!

**📋 Checkpoint**: After completing this step, you should be able to click "Run Assessment" in preview mode and see it pass (if environment is set up correctly).

**What you're doing**: Creating a **Standard Code Test** assessment that verifies students have successfully created a virtual environment and installed Rasa Pro in it. This assessment checks that both the virtual environment creation and Rasa Pro installation were completed correctly.

**🔍 Before You Start**: This assessment verifies that students completed the virtual environment creation and installation steps. Students must create a virtual environment and install Rasa Pro first (as described in Lab 0.1), then this assessment confirms both steps worked.

**📖 Assessment Type**: **Standard Code Test** (see "Codio Native Assessment Features Guide" above for details)

**How to do it**:

1. **Navigate to the Guide section**:
   - In Codio, click **Tools** → **Guides** → **Edit**
   - **Expected Result**: Guide editor opens, showing all unit sections in a list/outline view
   - **Find the section**: Look for **Unit 0 – Prerequisites & Setup** (or similar name)
   - **Scroll down**: Click on that section to expand it, then scroll to the very bottom
   - **Expected Result**: You should see the end of Unit 0 content, with a `+` button or "Add Assessment" option visible
   
   **⚠️ If you can't find the section**: 
   - Check if Guide editor has a search/filter box - search for "Unit 0"
   - Verify you're in Edit mode (not Preview mode)
   - Try collapsing and re-expanding sections

2. **Add a Standard Code Test assessment**:
   - **Click the `+` button** (usually at bottom right of Unit 0 section, might say "Add Assessment" or "Add Exercise")
   - **Expected Result**: Dropdown menu appears with assessment type options
   - **Select "Code Test"** or **"Standard Code Test"** from the dropdown
   - **Expected Result**: A code editor box appears below Unit 0 content, with a settings panel below it
   
   **⚠️ If dropdown doesn't appear**:
   - Try right-clicking in the Unit 0 section
   - Look for "Insert Assessment" or "Add Code Test" in context menu
   - Check Codio documentation for latest UI

3. **Configure the Standard Code Test** (We'll use a bash script to check both virtual environment and Rasa Pro):
   
   **a. In the Settings Panel** (below the code editor, or click gear icon ⚙️):
   
   - **Command field**: Type exactly: `bash -c 'cd /home/codio/workspace/level1 && source .venv/bin/activate && rasa --version'`
     - **What this does**: Changes to level1, activates the virtual environment, and runs Rasa version command
     - **Expected output**: Should contain "Rasa 3." or similar version string
     - **Why this approach**: Verifies both that `.venv` exists in level1 AND that Rasa Pro is installed in it
   
   - **Expected Output field**: Type: `Rasa 3.`
     - **What this does**: Codio checks if command output contains this text
     - **Note**: This is a substring match - any output containing "Rasa 3." will pass
   
   - **Working Directory field**: Type: `/home/codio/workspace`
     - **What this does**: Ensures command runs in project root where `.venv` should be
     - **Why needed**: The virtual environment should be in the project root
   
   - **Points field**: Type: `10`
     - **What this does**: Sets point value for this assessment
   
   - **Timeout field**: Type: `30`
     - **What this does**: Sets max time (seconds) for assessment to run
     - **Why 30s**: Version check is fast, 30s is plenty
   
   - **Fail Message field**: Paste this text:
     ```
     Virtual environment and Rasa Pro installation verification failed.
     
     You need to complete Lab 0.1 first! Follow these steps:
     
     1. Open a terminal in Codio (Tools → Terminal)
     2. Create a virtual environment: python3.11 -m venv .venv
     3. Activate the virtual environment: source .venv/bin/activate
        (Your prompt should show (.venv) at the beginning)
     4. Install Rasa Pro: pip install --no-cache-dir rasa-pro
        (This will take 2-5 minutes - wait for "Successfully installed" message)
     5. Verify installation: rasa --version
        (Should show "Rasa 3.x.x")
     
     If you see errors:
     - Make sure Python 3.11 is available: python3.11 -V
     - Check your internet connection
     - Make sure virtual environment is activated (check for (.venv) in prompt)
     - Try upgrading pip first: pip install --upgrade pip
     - Then retry the installation command
     
     Once both virtual environment creation and Rasa Pro installation are complete, run this assessment again to verify.
     ```
     - **What this does**: Shows helpful message if assessment fails
     - **Why detailed**: Helps students troubleshoot without asking for help
   
   **b. Code Editor Box** (optional):
   - **You can leave this empty** - Standard Code Test uses the Command field from settings
   - **OR** type the command here: `bash -c 'cd /home/codio/workspace/level1 && source .venv/bin/activate && rasa --version'`
   - **Note**: Settings panel takes precedence, so command field in settings is what matters

4. **Save the assessment**:
   - **Click Save button** (usually top right of settings panel, or "Save" button in Guide editor)
   - **Expected Result**: Settings panel closes (if it was open), assessment is saved
   - **Visual confirmation**: No error messages, assessment code box remains visible
   
   **✅ Checkpoint**: Assessment is configured with all fields filled in and saved.

5. **Test the assessment**:
   - **Save the Guide**: Click "Save" or "Done" button (top right of Guide editor) to save the entire Guide
   - **Enter Preview mode**: Click **Preview** button (eye icon 👁️) in Guide editor, OR click "Preview" tab
   - **Expected Result**: Guide displays as students will see it (read-only view)
   - **Navigate to Unit 0**: Scroll to find Unit 0 section
   - **Find assessment**: Look for "Check my work" or "Run Assessment" button (usually at bottom of Unit 0)
   - **Click "Run Assessment"**: Assessment executes
   - **Expected Result**: 
     - **If virtual environment and Rasa Pro are set up**: Shows ✅ PASS or "Success" message, displays Rasa version output
     - **If virtual environment or Rasa Pro not set up**: Shows ❌ FAIL with your fail message
   - **If it fails**: 
     - Read the fail message
     - Go back to Lab 0.1 and ensure virtual environment is created and Rasa Pro is installed
     - Test manually: Run `source .venv/bin/activate && rasa --version` in terminal to verify
     - Test assessment again
   
   **✅ Checkpoint**: Assessment runs successfully and shows appropriate pass/fail result.

**Expected output when passing**:
```
Rasa 3.8.0
```
(Or similar version number - any output containing "Rasa 3." will pass)

**🔍 What This Means**: The assessment verified that students successfully created a virtual environment and installed Rasa Pro in it. Students who see a pass have completed both steps and are ready to proceed with the next exercises. Students who fail need to complete the virtual environment creation and installation steps first (as described in Lab 0.1).

**💡 Optional: Add Additional Checks** (if you want more thorough verification):

You can add **additional Standard Code Tests** for other checks:

- **Check 2: .env file exists**
  - Command: `test -f /home/codio/workspace/level1/.env`
  - Expected Output: (leave empty - command returns 0 if file exists)
  - Points: 5

- **Check 3: Project structure exists**
  - Command: `test -d /home/codio/workspace/level1/domain && test -f /home/codio/workspace/level1/domain/basics.yml`
  - Expected Output: (leave empty)
  - Points: 5

**Note**: These are optional. The Rasa version check (Check 1) is the most critical and sufficient for Unit 0.

**Troubleshooting** (if assessment doesn't work as expected):

- **Problem**: Assessment fails with "Command not found"
  - **What You'll See**: Error like `python3.11: command not found`
  - **Fix**: 
    1. Verify Python 3.11 is installed: Run `python3.11 -V` in terminal
    2. If not installed, install it or use correct Python path
    3. Update Command field to use correct Python path
  - **Verify**: Run the command manually in terminal first

- **Problem**: Assessment passes but virtual environment or Rasa Pro isn't actually set up
  - **What You'll See**: Assessment shows pass but `source .venv/bin/activate && rasa --version` fails in terminal
  - **Fix**: 
    1. Check Expected Output field - might be too lenient
    2. Make Expected Output more specific: `Rasa 3.` (with period)
    3. Verify virtual environment exists: `test -d .venv` should pass
    4. Test again

- **Problem**: Assessment times out
  - **What You'll See**: Assessment runs but stops with "Timeout" message
  - **Fix**: 
    1. This shouldn't happen for version check (it's instant)
    2. If it does, increase timeout to 60s
    3. Check if Python/Rasa installation is hanging

- **Problem**: Assessment doesn't appear in preview
  - **What You'll See**: Created assessment but can't see "Run Assessment" button
  - **Fix**: 
    1. Ensure you saved the Guide (click Save button)
    2. Refresh preview (close and reopen)
    3. Verify you're in correct unit section
    4. Check assessment is visible in edit mode

- **Problem**: Settings panel fields are different than described
  - **What You'll See**: Field names don't match (e.g., "Command" vs "Test Command")
  - **Fix**: 
    1. Codio UI may vary - look for similar field names
    2. "Command" might be "Test Command" or "Execute"
    3. "Expected Output" might be "Expected Result" or "Match Pattern"
    4. Use Codio's help/documentation if needed

### Step 3: Configure Virtual Coach for Unit 0

**⏱️ Estimated Time**: 15-20 minutes

**💡 Time-Saving Tip**: Copy these Virtual Coach settings - you'll reuse similar patterns for other units. Save as a template!

**What you're doing**: Setting up AI hints so students get help when they're stuck.

**How to do it**:

1. **Enable Virtual Coach**:
   - In Codio, click **Education** → **Settings** → **Features**
   - Find **Virtual Coach** toggle and turn it **ON**
   - Click **Save**

2. **Configure Coach modes** (for Unit 0 specifically):
   - Still in **Education** → **Settings**, click **Virtual Coach** tab
   - Under **Summarize Prompt**, paste:
     ```
     Unit 0 Setup Checklist:
     1. Create virtual environment: python3.11 -m venv .venv
     2. Activate virtual environment: source .venv/bin/activate (prompt should show (.venv))
     3. Install Rasa Pro in virtual environment: pip install --no-cache-dir rasa-pro
     4. Verify Python 3.11 is installed (run: python3.11 -V)
     5. Verify Rasa Pro installation (run: rasa --version, with venv activated)
     6. Create .env file from .env.template
     7. Add your RASA_LICENSE and OPENAI_API_KEY to .env
     8. Verify project files exist (domain/, data/ folders)
     ```
   - Under **Error Augmentation**, add these mappings:
     ```
     Error: "command not found: python" → "Use 'python3.11' instead of 'python' in Codio"
     Error: "No module named rasa" → "Make sure virtual environment is activated (source .venv/bin/activate), then install Rasa Pro: pip install --no-cache-dir rasa-pro"
     Error: ".venv/bin/activate: No such file" → "Create virtual environment first: python3.11 -m venv .venv"
     Error: ".env file not found" → "Create .env by copying .env.template and adding your keys"
     ```
   - Under **Next Steps**, paste:
     ```
     If setup fails:
     1. Check that you're in /home/codio/workspace directory
     2. Verify Python 3.11: python3.11 -V
     3. Create virtual environment: python3.11 -m venv .venv
     4. Activate virtual environment: source .venv/bin/activate (check for (.venv) in prompt)
     5. Install Rasa Pro: pip install --no-cache-dir rasa-pro
     6. Verify installation: rasa --version (with venv activated)
     7. Create .env file with your license keys
     ```
   - Click **Save**

3. **Test Coach**:
   - Open student preview (click **Preview** in Guide editor)
   - In the bottom-right corner, click the **chatbot icon** (Virtual Coach)
   - Type: "How do I verify Rasa is installed?"
   - Verify Coach responds with helpful guidance

**Deliverables Checklist** (verify each item before moving to next unit):

- [ ] **Codio workspace configured**
  - ✅ Project created (`BankingBot-Level1`)
  - ✅ Ubuntu 22.04 stack selected
  - ✅ Project files imported (visible in file tree)
  
- [ ] **Python 3.11 verified** (Virtual environment and Rasa Pro will be created/installed by students in Lab 0.1)
  - ✅ `python3.11 -V` shows version
  - ✅ Sandboxed terminal is enabled (students can create virtual environments)
  - ✅ Students will create `.venv` and install Rasa Pro themselves
  
- [ ] **`.env.template` file created**
  - ✅ File exists in `level1/` folder
  - ✅ Contains `RASA_LICENSE=` and `OPENAI_API_KEY=` lines
  
- [ ] **Lab 0.1 Code Test assessment created**
  - ✅ Assessment appears in Guide editor (Unit 0 section)
  - ✅ Command configured: `bash -c 'cd /home/codio/workspace/level1 && source .venv/bin/activate && rasa --version'`
  - ✅ Settings configured (10 points, 30s timeout, working directory: /home/codio/workspace/level1 if field exists)
  - ✅ Fail message includes virtual environment creation instructions
  - ✅ Assessment saved
  
- [ ] **Lab 0.1 tested successfully**
  - ✅ Assessment appears in preview mode
  - ✅ "Run Assessment" button works
  - ✅ Assessment runs without errors
  - ✅ Shows ✅ PASS when virtual environment exists and Rasa Pro is installed
  - ✅ Shows ❌ FAIL with helpful message when virtual environment or Rasa Pro is missing
  
- [ ] **Virtual Coach configured**
  - ✅ Virtual Coach enabled in Features
  - ✅ Unit 0 context added to Summarize Prompt
  - ✅ Error augmentation configured
  - ✅ Tested in preview (ask Coach a question)

**🎯 Unit 0 = First Checkpoint**: If all checkboxes above are checked, your foundation is solid. Students can create venvs and install Rasa Pro; Lab 0.1 passes; Virtual Coach works. **You're ready for Day 1 (Units 1–2).**

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

### 1.4 Test Your Knowledge

**Objective**: Assess your understanding of conversational bots and Level 1 bot capabilities.

This section contains multiple choice questions to test your knowledge of:
- What conversational bots are and how they work
- Natural Language Understanding (NLU)
- Level 1 bot capabilities and limitations
- Real-world use cases for simple bots

---

## For Codio Team: Unit 1 Implementation Notes

**Type**: Guided Reading + Concept Check (Auto-graded)

**📋 IMPORTANT: Add Guide Content First**

**Before creating assessments**, add the student-facing content to Codio's Guide Editor:
- **Add Main Unit Content**: Copy content from `## For Students` (line 2132) to before `## For Codio Team` (line 2245). See "Adding Guide Content to Codio" section above.
- **⏱️ Estimated Time**: 10-15 minutes

**⏱️ Total Estimated Time**: 30-45 minutes

**💡 Time-Saving Tip**: Create all 3 questions in one session. Use Template 3 from Assessment Templates Library for consistent formatting.

**🤖 Codio AI Tip**: Add first Multiple Choice, ensure guide content above explains the topic, click **Generate** → **Generate Using AI**—review and apply. For questions 2 and 3, click **Duplicate and Save** on the first, then edit question text and options. Saves 5-15 minutes.

**Content Strategy**:
- Preserve all conceptual content from TUTORIAL.md
- Use concise explanations but maintain clarity
- Include examples and analogies

### Step 1: Create Concept Check Assessment (Multiple Choice + True/False)

**⏱️ Estimated Time**: 20-25 minutes

**💡 Time-Saving Tip**: Copy question format from Template 3. All questions use same settings (2 points, show explanations, 3 attempts).

**What you're doing**: Creating a quiz to verify students understand bot fundamentals before moving to hands-on work.

**How to do it**:

1. **Navigate to Unit 1 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Unit 1 – Introduction to Rasa Bots** section
   - Scroll to the bottom

2. **Add Multiple Choice assessment**:
   - Click **+** → Select **Multiple Choice** (or **Quiz**)

3. **Add Question 1** (Multiple Choice):
   - **Question text**: `What is a conversational bot?`
   - **Points**: `2`
   - **Answer options**:
     - `A computer program that follows strict rules` (uncheck "Correct")
     - `A program that can have natural, human-like conversations` (check "Correct" ✓)
     - `A database query system` (uncheck)
     - `A web application` (uncheck)
   - **Explanation**: `A conversational bot uses natural language processing to have human-like conversations, understanding what users mean even when phrased differently.`

4. **Add Question 2** (True/False):
   - Click **Add Question** button
   - **Question text**: `Level 1 Rasa bots can remember information from earlier in the conversation.`
   - **Question type**: Select **True/False**
   - **Points**: `1`
   - **Correct answer**: Select **False**
   - **Explanation**: `Level 1 bots use only predefined responses. Memory (slots) is added in Level 3.`

5. **Add Question 3** (Multiple Choice):
   - Click **Add Question** again
   - **Question text**: `What makes Level 1 bots different from advanced bots?`
   - **Points**: `2`
   - **Answer options**:
     - `Level 1 bots use AI, advanced bots don't` (uncheck)
     - `Level 1 bots only use predefined responses, advanced bots can execute custom code` (check "Correct" ✓)
     - `Level 1 bots are faster` (uncheck)
     - `There is no difference` (uncheck)
   - **Explanation**: `Level 1 bots use static responses. Advanced bots (Level 2+) can execute custom Python code (actions) and remember information (slots).`

6. **Configure assessment settings**:
   - **Total Points**: `5`
   - **Passing Score**: `3` (60% - allows one wrong answer)
   - **Show explanations after submission**: ✓
   - **Allow multiple attempts**: ✓ (max 3 attempts)
   - **Randomize question order**: Optional (uncheck for consistency)
   - Click **Save**

7. **Test the assessment**:
   - Click **Preview**
   - Navigate to Unit 1
   - Answer all questions (try both correct and incorrect answers)
   - Verify score calculation (should show "X/5 points")
   - Check explanations appear after submission

**Expected output**:
- Student sees 3 questions (2 multiple choice, 1 true/false)
- After submitting, sees score and explanations
- Can retake if enabled

**Troubleshooting**:
- **True/False question not showing**: Ensure question type is set to "True/False" (not multiple choice with 2 options)
- **Score incorrect**: Verify correct answers are marked with ✓ checkboxes
- **Explanations missing**: Check "Show explanations" is enabled in settings

### Step 2: Configure Virtual Coach for Unit 1

**What you're doing**: Adding conceptual hints for students learning bot fundamentals.

**How to do it**:

1. **Open Virtual Coach settings**:
   - Click **Education** → **Settings** → **Virtual Coach**

2. **Add Unit 1 context** (append to existing settings):
   - Under **Summarize Prompt**, add:
     ```
     Unit 1 Key Concepts:
     - Conversational bots understand natural language (NLU)
     - Bots can have human-like conversations
     - Rasa bots use LLMs to understand user intent
     - Level 1 bots use responses (predefined messages)
     - Level 1 bots cannot remember or execute custom code
     ```
   - Under **Error Augmentation**, add:
     ```
     Confusion about "bot vs program" → "Bots understand natural language. Regular programs need exact commands."
     Confusion about "what Level 1 can do" → "Level 1 bots provide predefined information only. No memory or custom code yet."
     ```
   - Under **Next Steps**, add:
     ```
     After Unit 1, you should understand:
     1. What makes a bot different from a regular program
     2. How bots understand natural language (NLU)
     3. What responses are (we'll create them in Unit 2)
     4. What Level 1 bots can and cannot do
     ```

3. **Save and test**: Click **Save**, then test in preview mode by asking Coach: "What can Level 1 bots do?"

**Deliverables Checklist**:
- [ ] Multiple Choice assessment created with 3 questions (2 MC, 1 T/F)
- [ ] All correct answers marked
- [ ] Explanations added for each question
- [ ] Assessment tested in preview mode
- [ ] Virtual Coach configured with Unit 1 concepts
- [ ] Coach tested with sample questions

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

**📋 IMPORTANT: Add Guide Content First**

**Before creating assessments**, add the student-facing content to Codio's Guide Editor:
- **Add Main Unit Content**: Copy content from `## For Students` (line 2379) to before `### Lab 2.1` (line 2464). See "Adding Guide Content to Codio" section above.
- **Add Lab Content**: Use Step 0.5 sections for Labs 2.1, 2.2, 2.3 (see below).
- **⏱️ Estimated Time**: 30-40 minutes (main content + 3 labs)

**⏱️ Total Estimated Time**: 2-3 hours

**💡 Time-Saving Tip**: Lab 2.2 grader is the most complex. Use Template 4 (Response Validation) as starting point, then expand. Lab 2.3 can copy Lab 2.2 and modify.

### Lab 2.1: Understanding YAML Syntax

**⏱️ Estimated Time**: 30-40 minutes

**Content Structure**:
- Brief YAML Primer (integrated into Unit 0.3)
- Interactive exploration of existing responses

#### Step 0.5: Add Lab 2.1 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 2.1 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 2.1 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 2 content to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**:
   - In Codio, click **Tools** → **Guides** → **Edit**
   - **Expected Result**: Guide editor opens, showing all unit sections

2. **Find or Create Unit 2 Section**:
   - **If Unit 2 doesn't exist**: Create a new section named **Unit 2: Understanding the Domain File**
   - **If Unit 2 already exists**: Click on it in the left sidebar to select it
   - **Expected Result**: Unit 2 section is selected and visible in the main editing area

3. **Add Lab 2.1 Subsection**:
   - **Scroll down** in Unit 2's content area (or click at the end of existing content)
   - **Click** in the content editing area where you want Lab 2.1 to appear
   - **Expected Result**: Cursor is positioned where you'll paste the content

4. **Copy and Paste the Markdown Content**:
   - **Select ALL the text** in the code block below (from `### Lab 2.1` to the `---` line)
   - **Copy it** (Ctrl+C / Cmd+C)
   - **Paste it** into Codio's Guide Editor at the location you selected (Ctrl+V / Cmd+V)
   - **Expected Result**: The Markdown content appears in the editor

5. **Verify the Content**:
   - **Check formatting**: You should see headings, code blocks, and lists formatted correctly
   - **Save**: Click **Save** button (Ctrl+S / Cmd+S)
   - **Preview**: Click **Preview** button (eye icon 👁️) to see how students will see it
   - **Expected Result**: Content displays nicely formatted with proper headings, code blocks with syntax highlighting, and bulleted lists

**✅ Checkpoint**: Lab 2.1 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 2.1**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 2.1. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If you can't find where to paste**: Look for the end of Unit 2's existing content, or create a new subsection/page for Lab 2.1

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 2.1 Assessment (Code Test for File Analysis)

**💡 Time-Saving Tip**: Use Template 2 (Bash File Checker) for Exercise 1 and 3. Exercise 2 is simple multiple choice - use Template 3.

**What you're doing**: Creating an assessment that checks if students can identify responses in the YAML file.

**How to do it**:

1. **Navigate to Unit 2 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Unit 2 – Understanding the Domain File** section
   - Find subsection **Lab 2.1: Understanding YAML Syntax**
   - Scroll to bottom of that subsection

2. **Add Code Test assessment**:
   - Click **+** → Select **Code Test**

3. **Paste grader script** (Exercise 1: Identify all responses):
   ```bash
   #!/bin/bash
   set -e
   
   cd /home/codio/workspace/level1
   
   # Exercise 1: Check student can identify responses
   echo "Exercise 1: Identifying responses..."
   
   # Expected responses in domain/basics.yml
   expected_responses=("utter_greet" "utter_help" "utter_contact")
   
   # Check if file exists
   if [ ! -f "domain/basics.yml" ]; then
       echo "❌ FAIL: domain/basics.yml not found"
       exit 1
   fi
   
   # Check each expected response exists
   missing=0
   for resp in "${expected_responses[@]}"; do
       if ! grep -q "$resp:" domain/basics.yml; then
           echo "❌ Missing response: $resp"
           missing=$((missing + 1))
       fi
   done
   
   if [ $missing -gt 0 ]; then
       echo "❌ FAIL: Found $missing missing responses. Expected: ${expected_responses[*]}"
       exit 1
   fi
   
   echo "✅ Exercise 1 PASS: All responses identified"
   echo "Found responses: ${expected_responses[*]}"
   ```

4. **Configure assessment**:
   - **Points**: `3`
   - **Timeout**: `30` seconds
   - **Fail Message**: `Review domain/basics.yml and identify all responses that start with "utter_". Make sure you can see utter_greet, utter_help, and utter_contact.`
   - Click **Save**

5. **Add Exercise 2** (Multiple Choice about metadata):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `What does "rephrase: True" in the metadata do?`
   - **Points**: `2`
   - **Options**:
     - `It allows the LLM to rephrase the response text` (check "Correct" ✓)
     - `It makes the response mandatory` (uncheck)
     - `It hides the response` (uncheck)
     - `It speeds up the bot` (uncheck)
   - **Explanation**: `rephrase: True tells Rasa to let the LLM rephrase the response text while keeping the same meaning, making conversations more natural.`
   - Click **Save**

6. **Add Exercise 3** (Code Test to count variations):
   - Click **+** → Select **Code Test**
   - Paste this script:
     ```bash
     #!/bin/bash
     set -e
     
     cd /home/codio/workspace/level1
     
     # Exercise 3: Count total response variations
     echo "Exercise 3: Counting response variations..."
     
     # Count total variations (lines starting with "- text:" in responses section)
     variation_count=$(grep -c "^\s*- text:" domain/basics.yml || echo "0")
     
     # Expected: at least 3 variations (one per response minimum)
     if [ "$variation_count" -lt 3 ]; then
         echo "❌ FAIL: Found only $variation_count variations. Expected at least 3."
         echo "Hint: Each response should have at least one '- text:' line"
         exit 1
     fi
     
     echo "✅ Exercise 3 PASS: Found $variation_count response variations"
     ```
   - **Points**: `1`
   - **Timeout**: `20` seconds
   - Click **Save**

7. **Test all exercises**:
   - Click **Preview**
   - Navigate to Lab 2.1
   - Run each exercise
   - Verify all pass

**Deliverables Checklist**:
- [ ] Exercise 1 Code Test created (identify responses)
- [ ] Exercise 2 Multiple Choice created (metadata question)
- [ ] Exercise 3 Code Test created (count variations)
- [ ] All exercises tested in preview mode

### Lab 2.2: Creating Your First Response

**Type**: Hands-On Lab with Auto-Grading (Rubric-based)

**⏱️ Estimated Time**: 1-1.5 hours (most complex assessment in Level 1)

**💡 Time-Saving Tip**: Use Template 4 (Response Validation) as base. The full grader script below is ready to copy-paste - modify only the response name if needed.

**Content Structure**:
- Complete step-by-step instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Add `utter_goodbye` response

#### Step 0.5: Add Lab 2.2 Guide Content to Codio

**⏱️ Estimated Time**: 10-15 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 2.2 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 2.2 student-facing content to Codio's Guide Editor so students can see the detailed step-by-step instructions.

**🔍 Before You Start**: Make sure you've added Unit 2 content and Lab 2.1 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**:
   - In Codio, click **Tools** → **Guides** → **Edit**
   - **Expected Result**: Guide editor opens, showing all unit sections

2. **Find Unit 2 Section**:
   - Click on **Unit 2: Understanding the Domain File** in the left sidebar
   - **Expected Result**: Unit 2 section is selected and visible in the main editing area

3. **Add Lab 2.2 Subsection**:
   - **Scroll down** in Unit 2's content area to find where Lab 2.1 ends
   - **Click** in the content editing area where you want Lab 2.2 to appear (after Lab 2.1)
   - **Expected Result**: Cursor is positioned where you'll paste the content

4. **Copy and Paste the Markdown Content**:
   - **Select ALL the text** in the code block below (from `### Lab 2.2` to the `---` line before Lab 2.3)
   - **Copy it** (Ctrl+C / Cmd+C)
   - **Paste it** into Codio's Guide Editor at the location you selected (Ctrl+V / Cmd+V)
   - **Expected Result**: The Markdown content appears in the editor

5. **Verify the Content**:
   - **Check formatting**: You should see headings, code blocks, lists, and checklists formatted correctly
   - **Save**: Click **Save** button (Ctrl+S / Cmd+S)
   - **Preview**: Click **Preview** button (eye icon 👁️) to see how students will see it
   - **Expected Result**: Content displays nicely formatted with proper headings, code blocks with syntax highlighting, bulleted lists, and checklists

**✅ Checkpoint**: Lab 2.2 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode. This is a longer lab with detailed step-by-step instructions - make sure all sections display properly.

**📋 Copy This Markdown for Lab 2.2**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 2.2. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If the content is very long**: This lab has detailed step-by-step instructions. Make sure you copied the entire block from `### Lab 2.2` to the `---` line before Lab 2.3
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 2.2 Assessment Using LLM Rubric Autograde

**⏱️ Estimated Time**: 10-15 minutes (reduced from 1-1.5 hours using LLM Rubric instead of custom Python script)

**💡 Time-Saving Tip**: Using LLM Rubric Autograde saves 45-75 minutes vs. writing a custom Python script. No coding required - just describe what to check!

**📖 Assessment Type**: **LLM Rubric Autograde** (see "Codio Native Assessment Features Guide" above for details)

**What you're doing**: Creating an LLM Rubric assessment that validates YAML structure, indentation, naming, and metadata for the `utter_goodbye` response using AI-powered grading.

**How to do it**:

1. **Navigate to Lab 2.2 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 2.2: Creating Your First Response** subsection
   - Scroll to bottom
   - **Expected Result**: You see the end of Lab 2.2 content, with `+` button visible

2. **Add LLM Rubric Assessment**:
   - Click **`+`** button
   - **Expected Result**: Dropdown menu appears with assessment type options
   - Look for **"LLM Rubric"**, **"Autograde"**, **"AI Grader"**, or **"Rubric Grader"** option
   - **If you don't see it**: Check Codio documentation or look for AI/LLM options in dropdown
   - Select **"LLM Rubric"** or **"Autograde"**
   - **Expected Result**: Form appears with multiple fields (instructions, rubric, files, etc.)

3. **Configure the Assessment** (Fill in all fields):

   **a. Assessment Instructions** (What student should do):
   - **Field Name**: "Instructions" or "Task Description"
   - **What to type** (copy exactly):
     ```
     Add a new response called "utter_goodbye" to the domain/basics.yml file. 
     
     The response should:
     - Be added under the responses: section
     - Have at least one text variation with a farewell message
     - Include metadata with rephrase: True
     - Use proper YAML syntax with correct indentation (2 spaces per level)
     ```
   - **Purpose**: Tells LLM what the student should accomplish

   **b. Rubric/Requirements** (What to check - be very specific):
   - **Field Name**: "Rubric", "Requirements", or "Grading Criteria"
   - **What to type** (copy exactly - this is critical for accurate grading):
     ```
     Requirements Checklist (all must be met):
     
     1. File Location and Existence:
        - File domain/basics.yml exists in /home/codio/workspace/level1/
        - File is valid YAML (no syntax errors, parses correctly)
     
     2. Response Structure:
        - Response "utter_goodbye" exists under the responses: section
        - Response is a list (starts with "- text:")
        - Response has at least one text variation (non-empty text)
        - Response text contains a farewell message (e.g., "Goodbye", "See you", etc.)
     
     3. YAML Syntax and Indentation:
        - Uses exactly 2 spaces for indentation (not tabs, not 4 spaces)
        - utter_goodbye: is indented 2 spaces from left margin
        - - text: is indented 4 spaces from left margin (2 spaces under utter_goodbye:)
        - metadata: is aligned with text: (6 spaces from left margin)
        - rephrase: True is indented 8 spaces from left margin (2 spaces under metadata:)
        - No tabs used anywhere in the response definition
     
     4. Metadata:
        - metadata: section exists in the response
        - metadata contains rephrase: True (exact value, boolean True, not string "True")
        - metadata is properly indented (aligned with text:)
     
     5. Response Content:
        - Response text is not empty
        - Response text is a meaningful farewell message
     
     Grading: Award full points (10) if all requirements are met. Deduct points for each missing requirement.
     ```
   - **Why detailed**: LLM needs specific criteria to grade accurately
   - **Note**: Be explicit about indentation (2 spaces) - this is the most common error

   **c. Solution File** (Reference for LLM):
   - **Field Name**: "Solution File" or "Reference File"
   - **What to type**: `/home/codio/workspace/level1/domain/basics.yml`
   - **Purpose**: Helps LLM understand expected YAML structure
   - **Note**: This should be the file with correct structure (can be template or example)

   **d. Files to Check**:
   - **Field Name**: "Files to Grade" or "Student Files"
   - **What to type**: `/home/codio/workspace/level1/domain/basics.yml`
   - **Purpose**: Tells LLM which file(s) to analyze
   - **Note**: This is the file students will modify

   **e. Guide Content Context** (Optional but recommended):
   - **Field Name**: "Guide Content" or "Context"
   - **What to type**: Copy the Lab 2.2 instructions from the guide (the student-facing content)
   - **Example** (copy from Lab 2.2 section):
     ```
     Lab 2.2: Creating Your First Response
     
     Objective: Add a new utter_goodbye response to your bot's domain file.
     
     Steps:
     1. Navigate to domain/basics.yml
     2. Find the responses: section
     3. Add utter_goodbye: (with colon)
     4. Add - text: "your message" (indented 2 spaces)
     5. Add metadata: section aligned with text:
     6. Add rephrase: True under metadata: (indented 2 more spaces)
     
     Example structure:
     utter_goodbye:
       - text: "Goodbye! Have a great day!"
         metadata:
           rephrase: True
     ```
   - **Purpose**: Helps LLM understand learning objectives and expected format

   **f. Points**:
   - **Field Name**: "Points" or "Max Score"
   - **What to type**: `10`
   - **Purpose**: Sets total points for this assessment

   **g. Timeout**:
   - **Field Name**: "Timeout"
   - **What to type**: `60` (seconds)
   - **Purpose**: LLM processing can take 10-30 seconds, so 60s gives buffer
   - **Why 60s**: LLM needs time to analyze YAML structure and check all criteria

4. **Save the Assessment**:
   - Click **Save** button (usually top right of form, or "Save" in Guide editor)
   - **Expected Result**: Form closes, assessment is saved
   - **Visual confirmation**: Assessment appears in guide editor, no error messages

5. **Enable Code Playback** (Optional but recommended):
   - Click **Education** → **Monitoring** → **Code Playback**
   - Ensure it's enabled for this assignment
   - Add `domain/basics.yml` to tracked files
   - **Purpose**: Allows instructors to review how students created the response

6. **Test the Assessment**:
   - **Save the Guide**: Click "Save" or "Done" button in Guide editor
   - **Enter Preview mode**: Click **Preview** button (eye icon 👁️)
   - **Navigate to Lab 2.2**: Scroll to find Lab 2.2 section
   - **Find assessment**: Look for "Check my work" or "Run Assessment" button
   - **Test Scenario 1 - Before student work** (should fail):
     - Ensure `utter_goodbye` doesn't exist in domain/basics.yml
     - Click "Run Assessment"
     - **Expected Result**: Assessment fails with feedback about missing response
   - **Test Scenario 2 - Correct student work** (should pass):
     - Add `utter_goodbye` response correctly (see example in guide)
     - Click "Run Assessment"
     - **Expected Result**: Assessment passes, shows feedback confirming all requirements met
   - **Test Scenario 3 - Intentional errors** (should catch errors):
     - Test with wrong indentation (tabs or 4 spaces)
     - Test with missing metadata
     - Test with empty text
     - **Expected Result**: Assessment fails with specific feedback about what's wrong
   - **If assessment doesn't work as expected**: Refine rubric to be more specific, test again

**Expected output when passing**:
```
✅ Assessment Passed

Feedback:
- ✓ File domain/basics.yml exists and is valid YAML
- ✓ Response "utter_goodbye" exists under responses: section
- ✓ Response has proper structure with text variation
- ✓ Correct indentation (2 spaces per level)
- ✓ Metadata section present with rephrase: True
- ✓ Response text is non-empty and meaningful

Score: 10/10
```

**🔍 What This Means**: The LLM analyzed the student's YAML file and verified all requirements. Students who see a pass have correctly created the response.

**Troubleshooting**:

- **Problem**: Assessment passes when it shouldn't (too lenient)
  - **What You'll See**: LLM passes incorrect work
  - **Fix**: 
    1. Make rubric more specific (add exact indentation requirements)
    2. Add examples of what NOT to accept in rubric
    3. Test with incorrect work and refine rubric based on results
  - **Example**: If it passes with tabs, add "No tabs allowed, only spaces" to rubric

- **Problem**: Assessment fails when it shouldn't (too strict)
  - **What You'll See**: LLM fails correct work
  - **Fix**: 
    1. Check rubric for overly strict requirements
    2. Provide solution file with correct example
    3. Add guide content context to help LLM understand expected format
  - **Example**: If it fails on valid YAML, check if solution file is correct

- **Problem**: Feedback is vague or unhelpful
  - **What You'll See**: Generic error messages
  - **Fix**: 
    1. Add specific error messages to rubric (e.g., "If indentation wrong, say: 'Use exactly 2 spaces, not tabs'")
    2. Include examples in guide content context
    3. Test and refine based on actual feedback

- **Problem**: Assessment times out
  - **What You'll See**: Assessment runs but stops with timeout
  - **Fix**: 
    1. Increase timeout to 90 seconds
    2. Simplify rubric (remove unnecessary checks)
    3. Check if file path is correct

- **Problem**: LLM Rubric option not available
  - **What You'll See**: Don't see "LLM Rubric" in assessment type dropdown
  - **Fix**: 
    1. Check Codio documentation for latest feature name
    2. Look for "AI Grader", "Autograde", or "Rubric Grader"
    3. Verify your Codio plan includes LLM features
    4. Contact Codio support if feature not available

**💡 Pro Tips**:
- **Start specific**: List exact requirements (file paths, key names, indentation)
- **Include examples**: Reference solution file or provide example in rubric
- **Test iteratively**: Run assessment, refine rubric based on results, test again
- **Use guide content**: Copy relevant guide sections to help LLM understand context
- **Be explicit about indentation**: This is the #1 student error - spell it out clearly

#### Step 2: Configure Virtual Coach for Lab 2.2

**What you're doing**: Adding specific hints for response creation errors.

**How to do it**:

1. **Open Virtual Coach settings**:
   - Click **Education** → **Settings** → **Virtual Coach**

2. **Add Lab 2.2 specific hints**:
   - Under **Summarize Prompt**, add:
     ```
     Lab 2.2 Checklist:
     1. Open domain/basics.yml
     2. Find the responses: section
     3. Add utter_goodbye: (with colon)
     4. Indent with 2 spaces: - text: "your message"
     5. Add metadata: section aligned with text:
     6. Add rephrase: True under metadata: (indented 2 more spaces)
     ```
   - Under **Error Augmentation**, add:
     ```
     YAMLError → "Check YAML syntax: missing colons, wrong indentation, or missing dashes. Use exactly 2 spaces per indent level."
     IndentationError → "Use exactly 2 spaces for indentation (not tabs, not 4 spaces). Enable 'show whitespace' in your editor to see spaces vs tabs."
     Missing metadata → "Every response needs metadata: with rephrase: True. Align metadata: with text:, then indent rephrase: True 2 more spaces."
     ```
   - Under **Next Steps**, add:
     ```
     If grader fails:
     1. Check indentation: utter_goodbye: (2 spaces), - text: (4 spaces), metadata: (6 spaces), rephrase: (8 spaces)
     2. Verify you're editing domain/basics.yml (not a different file)
     3. Ensure response text is not empty
     4. Make sure metadata: rephrase: True is included
     ```

3. **Save and test**: Click **Save**, then test in preview by asking Coach about indentation

**Deliverables Checklist**:
- [ ] Lab 2.2 Code Test created with Python grader script
- [ ] All rubric criteria validated (YAML, indentation, naming, metadata, structure)
- [ ] Code Playback enabled for domain/basics.yml
- [ ] Virtual Coach configured with Lab 2.2 hints
- [ ] Assessment tested with correct and incorrect student work

### Lab 2.3: Response Variations

**Type**: Hands-On Lab with Auto-Grading

**⏱️ Estimated Time**: 45 minutes

**💡 Time-Saving Tip**: Copy Lab 2.2 grader and modify - it's very similar. Change validation to check for 2+ variations instead of single response.

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Add multiple variations to `utter_goodbye`

#### Step 0.5: Add Lab 2.3 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 2.3 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 2.3 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 2 content, Lab 2.1, and Lab 2.2 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**:
   - In Codio, click **Tools** → **Guides** → **Edit**
   - **Expected Result**: Guide editor opens, showing all unit sections

2. **Find Unit 2 Section**:
   - Click on **Unit 2: Understanding the Domain File** in the left sidebar
   - **Expected Result**: Unit 2 section is selected and visible in the main editing area

3. **Add Lab 2.3 Subsection**:
   - **Scroll down** in Unit 2's content area to find where Lab 2.2 ends
   - **Click** in the content editing area where you want Lab 2.3 to appear (after Lab 2.2)
   - **Expected Result**: Cursor is positioned where you'll paste the content

4. **Copy and Paste the Markdown Content**:
   - **Select ALL the text** in the code block below (from `### Lab 2.3` to the end)
   - **Copy it** (Ctrl+C / Cmd+C)
   - **Paste it** into Codio's Guide Editor at the location you selected (Ctrl+V / Cmd+V)
   - **Expected Result**: The Markdown content appears in the editor

5. **Verify the Content**:
   - **Check formatting**: You should see headings, code blocks, and checklists formatted correctly
   - **Save**: Click **Save** button (Ctrl+S / Cmd+S)
   - **Preview**: Click **Preview** button (eye icon 👁️) to see how students will see it
   - **Expected Result**: Content displays nicely formatted with proper headings, code blocks with syntax highlighting, and checklists

**✅ Checkpoint**: Lab 2.3 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 2.3**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 2.3. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 2.3 Assessment Using LLM Rubric Autograde

**⏱️ Estimated Time**: 10-15 minutes (reduced from 30-40 minutes using LLM Rubric instead of custom Python script)

**💡 Time-Saving Tip**: Use LLM Rubric Autograde—no coding required! Duplicate Lab 2.2's LLM Rubric assessment, then edit the rubric to check for 2+ variations instead of single response.

**📖 Assessment Type**: **LLM Rubric Autograde** (see "Codio Native Assessment Features Guide" above)

**What you're doing**: Creating an LLM Rubric assessment that validates students added at least 2 variations to `utter_goodbye`, all properly structured, with no duplicate text.

**How to do it**:

1. **Navigate to Lab 2.3 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 2.3: Add Response Variations** subsection
   - Scroll to bottom

2. **Add LLM Rubric Assessment** (or Duplicate Lab 2.2's assessment and edit):
   - Click **`+`** button
   - Select **"LLM Rubric"** or **"Autograde"** (or Duplicate Lab 2.2's LLM Rubric, then modify)

3. **Configure the Assessment**:

   **a. Assessment Instructions**:
   - **What to type**:
     ```
     Add a second variation to the utter_goodbye response in domain/basics.yml.
     
     The response should:
     - Have at least 2 text variations (two '- text:' items with different farewell messages)
     - Include metadata with rephrase: True (can be on the last variation)
     - Use proper YAML syntax (2 spaces indentation)
     - Each variation must have different text (no duplicates)
     ```

   **b. Rubric/Requirements**:
   - **What to type**:
     ```
     Requirements Checklist (all must be met):
     
     1. File Location and Existence:
        - File domain/basics.yml exists and is valid YAML
     
     2. Response Structure:
        - Response "utter_goodbye" exists under responses: section
        - Response is a list with at least 2 items (2 or more '- text:' variations)
        - Each variation has a 'text' field with non-empty content
        - Variation texts are different (no duplicate text)
     
     3. YAML Syntax:
        - Uses exactly 2 spaces for indentation (not tabs)
        - Proper structure: utter_goodbye: (2 spaces), - text: (4 spaces), metadata: (6 spaces), rephrase: True (8 spaces)
     
     4. Metadata:
        - At least one variation includes metadata with rephrase: True
        - metadata is properly indented (aligned with text:)
     
     5. Variation Content:
        - All variation texts are non-empty
        - All variation texts are unique (different farewell messages)
        - No duplicate text across variations
     
     Grading: Award full points (8) if all requirements are met.
     ```

   **c. Solution File**: `/home/codio/workspace/level1/domain/basics.yml`

   **d. Files to Check**: `/home/codio/workspace/level1/domain/basics.yml`

   **e. Points**: `8`

   **f. Timeout**: `60` (seconds)

4. **🤖 Use Generate Rubrics First** (if available): Click **Generate Rubrics** → **Generate Using AI**, then refine the rubric to add the "at least 2 variations" and "no duplicates" requirements.

5. **Test the assessment**:
   - Test with 1 variation (should fail)
   - Test with 2 identical variations (should fail on duplicates)
   - Test with 2 different variations + metadata (should pass)

**Expected output when passing**:
```
✅ PASS: All checks passed! Score: 8/8
✓ Found 2 variations
✓ All variations properly structured
✓ Metadata with rephrase: True present
✓ All variations have unique text
```

**Troubleshooting**:
- **"Only 1 variation"**: Student didn't add second `- text:` item. Show example structure.
- **"Duplicate variations"**: Both variations have same text. Remind students to use different phrases.
- **"Missing metadata"**: Student removed metadata or didn't add it. Show where it should go.

#### Step 2: Update Virtual Coach for Lab 2.3

**What you're doing**: Adding hints specific to creating multiple variations.

**How to do it**:

1. **Open Virtual Coach settings**:
   - Click **Education** → **Settings** → **Virtual Coach**

2. **Add Lab 2.3 hints**:
   - Under **Summarize Prompt**, add:
     ```
     Lab 2.3 Steps:
     1. Find utter_goodbye in domain/basics.yml
     2. Add a second '- text:' item at the same indentation as the first
     3. Use different text (e.g., "See you later!" instead of "Goodbye!")
     4. Keep metadata: rephrase: True (can be on the last variation)
     ```
   - Under **Error Augmentation**, add:
     ```
     "only 1 variation" → "Add a second '- text:' item with different text. Both should be at the same indentation level (4 spaces)."
     "duplicate variations" → "Each variation must have different text. Try: 'Goodbye!', 'See you later!', 'Take care!'"
     "missing metadata" → "Keep the metadata: section with rephrase: True. It can be on the last variation."
     ```

3. **Save and test**: Click **Save**, test in preview

**Deliverables Checklist**:
- [ ] Lab 2.3 LLM Rubric Autograde created (or duplicated from Lab 2.2 and modified)
- [ ] Checks for at least 2 variations, structure, metadata, and uniqueness
- [ ] Assessment tested with various student submissions
- [ ] Virtual Coach updated with Lab 2.3 hints

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

### 3.3 Flow Descriptions and LLM Understanding

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

**Objective**: Create new flows with good descriptions that help the LLM match user messages.

**Before You Begin**:
- ✅ You've completed Lab 3.2 (created goodbye.yml)
- ✅ You understand flow structure (flows:, name:, description:, steps:)
- ✅ You know where `data/basics/` folder is located
- ✅ You can reference existing flows (greet.yml, goodbye.yml) as templates

#### Understanding Flow Descriptions

The `description` field is **critical** because the LLM uses it to match user messages to flows.

**How It Works**:
1. User sends a message: "What are your hours?"
2. LLM reads all flow descriptions
3. LLM matches the message to the best-fitting description
4. Rasa triggers that flow

**Writing Good Descriptions**:

✅ **Good descriptions**:
- Clear and specific: "Tell the user when the bank is open and what the operating hours are"
- Action-oriented: "Provide contact information for the bank"
- Context-aware: "Explain what the bot can help with"

❌ **Bad descriptions**:
- Too vague: "Help user" (what kind of help?)
- Too specific: "Respond when user says exactly 'hello'" (misses "hi", "hey")
- Missing context: "Say hello" (when? why?)

#### Task: Create 2 New Flows

Create 2 new flow files in `data/basics/` folder. Use `greet.yml` or `goodbye.yml` as templates for structure.

**Flow 1: Bank Hours**
- **File**: `data/basics/hours.yml`
- **Flow name**: `hours`
- **Description**: Write a clear, specific description about providing bank hours
- **Steps**: At least one action (e.g., `utter_hours` - you may need to create this response in domain/basics.yml first, or use an existing response)

**Flow 2: Account Balance Help**
- **File**: `data/basics/balance.yml`
- **Flow name**: `balance`
- **Description**: Write a clear, specific description about explaining how to check account balance
- **Steps**: At least one action (e.g., `utter_balance_help` or use an existing response)

#### Step-by-Step Instructions

1. **Create hours.yml**:
   - Copy the structure from `greet.yml` or `goodbye.yml` as a template
   - Change the flow name to `hours`
   - Write a good description (see examples below)
   - Add at least one step with an action

2. **Create balance.yml**:
   - Copy the structure from `greet.yml` or `goodbye.yml` as a template
   - Change the flow name to `balance`
   - Write a good description (see examples below)
   - Add at least one step with an action

#### Example: Good Descriptions

Here are examples of good flow descriptions for **different** flows (not the ones you're creating):

**Example 1: Contact Information Flow**:
```yaml
flows:
  contact:
    name: contact info
    description: "Provide contact information for the bank, including phone numbers and email addresses"
    steps:
      - action: utter_contact
```

**Example 2: Services Flow**:
```yaml
flows:
  services:
    name: available services
    description: "List all the services and features the bot can help with, including account management and support options"
    steps:
      - action: utter_help
```

**Key**: Be specific about what the flow does, not how the user asks for it. Notice how these descriptions:
- Use action verbs ("Provide", "List")
- Are specific about what information is given
- Include context about what the flow accomplishes
- Are at least 20 characters long

**Your Task**: Create similar descriptions for `hours.yml` and `balance.yml` following this pattern, but write your own descriptions (don't copy these examples).

#### Checklist

Before submitting, verify:
- ✅ Both files exist in `data/basics/` folder
- ✅ Both flows have `name:` fields
- ✅ Both flows have `description:` fields (at least 20 characters, specific and action-oriented)
- ✅ Both flows have `steps:` sections with at least one action
- ✅ Descriptions are unique (different from each other and from other flows)
- ✅ YAML syntax is correct (2 spaces indentation, no tabs)
- ✅ File structure matches the template (flows: at top level, proper indentation)

**AI Coach**: Ask "How do I write a good flow description?" or "What makes a description too vague?"

---

**Note**: Test Your Knowledge sections from Unit 3 onwards have been removed from the course; do not add a 3.5 Test Your Knowledge page.

---

## For Codio Team: Unit 3 Implementation Notes

**Type**: Guided Lab + Auto-Graded Exercises

**📋 IMPORTANT: Add Guide Content First**

**Before creating assessments**, add the student-facing content to Codio's Guide Editor:
- **Add Main Unit Content**: Copy content from `## For Students` (line 3601) to before `### Lab 3.1` (line 3682). See "Adding Guide Content to Codio" section above.
- **Add Lab Content**: Use Step 0.5 sections for Labs 3.1, 3.2, 3.3, 3.4 (see below).
- **⏱️ Estimated Time**: 35-50 minutes (main content + 4 labs)

**⏱️ Total Estimated Time**: 2-3 hours

**💡 Time-Saving Tip**: Lab 3.2 grader is similar to Lab 2.2 but for flows. Use Template 5 (Flow Validation) as base. Lab 3.1 is quick - use Template 3.

### Lab 3.1: Exploring Existing Flows

**Type**: Exploration Lab with Auto-Grading

**⏱️ Estimated Time**: 20-25 minutes

**💡 Time-Saving Tip**: All 3 exercises are simple multiple choice. Use Template 3. Create all 3 in one session.

**Content Structure**:
- Pre-populated flow files in `data/basics/` folder
- Brief explanation of flow structure (preserved from TUTORIAL.md)

#### Step 0.5: Add Lab 3.1 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 3.1 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 3.1 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 3 content to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 3 Section**: Click on **Unit 3: Understanding Flows** in the left sidebar

3. **Add Lab 3.1 Subsection**: Scroll down in Unit 3's content area and click where you want Lab 3.1 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 3.1 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 3.1**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 3.1. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 3.1 Assessments (Multiple Choice Exercises)

**What you're doing**: Creating three quick concept checks to verify students understand flow structure before they create their own.

**How to do it**:

1. **Navigate to Lab 3.1 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 3.1: Exploring Existing Flows** subsection
   - Scroll to bottom

2. **Add Exercise 1** (Matching flow names to purposes):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `Match the flow name to its purpose:`
   - **Question type**: Select **Matching** (if available) or use **Multiple Choice** with this format:
   - **Points**: `3`
   - **Options** (create as separate questions if matching not available):
     - Question 1a: `What does the "greet" flow do?`
       - `Greets the user when they start a conversation` (check "Correct" ✓)
       - `Provides help information` (uncheck)
       - `Shows contact details` (uncheck)
     - Question 1b: `What does the "help" flow do?`
       - `Explains what the bot can help with` (check "Correct" ✓)
       - `Greets the user` (uncheck)
       - `Provides contact info` (uncheck)
     - Question 1c: `What does the "contact" flow do?`
       - `Provides contact information for the bank` (check "Correct" ✓)
       - `Greets the user` (uncheck)
       - `Shows help menu` (uncheck)
   - **Explanation**: `Each flow has a specific purpose. Review data/basics/*.yml files to see their descriptions.`
   - Click **Save**

3. **Add Exercise 2** (Identify flow components):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `Which of these are required fields in a flow? (Select all that apply)`
   - **Question type**: Select **Multiple Select** (checkboxes) if available, otherwise use regular Multiple Choice
   - **Points**: `3`
   - **Options** (if Multiple Select):
     - `flows:` (top-level key) (check "Correct" ✓)
     - `name:` (human-readable name) (check "Correct" ✓)
     - `description:` (what the flow does) (check "Correct" ✓)
     - `steps:` (actions to execute) (check "Correct" ✓)
     - `version:` (uncheck - this is in domain, not flow)
     - `metadata:` (uncheck - this is in responses, not flows)
   - **Explanation**: `Required flow fields: flows: (top level), name:, description:, and steps:. The description field is critical for LLM matching.`
   - Click **Save**

4. **Add Exercise 3** (Explain description importance):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `Why is the "description:" field critical in flows?`
   - **Points**: `2`
   - **Options**:
     - `The LLM uses it to match user messages to the correct flow` (check "Correct" ✓)
     - `It makes the code run faster` (uncheck)
     - `It's required by YAML syntax` (uncheck)
     - `It's just for documentation` (uncheck)
   - **Explanation**: `The description field tells the LLM what the flow does. Without a good description, the LLM won't know when to trigger your flow.`
   - Click **Save**

5. **Test all exercises**:
   - Click **Preview**
   - Navigate to Lab 3.1
   - Answer all questions
   - Verify scoring works correctly

**Deliverables Checklist**:
- [ ] Exercise 1 created (matching/identifying flow purposes)
- [ ] Exercise 2 created (identifying required components)
- [ ] Exercise 3 created (explaining description importance)
- [ ] All exercises tested in preview mode

### Lab 3.2: Creating Your First Flow

**Type**: Hands-On Lab with Auto-Grading (Rubric-based)

**⏱️ Estimated Time**: 1.5-2 hours (second most complex assessment)

**💡 Time-Saving Tip**: Use Template 5 (Flow Validation) as base. The structure is very similar to Lab 2.2 but validates flows instead of responses. Copy Lab 2.2's indentation checking logic.

**Content Structure**:
- Complete step-by-step instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Create `goodbye.yml` flow

#### Step 0.5: Add Lab 3.2 Guide Content to Codio

**⏱️ Estimated Time**: 10-15 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 3.2 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 3.2 student-facing content to Codio's Guide Editor so students can see the detailed step-by-step instructions.

**🔍 Before You Start**: Make sure you've added Unit 3 content and Lab 3.1 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 3 Section**: Click on **Unit 3: Understanding Flows** in the left sidebar

3. **Add Lab 3.2 Subsection**: Scroll down in Unit 3's content area to find where Lab 3.1 ends, then click where you want Lab 3.2 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below (from `### Lab 3.2` to the `---` line before section 3.3), copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 3.2 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode. This is a longer lab with detailed step-by-step instructions - make sure all sections display properly.

**📋 Copy This Markdown for Lab 3.2**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 3.2. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting
- **If the content is very long**: This lab has detailed step-by-step instructions. Make sure you copied the entire block

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 3.2 Assessment Using LLM Rubric Autograde

**⏱️ Estimated Time**: 10-15 minutes (reduced from 1.5-2 hours using LLM Rubric instead of custom Python script)

**💡 Time-Saving Tip**: Using LLM Rubric Autograde saves 80-105 minutes vs. writing a custom Python script. No coding required!

**📖 Assessment Type**: **LLM Rubric Autograde** (see "Codio Native Assessment Features Guide" above for details)

**What you're doing**: Creating an LLM Rubric assessment that validates the `goodbye.yml` flow file structure, required fields, and YAML correctness using AI-powered grading.

**How to do it**:

1. **Navigate to Lab 3.2 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 3.2: Creating Your First Flow** subsection
   - Scroll to bottom
   - **Expected Result**: You see the end of Lab 3.2 content, with `+` button visible

2. **Add LLM Rubric Assessment**:
   - Click **`+`** button
   - Select **"LLM Rubric"** or **"Autograde"** from dropdown
   - **Expected Result**: Form appears with multiple fields

3. **Configure the Assessment** (Fill in all fields):

   **a. Assessment Instructions**:
   - **Field Name**: "Instructions" or "Task Description"
   - **What to type**:
     ```
     Create a new flow file called "goodbye.yml" in the data/basics/ folder.
     
     The flow should:
     - Be named "goodbye" (under flows: section)
     - Have a name field (e.g., "goodbye")
     - Have a description field that explains when this flow should trigger (e.g., "Farewell the user when they end the conversation")
     - Have a steps section with at least one action: utter_goodbye
     - Use proper YAML syntax with correct indentation (2 spaces per level)
     ```

   **b. Rubric/Requirements** (Be very specific):
   - **Field Name**: "Rubric" or "Requirements"
   - **What to type**:
     ```
     Requirements Checklist (all must be met):
     
     1. File Location and Existence:
        - File data/basics/goodbye.yml exists in /home/codio/workspace/level1/
        - File is valid YAML (no syntax errors, parses correctly)
        - File is in correct location (data/basics/, not data/ root)
     
     2. Flow Structure:
        - File contains a flows: section (top level, no indentation)
        - Flow named "goodbye" exists under flows: section
        - Flow is properly indented (goodbye: is 2 spaces from left margin)
     
     3. Required Fields:
        - Flow has a "name" field (e.g., name: goodbye)
        - Flow has a "description" field (non-empty, descriptive text explaining when flow triggers)
        - Flow has a "steps" field (list of actions)
        - All fields are properly indented (4 spaces from left margin, under goodbye:)
     
     4. Steps Section:
        - steps: section contains at least one action
        - Action format is correct: "- action: utter_goodbye"
        - Action is properly indented (6 spaces from left margin, under steps:)
        - Action references existing response (utter_goodbye should exist in domain file)
     
     5. Description Quality:
        - description field is not empty
        - description is meaningful (explains when/why flow triggers, >10 characters)
        - description helps LLM understand when to use this flow
     
     6. YAML Syntax and Indentation:
        - Uses exactly 2 spaces for indentation (not tabs, not 4 spaces)
        - flows: is at left margin (0 spaces)
        - goodbye: is indented 2 spaces
        - name:/description:/steps: are indented 4 spaces
        - - action: is indented 6 spaces
        - No tabs used anywhere
     
     Grading: Award full points (12) if all requirements are met. Deduct points for each missing requirement.
     ```

   **c. Solution File**:
   - **Field Name**: "Solution File" or "Reference File"
   - **What to type**: `/home/codio/workspace/level1/data/basics/goodbye.yml` (or path to example flow file)
   - **Purpose**: Helps LLM understand expected flow structure

   **d. Files to Check**:
   - **Field Name**: "Files to Grade" or "Student Files"
   - **What to type**: `/home/codio/workspace/level1/data/basics/goodbye.yml`
   - **Purpose**: Tells LLM which file to analyze

   **e. Guide Content Context**:
   - **Field Name**: "Guide Content" or "Context"
   - **What to type**: Copy Lab 3.2 instructions from guide (student-facing content about creating flows)

   **f. Points**: `12`

   **g. Timeout**: `60` (seconds)

4. **Save the Assessment**:
   - Click **Save** button
   - **Expected Result**: Assessment saved, no errors

5. **Enable Code Playback** (Optional):
   - Click **Education** → **Monitoring** → **Code Playback**
   - Add `data/basics/goodbye.yml` to tracked files

6. **Test the Assessment**:
   - Test with correct flow file (should pass)
   - Test with missing description (should fail with specific feedback)
   - Test with wrong indentation (should fail with indentation feedback)
   - Test with missing steps (should fail with steps feedback)

**Expected output when passing**:
```
✅ Assessment Passed

Feedback:
- ✓ File data/basics/goodbye.yml exists and is valid YAML
- ✓ Flow "goodbye" exists under flows: section
- ✓ Required fields present (name, description, steps)
- ✓ Description is meaningful and descriptive
- ✓ Steps section contains action: utter_goodbye
- ✓ Correct indentation (2 spaces per level)
- ✓ YAML syntax is correct

Score: 12/12
```

**Troubleshooting**: See Lab 2.2 troubleshooting section above (similar issues and fixes apply).

#### Step 2: Configure Virtual Coach for Lab 3.2

**What you're doing**: Adding specific hints for flow creation errors.

**How to do it**:

1. **Open Virtual Coach settings**:
   - Click **Education** → **Settings** → **Virtual Coach**

2. **Add Lab 3.2 specific hints**:
   - Under **Summarize Prompt**, add:
     ```
     Lab 3.2 Checklist:
     1. Create goodbye.yml in data/basics/ folder
     2. Start with 'flows:' (no indentation)
     3. Add 'goodbye:' (indent 2 spaces)
     4. Add 'name:', 'description:', 'steps:' (indent 4 spaces under goodbye:)
     5. Add '- action: utter_goodbye' (indent 6 spaces under steps:)
     6. CRITICAL: description must be non-empty and clear!
     ```
   - Under **Error Augmentation**, add:
     ```
     "Missing description" → "The description field is CRITICAL! The LLM uses it to match user messages. Add: 'description: Farewell the user when they end the conversation.'"
     "Wrong file location" → "Create goodbye.yml in data/basics/ folder, not data/ root. The path should be: data/basics/goodbye.yml"
     "Indentation errors" → "Use exactly 2 spaces per indent: flows: (0), goodbye: (2), name:/description:/steps: (4), - action: (6)"
     "Missing steps" → "Every flow needs a steps: section with at least one action. Format: '- action: utter_goodbye'"
     ```

3. **Save and test**: Click **Save**, test in preview

**Deliverables Checklist**:
- [ ] Lab 3.2 Code Test created with comprehensive grader
- [ ] All rubric criteria validated
- [ ] Code Playback enabled
- [ ] Virtual Coach configured with Lab 3.2 hints
- [ ] Assessment tested

### Lab 3.3: Multiple Steps in a Flow

**Type**: Hands-On Lab with Auto-Grading (LLM Rubric Autograde)

**⏱️ Estimated Time**: 10-15 minutes (using LLM Rubric instead of custom script)

**💡 Time-Saving Tip**: Duplicate Lab 3.2's LLM Rubric assessment, then edit the rubric to check for 2+ steps instead of 1. No coding required.

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Modify greet.yml to have two steps (e.g., utter_greet then utter_help)

#### Step 0.5: Add Lab 3.3 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 3.3 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 3.3 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 3 content, Lab 3.1, and Lab 3.2 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 3 Section**: Click on **Unit 3: Understanding Flows** in the left sidebar

3. **Add Lab 3.3 Subsection**: Scroll down in Unit 3's content area to find where Lab 3.2 ends, then click where you want Lab 3.3 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 3.3 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 3.3**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 3.3. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 3.3 Assessment Using LLM Rubric Autograde

**What you're doing**: Creating an LLM Rubric assessment that validates students modified a flow (e.g., greet.yml) to have at least 2 steps.

**How to do it**:

1. **Navigate to Lab 3.3 in Guides** → Scroll to bottom

2. **Add LLM Rubric Assessment** (or Duplicate Lab 3.2's assessment and edit):
   - Click **`+`** → Select **"LLM Rubric"** or **"Autograde"**

3. **Configure the Assessment**:

   **a. Assessment Instructions**:
   - **What to type**:
     ```
     Modify the greet flow in data/basics/greet.yml to have at least 2 steps.
     
     The flow should:
     - Have at least 2 actions in the steps section (e.g., utter_greet and utter_help)
     - Use proper YAML syntax (2 spaces indentation)
     - All action references (utter_*) should exist in domain/basics.yml
     - Steps execute in order (first action, then second)
     ```

   **b. Rubric/Requirements**:
   - **What to type**:
     ```
     Requirements Checklist (all must be met):
     
     1. File Location: data/basics/greet.yml exists and is valid YAML
     2. Flow Structure: Flow (e.g., greet) exists under flows: section
     3. Steps Section: steps: contains at least 2 actions
     4. Action Format: Each step is "- action: utter_X" (proper indentation, 6 spaces)
     5. Response References: All actions reference existing responses in domain
     6. YAML Syntax: Uses 2 spaces for indentation, no tabs
     
     Grading: Award full points (8) if all requirements are met.
     ```

   **c. Solution File**: `/home/codio/workspace/level1/data/basics/greet.yml`

   **d. Files to Check**: `/home/codio/workspace/level1/data/basics/greet.yml`

   **e. Points**: `8` | **Timeout**: `60` seconds

4. **🤖 Use Generate Rubrics First** (if available): Click **Generate Rubrics** → refine to add "at least 2 steps" requirement

5. **Test**: Verify passes with 2+ steps, fails with 1 step

**Deliverables Checklist**:
- [ ] Lab 3.3 LLM Rubric Autograde created (or duplicated from Lab 3.2 and modified)
- [ ] Checks for at least 2 steps, correct structure, existing responses

### Lab 3.4: Flow Descriptions and LLM Matching

**Type**: Hands-On Lab with Auto-Grading (LLM Rubric Autograde)

**⏱️ Estimated Time**: 10-15 minutes (using LLM Rubric instead of custom script)

**💡 Time-Saving Tip**: This assessment is similar to Lab 3.2 but validates 2 files and focuses on description quality. You can duplicate Lab 3.2's assessment and modify it.

**Content Structure**:
- Explain how `description:` field helps LLM match user messages
- Show examples of good vs bad descriptions
- Guide students to create 2 new flows from scratch (hours.yml, balance.yml)
- Remind students they can use existing flows (greet.yml, goodbye.yml) as templates

**Hands-On Exercise**:
- Student creates 2 new flow files: hours.yml and balance.yml
- Each flow must have proper structure (flows:, name:, description:, steps:)
- Focus on writing good, specific descriptions that help LLM matching

#### Step 0.5: Add Lab 3.4 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 3.4 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 3.4 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 3 content, Lab 3.1, Lab 3.2, and Lab 3.3 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 3 Section**: Click on **Unit 3: Understanding Flows** in the left sidebar

3. **Add Lab 3.4 Subsection**: Scroll down in Unit 3's content area to find where Lab 3.3 ends, then click where you want Lab 3.4 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 3.4 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 3.4**:

⬇️ START COPYING HERE ⬇️

### Lab 3.4: Flow Descriptions and LLM Matching

**Objective**: Create new flows with good descriptions that help the LLM match user messages.

**Before You Begin**:
- ✅ You've completed Lab 3.2 (created goodbye.yml)
- ✅ You understand flow structure (flows:, name:, description:, steps:)
- ✅ You know where `data/basics/` folder is located
- ✅ You can reference existing flows (greet.yml, goodbye.yml) as templates

#### Understanding Flow Descriptions

The `description` field is **critical** because the LLM uses it to match user messages to flows.

**How It Works**:
1. User sends a message: "What are your hours?"
2. LLM reads all flow descriptions
3. LLM matches the message to the best-fitting description
4. Rasa triggers that flow

**Writing Good Descriptions**:

✅ **Good descriptions**:
- Clear and specific: "Tell the user when the bank is open and what the operating hours are"
- Action-oriented: "Provide contact information for the bank"
- Context-aware: "Explain what the bot can help with"

❌ **Bad descriptions**:
- Too vague: "Help user" (what kind of help?)
- Too specific: "Respond when user says exactly 'hello'" (misses "hi", "hey")
- Missing context: "Say hello" (when? why?)

#### Task: Create 2 New Flows

Create 2 new flow files in `data/basics/` folder. Use `greet.yml` or `goodbye.yml` as templates for structure.

**Flow 1: Bank Hours**
- **File**: `data/basics/hours.yml`
- **Flow name**: `hours`
- **Description**: Write a clear, specific description about providing bank hours
- **Steps**: At least one action (e.g., `utter_hours` - you may need to create this response in domain/basics.yml first, or use an existing response)

**Flow 2: Account Balance Help**
- **File**: `data/basics/balance.yml`
- **Flow name**: `balance`
- **Description**: Write a clear, specific description about explaining how to check account balance
- **Steps**: At least one action (e.g., `utter_balance_help` or use an existing response)

#### Step-by-Step Instructions

1. **Create hours.yml**:
   - Copy the structure from `greet.yml` or `goodbye.yml` as a template
   - Change the flow name to `hours`
   - Write a good description (see examples below)
   - Add at least one step with an action

2. **Create balance.yml**:
   - Copy the structure from `greet.yml` or `goodbye.yml` as a template
   - Change the flow name to `balance`
   - Write a good description (see examples below)
   - Add at least one step with an action

#### Example: Good Descriptions

Here are examples of good flow descriptions for **different** flows (not the ones you're creating):

**Example 1: Contact Information Flow**:
```yaml
flows:
  contact:
    name: contact info
    description: "Provide contact information for the bank, including phone numbers and email addresses"
    steps:
      - action: utter_contact
```

**Example 2: Services Flow**:
```yaml
flows:
  services:
    name: available services
    description: "List all the services and features the bot can help with, including account management and support options"
    steps:
      - action: utter_help
```

**Key**: Be specific about what the flow does, not how the user asks for it. Notice how these descriptions:
- Use action verbs ("Provide", "List")
- Are specific about what information is given
- Include context about what the flow accomplishes
- Are at least 20 characters long

**Your Task**: Create similar descriptions for `hours.yml` and `balance.yml` following this pattern, but write your own descriptions (don't copy these examples).

#### Checklist

Before submitting, verify:
- ✅ Both files exist in `data/basics/` folder
- ✅ Both flows have `name:` fields
- ✅ Both flows have `description:` fields (at least 20 characters, specific and action-oriented)
- ✅ Both flows have `steps:` sections with at least one action
- ✅ Descriptions are unique (different from each other and from other flows)
- ✅ YAML syntax is correct (2 spaces indentation, no tabs)
- ✅ File structure matches the template (flows: at top level, proper indentation)

**AI Coach**: Ask "How do I write a good flow description?" or "What makes a description too vague?"

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 3.4. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

**Content Structure**:
- Explain how `description:` field helps LLM match user messages
- Show examples of good vs bad descriptions
- Guide students to create 2 new flows from scratch (hours.yml, balance.yml)
- Remind students they can use existing flows (greet.yml, goodbye.yml) as templates

**Hands-On Exercise**:
- Student creates 2 new flow files: hours.yml and balance.yml
- Each flow must have proper structure (flows:, name:, description:, steps:)
- Focus on writing good, specific descriptions that help LLM matching

**Auto-Grading**:
- Validates both files exist (hours.yml, balance.yml)
- Validates flow structure (flows:, name:, description:, steps:)
- Validates descriptions are descriptive (not empty, >20 characters, specific, action-oriented)
- Checks descriptions are unique (different from each other and other flows)
- Validates YAML syntax and indentation
- Points: 8

**Deliverables**:
- Lab instructions
- LLM Rubric Autograde assessment

#### Step 1: Create Lab 3.4 Assessment Using LLM Rubric Autograde

**⏱️ Estimated Time**: 10-15 minutes (using LLM Rubric instead of custom script)

**💡 Time-Saving Tip**: This assessment is similar to Lab 3.2 but validates 2 files and focuses on description quality. You can duplicate Lab 3.2's assessment and modify it.

**📖 Assessment Type**: **LLM Rubric Autograde** (see "Codio Native Assessment Features Guide" above for details)

**What you're doing**: Creating an LLM Rubric assessment that validates students created 2 new flow files (hours.yml, balance.yml) with proper structure and good descriptions.

**How to do it**:

1. **Navigate to Lab 3.4 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 3.4: Flow Descriptions and LLM Matching** subsection
   - Scroll to bottom
   - **Expected Result**: You see the end of Lab 3.4 content, with `+` button visible

2. **Add LLM Rubric Assessment**:
   - Click **`+`** button
   - Select **"LLM Rubric"** or **"Autograde"** from dropdown
   - **Expected Result**: Form appears with multiple fields

3. **Configure the Assessment** (Fill in all fields):

   **a. Assessment Instructions**:
   - **Field Name**: "Instructions" or "Task Description"
   - **What to type**:
     ```
     Create 2 new flow files in the data/basics/ folder:
     1. hours.yml - A flow that provides bank hours
     2. balance.yml - A flow that explains how to check account balance
     
     You can use greet.yml or goodbye.yml as templates for the structure.
     
     Each flow must have:
     - Proper flow structure (flows: section, flow name, name:, description:, steps:)
     - A clear, specific description (at least 20 characters, action-oriented)
     - At least one step with an action
     - Correct YAML syntax and indentation (2 spaces)
     - Unique descriptions (different from each other and from other flows)
     ```

   **b. Rubric/Requirements** (Be very specific):
   - **Field Name**: "Rubric" or "Requirements"
   - **What to type**:
     ```
     Requirements Checklist (all must be met):
     
     **Reference**: Use data/basics/greet.yml or data/basics/goodbye.yml as templates for structure and formatting.
     
     1. File Location and Existence:
        - File data/basics/hours.yml exists in /home/codio/workspace/level1/
        - File data/basics/balance.yml exists in /home/codio/workspace/level1/
        - Both files are valid YAML (no syntax errors, parses correctly)
        - Both files are in correct location (data/basics/, not data/ root)
     
     2. Flow Structure (hours.yml):
        - File contains a flows: section (top level, no indentation)
        - Flow named "hours" exists under flows: section
        - Flow is properly indented (hours: is 2 spaces from left margin)
        - Flow has a "name" field (e.g., name: bank hours)
        - Flow has a "description" field (non-empty, descriptive text)
        - Flow has a "steps" field (list of actions)
        - All fields are properly indented (4 spaces from left margin, under hours:)
     
     3. Flow Structure (balance.yml):
        - File contains a flows: section (top level, no indentation)
        - Flow named "balance" exists under flows: section
        - Flow is properly indented (balance: is 2 spaces from left margin)
        - Flow has a "name" field (e.g., name: balance help)
        - Flow has a "description" field (non-empty, descriptive text)
        - Flow has a "steps" field (list of actions)
        - All fields are properly indented (4 spaces from left margin, under balance:)
     
     4. Steps Sections:
        - hours.yml steps: section contains at least one action
        - balance.yml steps: section contains at least one action
        - Each action format is correct: "- action: utter_X"
        - Actions are properly indented (6 spaces from left margin, under steps:)
        - Actions reference existing responses in domain/basics.yml (or student may need to create them)
     
     5. Description Quality (CRITICAL - This is the main learning objective):
        - hours.yml description is non-empty and at least 20 characters long
        - balance.yml description is non-empty and at least 20 characters long
        - hours.yml description is specific (explains what the flow does, not vague like "help user")
        - balance.yml description is specific (explains what the flow does, not vague like "help user")
        - hours.yml description is action-oriented (uses verbs like "tell", "explain", "provide")
        - balance.yml description is action-oriented (uses verbs like "tell", "explain", "provide")
        - hours.yml description includes context (when/why the flow triggers, what it accomplishes)
        - balance.yml description includes context (when/why the flow triggers, what it accomplishes)
        - Descriptions help LLM understand each flow's purpose (clear enough for matching)
        - Descriptions avoid being too vague (not just "help" or "information")
        - Descriptions avoid being too specific about exact user phrases (focus on what, not how user asks)
     
     6. Description Uniqueness:
        - hours.yml description is unique (different from balance.yml description)
        - balance.yml description is unique (different from hours.yml description)
        - Both descriptions are different from other existing flow descriptions (greet.yml, goodbye.yml, etc.)
        - Each description is tailored to its flow's specific purpose
     
     7. YAML Syntax and Indentation:
        - Uses exactly 2 spaces for indentation (not tabs, not 4 spaces)
        - flows: is at left margin (0 spaces)
        - Flow names (hours:, balance:) are indented 2 spaces
        - name:/description:/steps: are indented 4 spaces
        - - action: items are indented 6 spaces
        - No tabs used anywhere
        - Overall indentation pattern matches template files (greet.yml, goodbye.yml)
     
     Grading: Award full points (8) if all requirements are met, especially description quality and uniqueness. Descriptions must be specific, action-oriented, and helpful for LLM matching. Deduct points for missing files, missing descriptions, vague descriptions (like "help user"), duplicate descriptions, incorrect structure, or syntax errors.
     ```

   **c. Solution File**:
   - **Field Name**: "Solution File" or "Reference File"
   - **What to type**: `/home/codio/workspace/level1/data/basics/greet.yml` (or path to example flow file)
   - **Purpose**: Helps LLM understand expected flow structure

   **d. Files to Check** (if available):
   - **Field Name**: "Files to Grade" or "Student Files"
   - **What to type**: `/home/codio/workspace/level1/data/basics/hours.yml, /home/codio/workspace/level1/data/basics/balance.yml`
   - **Purpose**: Tells LLM which files to analyze
   - **Note**: If this field doesn't exist, the LLM will check files mentioned in the rubric

   **e. Guide Content Context**:
   - **Field Name**: "Guide Content" or "Context"
   - **What to type**: Copy Lab 3.4 instructions from guide (student-facing content about creating flows with good descriptions)

   **f. Points**: `8`

   **g. Timeout**: `60` (seconds)

4. **Save the Assessment**:
   - Click **Save** button
   - **Expected Result**: Assessment saved, no errors

5. **Enable Code Playback** (Optional):
   - Click **Education** → **Monitoring** → **Code Playback**
   - Add `data/basics/hours.yml` and `data/basics/balance.yml` to tracked files

6. **Test the Assessment**:
   - Test with both files created correctly with good descriptions (should pass)
   - Test with missing files (should fail)
   - Test with vague descriptions like "help user" (should fail)
   - Test with duplicate descriptions (should fail)
   - Test with incorrect structure (should fail)
   - Test with missing description fields (should fail)

**Expected output when passing**:
```
✅ Assessment Passed

Feedback:
- ✓ Both files (hours.yml, balance.yml) exist in data/basics/
- ✓ Both flows have proper structure (flows:, name:, description:, steps:)
- ✓ Descriptions are specific, action-oriented, and meaningful (>20 characters)
- ✓ Descriptions are unique (different from each other and other flows)
- ✓ Steps sections contain actions
- ✓ Correct indentation (2 spaces per level)
- ✓ YAML syntax is correct

Score: 8/8
```

**Troubleshooting**:
- **"Missing files"**: Student didn't create both files. Remind them to create hours.yml and balance.yml.
- **"Vague descriptions"**: Descriptions are too generic (e.g., "help user"). Show examples of specific, action-oriented descriptions.
- **"Duplicate descriptions"**: Both flows have the same description. Remind students each flow needs a unique description tailored to its purpose.
- **"Missing description"**: Student forgot the description field. Remind them it's critical for LLM matching.

**Deliverables Checklist**:
- [ ] Lab 3.4 LLM Rubric Autograde created
- [ ] Checks for both files (hours.yml, balance.yml)
- [ ] Validates flow structure (flows:, name:, description:, steps:)
- [ ] Validates description quality (specific, action-oriented, >20 characters)
- [ ] Validates description uniqueness
- [ ] Assessment tested with various student submissions

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

**📋 IMPORTANT: Add Guide Content First**

**Before creating assessments**, add the student-facing content to Codio's Guide Editor:
- **Add Main Unit Content**: Copy content from `## For Students` (line 4677) to before `### Lab 4.1` (line 4777). See "Adding Guide Content to Codio" section above.
- **Add Lab Content**: Use Step 0.5 sections for Labs 4.1, 4.2 (see below).
- **⏱️ Estimated Time**: 25-35 minutes (main content + 2 labs)

### Lab 4.1: Understanding System Patterns

**Type**: Exploration Lab with Auto-Grading

**Content Structure**:
- Pre-populated `data/system/patterns/patterns.yml` file
- Brief explanation (preserved from TUTORIAL.md)

#### Step 0.5: Add Lab 4.1 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 4.1 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 4.1 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 4 content to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 4 Section**: Click on **Unit 4: System Patterns** in the left sidebar

3. **Add Lab 4.1 Subsection**: Scroll down in Unit 4's content area and click where you want Lab 4.1 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 4.1 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 4.1**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 4.1. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 4.1 Assessments (Multiple Choice)

**What you're doing**: Creating concept checks to verify students understand system patterns.

**How to do it**:

1. **Navigate to Lab 4.1 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 4.1: Understanding System Patterns** subsection
   - Scroll to bottom

2. **Add Exercise 1** (Explain pattern_session_start):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `What does pattern_session_start do?`
   - **Points**: `2`
   - **Options**:
     - `Triggers when a new conversation session begins` (check "Correct" ✓)
     - `Triggers when a flow completes` (uncheck)
     - `Triggers on every user message` (uncheck)
     - `Triggers when the bot errors` (uncheck)
   - **Explanation**: `pattern_session_start runs automatically when a new conversation starts, typically to greet the user.`
   - Click **Save**

3. **Add Exercise 2** (Explain pattern_completed):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `What does pattern_completed do?`
   - **Points**: `2`
   - **Options**:
     - `Triggers when a flow finishes executing` (check "Correct" ✓)
     - `Triggers when a session starts` (uncheck)
     - `Triggers on errors` (uncheck)
     - `Triggers on every step` (uncheck)
   - **Explanation**: `pattern_completed runs automatically after a flow completes, useful for cleanup or follow-up messages.`
   - Click **Save**

4. **Add Exercise 3** (Identify trigger points):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `When do system patterns trigger?`
   - **Points**: `2`
   - **Options**:
     - `Automatically based on conversation events (session start, flow completion)` (check "Correct" ✓)
     - `Only when explicitly called in flows` (uncheck)
     - `Only when the user asks for them` (uncheck)
     - `They don't trigger automatically` (uncheck)
   - **Explanation**: `System patterns trigger automatically based on conversation events, not user messages or explicit calls.`
   - Click **Save**

5. **Test all exercises**: Click **Preview**, navigate to Lab 4.1, verify all questions work

**Deliverables Checklist**:
- [ ] Exercise 1 created (pattern_session_start explanation)
- [ ] Exercise 2 created (pattern_completed explanation)
- [ ] Exercise 3 created (trigger identification)
- [ ] All exercises tested

### Lab 4.2: Modifying System Patterns

**Type**: Hands-On Lab with Auto-Grading

**⏱️ Estimated Time**: 30-35 minutes

**💡 Time-Saving Tip**: Use Template 1 (YAML Validator). Very simple - just check file exists, YAML parses, and pattern exists. Minimal customization needed.

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Hands-on exercise: Modify greeting message in `pattern_session_start`

#### Step 0.5: Add Lab 4.2 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 4.2 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 4.2 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 4 content and Lab 4.1 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 4 Section**: Click on **Unit 4: System Patterns** in the left sidebar

3. **Add Lab 4.2 Subsection**: Scroll down in Unit 4's content area to find where Lab 4.1 ends, then click where you want Lab 4.2 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 4.2 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 4.2**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 4.2. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 4.2 Assessment Using LLM Rubric Autograde

**⏱️ Estimated Time**: 10-15 minutes (reduced from 30-35 minutes using LLM Rubric instead of custom Python script)

**💡 Time-Saving Tip**: Using LLM Rubric Autograde saves 15-20 minutes vs. writing a custom Python script. No coding required!

**📖 Assessment Type**: **LLM Rubric Autograde** (see "Codio Native Assessment Features Guide" above for details)

**What you're doing**: Creating an LLM Rubric assessment that validates the `pattern_session_start` modification using AI-powered grading.

**How to do it**:

1. **Navigate to Lab 4.2 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 4.2: Modifying System Patterns** subsection
   - Scroll to bottom

2. **Add LLM Rubric Assessment**:
   - Click **`+`** button
   - Select **"LLM Rubric"** or **"Autograde"** from dropdown

3. **Configure the Assessment**:

   **a. Assessment Instructions**:
   - **What to type**:
     ```
     Modify the pattern_session_start flow in data/system/patterns/patterns.yml to add a second step that provides contact information.
     
     The pattern should:
     - Keep the existing utter_greet step
     - Add a new step: - action: utter_contact
     - Maintain proper YAML syntax and indentation
     ```

   **b. Rubric/Requirements**:
   - **What to type**:
     ```
     Requirements Checklist (all must be met):
     
     1. File Location and Existence:
        - File data/system/patterns/patterns.yml exists in /home/codio/workspace/level1/
        - File is valid YAML (no syntax errors, parses correctly)
     
     2. Pattern Structure:
        - pattern_session_start exists under patterns: section (or flows: section, depending on file structure)
        - Pattern has a steps: section
        - Steps section is a list (contains action items)
     
     3. Required Steps:
        - Steps section contains at least one action: utter_greet
        - Steps section contains action: utter_contact
        - Both actions are properly formatted: "- action: utter_X"
        - Actions are properly indented (6 spaces from left margin, under steps:)
     
     4. Response References:
        - All action references (utter_greet, utter_contact) should exist in domain/basics.yml
        - Action names start with "utter_"
     
     5. YAML Syntax and Indentation:
        - Uses exactly 2 spaces for indentation (not tabs, not 4 spaces)
        - Proper indentation throughout file
        - No tabs used
     
     Grading: Award full points (6) if all requirements are met. Deduct points for each missing requirement.
     ```

   **c. Solution File**: `/home/codio/workspace/level1/data/system/patterns/patterns.yml`

   **d. Files to Check**: `/home/codio/workspace/level1/data/system/patterns/patterns.yml`

   **e. Guide Content Context**: Copy Lab 4.2 instructions from guide

   **f. Points**: `6`

   **g. Timeout**: `60` (seconds)

4. **Save the Assessment**: Click **Save** button

5. **Enable Code Playback** (Optional):
   - Click **Education** → **Monitoring** → **Code Playback**
   - Add `data/system/patterns/patterns.yml` to tracked files

6. **Test the Assessment**:
   - Test with correct modification (should pass)
   - Test with missing utter_contact step (should fail)
   - Test with wrong indentation (should fail)

**Deliverables Checklist**:
- [ ] Lab 4.2 Code Test created
- [ ] Validates YAML, response reference, structure
- [ ] Code Playback enabled
- [ ] Assessment tested

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

**📋 IMPORTANT: Add Guide Content First**

**Before creating assessments**, add the student-facing content to Codio's Guide Editor:
- **Add Main Unit Content**: Copy content from `## For Students` (line 5139) to before `### Lab 5.1` (line 5312). See "Adding Guide Content to Codio" section above.
- **Add Lab Content**: Use Step 0.5 section for Lab 5.1 (see below).
- **⏱️ Estimated Time**: 20-30 minutes (main content + 1 lab)

**⏱️ Total Estimated Time**: 1 hour

**💡 Time-Saving Tip**: All 6 questions are multiple choice. Use Template 3. Create all in one batch session (saves 15-20 minutes vs. creating separately).

**Content Structure**:
- Pre-populated config files (`config.yml`, `credentials.yml`, `endpoints.yml`)
- Brief explanation of each file (preserved from TUTORIAL.md)

#### Step 0.5: Add Lab 5.1 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 5.1 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 5.1 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 5 content to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 5 Section**: Click on **Unit 5: Configuration Files** in the left sidebar

3. **Add Lab 5.1 Subsection**: Scroll down in Unit 5's content area and click where you want Lab 5.1 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 5.1 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 5.1**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 5.1. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 5 Assessments (Multiple Choice)

**💡 Time-Saving Tip**: Create all 6 questions in one session. Use the same settings for all (Template 3). Copy question format and modify content only.

**What you're doing**: Creating concept checks to verify students understand config file purposes.

**How to do it**:

1. **Navigate to Unit 5 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Unit 5 – Configuration Files** section
   - Scroll to bottom

2. **Add Exercise 1** (Identify file purposes):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `What does config.yml define?`
   - **Points**: `1`
   - **Options**:
     - `How to build the bot (architecture, LLM, language)` (check "Correct" ✓)
     - `How the bot connects to chat interfaces` (uncheck)
     - `Where to find actions and LLM configuration` (uncheck)
   - **Explanation**: `config.yml defines the bot's architecture, language, and LLM pipeline.`
   - Click **Save**

3. **Add Exercise 1b** (credentials.yml):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `What does credentials.yml define?`
   - **Points**: `1`
   - **Options**:
     - `How the bot connects to chat interfaces` (check "Correct" ✓)
     - `How to build the bot` (uncheck)
     - `Where to find actions` (uncheck)
   - **Explanation**: `credentials.yml defines connections to chat channels like REST API and Socket.IO.`
   - Click **Save**

4. **Add Exercise 1c** (endpoints.yml):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `What does endpoints.yml define?`
   - **Points**: `1`
   - **Options**:
     - `Where to find actions, tools, and LLM configuration` (check "Correct" ✓)
     - `How to build the bot` (uncheck)
     - `How the bot connects to interfaces` (uncheck)
   - **Explanation**: `endpoints.yml defines where actions are located and LLM configuration for NLG.`
   - Click **Save**

5. **Add Exercise 2** (Explain key sections - config.yml):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `What does the "pipeline:" section in config.yml do?`
   - **Points**: `2`
   - **Options**:
     - `Defines how Rasa understands user messages (uses LLM)` (check "Correct" ✓)
     - `Defines chat channel connections` (uncheck)
     - `Defines where actions are located` (uncheck)
   - **Explanation**: `The pipeline section defines the NLU (Natural Language Understanding) components, including which LLM to use.`
   - Click **Save**

6. **Add Exercise 2b** (endpoints.yml nlg):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `What does the "nlg:" section in endpoints.yml do?`
   - **Points**: `2`
   - **Options**:
     - `Defines how responses are generated (allows rephrasing)` (check "Correct" ✓)
     - `Defines chat connections` (uncheck)
     - `Defines bot architecture` (uncheck)
   - **Explanation**: `The nlg (Natural Language Generation) section enables response rephrasing via LLM, which is why rephrase: True works in responses.`
   - Click **Save**

7. **Add Exercise 2c** (model_groups):
   - Click **+** → Select **Multiple Choice**
   - **Question**: `What does "temperature: 0.3" in model_groups control?`
   - **Points**: `1`
   - **Options**:
     - `How creative/deterministic the LLM responses are` (check "Correct" ✓)
     - `The speed of the LLM` (uncheck)
     - `The cost of API calls` (uncheck)
   - **Explanation**: `Temperature controls creativity: 0.0 = deterministic (same input = same output), 1.0 = very creative. 0.3 is a balanced setting.`
   - Click **Save**

8. **Test all exercises**: Click **Preview**, verify all questions work

**Deliverables Checklist**:
- [ ] Exercise 1 created (file purposes - 3 questions)
- [ ] Exercise 2 created (key sections - 3 questions)
- [ ] All exercises tested
- [ ] Virtual Coach enabled for Unit 5 (students can ask about config files)

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

**What you'll do**: In **Lab 6.1** below you'll run the training command, see what success looks like, and fix common errors. The lab is split into **Part 1: In Codio** and **Part 2: Running locally** — follow the part that matches your setup.

---

# Lab 6.1: Training Your Bot

**Objective**: Train your bot and verify it works.

---

## Part 1: In Codio

**1. In the terminal, go to the project folder**
- In Codio, click **Tools** → **Terminal** (or use the terminal icon).
- Navigate to the `level1` folder where your bot files live:
  ```bash
  cd level1
  ```
- Confirm you're in the right place: run `pwd` — you should see something like `/home/codio/workspace/level1`.

**2. Create and activate the virtual environment**
- Check if a virtual environment already exists:
  ```bash
  ls -la .venv
  ```
- **If `.venv` exists**: Activate it:
  ```bash
  source .venv/bin/activate
  ```
- **If `.venv` doesn't exist**: Create it first, then activate:
  ```bash
  python3.11 -m venv .venv
  source .venv/bin/activate
  ```
- **Verify activation**: Your prompt should start with `(.venv)`. If not, run `source .venv/bin/activate` again.
- **Note**: Rasa loads your `.env` when you run from `level1/`, so being in this folder with venv active is required.

**3. Install Rasa Pro (if not already installed)**
- With the venv active, check if Rasa is installed:
  ```bash
  python -m rasa --version
  ```
- **If you see an error** (e.g., "No module named 'rasa'"): Install Rasa Pro:
  ```bash
  python -m pip install --no-cache-dir rasa-pro
  ```
- Wait for installation to complete (2-5 minutes). You should see "Successfully installed rasa-pro-x.x.x" at the end.

**4. Run the training command**
- From the `level1` folder (with venv active), run:
  ```bash
  python -m rasa train
  ```
- Wait for training to complete (usually 1–3 minutes). Do not close the terminal until you see "Successfully saved model" or an error.

**5. What you'll see**
- When training starts, output will look like:
  ```
  Training Core model...
  2025-01-12 12:08:17 INFO     rasa.core.training  - Training FlowPolicy...
  2025-01-12 12:08:17 INFO     rasa.core.training  - FlowPolicy training completed.
  2025-01-12 12:08:17 INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'.
  ```
- **"Training Core model"**: Building the conversation logic  
- **"Training FlowPolicy"**: Processing your flows  
- **"Successfully saved model"**: Training completed, model saved

**6. Verify success**
- The terminal shows **"Successfully saved model to 'models/...'"** and there are no error messages at the end.
- In the file tree, open `level1/models/` — you should see a new `.tar.gz` file with a timestamp (e.g. `20250112-120817-descent-lard.tar.gz`).
- If `models/` is empty or there's no new file, training did not complete; see **Common training errors** below, fix the issue, and run the command again.

**7. Common training errors (Codio)**

| Error | What to do |
|-------|------------|
| **YAML syntax error** (e.g. "block mapping", line/column given) | Check that line: use **2 spaces** (not tabs, not 4 spaces), colons after keys, dashes before list items. Fix and save, then train again. |
| **Response 'utter_xyz' not found** | The flow uses a response that isn't in `domain/basics.yml`. Add the response in the domain or fix the typo in the flow so the name matches exactly. |
| **No module named 'rasa'** | Venv not active or Rasa not installed. Run `source .venv/bin/activate`, then `rasa --version`. If it fails, install Rasa Pro: `python -m pip install --no-cache-dir rasa-pro`. |
| **RASA_LICENSE / OPENAI_API_KEY not set** | Credentials are pre-configured on Codio. Run the verification commands from Lab 0.1 step 5; if they report "is not set", ask your instructor. Otherwise run training from the `level1/` folder. |

**AI Coach**: Ask "How do I know training succeeded?" or "What should I see when training works?"

---

## Part 2: Running locally

If you're **not** using Codio, follow these steps:

**1. Open a terminal and go to the project folder**
- Open a terminal (PowerShell on Windows, Terminal.app on Mac, or Terminal on Linux).
- Navigate to your project root, then `cd level1` (or whatever folder contains `config.yml`, `domain/`, `data/`).
- Confirm you're in the right place: check that `config.yml` exists in the current directory.

**2. Create and activate the virtual environment**
- Check if a virtual environment already exists:
  - Linux/Mac: `ls -la .venv`
  - Windows: `dir .venv` (PowerShell) or `dir .venv` (Cmd)
- **If `.venv` exists**: Activate it:
  - Linux/Mac: `source .venv/bin/activate`
  - Windows PowerShell: `.venv\Scripts\Activate.ps1`
  - Windows Cmd: `.venv\Scripts\activate.bat`
- **If `.venv` doesn't exist**: Create it first, then activate:
  - Linux/Mac: `python3.11 -m venv .venv` then `source .venv/bin/activate`
  - Windows: `python -m venv .venv` then `.venv\Scripts\Activate.ps1` (PowerShell) or `.venv\Scripts\activate.bat` (Cmd)
- **Verify activation**: Your prompt should start with `(.venv)`. If not, activate it again.

**3. Install Rasa Pro (if not already installed)**
- With the venv active, check if Rasa is installed:
  ```bash
  python -m rasa --version
  ```
- **If you see an error** (e.g., "No module named 'rasa'"): Install Rasa Pro:
  ```bash
  python -m pip install --no-cache-dir rasa-pro
  ```
- Wait for installation to complete (2-5 minutes). You should see "Successfully installed rasa-pro-x.x.x" at the end.

**4. Set up environment variables**
- Rasa loads `.env` from the current directory. Create a `.env` file in the same folder as `config.yml` with:
  ```
  RASA_LICENSE=your-actual-license
  OPENAI_API_KEY=sk-your-actual-key
  ```
- **Important**: No quotes around values; no placeholder values. If you see "RASA_LICENSE not set" or "OPENAI_API_KEY not found", check that `.env` exists, has the right variable names, and you're running `rasa train` from that folder.

**5. Run the training command**
- From the project folder (with venv active), run:
  ```bash
  python -m rasa train
  ```
- Wait for training to complete (usually 1–3 minutes). Do not close the terminal until you see "Successfully saved model" or an error.

**6. What you'll see**
- When training starts, output will look like:
  ```
  Training Core model...
  2025-01-12 12:08:17 INFO     rasa.core.training  - Training FlowPolicy...
  2025-01-12 12:08:17 INFO     rasa.core.training  - FlowPolicy training completed.
  2025-01-12 12:08:17 INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'.
  ```
- **"Training Core model"**: Building the conversation logic  
- **"Training FlowPolicy"**: Processing your flows  
- **"Successfully saved model"**: Training completed, model saved

**7. Verify success**
- The terminal shows **"Successfully saved model to 'models/...'"** and there are no error messages at the end.
- Check the `models/` folder — you should see a new `.tar.gz` file with a timestamp (e.g. `20250112-120817-descent-lard.tar.gz`).
- If `models/` is empty or there's no new file, training did not complete; check error messages and fix the issue, then run the command again.

**8. Common training errors (local)**

| Error | What to do |
|-------|------------|
| **YAML syntax error** (e.g. "block mapping", line/column given) | Check that line: use **2 spaces** (not tabs, not 4 spaces), colons after keys, dashes before list items. Fix and save, then train again. |
| **Response 'utter_xyz' not found** | The flow uses a response that isn't in `domain/basics.yml`. Add the response in the domain or fix the typo in the flow so the name matches exactly. |
| **No module named 'rasa'** | Venv not active or Rasa not installed. Activate the venv, then run `python -m pip install --no-cache-dir rasa-pro`. |
| **RASA_LICENSE / OPENAI_API_KEY not set** | Create a `.env` file in the same folder as `config.yml` with `RASA_LICENSE=...` and `OPENAI_API_KEY=...` (no quotes, no placeholders). Make sure you're running `rasa train` from that folder. |

**AI Coach**: Ask "Where do I put my Rasa license?" or "How do I set environment variables?"

---

### 6.3 Using Rasa Inspector

**Inspector** is Rasa's built-in testing interface. It lets you chat with your bot in a web page so you can see how it responds. You start it from the **terminal**, then open the chat in your **browser** (or in Codio's Rasa Inspect tab).

#### Step 1: Activate the virtual environment

1. **In the terminal, make sure you're in the right folder** with the venv active (same as Lab 6.1):
   - You should be in the `level1` folder (run `pwd`; you should see a path ending in `level1`).
   - Your prompt should start with `(.venv)`. If not, run:
     ```bash
     cd level1
     source .venv/bin/activate
     ```

#### Step 2: Start Inspector in the terminal

From the `level1` folder (with venv active), run:

```bash
python -m rasa inspect --debug
```

**What you'll see**: The terminal will show a lot of output, including something like:
```
Starting Rasa server on http://0.0.0.0:5005
...
```
**Leave this terminal open.** Inspector is running as a server; if you close the terminal, it will stop.

#### Step 3: Open the chat in Codio

In Codio, go to the top menu bar and click the **Rasa Inspect** tab. The chat interface should open.

Try a few questions, for example:
- "How do I contact support?"
- "What can you do?"
- "Hi!"

At this stage the bot only uses simple responses, so the answers will be straightforward.

#### Inspector interface: what you see (beginner guide)

When Inspector opens, you'll see several areas. You don't need to understand every part to use it—here's what matters at Level 1.

1. **Chat area (main part)**
   - This is where you type and where the bot's replies appear.
   - Use it like a normal chat: type a message, press Enter, and see what the bot says.
   - Your conversation history stays visible so you can scroll back.

2. **Flow / diagram area**
   - This shows which **flow** the bot is following right now (e.g. "greet", "help", "contact").
   - Think of it as "which conversation path the bot chose." When you type "Hi!", you should see something like the greet flow; when you ask for help, the help flow.
   - If the wrong flow appears for what you said, you can use this to notice and then improve your flow descriptions later.

3. **Debug / technical details**
   - This area shows more technical information: which flow was triggered, what the bot "thought" your message meant, and so on.
   - You can ignore it at first. When something doesn't work as expected, this is where you can look to see why the wrong flow might have run.

4. **Slots**
   - Slots are for "remembering" information in a conversation. **In Level 1 we don't use them**, so this will be empty. You can ignore it until later levels.

**In short**: Use the **chat** to talk to your bot. Use the **flow** and **debug** areas to see which flow ran and to fix things when the bot doesn't do what you want.

#### Launching Rasa Inspector locally

If you're **not** using Codio and want to run Inspector on your own computer, follow the steps for your operating system. You'll need: the `level1` project folder, a virtual environment with Rasa Pro installed, and a `.env` file in `level1` with `RASA_LICENSE` and `OPENAI_API_KEY` set (see Unit 0 and Lab 0.1).

**1. Go to your project folder**

- Open a terminal (or PowerShell on Windows).
- Navigate into the `level1` folder (the one that contains `config.yml`, `domain/`, and `data/`).
- Example: `cd C:\Users\You\Minimal_Banking_Bot\level1` or `cd ~/Minimal_Banking_Bot/level1`.

**2. Activate the virtual environment and start Inspector**

- **Windows (PowerShell)**  
  ```powershell
  .venv\Scripts\Activate.ps1
  python -m rasa inspect --debug
  ```
- **Windows (Command Prompt)**  
  ```cmd
  .venv\Scripts\activate.bat
  python -m rasa inspect --debug
  ```
- **macOS / Linux**  
  ```bash
  source .venv/bin/activate
  python -m rasa inspect --debug
  ```

Leave this terminal window open. When you see something like `Starting Rasa server on http://0.0.0.0:5005`, Inspector is running.

**3. Open Inspector in your browser**

- Open a web browser (Chrome, Firefox, Edge, etc.).
- Go to: **http://localhost:5005**  
  If that shows a status page or doesn't open the chat, try: **http://localhost:5005/webhooks/socketio/inspect.html**
- You should see the Inspector chat interface. Type a message and press Enter to talk to your bot.

**Troubleshooting (local)**

- **"No module named 'rasa'"** – Activate the virtual environment again and make sure Rasa is installed (`pip install rasa-pro`).
- **"RASA_LICENSE" or "OPENAI_API_KEY" not set** – Create or edit `.env` in the `level1` folder with both variables (no quotes around the values). Restart the terminal and run `rasa inspect` again from `level1`.
- **"Address already in use" or port 5005 in use** – Another program is using port 5005. Close other Rasa or Python processes, or use a different port: `python -m rasa inspect --debug --port 5006` and then open **http://localhost:5006** (or …/inspect.html on 5006) in your browser.

---

### Lab 6.2: Using Rasa Inspector

**Objective**: Start Inspector and test a simple conversation.

#### Steps

1. **Open a terminal and get ready**
   - Click **Tools** → **Terminal** (or open your predefined terminal tab).
   - Ensure you're in the `level1` folder with the virtual environment active (run `cd level1` and `source .venv/bin/activate` if needed; your prompt should show `(.venv)`).

2. **Start Inspector in the terminal**
   ```bash
   python -m rasa inspect --debug --log-file logs/logs.out
   ```
   Wait until you see a line like "Starting Rasa server on http://0.0.0.0:5005". **Leave the terminal open.**

3. **Open Inspector in your browser**
   - Open the **Ports** view: **Tools** → **Ports**, or the **Preview** menu, or a **Ports** tab at the bottom of the window (see section 6.3 Step 3 for more options).
   - Find **port 5005** in the list and click its URL (or "Open in browser").
   - Inspector opens in a new browser tab—you should see a chat interface.

4. **Test a simple conversation**
   - In the Inspector chat window, type **hello** and press Enter.
   - The bot should respond.
   - Check that the correct flow triggered (e.g. in the debug/flow panel if visible).

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

**⏱️ Total Estimated Time**: 2-3 hours

**📋 IMPORTANT: Add Guide Content First**

**Before creating assessments**, add the student-facing content to Codio's Guide Editor:
- **Add Main Unit Content**: Copy content from `## For Students` (line 5491) to before `### Lab 6.1` (line 5735). See "Adding Guide Content to Codio" section above.
- **Add Lab Content**: Use Step 0.5 sections for Labs 6.1, 6.2, 6.3 (see below).
- **⏱️ Estimated Time**: 30-40 minutes (main content + 3 labs)

**💡 Time-Saving Tip**: Lab 6.3 (API testing) is most complex. Use Template 2 (Bash) for Lab 6.1. Lab 6.2 is very simple (just command check).

### Lab 6.1: Training Your Bot

**Type**: Hands-On Lab with Auto-Grading

**⏱️ Estimated Time**: 45 minutes

**💡 Time-Saving Tip**: Use Template 2 (Bash File Checker). Modify to check for model files instead of YAML files. Simple file/directory checks.

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Explain what training does
- Show command: `python -m rasa train`

#### Step 0.5: Add Lab 6.1 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 6.1 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 6.1 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 6 content to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 6 Section**: Click on **Unit 6: Training and Testing** in the left sidebar

3. **Add Lab 6.1 Subsection**: Scroll down in Unit 6's content area and click where you want Lab 6.1 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 6.1 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 6.1**:

⬇️ START COPYING HERE ⬇️

# Lab 6.1: Training Your Bot

**Objective**: Train your bot and verify it works.

---

## Part 1: In Codio

**1. In the terminal, go to the project folder**
- In Codio, click **Tools** → **Terminal** (or use the terminal icon).
- Navigate to the `level1` folder where your bot files live:
  ```bash
  cd level1
  ```
- Confirm you're in the right place: run `pwd` — you should see something like `/home/codio/workspace/level1`.

**2. Create and activate the virtual environment**
- Check if a virtual environment already exists:
  ```bash
  ls -la .venv
  ```
- **If `.venv` exists**: Activate it:
  ```bash
  source .venv/bin/activate
  ```
- **If `.venv` doesn't exist**: Create it first, then activate:
  ```bash
  python3.11 -m venv .venv
  source .venv/bin/activate
  ```
- **Verify activation**: Your prompt should start with `(.venv)`. If not, run `source .venv/bin/activate` again.
- **Note**: Rasa loads your `.env` when you run from `level1/`, so being in this folder with venv active is required.

**3. Install Rasa Pro (if not already installed)**
- With the venv active, check if Rasa is installed:
  ```bash
  python -m rasa --version
  ```
- **If you see an error** (e.g., "No module named 'rasa'"): Install Rasa Pro:
  ```bash
  python -m pip install --no-cache-dir rasa-pro
  ```
- Wait for installation to complete (2-5 minutes). You should see "Successfully installed rasa-pro-x.x.x" at the end.

**4. Run the training command**
- From the `level1` folder (with venv active), run:
  ```bash
  python -m rasa train
  ```
- Wait for training to complete (usually 1–3 minutes). Do not close the terminal until you see "Successfully saved model" or an error.

**5. What you'll see**
- When training starts, output will look like:
  ```
  Training Core model...
  2025-01-12 12:08:17 INFO     rasa.core.training  - Training FlowPolicy...
  2025-01-12 12:08:17 INFO     rasa.core.training  - FlowPolicy training completed.
  2025-01-12 12:08:17 INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'.
  ```
- **"Training Core model"**: Building the conversation logic  
- **"Training FlowPolicy"**: Processing your flows  
- **"Successfully saved model"**: Training completed, model saved

**6. Verify success**
- The terminal shows **"Successfully saved model to 'models/...'"** and there are no error messages at the end.
- In the file tree, open `level1/models/` — you should see a new `.tar.gz` file with a timestamp (e.g. `20250112-120817-descent-lard.tar.gz`).
- If `models/` is empty or there's no new file, training did not complete; see **Common training errors** below, fix the issue, and run the command again.

**7. Common training errors (Codio)**

| Error | What to do |
|-------|------------|
| **YAML syntax error** (e.g. "block mapping", line/column given) | Check that line: use **2 spaces** (not tabs, not 4 spaces), colons after keys, dashes before list items. Fix and save, then train again. |
| **Response 'utter_xyz' not found** | The flow uses a response that isn't in `domain/basics.yml`. Add the response in the domain or fix the typo in the flow so the name matches exactly. |
| **No module named 'rasa'** | Venv not active or Rasa not installed. Run `source .venv/bin/activate`, then `rasa --version`. If it fails, install Rasa Pro: `python -m pip install --no-cache-dir rasa-pro`. |
| **RASA_LICENSE / OPENAI_API_KEY not set** | Credentials are pre-configured on Codio. Run the verification commands from Lab 0.1 step 5; if they report "is not set", ask your instructor. Otherwise run training from the `level1/` folder. |

**AI Coach**: Ask "How do I know training succeeded?" or "What should I see when training works?"

---

## Part 2: Running locally

If you're **not** using Codio, follow these steps:

**1. Open a terminal and go to the project folder**
- Open a terminal (PowerShell on Windows, Terminal.app on Mac, or Terminal on Linux).
- Navigate to your project root, then `cd level1` (or whatever folder contains `config.yml`, `domain/`, `data/`).
- Confirm you're in the right place: check that `config.yml` exists in the current directory.

**2. Create and activate the virtual environment**
- Check if a virtual environment already exists:
  - Linux/Mac: `ls -la .venv`
  - Windows: `dir .venv` (PowerShell) or `dir .venv` (Cmd)
- **If `.venv` exists**: Activate it:
  - Linux/Mac: `source .venv/bin/activate`
  - Windows PowerShell: `.venv\Scripts\Activate.ps1`
  - Windows Cmd: `.venv\Scripts\activate.bat`
- **If `.venv` doesn't exist**: Create it first, then activate:
  - Linux/Mac: `python3.11 -m venv .venv` then `source .venv/bin/activate`
  - Windows: `python -m venv .venv` then `.venv\Scripts\Activate.ps1` (PowerShell) or `.venv\Scripts\activate.bat` (Cmd)
- **Verify activation**: Your prompt should start with `(.venv)`. If not, activate it again.

**3. Install Rasa Pro (if not already installed)**
- With the venv active, check if Rasa is installed:
  ```bash
  python -m rasa --version
  ```
- **If you see an error** (e.g., "No module named 'rasa'"): Install Rasa Pro:
  ```bash
  python -m pip install --no-cache-dir rasa-pro
  ```
- Wait for installation to complete (2-5 minutes). You should see "Successfully installed rasa-pro-x.x.x" at the end.

**4. Set up environment variables**
- Rasa loads `.env` from the current directory. Create a `.env` file in the same folder as `config.yml` with:
  ```
  RASA_LICENSE=your-actual-license
  OPENAI_API_KEY=sk-your-actual-key
  ```
- **Important**: No quotes around values; no placeholder values. If you see "RASA_LICENSE not set" or "OPENAI_API_KEY not found", check that `.env` exists, has the right variable names, and you're running `rasa train` from that folder.

**5. Run the training command**
- From the project folder (with venv active), run:
  ```bash
  python -m rasa train
  ```
- Wait for training to complete (usually 1–3 minutes). Do not close the terminal until you see "Successfully saved model" or an error.

**6. What you'll see**
- When training starts, output will look like:
  ```
  Training Core model...
  2025-01-12 12:08:17 INFO     rasa.core.training  - Training FlowPolicy...
  2025-01-12 12:08:17 INFO     rasa.core.training  - FlowPolicy training completed.
  2025-01-12 12:08:17 INFO     rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'.
  ```
- **"Training Core model"**: Building the conversation logic  
- **"Training FlowPolicy"**: Processing your flows  
- **"Successfully saved model"**: Training completed, model saved

**7. Verify success**
- The terminal shows **"Successfully saved model to 'models/...'"** and there are no error messages at the end.
- Check the `models/` folder — you should see a new `.tar.gz` file with a timestamp (e.g. `20250112-120817-descent-lard.tar.gz`).
- If `models/` is empty or there's no new file, training did not complete; check error messages and fix the issue, then run the command again.

**8. Common training errors (local)**

| Error | What to do |
|-------|------------|
| **YAML syntax error** (e.g. "block mapping", line/column given) | Check that line: use **2 spaces** (not tabs, not 4 spaces), colons after keys, dashes before list items. Fix and save, then train again. |
| **Response 'utter_xyz' not found** | The flow uses a response that isn't in `domain/basics.yml`. Add the response in the domain or fix the typo in the flow so the name matches exactly. |
| **No module named 'rasa'** | Venv not active or Rasa not installed. Activate the venv, then run `python -m pip install --no-cache-dir rasa-pro`. |
| **RASA_LICENSE / OPENAI_API_KEY not set** | Create a `.env` file in the same folder as `config.yml` with `RASA_LICENSE=...` and `OPENAI_API_KEY=...` (no quotes, no placeholders). Make sure you're running `rasa train` from that folder. |

**AI Coach**: Ask "Where do I put my Rasa license?" or "How do I set environment variables?"

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 6.1. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 6.1 Assessment (Code Test)

## Step-by-Step: Lab 6.1 Assessment Setup

### Step 1: Navigate to Lab 6.1 in Codio Guides

1. Open your Codio project.
2. Go to **Tools** → **Guides** → **Edit**.
3. Find the **Lab 6.1: Training Your Bot** subsection.
4. Scroll to the bottom of that subsection (after the student content).

### Step 2: Create the Code Test Assessment

1. Click the **+** button at the bottom of the Lab 6.1 subsection.
2. Select **Code Test** from the assessment types.

### Step 3: Paste the Grader Script

In the code editor box, paste this grader script:

```bash
#!/bin/bash
set -e
cd /home/codio/workspace/level1

score=0
max_score=10

echo "Running Lab 6.1 Assessment Checks..."
echo ""

# Check 0: Virtual environment exists and is activated (2 points)
echo "Check 0: Verifying virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ Check 0: FAILED - Virtual environment (.venv) not found (0 points)"
    echo "Hint: Create virtual environment with 'python3.11 -m venv .venv'"
    exit 1
fi

# Activate venv for checks
source .venv/bin/activate
echo "✅ Check 0: PASSED - Virtual environment found and activated (2 points)"
score=$((score + 2))
echo ""

# Check 1: Model file exists (2 points)
echo "Check 1: Verifying model file exists..."
if [ -d "models" ] && [ -n "$(ls -A models/*.tar.gz 2>/dev/null)" ]; then
    echo "✅ Check 1: PASSED - Model file created (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 1: FAILED - No model file found in models/ directory (0 points)"
    echo "Hint: Run 'python3.11 -m rasa train' (with venv activated) to create the model"
    exit 1
fi
echo ""

# Check 2: Training completed successfully (check for recent model)
echo "Check 2: Verifying model is recent..."
model_file=$(ls -t models/*.tar.gz 2>/dev/null | head -1)
if [ -z "$model_file" ]; then
    echo "❌ Check 2: FAILED - No model files found (0 points)"
    exit 1
fi

# Check model is recent (created in last 10 minutes)
if [ -f "$model_file" ]; then
    model_age=$(( $(date +%s) - $(stat -c %Y "$model_file") ))
    if [ $model_age -lt 600 ]; then
        echo "✅ Check 2: PASSED - Model file is recent (training completed within 10 minutes) (3 points)"
        score=$((score + 3))
    else
        echo "⚠️  WARNING: Model file is old. Re-run training to ensure it's current."
        echo "⚠️  Check 2: PARTIAL - Model exists but is older than 10 minutes (0 points)"
    fi
fi
echo ""

# Check 3: No obvious errors (check for common error patterns in logs if available)
echo "Check 3: Checking for errors in logs..."
if [ -f "logs/logs.out" ]; then
    if grep -qi "error\|exception\|failed" logs/logs.out 2>/dev/null; then
        echo "⚠️  WARNING: Possible errors found in logs. Review logs/logs.out"
        echo "⚠️  Check 3: PARTIAL - Logs found but may contain errors (0 points)"
    else
        echo "✅ Check 3: PASSED - No obvious errors in logs (3 points)"
        score=$((score + 3))
    fi
else
    echo "✅ Check 3: PASSED - No log file found (training may not have logged) (3 points)"
    score=$((score + 3))  # Give points if no log file (training might not have logged)
fi
echo ""

# Check 4: Training time reasonable (model exists = training completed)
echo "Check 4: Verifying training completed successfully..."
echo "✅ Check 4: PASSED - Training completed successfully (2 points)"
score=$((score + 2))
echo ""

# Final summary
echo "=========================================="
echo "✅ PASS: Training verification complete! Score: $score/$max_score"
echo "=========================================="
echo ""
echo "Summary of checks:"
echo "✓ Check 0: Virtual environment exists and activated"
echo "✓ Check 1: Model file created"
echo "✓ Check 2: Model file is recent"
echo "✓ Check 3: No critical errors detected"
echo "✓ Check 4: Training completed successfully"
echo ""
echo "✅ PASS: Training verification complete! Score: $score/$max_score"
```

**What the script checks:**
- ✅ Virtual environment exists (`.venv` directory)
- ✅ Model file exists (`.tar.gz` in `models/`)
- ✅ Model is recent (created within last 10 minutes)
- ✅ No obvious errors in logs (if logs exist)
- ✅ Training completed successfully

### Step 4: Configure Assessment Settings

Set these fields:

- **Points**: `10`
- **Timeout**: `60` seconds
- **Language**: **Bash**
- **Working Directory**: `/home/codio/workspace/level1` (if available)
- **Fail Message**: 
  ```
  Training incomplete. Ensure: 1) Virtual environment exists (.venv), 2) Run 'python3.11 -m rasa train' (with venv activated), 3) Wait for completion. Check for YAML syntax errors if training fails.
  ```

### Step 5: Save and Test

1. Click **Save**.
2. Test the assessment:
   - Complete Lab 6.1 steps (create venv, train bot).
   - Run the assessment.
   - Verify it passes when training is complete.

### Step 6: Enable Learning Analytics (Optional)

1. Click **Education** → **Analytics** → **Enable**.
2. Track: training attempts, completion time, error frequency.

### What Students Will See

When students click "Run Assessment" or "Submit":
- The grader checks if `.venv` exists (fails if missing).
- Checks if a model file exists in `models/`.
- Verifies the model is recent (within 10 minutes).
- Provides hints if checks fail.

### Important Notes

1. **Virtual Environment**: The grader activates the venv itself, so students don't need to activate it before running the assessment.
2. **Python Version**: The script uses `python3.11` to match Codio's Python version.
3. **Recency Check**: The 10-minute recency check ensures students ran training recently, not just copied an old model.
4. **Early Exit**: The script exits early if critical checks fail (no venv, no model), so students get immediate feedback.

This setup verifies that students:
- ✅ Created the virtual environment
- ✅ Successfully ran training
- ✅ Generated a model file
- ✅ Completed the lab correctly

### Lab 6.2: Using Rasa Inspector

**Type**: Guided Exercise

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Explain what Rasa Inspector is
- Show how to start it

#### Step 0.5: Add Lab 6.2 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 6.2 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 6.2 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 6 content and Lab 6.1 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 6 Section**: Click on **Unit 6: Training and Testing** in the left sidebar

3. **Add Lab 6.2 Subsection**: Scroll down in Unit 6's content area to find where Lab 6.1 ends, then click where you want Lab 6.2 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 6.2 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 6.2**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 6.2. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Configure Rasa Inspector Access

**What you're doing**: Setting up Inspector so students can access it in Codio.

**How to do it**:

1. **Configure port forwarding for Rasa Inspector** (Saves 15-30 min of confusion):

   **📖 Why This Matters**: Rasa Inspector runs on port 5005. Students need to access it in a browser. Codio must expose this port so the Inspector URL works.

   **Step-by-Step (Codio-Specific)**:
   
   a. **Find Port Forwarding Settings**:
      - **Option A**: In your Codio project, look for **Tools** → **Ports** (or **Port Forwarding**) in the top menu
      - **Option B**: Look for a **"Ports"** tab or panel—often in the bottom area or right sidebar when the project is open
      - **Option C**: Click **Project** → **Settings** (or gear icon) → look for **Ports** or **Port Forwarding**
      - **Expected**: You'll see a list of ports and a way to add/expose ports
   
   b. **Add Port 5005**:
      - Click **Add Port** or **+** (or similar)
      - Enter port number: `5005`
      - **Port Type**: Select **Public** or **Open** (so students can access via URL)
      - **Description** (optional): "Rasa Inspector"
      - Save
   
   c. **Get the Inspector URL**:
      - After adding port 5005, Codio shows a URL (e.g., `https://xxx-5005.codio.io` or similar)
      - **Copy this URL**—students will use it to access Inspector
      - Add this URL to the guide instructions for Lab 6.2
   
   d. **Verify**:
      - Start Inspector: `python3.11 -m rasa inspect --debug --log-file logs/logs.out`
      - Open the Codio-provided URL in a browser (or use Codio's "Open in Browser" link for port 5005)
      - **Expected**: You see the Inspector chat interface
   
   **⚠️ If You Can't Find Port Forwarding**: Codio UI varies. Try: **Tools** → **Ports**; or **Project** → **Settings** → **Ports**. Check Codio docs: https://docs.codio.com for "port forwarding" or "ports".

2. **Add Lab 6.2 assessment** (simple check):
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 6.2: Using Rasa Inspector** subsection
   - Click **+** → Select **Code Test**

3. **Paste simple checker**:
   ```bash
   #!/bin/bash
   # Check if Inspector can be started (verify command works)
   cd /home/codio/workspace/level1
   
   if python3.11 -m rasa inspect --help > /dev/null 2>&1; then
       echo "✅ PASS: Rasa Inspector command is available"
       echo "Start Inspector with: python3.11 -m rasa inspect --debug --log-file logs/logs.out"
       echo "Then access it via the Codio port forwarding URL"
   else
       echo "❌ FAIL: Rasa Inspector not available. Check Rasa installation."
       exit 1
   fi
   ```

4. **Configure assessment**:
   - **Points**: `5`
   - **Timeout**: `20` seconds
   - **Fail Message**: `Verify Rasa is installed: python3.11 -m rasa --version`
   - Click **Save**

5. **Enable Code Playback**:
   - Click **Education** → **Monitoring** → **Code Playback**
   - Track terminal commands and Inspector usage

**Deliverables Checklist**:
- [ ] Port forwarding configured for Inspector
- [ ] Lab 6.2 assessment created (command availability check)
- [ ] Code Playback enabled
- [ ] Instructions provided for accessing Inspector URL

### Lab 6.3: Testing Your Bot

**Type**: Hands-On Lab with Auto-Grading (Rubric-based)

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Objective: Test all three flows (greet, help, contact)
- Explain testing process

#### Step 0.5: Add Lab 6.3 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 6.3 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 6.3 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 6 content, Lab 6.1, and Lab 6.2 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 6 Section**: Click on **Unit 6: Training and Testing** in the left sidebar

3. **Add Lab 6.3 Subsection**: Scroll down in Unit 6's content area to find where Lab 6.2 ends, then click where you want Lab 6.3 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 6.3 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 6.3**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 6.3. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

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

**⏱️ Estimated Time**: 1-1.5 hours (requires API testing)

**💡 Time-Saving Tip**: This is the only assessment that requires Rasa server to be running. Test it last, after server is configured. The script handles connection errors gracefully.

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Objective: Test all three flows (greet, help, contact)
- Explain testing process

#### Step 1: Create Lab 6.3 Assessment (Bot Testing Script)

**💡 Time-Saving Tip**: The Python script below includes error handling for server not running. Copy it exactly - it's ready to use.

**What you're doing**: Creating a Code Test that programmatically tests the bot via Rasa API to verify flows trigger correctly.

**⚠️ Why Advanced Code Test (Python Script) is Appropriate Here**:

This is one of the **rare cases** where a Python script is necessary and appropriate:

- **Requires HTTP requests**: Must make POST requests to Rasa's REST API (`http://localhost:5005/webhooks/rest/webhook`)
- **JSON parsing**: Needs to parse JSON responses and check specific fields (e.g., `text`, `response`)
- **Error handling**: Must handle cases where the server isn't running or returns errors
- **Complex validation**: Checks multiple flows (greet, help, contact) with different test messages

**This is NOT a case where LLM Rubric or Standard Code Test would work**:
- ❌ **LLM Rubric**: Can't make HTTP requests or test live API endpoints
- ❌ **Standard Code Test**: Can't handle JSON parsing, multiple API calls, or complex conditional logic

**✅ This matches Codio's guidance**: Advanced Code Test is designed for exactly this type of scenario (API testing, complex validation logic). See "Assessment Type 2: Advanced Code Test" section above for when to use it.

**How to do it**:

1. **Navigate to Lab 6.3 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 6.3: Testing Your Bot** subsection
   - Scroll to bottom

2. **Add Code Test assessment**:
   - Click **+** → Select **Code Test**

3. **Paste grader script** (Python - tests bot via API):
   ```python
   #!/usr/bin/env python3
   """
   Lab 6.3 Grader: Tests bot flows via Rasa API
   Checks: greet, help, contact flows trigger correctly
   """
   import requests
   import json
   import sys
   import time
   import subprocess
   from pathlib import Path
   
   def start_rasa_server():
       """Start Rasa server in background if not running."""
       # Check if server is already running
       try:
           requests.get("http://localhost:5005/status", timeout=2)
           return True  # Server already running
       except:
           pass
       
       # Start server (in background - Codio may handle this differently)
       # For Codio, students should start server manually
       print("⚠️  NOTE: Ensure Rasa server is running: python3.11 -m rasa run --enable-api")
       return False
   
   def test_flow(sender_id, message, expected_flow_keywords=None):
       """Send message to bot and check response."""
       url = "http://localhost:5005/webhooks/rest/webhook"
       payload = {
           "sender": sender_id,
           "message": message
       }
       
       try:
           response = requests.post(url, json=payload, timeout=10)
           if response.status_code != 200:
               return False, f"HTTP {response.status_code}"
           
           data = response.json()
           if not data or len(data) == 0:
               return False, "No response from bot"
           
           # Check response text contains expected content
           response_text = " ".join([item.get("text", "") for item in data]).lower()
           return True, response_text
       except requests.exceptions.ConnectionError:
           return False, "Cannot connect to Rasa server. Start it with: python3.11 -m rasa run --enable-api"
       except Exception as e:
           return False, str(e)
   
   def main():
       score = 0
       max_score = 10
       
       # Check if model exists
       model_dir = Path("/home/codio/workspace/level1/models")
       if not model_dir.exists() or not list(model_dir.glob("*.tar.gz")):
           print("❌ FAIL: No trained model found. Complete Lab 6.1 first (run: python3.11 -m rasa train)")
           sys.exit(1)
       
       # Check server is running
       try:
           requests.get("http://localhost:5005/status", timeout=2)
       except:
           print("❌ FAIL: Rasa server not running.")
           print("Start it with: python3.11 -m rasa run --enable-api")
           print("Then run this assessment again.")
           sys.exit(1)
       
       # Test 1: Greet flow (2 points)
       print("Testing greet flow...")
       success, result = test_flow("test_user_1", "hello")
       if success and ("greet" in result or "help" in result or "banking" in result):
           print("✓ Greet flow works")
           score += 2
       else:
           print(f"❌ Greet flow failed: {result}")
       
       # Test 2: Help flow (2 points)
       print("Testing help flow...")
       success, result = test_flow("test_user_2", "what can you do")
       if success and ("help" in result or "balance" in result or "transfer" in result):
           print("✓ Help flow works")
           score += 2
       else:
           print(f"❌ Help flow failed: {result}")
       
       # Test 3: Contact flow (2 points)
       print("Testing contact flow...")
       success, result = test_flow("test_user_3", "how do I contact you")
       if success and ("contact" in result or "email" in result or "support" in result or "call" in result):
           print("✓ Contact flow works")
           score += 2
       else:
           print(f"❌ Contact flow failed: {result}")
       
       # Test 4: Bot responds (3 points)
       if score >= 4:  # At least 2 flows work
           print("✓ Bot responds correctly")
           score += 3
       
       # Test 5: All flows independent (1 point)
       if score >= 9:
           print("✓ All flows work independently")
           score += 1
       
       if score >= 7:
           print(f"✅ PASS: Bot testing complete! Score: {score}/{max_score}")
       else:
           print(f"❌ FAIL: Bot testing incomplete. Score: {score}/{max_score}")
           print("Check flow descriptions and ensure bot is trained and running.")
           sys.exit(1)
   
   if __name__ == "__main__":
       main()
   ```

4. **Configure assessment**:
   - **Points**: `10`
   - **Timeout**: `120` seconds (API calls may take time)
   - **Language**: **Python 3**
   - **Prerequisites**: Note in instructions that students must start Rasa server first
   - **Fail Message**: `Bot testing failed. Ensure: 1) Bot is trained (Lab 6.1), 2) Rasa server is running (python3.11 -m rasa run --enable-api), 3) Flow descriptions are clear.`
   - Click **Save**

5. **Configure Virtual Coach**:
   - Add hints for common testing issues (see AI Coach Configuration in original)

**Deliverables Checklist**:
- [ ] Lab 6.3 Code Test created (API-based bot testing)
- [ ] Tests greet, help, contact flows
- [ ] Validates responses
- [ ] Virtual Coach configured with testing hints
- [ ] Assessment tested (requires running Rasa server)

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

**📋 IMPORTANT: Add Guide Content First**

**Before creating assessments**, add the student-facing content to Codio's Guide Editor:
- **Add Main Unit Content**: Copy content from `## For Students` (line 6606) to before `### Lab 7.1` (line 6696). See "Adding Guide Content to Codio" section above.
- **Add Lab Content**: Use Step 0.5 sections for Labs 7.1, 7.2 (see below). Lab 7.3 has been removed from the course.
- **⏱️ Estimated Time**: 30-40 minutes (main content + 3 labs)

### Lab 7.1: Complete Bot Walkthrough

**Type**: Guided Demonstration

#### Step 0.5: Add Lab 7.1 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 7.1 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 7.1 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 7 content to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 7 Section**: Click on **Unit 7: Putting It All Together** in the left sidebar

3. **Add Lab 7.1 Subsection**: Scroll down in Unit 7's content area and click where you want Lab 7.1 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 7.1 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 7.1**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 7.1. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

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

#### Step 0.5: Add Lab 7.2 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 7.2 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 7.2 student-facing content to Codio's Guide Editor so students can see the project instructions.

**🔍 Before You Start**: Make sure you've added Unit 7 content and Lab 7.1 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 7 Section**: Click on **Unit 7: Putting It All Together** in the left sidebar

3. **Add Lab 7.2 Subsection**: Scroll down in Unit 7's content area to find where Lab 7.1 ends, then click where you want Lab 7.2 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 7.2 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 7.2**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 7.2. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

#### Step 1: Create Lab 7.2 Comprehensive Assessment Using LLM Rubric Autograde

**⏱️ Estimated Time**: 15-20 minutes (reduced from 1-1.5 hours using LLM Rubric instead of custom Python script)

**💡 Time-Saving Tip**: Using LLM Rubric Autograde saves 45-70 minutes vs. writing a comprehensive custom Python script. No coding required!

**📖 Assessment Type**: **LLM Rubric Autograde** (see "Codio Native Assessment Features Guide" above for details)

**What you're doing**: Creating an LLM Rubric assessment that validates students created a complete new feature (new response + new flow) using AI-powered grading.

**How to do it**:

1. **Navigate to Lab 7.2 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Lab 7.2: Build Your Own Feature** subsection
   - Scroll to bottom

2. **Add LLM Rubric Assessment**:
   - Click **`+`** button
   - Select **"LLM Rubric"** or **"Autograde"** from dropdown

3. **Configure the Assessment**:

   **a. Assessment Instructions**:
   - **What to type**:
     ```
     Create a complete new feature for your banking bot by:
     1. Adding a new response to domain/basics.yml (e.g., utter_account_info, utter_transfer_help, etc.)
     2. Creating a new flow file in data/basics/ that uses this new response
     3. Ensuring the flow has proper structure (name, description, steps)
     4. Following best practices (descriptive description, rephrase metadata)
     
     The new feature should be different from existing features (greet, help, contact, goodbye).
     ```

   **b. Rubric/Requirements** (Be very specific - this is a comprehensive project):
   - **What to type**:
     ```
     Requirements Checklist (all must be met):
     
     1. New Response Created:
        - A new response exists in domain/basics.yml
        - Response name is different from existing responses (utter_greet, utter_help, utter_contact, utter_goodbye)
        - Response follows naming convention (starts with "utter_")
        - Response has proper structure (list with at least one text item)
        - Response text is non-empty and meaningful
        - File domain/basics.yml is valid YAML (no syntax errors)
     
     2. New Flow Created:
        - A new flow file exists in data/basics/ directory
        - Flow file name is different from existing flows (greet.yml, help.yml, contact.yml, goodbye.yml)
        - Flow file is valid YAML (no syntax errors)
        - Flow file contains a flows: section
        - Flow has a name (under flows: section, e.g., "account_info", "transfer_help")
     
     3. Flow Structure:
        - Flow has a "name" field (non-empty)
        - Flow has a "description" field (non-empty, descriptive text explaining when flow triggers)
        - Flow has a "steps" section (list of actions)
        - Steps section contains at least one action
        - All fields are properly indented (2 spaces per level)
     
     4. Flow References Response:
        - Flow's steps section references the new response created in step 1
        - Action format is correct: "- action: utter_X" (where X matches new response name)
        - Action is properly indented (6 spaces from left margin)
     
     5. Best Practices:
        - Flow description is descriptive (explains when/why flow triggers, >20 characters)
        - Response includes metadata with rephrase: True (if applicable)
        - Code follows YAML conventions (proper indentation, no tabs)
     
     6. File Locations:
        - New response is in /home/codio/workspace/level1/domain/basics.yml
        - New flow file is in /home/codio/workspace/level1/data/basics/
        - All files are valid YAML
     
     Grading: Award full points (14) if all requirements are met. Deduct points for each missing requirement.
     Partial credit may be awarded for incomplete features (e.g., response exists but flow missing, or vice versa).
     ```

   **c. Solution File**: `/home/codio/workspace/level1/domain/basics.yml` (and example flow file if available)

   **d. Files to Check**: 
   - `/home/codio/workspace/level1/domain/basics.yml`
   - `/home/codio/workspace/level1/data/basics/*.yml` (or list specific new flow file if known)

   **e. Guide Content Context**: Copy Lab 7.2 instructions from guide (student-facing project description)

   **f. Points**: `14`

   **g. Timeout**: `90` (seconds - comprehensive check may take longer)

4. **Save the Assessment**: Click **Save** button

5. **Enable Code Playback** (Recommended for project review):
   - Click **Education** → **Monitoring** → **Code Playback**
   - Track: `domain/basics.yml`, `data/basics/*.yml`
   - **Purpose**: Allows instructors to review how students created the feature

6. **Test the Assessment**:
   - Test with complete feature (new response + new flow) - should pass
   - Test with only new response (no flow) - should fail with specific feedback
   - Test with only new flow (no new response) - should fail with specific feedback
   - Test with incorrect structure - should fail with specific feedback

**Deliverables Checklist**:
- [ ] Lab 7.2 Code Test created (comprehensive feature validation)
- [ ] Validates response, flow, training, best practices
- [ ] Code Playback enabled for full review
- [ ] Virtual Coach available for project help
- [ ] Assessment tested

### Lab 7.3: Best Practices Application — REMOVED

**Note:** Lab 7.3 has been removed from Level 1. Do not add it to Codio. The section below is retained for reference only.

**Type**: Auto-Graded Exercise (lab removed; skip)

**Content Structure**:
- Brief instructions (preserved from TUTORIAL.md)
- Explain best practices learned
- Objective: Apply to existing code

#### Step 0.5: Add Lab 7.3 Guide Content to Codio

**⏱️ Estimated Time**: 5-10 minutes

**🎯 Purpose**: Before creating assessments, you need to add the student-facing content to Codio's Guide Editor. This step shows you exactly what Markdown to copy and paste.

**📋 Checkpoint**: After completing this step, Lab 7.3 content should be visible in Codio's Guide Editor and render correctly in Preview mode.

**What you're doing**: Adding the Lab 7.3 student-facing content to Codio's Guide Editor so students can see the instructions.

**🔍 Before You Start**: Make sure you've added Unit 7 content, Lab 7.1, and Lab 7.2 to Codio's Guide Editor. You should have Codio open with your project loaded.

**How to do it**:

1. **Open Codio's Guide Editor**: Click **Tools** → **Guides** → **Edit**

2. **Find Unit 7 Section**: Click on **Unit 7: Putting It All Together** in the left sidebar

3. **Add Lab 7.3 Subsection**: Scroll down in Unit 7's content area to find where Lab 7.2 ends, then click where you want Lab 7.3 to appear

4. **Copy and Paste the Markdown Content**: Select ALL the text in the code block below, copy it (Ctrl+C / Cmd+C), and paste it into Codio's Guide Editor (Ctrl+V / Cmd+V)

5. **Verify the Content**: Check formatting, save (Ctrl+S / Cmd+S), and preview to ensure it renders correctly

**✅ Checkpoint**: Lab 7.3 content is visible in Codio's Guide Editor, saved, and renders correctly in Preview mode.

**📋 Copy This Markdown for Lab 7.3**:

⬇️ START COPYING HERE ⬇️

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

⬆️ STOP COPYING HERE ⬆️

---

**✅ Step 0.5 Complete**: You've copied the student-facing content for Lab 7.3. The content between the visual markers above contains ONLY what students will see in Codio.

**⚠️ IMPORTANT**: The troubleshooting tips below are for YOU (the implementer), NOT for students. Do NOT copy them to Codio.

**💡 Troubleshooting for Implementers** (Do NOT copy to Codio):
- **If content doesn't paste**: Make sure you're in Edit mode (not Preview mode) in Codio's Guide Editor
- **If formatting looks wrong**: Codio uses Markdown - the content above is already formatted correctly. Try refreshing Preview mode
- **If code blocks don't render**: Check that the triple backticks (```) are preserved when pasting

---

## 🎯 FOR IMPLEMENTERS ONLY: Assessment Creation Steps

**The steps below are for creating assessments in Codio. Students will NOT see these instructions.**

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

**⏱️ Total Estimated Time**: 1.5-2 hours

**📋 IMPORTANT: Add Guide Content First**

**Before creating assessments**, add the student-facing content to Codio's Guide Editor:
- **Add Main Unit Content**: Copy content from `## For Students` (line 7203) to before `## For Codio Team` (line 7432). See "Adding Guide Content to Codio" section above.
- **⏱️ Estimated Time**: 10-15 minutes (main content only - no labs in Unit 8)

**💡 Time-Saving Tip**: Knowledge Check = batch create 10-15 multiple choice (Template 3). Practical Exercise = copy Lab 7.2 and make stricter. Code Review = manual setup only.

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

#### Step 1: Create Final Knowledge Check Assessment

**⏱️ Estimated Time**: 45-60 minutes (or 30-40 min with Duplicate + AI Generate)

**💡 Time-Saving Tip**: Create all 10-15 questions in ONE batch session using **Duplicate** and **AI Generate**:
1. Create **first** question (manually or with AI Generate from guide content)
2. Click **Duplicate and Save** 9-14 times
3. Edit each copy: change question text, options, correct answer only—structure stays the same
4. Saves 30-45 minutes vs. creating each question from scratch

**What you're doing**: Creating a comprehensive multiple-choice quiz covering all Level 1 concepts.

**How to do it**:

1. **Navigate to Unit 8 in Guides**:
   - Click **Tools** → **Guides** → **Edit**
   - Find **Unit 8 – Final Assessment** section
   - Find **Knowledge Check** subsection

2. **Create Multiple Choice assessment**:
   - Click **+** → Select **Multiple Choice** (or **Quiz**)
   - Add 10-15 questions covering:
     - Domain files (responses, YAML structure)
     - Flows (structure, descriptions, steps)
     - System patterns (session_start, completed)
     - Config files (config.yml, credentials.yml, endpoints.yml)
     - Training and testing
   
   **Sample questions** (create similar ones):
   - "What is the purpose of the domain file?" → "Defines what the bot can say (responses)"
   - "Why is the flow description field critical?" → "LLM uses it to match user messages"
   - "When does pattern_session_start trigger?" → "When a new conversation starts"
   - "What does 'rephrase: True' do?" → "Allows LLM to rephrase response text"
   - "What command trains the bot?" → "python -m rasa train"
   - (Add 5-10 more questions covering all units)

3. **Configure assessment**:
   - **Total Points**: `20`
   - **Passing Score**: `14` (70%)
   - **Show explanations**: ✓
   - **Allow multiple attempts**: Optional (recommend max 2)
   - **Randomize question order**: ✓ (if available)
   - Click **Save**

#### Step 2: Create Final Practical Exercise Assessment

**What you're doing**: Creating a stricter version of Lab 7.2 for final assessment.

**How to do it**:

1. **Navigate to Practical Exercise subsection**:
   - In Unit 8, find **Practical Exercise** subsection
   - Scroll to bottom

2. **Add Code Test assessment** (similar to Lab 7.2 but stricter):
   - Click **+** → Select **Code Test**
   - Use similar grader script as Lab 7.2, but:
     - Require descriptive flow description (min 30 chars)
     - Require rephrase metadata
     - Require successful training
     - Can add API testing requirement (flow actually works)

3. **Configure assessment**:
   - **Points**: `20`
   - **Timeout**: `120` seconds
   - **Strict mode**: Enable (no partial credit for incomplete work)
   - Click **Save**

#### Step 3: Configure Code Playback for Code Review

**What you're doing**: Setting up Code Playback so instructors can review student work.

**How to do it**:

1. **Enable Code Playback**:
   - Click **Education** → **Monitoring** → **Code Playback**
   - Ensure it's enabled for Unit 8

2. **Track key files**:
   - `domain/basics.yml`
   - `data/basics/*.yml`
   - `data/system/patterns/patterns.yml`
   - `config.yml`, `credentials.yml`, `endpoints.yml`

3. **Create Code Review assignment** (manual grading):
   - In Codio, create a **Manual Grading** assignment
   - Instructors review Code Playback recordings
   - Provide rubric: Code quality (3), Best practices (3), Completeness (2), Documentation (2) = 10 points

**Deliverables Checklist**:
- [ ] Knowledge Check created (10-15 questions, 20 points)
- [ ] Practical Exercise created (stricter Lab 7.2, 20 points)
- [ ] Code Playback configured for review
- [ ] Manual grading assignment created (10 points)
- [ ] All assessments tested

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


<a id="implementation-overview"></a>
## Implementation Overview for Codio Team

### Executive Summary

This guide outlines how to implement the Level 1 Rasa Bot course as an interactive Codio experience with AI-enhanced learning, auto-grading, Code Playback, and AI Coach.

**Key Goals**:
- All educational content is in this guide (copy-paste ready)
- Convert hands-on exercises into auto-graded labs with immediate feedback
- Students create their own virtual environment and install Rasa Pro (Lab 0.1); project structure is pre-configured
- AI Coach provides real-time student support
- Use Code Playback for instructor review and student debugging
- Implement comprehensive analytics for learning insights

**Expected Outcomes** (based on Codio research):
- 2x higher completion rates
- 15% average grade improvement
- 70% faster time to first success
- 50% reduction in support tickets

### Content Integration Strategy

**All content is in this guide** (no separate TUTORIAL.md):
- Full conceptual explanations
- Complete step-by-step labs
- All examples, analogies, and code samples
- Glossary and troubleshooting (AI Coach handles real-time help)

**Exercises are labs**:
- Step-by-step tutorials → Hands-on labs with auto-grading
- Knowledge checks → Auto-graded assessments
- Verification steps → Auto-grading checks

**AI Coach replaces extensive troubleshooting text** for real-time student support.

---

<a id="technical-specifications"></a>
## Technical Specifications for Codio Team

### Lab Environment Configuration

**Base Environment Requirements**:
- Operating System: Linux (Ubuntu 22.04 or similar)
- Python: 3.11
- IDE: Browser-based VSCode (Codio standard)
- Terminal: Bash shell

**Pre-Installed / Student-Installed**:
```bash
# Pre-installed in Codio
python3.11
pip (latest version)
git

# Students install in Lab 0.1 (venv + Rasa Pro)
# python3.11 -m venv .venv && source .venv/bin/activate && pip install rasa-pro
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

<a id="quality-assurance"></a>
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

## 📋 APPENDIX: Consolidated Guide Content Reference

**📌 Reference Only**: This Appendix consolidates lookup tables for quick access. **Workflow instructions** (how to copy, where to paste) are in the main body—see [Adding Guide Content](#adding-guide-content). Use this section when you need to find content locations fast.

### How to Use This Appendix

1. **Main Unit Content**: Table below → search `# Unit X:` and `## For Students`
2. **Lab Content**: Table below → go to Step 0.5 for each lab
3. **Batch workflow**: See "Adding Guide Content" section (main body)

### Main Unit Content Locations

**Each unit's main content** (concepts, explanations, examples) is located between `## For Students` and the first lab heading.

**💡 Finding Content**: Use the search function (Ctrl+F / Cmd+F) in this guide to find `# Unit X:` or `## For Students` sections. Line numbers are approximate and may vary if the guide is updated.

| Unit | Content Starts At | Content Ends At | Estimated Time |
|------|-------------------|-----------------|----------------|
| 0 | Search: `# Unit 0:` → Find `## For Students` | Before `### Lab 0.1` | 10-15 min |
| 1 | Search: `# Unit 1:` → Find `## For Students` | Before `## For Codio Team` | 10-15 min |
| 2 | Search: `# Unit 2:` → Find `## For Students` | Before `### Lab 2.1` | 10-15 min |
| 3 | Search: `# Unit 3:` → Find `## For Students` | Before `### Lab 3.1` | 10-15 min |
| 4 | Search: `# Unit 4:` → Find `## For Students` | Before `### Lab 4.1` | 10-15 min |
| 5 | Search: `# Unit 5:` → Find `## For Students` | Before `### Lab 5.1` | 10-15 min |
| 6 | Search: `# Unit 6:` → Find `## For Students` | Before `### Lab 6.1` | 10-15 min |
| 7 | Search: `# Unit 7:` → Find `## For Students` | Before `### Lab 7.1` | 10-15 min |
| 8 | Search: `# Unit 8:` → Find `## For Students` | Before `## For Codio Team` | 10-15 min |

**How to copy**: Search `# Unit X:` → Find `## For Students` → Copy to (exclude) first `### Lab X.X:` → Paste into Codio Guide Editor.

### Lab Content Locations (Step 0.5 Sections)

**Each lab has explicit copy-paste Markdown in its Step 0.5 section:**

| Unit | Lab | Step 0.5 Section Location | Markdown Block Location |
|------|-----|---------------------------|-------------------------|
| 0 | 0.1 | Unit 0 → Step 1.5 | After "📋 Copy This Markdown for Lab 0.1" |
| 2 | 2.1 | Unit 2 → Lab 2.1 → Step 0.5 | After "📋 Copy This Markdown for Lab 2.1" |
| 2 | 2.2 | Unit 2 → Lab 2.2 → Step 0.5 | After "📋 Copy This Markdown for Lab 2.2" |
| 2 | 2.3 | Unit 2 → Lab 2.3 → Step 0.5 | After "📋 Copy This Markdown for Lab 2.3" |
| 3 | 3.1 | Unit 3 → Lab 3.1 → Step 0.5 | After "📋 Copy This Markdown for Lab 3.1" |
| 3 | 3.2 | Unit 3 → Lab 3.2 → Step 0.5 | After "📋 Copy This Markdown for Lab 3.2" |
| 3 | 3.3 | Unit 3 → Lab 3.3 → Step 0.5 | After "📋 Copy This Markdown for Lab 3.3" |
| 3 | 3.4 | Unit 3 → Lab 3.4 → Step 0.5 | After "📋 Copy This Markdown for Lab 3.4" |
| 4 | 4.1 | Unit 4 → Lab 4.1 → Step 0.5 | After "📋 Copy This Markdown for Lab 4.1" |
| 4 | 4.2 | Unit 4 → Lab 4.2 → Step 0.5 | After "📋 Copy This Markdown for Lab 4.2" |
| 5 | 5.1 | Unit 5 → Lab 5.1 → Step 0.5 | After "📋 Copy This Markdown for Lab 5.1" |
| 6 | 6.1 | Unit 6 → Lab 6.1 → Step 0.5 | After "📋 Copy This Markdown for Lab 6.1" |
| 6 | 6.2 | Unit 6 → Lab 6.2 → Step 0.5 | After "📋 Copy This Markdown for Lab 6.2" |
| 6 | 6.3 | Unit 6 → Lab 6.3 → Step 0.5 | After "📋 Copy This Markdown for Lab 6.3" |
| 7 | 7.1 | Unit 7 → Lab 7.1 → Step 0.5 | After "📋 Copy This Markdown for Lab 7.1" |
| 7 | 7.2 | Unit 7 → Lab 7.2 → Step 0.5 | After "📋 Copy This Markdown for Lab 7.2" |
| 7 | 7.3 | Unit 7 — 7.3 Best Practices content only (Lab 7.3 removed) | — |

**How to copy**: Go to lab's Step 0.5 → Copy from `⬇️ START COPYING HERE` to `⬆️ STOP COPYING HERE` → Paste after main unit content.

### Quick Content Addition Workflow

**For Maximum Efficiency**:

1. **Open two tabs**:
   - Tab 1: Codio Guide Editor (Tools → Guides → Edit)
   - Tab 2: This guide

2. **For each unit**:
   - **Add main content** (copy from `## For Students` to first lab)
   - **Add all lab content** (use Step 0.5 sections)
   - **Save once** after completing the unit
   - **Preview** to verify formatting

3. **Move to next unit** and repeat

**Total Time**: 3-4.5 hours for all content (can be done in one focused session)

### Content Verification Checklist

After adding content for each unit, verify:

- [ ] Main unit content is present and formatted correctly
- [ ] All labs for that unit are present
- [ ] Code blocks render with syntax highlighting
- [ ] Headings are properly sized
- [ ] Lists are bulleted/numbered correctly
- [ ] Links work (if any)
- [ ] Content flows logically (concepts → labs)

---

<a id="assessment-templates"></a>
## 📚 ASSESSMENT TEMPLATES LIBRARY

**💡 Time-Saving**: Copy these templates and modify for your specific needs. Saves 1-2 hours of coding time.

**🎯 Important Update**: This library now prioritizes **Codio's native assessment features** (LLM Rubric Autograde, Standard Code Test, Multiple Choice) over custom scripts. This reduces development time from 20-25 hours to 8-12 hours.

**📋 Template Selection Guide**:
- **YAML/Code Structure Validation** → Use **Template 1: LLM Rubric Autograde** (saves 20-45 min per assessment)
- **Simple Command/File Checks** → Use **Template 2: Standard Code Test** (saves 10-15 min per assessment)
- **Knowledge/Concept Checks** → Use **Template 3: Multiple Choice** (saves 5-10 min per assessment)
- **Response Validation** → Use **Template 4: LLM Rubric Autograde** (saves 20-30 min per assessment)
- **Flow Validation** → Use **Template 5: LLM Rubric Autograde** (saves 20-30 min per assessment)
- **API Testing** → Use **Template 7: Advanced Code Test** (required for API calls)
- **Virtual Coach Setup** → Use **Template 6: Virtual Coach Configuration** (reusable)

**⚠️ Legacy Templates**: Templates marked as "Legacy" (1B, 4B, 5B) are kept for reference only. Use them **only if** LLM Rubric Autograde is not available in your Codio plan.

**🤖 Codio AI Features First** (saves 2-5 hours total):
- **Multiple Choice, Fill in the Blanks**: Add empty assessment → Click **Generate** → **Generate Using AI** → Review → Apply
- **LLM Rubric Autograde**: Fill instructions + solution file → Click **Generate Rubrics** → Review → Refine
- **Duplicate Assessment**: Create one, click **Duplicate and Save**, edit the copy for similar questions
- See "Codio AI-Powered Time Savers" section (above) for full instructions

### Template 1: LLM Rubric Autograde for YAML Validation ⭐ **RECOMMENDED**

**Use for**: Lab 2.2, Lab 3.2, Lab 4.2, Lab 7.2 (any YAML file validation)

**⏱️ Time Saved**: 20-45 minutes per assessment vs. writing custom Python script

**When to Use**: Any assessment that validates YAML structure, file content, or code quality. **Use this instead of Template 1 (Python YAML Validator) or Template 4/5 (Response/Flow Validation scripts).**

**Configuration Template** (copy-paste ready):

**Assessment Type**: LLM Rubric Autograde

**Instructions Field**:
```
[Describe what student should accomplish - be specific about file paths and expected changes]
```

**Rubric Field** (copy this structure, customize requirements):
```
Requirements Checklist (all must be met):

1. File Location and Existence:
   - File [FILE_PATH] exists in /home/codio/workspace/level1/
   - File is valid YAML (no syntax errors, parses correctly)

2. [Structure/Content Requirements]:
   - [Specific requirement 1]
   - [Specific requirement 2]
   - [Specific requirement 3]

3. YAML Syntax and Indentation:
   - Uses exactly 2 spaces for indentation (not tabs, not 4 spaces)
   - [Specific indentation requirements]
   - No tabs used anywhere

Grading: Award full points ([POINTS]) if all requirements are met. Deduct points for each missing requirement.
```

**Solution File**: `/home/codio/workspace/level1/[FILE_PATH]`

**Files to Check**: `/home/codio/workspace/level1/[FILE_PATH]`

**Guide Content Context**: Copy relevant guide section explaining the task

**Points**: `[POINTS]` (typically 6-14 depending on complexity)

**Timeout**: `60` (seconds)

**Example Use Cases**:
- **Lab 2.2**: Validate `utter_goodbye` response in domain/basics.yml
- **Lab 3.2**: Validate `goodbye.yml` flow file structure
- **Lab 4.2**: Validate `pattern_session_start` modification
- **Lab 7.2**: Validate complete new feature (response + flow)

**⚠️ Important**: Be very specific in rubric. Include exact file paths, key names, indentation requirements, and structure expectations. Test with incorrect work to refine rubric.

---

### Template 1B: Standard Python YAML Validator (Legacy - Use Template 1 Instead)

**⚠️ DEPRECATED**: Use **Template 1: LLM Rubric Autograde** instead. This template is kept for reference only if LLM Rubric is not available.

**Use for**: Lab 2.2, Lab 3.2, Lab 4.2, Lab 7.2 (any YAML file validation) - **ONLY if LLM Rubric Autograde is not available**

```python
#!/usr/bin/env python3
"""
Template: YAML File Validator
Modify: file_path, required_keys, validation_logic
"""
import yaml
import sys
from pathlib import Path

def validate_yaml_file(file_path, required_keys=None, custom_checks=None):
    """Validate YAML file structure and content."""
    file_path = Path(file_path)
    
    # Check file exists
    if not file_path.exists():
        print(f"❌ FAIL: {file_path} not found")
        sys.exit(1)
    
    # Parse YAML
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ FAIL: YAML syntax error: {e}")
        sys.exit(1)
    
    # Check required keys
    if required_keys:
        for key in required_keys:
            if key not in data:
                print(f"❌ FAIL: Missing required key: {key}")
                sys.exit(1)
    
    # Run custom checks
    if custom_checks:
        for check_name, check_func in custom_checks.items():
            if not check_func(data):
                print(f"❌ FAIL: Custom check failed: {check_name}")
                sys.exit(1)
    
    print("✅ PASS: YAML file is valid")
    return data

# Example usage:
if __name__ == "__main__":
    data = validate_yaml_file(
        "/home/codio/workspace/level1/domain/basics.yml",
        required_keys=['responses'],
        custom_checks={
            'has_responses': lambda d: len(d.get('responses', {})) > 0
        }
    )
```

### Template 2: Standard Bash File Checker

**Use for**: Lab 0.1, Lab 2.1, Lab 6.1 (simple file/directory checks)

```bash
#!/bin/bash
set -e

cd /home/codio/workspace/level1
score=0
max_score=10

# Check 1: File exists
if [ -f "path/to/file.yml" ]; then
    echo "✓ File exists"
    score=$((score + 2))
else
    echo "❌ FAIL: File not found"
    exit 1
fi

# Check 2: Directory exists
if [ -d "path/to/dir" ]; then
    echo "✓ Directory exists"
    score=$((score + 2))
else
    echo "❌ FAIL: Directory not found"
    exit 1
fi

# Check 3: File contains expected content
if grep -q "expected_text" "path/to/file.yml"; then
    echo "✓ File contains expected content"
    score=$((score + 3))
else
    echo "❌ FAIL: File missing expected content"
    exit 1
fi

# Check 4: File count
file_count=$(find path/to/dir -name "*.yml" | wc -l)
if [ "$file_count" -ge 3 ]; then
    echo "✓ Sufficient files found"
    score=$((score + 3))
else
    echo "❌ FAIL: Expected at least 3 files, found $file_count"
    exit 1
fi

echo "✅ PASS: All checks passed! Score: $score/$max_score"
```

### Template 3: Multiple Choice Question (Standard Settings)

**Use for**: Units 1, 3, 4, 5, 8 (all concept checks)

**Configuration** (copy-paste ready):
- **Points**: `2` (single question) or `5-8` (question set)
- **Show explanations**: ✓ Enabled
- **Allow multiple attempts**: ✓ Enabled (max 3)
- **Randomize order**: Optional (✓ if available)

**Question Format**:
```
Question: [Your question text]

Options:
- [Option A] (uncheck)
- [Option B - Correct Answer] (check "Correct" ✓)
- [Option C] (uncheck)
- [Option D] (uncheck)

Explanation: [Why B is correct and others are wrong]
```

### Template 4: LLM Rubric Autograde for Response Validation ⭐ **RECOMMENDED**

**Use for**: Lab 2.2, Lab 2.3 (response validation)

**⏱️ Time Saved**: 20-30 minutes per assessment vs. writing custom Python script

**When to Use**: Validating responses in domain files. **Use this instead of Template 4B (Python script).**

**Configuration Template** (copy-paste ready):

**Assessment Type**: LLM Rubric Autograde

**Instructions Field**:
```
Add a new response called "[RESPONSE_NAME]" to domain/basics.yml.

The response should:
- Be added under the responses: section
- Have at least [N] text variation(s) with [DESCRIPTION]
- Include metadata with rephrase: True
- Use proper YAML syntax with correct indentation (2 spaces per level)
```

**Rubric Field**:
```
Requirements Checklist (all must be met):

1. File Location and Existence:
   - File domain/basics.yml exists in /home/codio/workspace/level1/
   - File is valid YAML (no syntax errors, parses correctly)

2. Response Structure:
   - Response "[RESPONSE_NAME]" exists under the responses: section
   - Response is a list (starts with "- text:")
   - Response has at least [N] text variation(s) (non-empty text)
   - Response text contains [EXPECTED_CONTENT]

3. YAML Syntax and Indentation:
   - Uses exactly 2 spaces for indentation (not tabs, not 4 spaces)
   - [RESPONSE_NAME]: is indented 2 spaces from left margin
   - - text: is indented 4 spaces from left margin
   - metadata: is aligned with text: (6 spaces from left margin)
   - rephrase: True is indented 8 spaces from left margin
   - No tabs used anywhere

4. Metadata:
   - metadata: section exists in the response
   - metadata contains rephrase: True (exact value, boolean True)
   - metadata is properly indented (aligned with text:)

Grading: Award full points ([POINTS]) if all requirements are met. Deduct points for each missing requirement.
```

**Solution File**: `/home/codio/workspace/level1/domain/basics.yml`

**Files to Check**: `/home/codio/workspace/level1/domain/basics.yml`

**Points**: `10` (Lab 2.2) or `5` (Lab 2.3)

**Timeout**: `60` (seconds)

---

### Template 4B: Response Validation (Python Script - Legacy)

**⚠️ DEPRECATED**: Use **Template 4: LLM Rubric Autograde** instead. This template is kept for reference only if LLM Rubric is not available.

**Use for**: Lab 2.2, Lab 2.3 (modify response name and criteria) - **ONLY if LLM Rubric Autograde is not available**

```python
#!/usr/bin/env python3
"""
Template: Response Validator
Modify: response_name, min_variations, require_metadata
"""
import yaml
import sys
from pathlib import Path

def validate_response(domain_file, response_name, min_variations=1, require_metadata=True):
    """Validate a specific response in domain file."""
    domain_file = Path(domain_file)
    
    # Load domain
    with open(domain_file, 'r', encoding='utf-8') as f:
        domain = yaml.safe_load(f)
    
    # Check response exists
    if 'responses' not in domain or response_name not in domain['responses']:
        print(f"❌ FAIL: Response '{response_name}' not found")
        sys.exit(1)
    
    response = domain['responses'][response_name]
    
    # Check variations
    if not isinstance(response, list) or len(response) < min_variations:
        print(f"❌ FAIL: Response needs at least {min_variations} variation(s)")
        sys.exit(1)
    
    # Check metadata
    if require_metadata:
        has_metadata = any('metadata' in item and item['metadata'].get('rephrase') is True 
                          for item in response)
        if not has_metadata:
            print(f"❌ FAIL: Response missing metadata with rephrase: True")
            sys.exit(1)
    
    print(f"✅ PASS: Response '{response_name}' is valid")
    return True

# Example usage:
if __name__ == "__main__":
    validate_response(
        "/home/codio/workspace/level1/domain/basics.yml",
        "utter_goodbye",
        min_variations=2,
        require_metadata=True
    )
```

### Template 5: LLM Rubric Autograde for Flow Validation ⭐ **RECOMMENDED**

**Use for**: Lab 3.2, Lab 3.3 (flow validation)

**⏱️ Time Saved**: 20-30 minutes per assessment vs. writing custom Python script

**When to Use**: Validating flows in flow files. **Use this instead of Template 5B (Python script).**

**Configuration Template** (copy-paste ready):

**Assessment Type**: LLM Rubric Autograde

**Instructions Field**:
```
Create a new flow file called "[FLOW_FILE].yml" in the data/basics/ folder.

The flow should:
- Be named "[FLOW_NAME]" (under flows: section)
- Have a name field (e.g., "[FLOW_NAME]")
- Have a description field that explains when this flow should trigger
- Have a steps section with at least one action: [ACTION_NAME]
- Use proper YAML syntax with correct indentation (2 spaces per level)
```

**Rubric Field**:
```
Requirements Checklist (all must be met):

1. File Location and Existence:
   - File data/basics/[FLOW_FILE].yml exists in /home/codio/workspace/level1/
   - File is valid YAML (no syntax errors, parses correctly)
   - File is in correct location (data/basics/, not data/ root)

2. Flow Structure:
   - File contains a flows: section (top level, no indentation)
   - Flow named "[FLOW_NAME]" exists under flows: section
   - Flow is properly indented ([FLOW_NAME]: is 2 spaces from left margin)

3. Required Fields:
   - Flow has a "name" field (non-empty)
   - Flow has a "description" field (non-empty, descriptive text explaining when flow triggers)
   - Flow has a "steps" field (list of actions)
   - All fields are properly indented (4 spaces from left margin, under [FLOW_NAME]:)

4. Steps Section:
   - steps: section contains at least one action
   - Action format is correct: "- action: [ACTION_NAME]"
   - Action is properly indented (6 spaces from left margin, under steps:)

5. Description Quality:
   - description field is not empty
   - description is meaningful (explains when/why flow triggers, >10 characters)

6. YAML Syntax and Indentation:
   - Uses exactly 2 spaces for indentation (not tabs, not 4 spaces)
   - flows: is at left margin (0 spaces)
   - [FLOW_NAME]: is indented 2 spaces
   - name:/description:/steps: are indented 4 spaces
   - - action: is indented 6 spaces
   - No tabs used anywhere

Grading: Award full points ([POINTS]) if all requirements are met. Deduct points for each missing requirement.
```

**Solution File**: `/home/codio/workspace/level1/data/basics/[FLOW_FILE].yml`

**Files to Check**: `/home/codio/workspace/level1/data/basics/[FLOW_FILE].yml`

**Points**: `12` (Lab 3.2) or `8` (Lab 3.3)

**Timeout**: `60` (seconds)

---

### Template 5B: Flow Validation (Python Script - Legacy)

**⚠️ DEPRECATED**: Use **Template 5: LLM Rubric Autograde** instead. This template is kept for reference only if LLM Rubric is not available.

**Use for**: Lab 3.2, Lab 3.3 (modify flow name and criteria) - **ONLY if LLM Rubric Autograde is not available**

```python
#!/usr/bin/env python3
"""
Template: Flow Validator
Modify: flow_file, flow_name, require_description, min_steps
"""
import yaml
import sys
from pathlib import Path

def validate_flow(flow_file, flow_name, require_description=True, min_steps=1):
    """Validate a specific flow in flow file."""
    flow_file = Path(flow_file)
    
    # Load flow file
    with open(flow_file, 'r', encoding='utf-8') as f:
        flow_data = yaml.safe_load(f)
    
    # Check flows key
    if 'flows' not in flow_data:
        print("❌ FAIL: Missing 'flows:' key")
        sys.exit(1)
    
    # Check flow exists
    if flow_name not in flow_data['flows']:
        print(f"❌ FAIL: Flow '{flow_name}' not found")
        sys.exit(1)
    
    flow = flow_data['flows'][flow_name]
    
    # Check required fields
    if 'name' not in flow or 'steps' not in flow:
        print(f"❌ FAIL: Flow missing required fields (name or steps)")
        sys.exit(1)
    
    # Check description
    if require_description:
        if 'description' not in flow or not str(flow['description']).strip():
            print(f"❌ FAIL: Flow missing non-empty description (CRITICAL!)")
            sys.exit(1)
    
    # Check steps
    if len(flow.get('steps', [])) < min_steps:
        print(f"❌ FAIL: Flow needs at least {min_steps} step(s)")
        sys.exit(1)
    
    print(f"✅ PASS: Flow '{flow_name}' is valid")
    return True

# Example usage:
if __name__ == "__main__":
    validate_flow(
        "/home/codio/workspace/level1/data/basics/goodbye.yml",
        "goodbye",
        require_description=True,
        min_steps=1
    )
```

### Template 6: Virtual Coach Configuration (Reusable)

**Use for**: All units (copy and modify per unit)

```yaml
# Virtual Coach - Summarize Prompt (Unit X)
Unit X Key Concepts:
- [Concept 1 from unit]
- [Concept 2 from unit]
- [Common pattern]

# Virtual Coach - Error Augmentation (Reusable across units)
YAMLError → "Check YAML syntax: missing colons, wrong indentation, or missing dashes. Use exactly 2 spaces per indent level."
IndentationError → "Use exactly 2 spaces for indentation (not tabs, not 4 spaces). Enable 'show whitespace' in your editor."
FileNotFoundError → "Check file path. Ensure file is in correct location and name matches exactly (case-sensitive)."
MissingDescription → "The description field is CRITICAL! The LLM uses it to match user messages. Add a clear, specific description."

# Virtual Coach - Next Steps (Unit X specific)
If grader fails:
1. [Unit-specific step 1]
2. [Unit-specific step 2]
3. [Unit-specific step 3]
```

### Template 7: Code Test Assessment Configuration

**Standard Settings** (copy-paste ready):

```yaml
Assessment Type: Code Test
Points: 10
Timeout: 30 seconds
Language: Python 3
Fail on Error: ✓ Enabled
Max Attempts: 3
Show Output: ✓ Enabled

# For complex assessments:
Points: 12-14
Timeout: 60 seconds
Language: Python 3
```

### Template 8: Batch Assessment Creation Workflow

**Time-Saving Workflow** (saves ~1 hour):

1. **Create all Multiple Choice questions first** (Units 1, 3, 4, 5, 8)
   - Open Guide editor
   - Navigate to Unit 1 → Create all 3 questions
   - Navigate to Unit 3 → Create all 3 questions
   - Navigate to Unit 4 → Create all 3 questions
   - Navigate to Unit 5 → Create all 6 questions
   - Navigate to Unit 8 → Create all 10-15 questions
   - **Total time**: 2-3 hours (vs 4-5 hours if done separately)

2. **Create all Code Tests second** (Units 0, 2, 3, 4, 6, 7)
   - Use templates above
   - Copy-paste and modify
   - **Total time**: 3-4 hours (vs 5-6 hours if done separately)

3. **Configure Virtual Coach once** (all units)
   - Set up base configuration
   - Copy to each unit and modify
   - **Total time**: 1 hour (vs 2-3 hours if done separately)

4. **Enable Code Playback once** (all tracked files)
   - Add all files at once: `domain/basics.yml`, `data/basics/*.yml`, `data/system/patterns/patterns.yml`
   - **Total time**: 15 minutes (vs 1 hour if done separately)

### Template 9: Common Validation Functions

**Reusable helper functions** (add to any Python grader):

```python
def check_indentation(line, expected_spaces):
    """Check if line starts with expected number of spaces."""
    if line.startswith('\t'):
        return False, "Line contains tabs. Use spaces only."
    leading_spaces = len(line) - len(line.lstrip())
    return leading_spaces == expected_spaces, f"Expected {expected_spaces} spaces, found {leading_spaces}"

def validate_yaml_structure(file_path, top_level_key, nested_key=None):
    """Validate YAML has expected structure."""
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    
    if top_level_key not in data:
        return False, f"Missing top-level key: {top_level_key}"
    
    if nested_key and nested_key not in data[top_level_key]:
        return False, f"Missing nested key: {nested_key}"
    
    return True, "Structure valid"

def check_file_in_directory(directory, filename_pattern):
    """Check if file matching pattern exists in directory."""
    from pathlib import Path
    dir_path = Path(directory)
    matches = list(dir_path.glob(filename_pattern))
    return len(matches) > 0, matches
```

### Template 10: Assessment Testing Checklist

**Before marking assessment complete**:

```markdown
- [ ] Assessment appears in Guide preview
- [ ] Assessment runs without errors
- [ ] Correct answer passes (test with expected student work)
- [ ] Incorrect answer fails with helpful error message
- [ ] Points are awarded correctly
- [ ] Timeout is appropriate (not too short/long)
- [ ] Error messages are clear and actionable
- [ ] Virtual Coach can help with common errors
```

### Template 11: Complete Unit Implementation Script

**Use this as a checklist for each unit** (saves 10-15 minutes per unit):

```markdown
Unit X Implementation:
- [ ] Read unit instructions (5 min)
- [ ] Identify which templates to use (2 min)
- [ ] Create all assessments for unit (varies)
  - [ ] Assessment 1 (use Template X)
  - [ ] Assessment 2 (use Template Y)
  - [ ] Assessment 3 (use Template Z)
- [ ] Configure Virtual Coach (5 min)
- [ ] Enable Code Playback if needed (2 min)
- [ ] Test all assessments (5 min)
- [ ] Fix any errors (varies)
- [ ] Mark unit complete in Master Checklist
```

**⏱️ Time Saved**: 10-15 minutes per unit (prevents forgetting steps)

### Template 12: Error Message Library (Copy-Paste Ready)

**Common error messages to use in assessments** (ensures consistency):

```python
# File not found
"❌ FAIL: File not found. Check file path and name (case-sensitive)."

# YAML syntax error
"❌ FAIL: YAML syntax error. Check indentation (2 spaces), colons, and dashes."

# Missing required field
"❌ FAIL: Missing required field: [field_name]. Add it to your [file_type]."

# Wrong indentation
"❌ FAIL: Indentation error. Use exactly 2 spaces per indent level (not tabs)."

# Missing response/flow
"❌ FAIL: [response_name/flow_name] not found. Create it in [file_path]."

# Validation failed
"❌ FAIL: Validation failed. [Specific reason]. Check [what to check]."
```

**⏱️ Time Saved**: 2-3 minutes per assessment (no typing, ensures consistency)

### 💡 Pro Tips for Maximum Efficiency

1. **Use Codio's "Duplicate Assessment" feature** (if available)
   - Create one assessment, duplicate it, then modify
   - Saves 50% time on similar assessments

2. **Keep a text file with common error messages**
   - Copy-paste error messages rather than typing
   - Ensures consistency across assessments

3. **Test in batches**
   - Create 3-5 assessments, then test all at once
   - Fix errors in batch rather than one-by-one

4. **Use browser bookmarks**
   - Bookmark Codio Guide editor, Settings, Analytics
   - Saves navigation time

5. **Document customizations**
   - Keep notes on any deviations from templates
   - Helps with future levels or updates

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
