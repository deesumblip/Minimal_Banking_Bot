# Level 5: Tool Calling - Course Outline

## Course Overview

**Title**: Level 5: Tool Calling  
**Description**: Adding LLM-Driven Tool Selection to Your Banking Agent  
**Prerequisites**: Level 1, Level 2, Level 3, and Level 4 must be completed  
**Learning Objective**: Students learn to define tools (functions the LLM can call), register them in endpoints.yml, and use them in a flow so the main agent's LLM dynamically selects and invokes tools based on conversation context. Labs are ordered: tools folder (Lab 2.1) -> register tools (Lab 3.1) -> flow and action (Lab 4.1) -> train and test (Labs 5.1, 5.2).

---

## Course Structure (7 units: 0-6)

### Unit 0: Recap - What you built in Level 4
**Type**: Content Page | **Assessment**: None
**Sections**: 0.1 Your Level 4 Banking Agent | 0.2 What Level 5 Adds
**Key Concepts**: Recap of Level 4 / Level 4 completion; **`level5/`** as the working tree; how git **`level4/`** relates to **`level5/`** (page 0.1); what Level 5 adds (tools, `tools_module`, `transfer_money_tools` flow).

### Unit 1: Introduction to Tools
**Type**: Content Page | **Assessment**: None
**Sections**: 1.1 Tools vs Actions | 1.2 When to Use Tools | 1.3 Test Your Knowledge
**Key Concepts**: Tools = functions the LLM selects at runtime; actions = explicitly called in flows.

### Unit 2: Creating Tool Functions
**Type**: Content + Lab | **Assessment**: Lab 2.1
**Sections**: 2.1 Creating Tool Functions + Lab 2.1
**Key Concepts**: tools/ folder, banking_tools.py, __all__, docstrings, return dicts.

### Unit 3: Registering Tools
**Type**: Content + Lab | **Assessment**: Lab 3.1
**Sections**: 3.1 Registering Tools + Lab 3.1
**Key Concepts**: endpoints.yml tools section, tools_module.

### Unit 4: Using Tools in Conversations
**Type**: Content + Lab | **Assessment**: Lab 4.1
**Sections**: 4.1 Using Tools in a Flow + Lab 4.1
**Key Concepts**: transfer_money_tools.yml, action_process_transfer_with_tools.

### Unit 5: Training and Testing
**Type**: Content + Labs | **Assessment**: Lab 5.1, Lab 5.2
**Sections**: 5.1 Training Level 5 | Lab 5.1 | 5.2 Testing Tool Calling | Lab 5.2 (linear: concept, lab, concept, lab)
**Key Concepts**: Train from level5; completion check.

### Unit 6: Summary and Next Steps
**Type**: Content Page | **Assessment**: None
**Sections**: 6.1 Complete Agent Walkthrough | 6.2 What You've Learned | 6.3 What's Next | 6.4 Knowledge Check | 6.5 Limitations of Level 5 | 6.6 What's Next: Level 6 Preview | 6.7 Course Completion Checklist
**Key Concepts**: Level 5 summary; next steps (Level 6 sub-agents); knowledge check; limitations; Level 6 preview; completion checklist.

---

## Assessment Summary
Labs 2.1, 3.1, 4.1, 5.1, 5.2 - each 10 points, total 50. Graders in .guides/secure/level5_graders/.

## Codio guide folder ID
Use unique ID for Level 5: e.g. Chapter-1-5---Tool-Calling-f9e0 (suffix f9e0; do not reuse d3b4, 30d6, a4b5, e5f6).

---

## Assessment Summary

| Lab   | Points | Type                    | Grader Script / Solution Ref                    |
|-------|--------|-------------------------|-------------------------------------------------|
| 2.1   | 10     | LLM Rubric or Code Test | lab_2.1_grader.py / lab_2.1_solution_reference.md |
| 3.1   | 10     | LLM Rubric or Code Test | lab_3.1_grader.py / lab_3.1_solution_reference.md |
| 4.1   | 10     | LLM Rubric or Code Test | lab_4.1_grader.py / lab_4.1_solution_reference.md |
| 5.1   | 10     | Code Test               | lab_5.1_grader.py / lab_5.1_solution_reference.md |
| 5.2   | 10     | Code Test (completion)  | lab_5.2_grader.py / lab_5.2_solution_reference.md |

**Total assessment points**: 50. All graders in `.guides/secure/level5_graders/`. Codio: use **substring match** for expected output `PASS`, Working Directory `/home/codio/workspace`, venv Python in COMMAND.

---

## File Organization (Sync to Codio)

All source files live in **level5/**. When creating the Level 5 chapter in Codio, use a **unique chapter ID** so it does not overlap with existing content in `.guides/content/`.

### Codio guide folder ID (do not overlap)

Existing: Chapter-1-1 (d3b4), Chapter-1-2 (30d6), Chapter-1-3 (a4b5), Chapter-1-4 (e5f6). Use **Chapter-1-5---Tool-Calling-f9e0** (suffix f9e0). Ensure unit and page IDs under this chapter are also unique.

### Unit Content (one file per section)

| Unit | File |
|------|------|
| 0.1 | Level5_Unit0_Content_0.1_Your-Level-4-Banking-Agent.md |
| 0.2 | Level5_Unit0_Content_0.2_What-Level-5-Adds.md |
| 1.1 | Level5_Unit1_Content_1.1_Tools-vs-Actions.md |
| 1.2 | Level5_Unit1_Content_1.2_When-to-Use-Tools.md |
| 2.1 | Level5_Unit2_Content_2.1_Creating-Tool-Functions.md |
| 3.1 | Level5_Unit3_Content_3.1_Registering-Tools.md |
| 4.1 | Level5_Unit4_Content_4.1_Using-Tools-in-a-Flow.md |
| 5.1 | Level5_Unit5_Content_5.1_Training-Level-5.md |
| 5.2 | Level5_Unit5_Content_5.2_Testing-Tool-Calling.md |
| 6.1 | Level5_Unit6_Content_6.1_Complete-Agent-Walkthrough.md |
| 6.2 | Level5_Unit6_Content_6.2_What-Youve-Learned.md |
| 6.3 | Level5_Unit6_Content_6.3_Whats-Next.md |

### Lab Content + Assessment Setup

| Lab   | Content File              | Assessment Setup File                 |
|-------|---------------------------|---------------------------------------|
| 2.1   | Level5_Lab2.1_Content.md  | Level5_Lab2.1_Assessment_Setup.md     |
| 3.1   | Level5_Lab3.1_Content.md  | Level5_Lab3.1_Assessment_Setup.md     |
| 4.1   | Level5_Lab4.1_Content.md  | Level5_Lab4.1_Assessment_Setup.md     |
| 5.1   | Level5_Lab5.1_Content.md  | Level5_Lab5.1_Assessment_Setup.md     |
| 5.2   | Level5_Lab5.2_Content.md  | Level5_Lab5.2_Assessment_Setup.md     |

### Graders

`.guides/secure/level5_graders/lab_2.1_grader.py` through `lab_5.2_grader.py`, and `lab_2.1_solution_reference.md` through `lab_5.2_solution_reference.md`.

---

## Technical Requirements

- **Environment**: Same as Level 4 (Codio or local)
- **Virtual environment**: One .venv in project root. Activate from root, then `cd level5`.
- **Rasa**: Rasa Pro (latest stable)
- **Inspector on Codio**: Use Rasa Inspect tab (no Ports / 5005).
- **Prerequisites**: Level 1, 2, 3, and 4 completed.
