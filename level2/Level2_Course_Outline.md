# Level 2: Simple Actions - Course Outline

## Course Overview

**Title**: Level 2: Simple Actions  
**Description**: A Complete Guide to Adding Custom Python Code to Your Banking Bot  
**Prerequisites**: Level 1 must be completed  
**Learning Objective**: Students learn to create custom Python actions that extend their Level 1 bot with dynamic functionality.

---

## Course Structure

### Unit 0: Recap - What You Built in Level 1
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 0.1 Your Level 1 Banking Bot
  - What you have from Level 1 (domain, flows, patterns, config)
  - What Level 1 couldn't do (limitations)
- 0.2 What Level 2 Adds
  - Introduction to Actions
  - New files in Level 2
  - Modified files in Level 2
  - Unchanged files (Level 1 content remains)

**Key Concepts**: Recap, building on existing work

---

### Unit 1: Introduction to Actions
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 1.1 What is an Action?
  - Actions vs. Responses (`utter_*` vs `action_*`)
  - When to use actions
  - When not to use actions
  - Example: Bank Hours (Level 1 vs Level 2 approach)
- 1.2 How Actions Work
  - Flow diagram showing action execution
  - Step-by-step process
- 1.3 The Action Class Structure
  - Basic action class template
  - Required methods (`name()`, `run()`)

**Key Concepts**: Actions, custom Python code, action vs response

---

### Unit 2: Understanding the Action Class
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 2.1 The Action Class Deep Dive
  - Complete `action_bank_hours.py` file walkthrough
  - Breaking down each component:
    - Imports
    - Class definition
    - `name()` method
    - `run()` method
    - Sending messages
- 2.2 Understanding the Parameters
  - Dispatcher (sending messages)
  - Tracker (conversation history - preview for Level 3)
  - Domain (bot configuration)

**Key Concepts**: Action class structure, dispatcher, tracker, domain

---

### Unit 3: Creating Your First Action
**Type**: Lab (with Assessment)  
**Assessment**: Lab 3.1 - Creating Your First Action (12 points)

**Sections**:
- 3.1 Step-by-Step: Creating an Action
  - Before You Begin checklist
  - Step 1: Navigate to Actions Folder
  - Step 2: Create the Action File
  - Step 3: Add the Action Class Structure
  - Step 4: Verify Your Code
  - Step 5: Save the File
- 3.2 Understanding Action Execution
  - How Rasa executes actions (7-step process)

**Key Concepts**: Creating action files, Python class structure, imports

**Assessment Checks** (Lab 3.1 verifies student-created `action_holiday_hours.py` with date-based logic):
- Virtual environment exists
- Actions folder exists
- `__init__.py` exists
- `action_holiday_hours.py` exists (created by student)
- Correct imports (including `datetime` for date-based logic)
- Action class inherits from Action (`ActionHolidayHours`)
- `name()` method exists and returns `"action_holiday_hours"`
- `run()` uses `dispatcher.utter_message()` and returns `[]`
- Uses `datetime` to choose message (e.g. "closed today" on a holiday vs general schedule)

---

### Unit 4: Registering Actions in the Domain
**Type**: Lab (with Assessment)  
**Assessment**: Lab 4.1 - Registering Actions in the Domain (10 points)

**Sections**:
- 4.1 Why Register Actions?
  - Explanation of registration requirement
- 4.2 The Actions Section
  - Domain structure in Level 2
  - How to register an action
- 4.3 Step-by-Step: Registering Your Action
  - Step 1: Open the Domain File
  - Step 2: Add the Actions Section
  - Step 3: Verify Registration
- 4.4 Multiple Actions
  - How to register multiple actions

**Key Concepts**: Domain registration, YAML syntax, action naming

**Assessment Checks**:
- Virtual environment exists
- `domain/basics.yml` exists
- `actions:` section exists
- `action_bank_hours` is registered
- Correct YAML syntax
- Domain file is valid YAML

---

