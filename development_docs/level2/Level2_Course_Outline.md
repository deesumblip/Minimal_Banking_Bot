# Level 2: Simple Actions - Course Outline

## Course Overview

**Title**: Level 2: Simple Actions  
**Description**: A Complete Guide to Adding Custom Python Code to Your Banking Agent  
**Prerequisites**: Level 1 must be completed  
**Learning Objective**: Students learn to create custom Python actions that extend their Level 1 agent with dynamic functionality.

---

## Course Structure

### Unit 0: Recap - What you built in Level 1
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 0.1 Your Level 1 Banking Agent — and what Level 2 adds
  - What you have from Level 1 (domain, flows, patterns, config)
  - What Level 1 couldn't do (limitations)
  - What Level 2 adds (actions, starter vs labs, modified and unchanged files, configuration)

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
  - Domain (agent configuration)

**Key Concepts**: Action class structure, dispatcher, tracker, domain

---

### Unit 3: Creating Your First Action
**Type**: Lab (with Assessment)  
**Assessment**: Lab 3.1 - Creating Your First Action (13 points: 5 fill-in + 8 code test)

**Sections**:
- Lab 3.1: Create Your Own Action (only page in Unit 3; segue from Unit 2.1; fill-in + paste + Code Test; ends with how Rasa executes your action—7 steps)

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
**Assessment**: Lab 4.1 – Registering Actions in the Domain (11 points).

**Sections**:
- 4.1 Why Register Actions?
- Lab 4.1: Registering Actions in the Domain

*(Lab 6.2: Verify Domain and Training appears in Unit 6, right after Lab 6.1.)*

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
**Assessment**: Lab 5.1 - Using Actions in Flows (12 points)

**Sections**:
- 5.1 Actions vs. Responses in Flows
  - Level 1 flow (response) example
  - Level 2 flow (action) example
  - Key differences
- Lab 5.1 — create flows (hours.yml, holiday_hours.yml); see lab for full steps
- 5.2 Mixing Responses and Actions
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

### Unit 6: Training, Testing, and Level 2 Wrap-Up
**Type**: Lab (with Assessments) + closing content page  
**Assessments**: Lab 6.1 - Training and Testing with Actions (4 points). Lab 6.2 - Verify Domain and Training (11 points; right after Lab 6.1). **6.4** embeds five multiple-choice Check It! items on the page (not part of the 51 graded lab points).

**Sections**:
- Lab 6.1: Training and Testing with Actions (training overview, `cd level2` + `rasa train`, assessment)
- 6.2 Common Training Errors with Actions
  - Error: Action Not Found
  - Error: Import Error
  - Error: Name Mismatch
- 6.3 Testing and Debugging Your Action (workflow, Inspector, debug panel, common issues)
- Lab 6.2: Verify Domain and Training (domain + model file check; optional Inspector)
- **6.4 See it all together** (stem `6-4-Level-2-Wrap-Up-d798`)
  - Full conversation example (Level 1 + example action + your Lab 3.1 action)
  - Project structure at a glance; best practices; **5×** Check It! MCQs
- **6.5 Before you continue** (stem `6-5-Core-Ideas-and-Level-3-Readiness-b91a`; no assessments)
  - Short L2 checkpoint; readiness bullets; points to Level 3 Unit 0 for full recap (avoids overlap with **0-1** / **0-2**)

**Key Concepts**: Training, testing, debugging, Rasa Inspector, port forwarding; integration, review, next level

**Assessment Checks**:
- Virtual environment exists
- Model file created
- Model file is recent (within 10 minutes)
- No critical errors in logs
- Action file exists

**Special Configuration**: Terminal pre-configured for Inspector (cd + venv activation)

---

### Unit 7: Putting It All Together — Wrap-Up *(not a separate Codio unit; see Unit 6 pages 6.4–6.5)*
**Type**: Content Page  
**Assessment**: Embedded knowledge check (5× multiple-choice via Check It! on **6.4**)

**Sections** (historical outline; in the live guide this is **6.4** + **6.5**; former Unit 8 merged here):
- Full conversation example (Level 1 + example action + your Lab 3.1 action)
- Project structure at a glance (domain, flows, actions, config)
- Best practices: organizing flows, responses, descriptions, testing with Inspector and logs
- Knowledge check (5 MCQs)
- Core ideas and skills recap; what Level 2 still doesn’t do; Level 3 preview (same agent); readiness checklist

**Key Concepts**: Integration, review, limitations, next level (slots), course completion

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

