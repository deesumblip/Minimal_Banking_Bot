# Level 1: Just Responses - Course Outline

## Course Overview

**Title**: Level 1: Just Responses  
**Description**: A Complete Guide to Building Your First Rasa Agent  
**Prerequisites**: Basic Python, command line, text editor  
**Learning Objective**: Students build a working banking assistant agent that can greet users, provide information, and handle basic conversations using responses and flows only (no actions or slots).

---

## Course Structure

### Unit 0: Prerequisites and Setup
**Type**: Content + Lab  
**Assessment**: Lab 0.1 (Virtual Environment and Install Rasa Pro)

**Sections**:
- 0.1 What You Need Before Starting
- 0.2 Project Structure
- 0.4 Getting Help
- Lab 0.1: Create Virtual Environment and Install Rasa Pro

**Key Concepts**: Environment, project layout, where to get help

**Note:** Unit **0.3** (YAML syntax) is not included in the Codio guide TOC; optional mirror files may exist under `level1/`.

---

### Unit 1: Introduction to Rasa Agents
**Type**: Content Page  
**Assessment**: Concept Check (optional)

**Sections**:
- 1.1 What is a Conversational Agent?
- 1.2 The Simplest Agent Possible

**Key Concepts**: Conversational agents, NLU, Level 1 scope and limitations

**Note:** Unit **1.3** (real-world use cases) and **1.4** (test your knowledge) are not in the Codio guide TOC; optional mirror files may exist under `level1/`.

---

### Unit 2: Understanding the Domain File
**Type**: Content + Labs  
**Assessments**: Lab 2.2, Lab 2.3 (as configured)

**Sections**:
- 2.1 What is a Domain?
- 2.2 Understanding Responses
- Lab 2.2: Creating Your First Response
- Lab 2.3: Add Response Variations

**Key Concepts**: Domain file, responses, YAML structure for responses

**Note:** **Lab 2.1** (YAML syntax for responses) is not in the Codio guide TOC; `Level1_Lab2.1_Content.md` may remain as reference only.

---

### Unit 3: Understanding Flows
**Type**: Content + Labs  
**Assessments**: Lab 3.1–3.5 (as configured)

**Sections**:
- 3.1 What is a Flow?
- Lab 3.1: Exploring Existing Flows
- 3.2 Flow Structure Deep Dive
- Lab 3.2: Creating Your First Flow
- Lab 3.3: Multi-Step Flow
- 3.3 Flow Descriptions and LLM Understanding
- Lab 3.4: Flow Descriptions and LLM Matching
- Lab 3.5: Complete Your Agent for Training
- 3.4 Test Your Knowledge

**Key Concepts**: Flows, steps, flow descriptions, LLM matching

---

### Unit 4: System Patterns
**Type**: Content + Labs  
**Assessments**: Lab 4.1, Lab 4.2 (as configured)

**Sections**:
- 4.1 What are System Patterns?
- 4.2 Session Start Pattern
- 4.3 Pattern Completed
- Lab 4.1: Understanding System Patterns
- 4.4 Modifying System Patterns
- Lab 4.2: Modifying System Patterns

**Key Concepts**: Session start, pattern completed, lifecycle

---

### Unit 5: Configuration Files
**Type**: Content + Lab  
**Assessment**: Lab 5.1 (as configured)

**Sections**:
- 5.1 The config.yml File
- 5.2 credentials.yml
- 5.3 endpoints.yml
- Lab 5.1: Configuration Exploration

**Key Concepts**: config.yml, credentials, endpoints

---

### Unit 6: Training and Testing
**Type**: Content + Labs  
**Assessment**: Lab 6.1 (Training Your Agent)

**Sections** (Codio TOC order):
- 6.1 Training: What It Does and How to Run It
- Lab 6.1: Training Your Agent
- Lab 6.2: Using Rasa Inspector
- 6.2 Testing Your Agent (reading; testing workflow)

**Key Concepts**: Training, Inspector, testing workflow

**Note:** The former guide page **6.4 Understanding Agent Behavior** was removed from the Codio TOC. Mirror files `Level1_Unit6_Content_6.2_Using-Rasa-Inspector.md`, `Level1_Unit6_Content_6.4_Testing-Your-Agent.md`, and `Level1_Unit6_Content_6.5_Understanding-Agent-Behavior.md` may still exist under `level1/`; numbering does not match Codio page slugs one-to-one. **`Level1_Lab6.3_Content.md`** is not linked as a separate Codio page in the current unit order.