### Unit 5: Using Actions in Flows
**Type**: Lab (with Assessment)  
**Assessment**: Lab 5.1 - Using Actions in Flows (10 points)

**Sections**:
- 5.1 Actions vs. Responses in Flows
  - Level 1 flow (response) example
  - Level 2 flow (action) example
  - Key differences
- 5.2 Creating a Flow That Uses an Action
  - Step 1: Navigate to Data Folder
  - Step 2: Create the Hours Flow
  - Step 3: Understanding the Flow
  - Step 4: Verify the Flow
- 5.3 Mixing Responses and Actions
  - Using both in the same flow

**Key Concepts**: Flow creation, action references in flows, mixing responses and actions

**Assessment Checks**:
- Virtual environment exists
- `hours.yml` file exists in `data/basics/`
- `flows:` section exists
- `hours` flow exists
- Flow has `name` and `description`
- Flow has `steps:` section
- Flow uses `action_bank_hours`

---

### Unit 6: Training and Testing with Actions
**Type**: Lab (with Assessment)  
**Assessment**: Lab 6.1 - Training and Testing with Actions (10 points)

**Sections**:
- 6.1 Training with Actions
  - Training command (Codio and local)
  - What happens during training (4-step process)
- 6.2 Common Training Errors with Actions
  - Error: Action Not Found
  - Error: Import Error
  - Error: Name Mismatch
- 6.3 Testing Your Action
  - Basic testing workflow
  - Using Rasa Inspector
  - Port forwarding setup (Codio)
  - Verifying Level 1 flows still work
- 6.4 Debugging Actions
  - Check debug output
  - Common issues and solutions

**Key Concepts**: Training, testing, debugging, Rasa Inspector, port forwarding

**Assessment Checks**:
- Virtual environment exists
- Model file created
- Model file is recent (within 10 minutes)
- No critical errors in logs
- Action file exists

**Special Configuration**: Terminal pre-configured for Inspector (cd + venv activation)

---

### Unit 7: Putting It All Together
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 7.1 Complete Bot Walkthrough
  - Full conversation example showing Level 1 + Level 2 working together
- 7.2 Your Level 2 Banking Bot: Summary
  - Complete bot structure
  - What your bot can do now
  - What's still missing (preview of future levels)
- 7.3 Best Practices
  - Organizing actions
  - Writing good actions
  - Action naming conventions

**Key Concepts**: Integration, best practices, course summary

---

### Unit 8: Assessment and Next Steps
**Type**: Content Page (Knowledge Check)  
**Assessment**: None (knowledge check questions only)

**Sections**:
- 8.1 Knowledge Check
  - 5 multiple-choice questions with answers and explanations
- 8.2 What You've Learned
  - Key concepts summary
  - Skills developed checklist
- 8.3 Limitations of Level 2
  - What Level 2 cannot do
  - When Level 2 is sufficient
  - When you need more (Level 3)
- 8.4 What's Next: Level 3 Preview
  - Building on existing bot (not starting from scratch)
  - What slots enable
  - Key concepts in Level 3
- 8.5 Course Completion Checklist
  - 7-item checklist before moving to Level 3

**Key Concepts**: Review, limitations, next steps, Level 3 preview

---

## Additional Resources

### Troubleshooting Guide
**Type**: Reference Content  
**File**: `Level2_Troubleshooting_Content.md`

**Sections**:
- Issue: Action Not Found Error
- Issue: Action Executes But No Message
- Issue: Import Error

### Additional Resources
**Type**: Extension Content  
**File**: `Level2_AdditionalResources_Content.md`

**Sections**:
- Exercise 1: Add More Actions
- Exercise 2: Dynamic Responses
- Exercise 3: Action with Calculations
- Conclusion and next steps

---

## Assessment Summary

| Unit | Lab | Points | Type | Grader Script |
|--------|-----|--------|------|---------------|
| Unit 3 | Lab 3.1 | 12 | Standard Code Test | `lab_3.1_grader.sh` |
| Unit 4 | Lab 4.1 | 10 | Standard Code Test | `lab_4.1_grader.sh` |
| Unit 5 | Lab 5.1 | 10 | Standard Code Test | `lab_5.1_grader.sh` |
| Unit 6 | Lab 6.1 | 10 | Standard Code Test | `lab_6.1_grader.sh` |