| Unit | Lab | Points | Type | Grader / task |
|--------|-----|--------|------|---------------|
| Unit 3 | Lab 3.1 (fill-in) | 5 | Fill in the Blanks | `fill-in-the-blanks-201030010` |
| Unit 3 | Lab 3.1 (code) | 8 | Standard Code Test | `lab_3.2_grader.sh` (`code-output-compare-2266471391`) |
| Unit 4 | Lab 4.1 | 11 | Standard Code Test | `lab_4.1_grader.sh` |
| Unit 5 | Lab 5.1 | 12 | Standard Code Test | `lab_5.1_grader.sh` |
| Unit 6 | Lab 6.1 | 4 | Standard Code Test | `lab_6.1_grader.sh` |
| Unit 6 | Lab 6.2 | 11 | Code Output Compare | `lab_4.2_grader.sh` (domain + model file) |

**Total Assessment Points**: 51 points (5 + 8 + 11 + 12 + 4 + 11)

**Codio: Grader updates from GitHub**  
When you set up or edit assessments on Codio, configure each Code Test to **run the grader script from the workspace** (e.g. `bash /home/codio/workspace/.guides/secure/level2_graders/lab_5.1_grader.sh`). Do **not** upload or paste the script content into the assessment. That way, when you push grader changes to GitHub and pull on Codio, the assessment will use the updated script automatically.

**Level 2 (Codio guide)**: Code-output-compare Check It! tags are on Labs 3.1, 4.1, 5.1, 6.1, 6.2. Multiple-choice Check It! tags are on content pages: 1.1, 1.4, 2.2, 2.3, Lab 2.1, 3.1 (fill-in + code test), **6.4** *See it all together* (knowledge check; former 8.1-style MCQs; **6.5** *Before you continue* has no Check It!; see `.guides/content/Level-2---Custom-Actions-30d6/`).

---

## File Organization

### Content Files (Copy/Paste into Codio)
Content is split by subsection (one file per numbered subsection). Examples:
- **Unit 0**: `Level2_Unit0_Content_0.1_Your-Level-1-Banking-Agent.md` (recap + what Level 2 adds)
- **Unit 1**: `Level2_Unit1_Content_1.1_*.md` … `1.3_*.md`
- **Unit 2**: `Level2_Unit2_Content_2.1_*.md`, `2.2_*.md`
- **Unit 3**: Lab 3.1 only in the guide (execution summary at end of that page). Mirror: `Level2_Lab3.1_Content.md`; `action_bank_hours` example in Unit 2.1 / `Level2_Unit2_Content_2.1_*.md`. The old `Level2_Unit3_Content_3.2_*.md` stub notes content merged into Lab 3.1.
- **Units 4–6**: `Level2_UnitN_Content_N.M_*.md` (see level2 folder for full list)
- `Level2_Troubleshooting_Content.md` - Troubleshooting guide
- `Level2_AdditionalResources_Content.md` - Extension exercises

### Assessment Files (Implementation Instructions)
- `Level2_Lab3.1_Content.md` / `Level2_Lab3.1_Assessment_Setup.md` - Lab 3.1 (student page + implementer doc)
- `Level2_Lab4.1_Content.md` / `Level2_Lab4.1_Assessment_Setup.md` – Lab 4.1
- `Level2_Lab6.2_Content.md` / `Level2_Lab6.2_Assessment_Setup.md` – Lab 6.2 (Verify Domain and Training)
- `Level2_Lab5.1_Content.md` / `Level2_Lab5.1_Assessment_Setup.md` - Lab 5.1
- `Level2_Lab6.1_Content.md` / `Level2_Lab6.1_Assessment_Setup.md` - Lab 6.1

### Implementation Files
- `Level2_Implementation_Overview.md` - Codio team guide
- `Level2_Course_Outline.md` - This file

---

## Learning Path

```
Unit 0: Recap - What you built in Level 1
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
Unit 6: Training, Testing, and Level 2 Wrap-Up (Hands-on Labs + **6.4** *See it all together* + **6.5** *Before you continue*) ✓ Lab 6.1 & Lab 6.2 Assessments; **6.4** = integration + knowledge check; **6.5** = readiness handoff to Level 3
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
- **Rasa**: Rasa Pro 3.16.3 (`rasa-pro==3.16.3`)
- **Port Forwarding**: Required for Unit 6 (Rasa Inspector)
- **Prerequisites**: Level 1 completed

---

## Estimated Time

- **Unit 0-2**: 30-45 minutes (conceptual content)
- **Unit 3**: 45-60 minutes (lab + assessment)
- **Unit 4**: 30-45 minutes (lab + assessment)
- **Unit 5**: 30-45 minutes (lab + assessment)
- **Unit 6** (labs + testing + wrap-up pages **6.4**–**6.5**): 60-90 minutes (labs + assessment + testing + integration review + closing pages)

**Total Estimated Time**: 4-5 hours

---
