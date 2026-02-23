# Level 3: Slot Collection - Course Outline

## Course Overview

**Title**: Level 3: Slot Collection  
**Description**: A Complete Guide to Adding Memory (Slots) to Your Banking Bot  
**Prerequisites**: Level 1 and Level 2 must be completed  
**Learning Objective**: Students learn to define slots, read slots in actions, and collect slot values in flows so the bot can remember and use user-provided information. Labs are ordered so that implementation is chronological: domain (Lab 3.1) → action (Lab 4.1) → flow (Lab 5.1).

---

## Course Structure

### Unit 0: Recap - What You Built in Level 2
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 0.1 Your Level 2 Banking Bot
  - What you have from Level 2 (domain, flows, actions)
  - What Level 2 couldn't do (no memory)
- 0.2 What Level 3 Adds
  - Introduction to slots (conversation memory)
  - New in domain: `slots:`, `utter_ask_account`
  - New action: `action_check_balance_simple`
  - New flow: `check_balance.yml`

**Key Concepts**: Recap, building on Level 2, slots as memory

---

### Unit 1: Introduction to Slots
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 1.1 What is a Slot?
  - Slots = bot memory
  - Example: account number with vs without slots
- 1.2 How Slots Work
  - Define in domain, collect in flow, read in action
- 1.3 Slot Collection
  - If slot empty → bot asks; if has value → flow continues

**Key Concepts**: Slots, memory, collect step

---

### Unit 2: Understanding Slot Types
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 2.1 Slot Types
  - Text slots (used in Level 3)
  - Other types (advanced)
- 2.2 Slot Naming
  - Good vs bad slot names, conventions
- 2.3 Test Your Knowledge
  - 3 multiple choice questions (Units 0–2: slots, collect step, slot types and naming)

**Key Concepts**: Slot types, naming

---

### Unit 3: Defining Slots in the Domain
**Type**: Lab (with Assessment)  
**Assessment**: Lab 3.1 - Defining a Slot in the Domain (suggested points: 6–8)

**Sections**:
- 3.1 The Slots Section
  - Domain structure with `slots:`
- Lab 3.1: Defining a Slot in the Domain
  - Step-by-step instructions: Add `slots:` and `account` slot, add `utter_ask_account` response

**Key Concepts**: Domain slots section, utter_ask_* naming

**Assessment Checks** (Lab 3.1):
- Virtual environment (from project root)
- `domain/basics.yml` has `slots:` section
- `account` slot defined (type: text)
- `utter_ask_account` response exists

---

### Unit 4: Reading Slots in Actions
**Type**: Content + Lab (no assessment)  
**Assessment**: None. Lab 4.1 – Exploring Actions with Slots (ungraded).

**Placement**: This unit comes **before** Unit 5 so students understand how the action uses the slot before they create the flow that runs it.

**Sections**:
- 4.1 Accessing Slots in Actions
  - `tracker.get_slot("slot_name")`
- 4.2 Placeholder Handling
  - Check for None, placeholders; re-prompt with utter_ask_account

**Lab 4.1**: Explore `action_check_balance_simple.py` (provided); see how it reads the slot and handles placeholders. No graded assessment.

**Key Concepts**: Tracker, get_slot, placeholder handling

---

### Unit 5: Collecting Slots in Flows
**Type**: Lab (with Assessment)  
**Assessment**: Lab 5.1 - Creating a Flow with Slot Collection (suggested points: 6–8)

**Placement**: This unit comes **after** Unit 4 so students create the flow after exploring the action.

**Sections**:
- 5.1 The Collect Step
  - `collect:` syntax and `description:`; Rasa asks when slot is empty
- 5.2 How Collection Works
  - Runtime: ask if empty, store, then action; key point (only asks when empty)
- 5.3 Creating the Flow
  - What you'll build (collect + action); pointer to Lab 5.1 for steps
- Lab 5.1: Creating a Flow with Slot Collection
  - Single place for full step-by-step and YAML

**Key Concepts**: collect step, flow with collect

**Assessment Checks** (Lab 5.1):
- `data/basics/check_balance.yml` exists
- Flow has `collect: account` and `action: action_check_balance_simple`

---

### Unit 6: Training and Testing with Slots
**Type**: Labs (6.1 graded; 6.2 ungraded)  
**Assessment**: Lab 6.1 – Training and Testing with Slots (12 points). Lab 6.2 – Testing Slot Collection (no assessment).