**Total Assessment Points**: 42 points

---

## File Organization

### Content Files (Copy/Paste into Codio)
Content is split by subsection (one file per numbered subsection). Examples:
- **Unit 0**: `Level2_Unit0_Content_0.1_*.md`, `Level2_Unit0_Content_0.2_*.md`
- **Unit 1**: `Level2_Unit1_Content_1.1_*.md` … `1.3_*.md`
- **Unit 2**: `Level2_Unit2_Content_2.1_*.md`, `2.2_*.md`
- **Unit 3**: `Level2_Unit3_Content_3.1_Step-by-Step-Creating-an-Action.md`, `Level2_Unit3_Content_3.2_Understanding-Action-Execution.md`
- **Units 4–8**: `Level2_UnitN_Content_N.M_*.md` (see level2 folder for full list)
- `Level2_Troubleshooting_Content.md` - Troubleshooting guide
- `Level2_AdditionalResources_Content.md` - Extension exercises

### Assessment Files (Implementation Instructions)
- `Level2_Lab3.1_Assessment.md` - Lab 3.1 setup
- `Level2_Unit4_Assessment.md` - Lab 4.1 setup
- `Level2_Unit5_Assessment.md` - Lab 5.1 setup
- `Level2_Unit6_Assessment.md` - Lab 6.1 setup

### Implementation Files
- `Level2_Implementation_Overview.md` - Codio team guide
- `Level2_Course_Outline.md` - This file

---

## Learning Path

```
Unit 0: Recap
    ↓
Unit 1: Introduction to Actions (Conceptual)
    ↓
Unit 2: Understanding the Action Class (Conceptual)
    ↓
[Optional: Lab 2.1 – Explore the actions/ folder (MC/FIB)]
    ↓
Unit 3: Creating Your First Action (Hands-on Lab) ✓ Lab 3.1 Assessment
    ↓
Unit 4: Registering Actions (Hands-on Lab) ✓ Lab 4.1 Assessment
    ↓
Unit 5: Using Actions in Flows (Hands-on Lab) ✓ Lab 5.1 Assessment
    ↓
Unit 6: Training and Testing (Hands-on Lab) ✓ Lab 6.1 Assessment
    ↓
Unit 7: Putting It All Together (Integration)
    ↓
Unit 8: Assessment and Next Steps (Review)
```

**Note:** Lab 2.1 (Exploring the Actions Folder) is optional and fits after Unit 2. It reinforces the action class structure with multiple-choice and fill-in-the-blank questions; the main sequence continues with Unit 3 and Lab 3.1.

---

## Key Learning Outcomes

By the end of Level 2, students should be able to:

1.  Explain what an action is and how it differs from a response
2.  Create a new action in Python with correct structure
3.  Register an action in the domain file
4.  Create a flow that uses an action
5.  Understand how actions are executed
6.  Debug when actions don't work
7.  Understand that Level 2 builds on Level 1 (all Level 1 content remains)

---

## Technical Requirements

- **Environment**: Codio (Linux Ubuntu 22.04)
- **Python**: 3.11
- **Rasa**: Rasa Pro (latest stable)
- **Port Forwarding**: Required for Unit 6 (Rasa Inspector)
- **Prerequisites**: Level 1 completed

---

## Estimated Time

- **Unit 0-2**: 30-45 minutes (conceptual content)
- **Unit 3**: 45-60 minutes (lab + assessment)
- **Unit 4**: 30-45 minutes (lab + assessment)
- **Unit 5**: 30-45 minutes (lab + assessment)
- **Unit 6**: 45-60 minutes (lab + assessment + testing)
- **Unit 7-8**: 30-45 minutes (integration + review)

**Total Estimated Time**: 4-5 hours

---