---

### Unit 7: Putting It All Together
**Type**: Content + Labs  
**Assessments**: Lab 7.1, 7.2 (as configured)

**Sections**:
- 7.1 Complete Agent Walkthrough
- Lab 7.1: Complete Agent Walkthrough
- 7.2 Your Level 1 Banking Agent: Summary
- Lab 7.2: Build Your Own Feature (Project)

**Key Concepts**: Integration, summary

---

### Unit 8: Assessment and Next Steps
**Type**: Content Page  
**Assessment**: Knowledge Check (optional)

**Sections**:
- 8.1 Knowledge Check
- 8.3 Limitations of Level 1

**Key Concepts**: Review, limitations

**Note:** **8.2**, **8.4**, and **8.5** are not in the Codio guide TOC; optional mirror files may exist under `level1/`.

---

## File Organization

### Content Files (one per numbered subsection)
- **Unit 0**: `Level1_Unit0_Content_0.1_What-You-Need-Before-Starting.md`, `Level1_Unit0_Content_0.2_Project-Structure.md`, `Level1_Unit0_Content_0.4_Getting-Help.md` (plus optional mirror `0.3` not in Codio TOC)
- **Unit 1**: `Level1_Unit1_Content_1.1_What-is-a-Conversational-Agent.md`, `Level1_Unit1_Content_1.2_The-Simplest-Agent-Possible.md` (plus optional mirrors `1.3`, `1.4` not in Codio TOC)
- **Units 2–8**: `Level1_UnitN_Content_N.M_*.md` (see level1 folder for full list)

### Lab Content (student-facing)
- `Level1_Lab0.1_Content.md`, `Level1_Lab2.2_Content.md`, `Level1_Lab2.3_Content.md` (`Level1_Lab2.1_Content.md` optional / not in Codio TOC)
- `Level1_Lab3.1_Content.md` … `Level1_Lab3.4_Content.md`
- `Level1_Lab4.1_Content.md`, `Level1_Lab4.2_Content.md`
- `Level1_Lab5.1_Content.md`
- `Level1_Lab6.1_Content.md`, `Level1_Lab6.2_Content.md`, `Level1_Lab6.3_Content.md`
- `Level1_Lab7.1_Content.md`, `Level1_Lab7.2_Content.md`

### Assessment Setup (for implementers)
- `Level1_Lab0.1_Assessment_Setup.md`, `Level1_Lab3.5_Assessment_Setup.md`, `Level1_Lab6.1_Assessment_Setup.md`, `Level1_Lab7.2_Assessment_Setup.md` (one per graded lab that involves file manipulation)

### Implementation Files
- `Level1_Implementation_Overview.md` – Codio team guide
- `Level1_Course_Outline.md` – This file

---

## Learning Path

```
Unit 0: Prerequisites and Setup ✓ Lab 0.1
    ↓
Unit 1: Introduction to Rasa Agents
    ↓
Unit 2: Understanding the Domain File ✓ Labs 2.1, 2.2, 2.3
    ↓
Unit 3: Understanding Flows ✓ Labs 3.1–3.5
    ↓
Unit 4: System Patterns ✓ Labs 4.1, 4.2
    ↓
Unit 5: Configuration Files ✓ Lab 5.1
    ↓
Unit 6: Training and Testing ✓ Lab 6.1, 6.2
    ↓
Unit 7: Putting It All Together ✓ Labs 7.1, 7.2
    ↓
Unit 8: Assessment and Next Steps
```

---

## Key Learning Outcomes

By the end of Level 1, students should be able to:

1. Explain what a conversational agent is and what Level 1 includes (responses only).
2. Edit the domain file to add and vary responses.
3. Create and modify flows and understand flow descriptions.
4. Configure system patterns (session start, pattern completed).
5. Train the agent and test it using Rasa Inspector.
6. Describe limitations of Level 1 and what Level 2 adds.

---

## Technical Requirements

- **Environment**: Codio (Linux) or local (Python 3.11)
- **Rasa**: Rasa Pro (latest stable)
- **Port Forwarding**: Required for Unit 6 (Rasa Inspector, port 5005)

---

## Estimated Time

- **Unit 0**: 30–45 minutes  
- **Units 1–2**: 45–60 minutes  
- **Units 3–5**: 1–1.5 hours  
- **Unit 6**: 45–60 minutes (training + Inspector)  
- **Units 7–8**: 30–45 minutes  

**Total**: 2–3 hours (thorough completion)