**Sections**:
- 6.1 Training with Slots → **Lab 6.1** (graded)
- 6.2 Testing Slot Collection → **Lab 6.2** (hands-on steps; no assessment)
- 6.3 Understanding Slot State
- 6.4 Common Issues with Slots

**Key Concepts**: Training, testing, Inspector, slot state

**Assessment Checks** (Lab 6.1 only):
- Venv in project root, activated; `cd level3`
- Model file exists in `level3/models/`
- Model recent, no critical errors in logs

---

### Unit 7: Putting It All Together
**Type**: Content + Lab (no assessment)  
**Assessment**: None. Lab 7.1 – Complete Bot Walkthrough (ungraded).

**Sections**:
- 7.1 Complete Bot Walkthrough → **Lab 7.1** (guided demo; no assessment)
- 7.2 Your Level 3 Banking Bot: Summary
- 7.3 Best Practices

**Key Concepts**: Integration, summary, best practices

---

### Unit 8: Assessment and Next Steps
**Type**: Content Page  
**Assessment**: None

**Sections**:
- 8.1 Knowledge Check
- 8.2 What You've Learned
- 8.3 Limitations of Level 3
- 8.4 What's Next: Level 4 Preview
- 8.5 Course Completion Checklist

**Key Concepts**: Review, Level 4 preview

---

## Assessment Summary

| Unit | Lab | Points | Type | Grader Script |
|------|-----|--------|------|---------------|
| Unit 3 | Lab 3.1 | 8 | LLM Rubric (recommended) or Standard Code Test | `lab_3.1_solution_reference.md` / `lab_3.1_grader.sh` |
| Unit 5 | Lab 5.1 | 8 | LLM Rubric (recommended) or Standard Code Test | `lab_5.1_solution_reference.md` / `lab_5.1_grader.sh` |
| Unit 6 | Lab 6.1 | 12 | Standard Code Test (Python) | `lab_6.1_grader.py` |

**Total Assessment Points**: ~24–28 (adjust per course design)

**Conventions** (same as L1/L2):
- Grader runs from **workspace root**; activates venv, then `cd level3`.
- Script prints `PASS` / `Successfully passed!` on full score.
- Codio Working Directory: `/home/codio/workspace`.

---

## File Organization

### Content Files (source of truth in level3/)
- `Level3_Unit0_Content_0.1_*.md`, `Level3_Unit0_Content_0.2_*.md`
- `Level3_Unit1_Content_1.1_*.md` … `1.3_*.md`
- `Level3_Unit2_Content_2.1_*.md`, `2.2_*.md`, `2.3_Test-Your-Knowledge.md`
- `Level3_Unit3_Content_3.1_*.md`
- … (Units 4–8 same pattern)
- Copy into Codio Guide Editor or `.guides/content` when ready.

### Lab Content + Assessment Setup
- `Level3_Lab3.1_Content.md` / `Level3_Lab3.1_Assessment_Setup.md` (graded)
- `Level3_Lab4.1_Content.md` / `Level3_Lab4.1_Assessment_Setup.md` (ungraded, exploration)
- `Level3_Lab5.1_Content.md` / `Level3_Lab5.1_Assessment_Setup.md` (graded)
- `Level3_Lab6.1_Content.md` / `Level3_Lab6.1_Assessment_Setup.md` (graded)
- `Level3_Lab6.2_Content.md` / `Level3_Lab6.2_Assessment_Setup.md` (ungraded, testing)
- `Level3_Lab7.1_Content.md` / `Level3_Lab7.1_Assessment_Setup.md` (ungraded, walkthrough)

### Implementation
- `Level3_Implementation_Overview.md` – Codio team
- `Level3_Course_Outline.md` – This file
- `LEVEL3_DEVELOPMENT_PLAN.md` – Development plan

---

## Technical Requirements

- **Environment**: Same as L1/L2 (Codio or local)
- **Virtual environment**: **One .venv in project root** (created in Lab 0.1). Activate from root, then `cd level3`.
- **Rasa**: Rasa Pro (latest stable)
- **Inspector on Codio**: Use **Rasa Inspect** tab (no Ports / port 5005).
- **Prerequisites**: Level 1 and Level 2 completed.
