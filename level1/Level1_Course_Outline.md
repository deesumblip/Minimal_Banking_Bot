# Level 1: Just Responses - Course Outline

## Course Overview

**Title**: Level 1: Just Responses  
**Description**: A Complete Guide to Building Your First Rasa Bot  
**Prerequisites**: Basic Python, command line, text editor  
**Learning Objective**: Students build a working banking assistant bot that can greet users, provide information, and handle basic conversations using responses and flows only (no actions or slots).

---

## Course Structure

### Unit 0: Prerequisites and Setup
**Type**: Content + Lab  
**Assessment**: Lab 0.1 (Virtual Environment and Install Rasa Pro)

**Sections**:
- 0.1 What You Need Before Starting
- 0.2 Project Structure
- Lab 0.1: Create Virtual Environment and Install Rasa Pro
- 0.3 Understanding YAML Syntax
- 0.4 Getting Help

**Key Concepts**: Environment, project layout, YAML basics

---

### Unit 1: Introduction to Rasa Bots
**Type**: Content Page  
**Assessment**: Concept Check (optional)

**Sections**:
- 1.1 What is a Conversational Bot?
- 1.2 The Simplest Bot Possible
- 1.3 Real-World Use Cases
- 1.4 Test Your Knowledge

**Key Concepts**: Conversational bots, NLU, Level 1 scope and limitations

---

### Unit 2: Understanding the Domain File
**Type**: Content + Labs  
**Assessments**: Lab 2.1, Lab 2.2, Lab 2.3 (as configured)

**Sections**:
- 2.1 What is a Domain?
- 2.2 Understanding Responses
- Lab 2.1: YAML Syntax for Responses
- Lab 2.2: Creating Your First Response
- 2.3 Response Variations
- Lab 2.3: Add Response Variations

**Key Concepts**: Domain file, responses, YAML syntax for responses

---

### Unit 3: Understanding Flows
**Type**: Content + Labs  
**Assessments**: Lab 3.1–3.4 (as configured)

**Sections**:
- 3.1 What is a Flow?
- Lab 3.1: Exploring Existing Flows
- 3.2 Flow Structure Deep Dive
- Lab 3.2: Creating Your First Flow
- Lab 3.3: Multi-Step Flow
- 3.4 Flow Descriptions and LLM Understanding
- Lab 3.4: Flow Descriptions and LLM Matching

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
**Assessment**: Lab 6.1 (Training Your Bot)

**Sections**:
- 6.1 What is Training?
- 6.2 How to Train Your Bot
- Lab 6.1: Training Your Bot
- 6.3 Using Rasa Inspector
- Lab 6.2: Using Rasa Inspector
- 6.4 Testing Your Bot
- Lab 6.3: Testing Your Bot
- 6.5 Understanding Bot Behavior

**Key Concepts**: Training, Inspector, testing workflow

---

### Unit 7: Putting It All Together
**Type**: Content + Labs  
**Assessments**: Lab 7.1, 7.2, 7.3 (as configured)

**Sections**:
- 7.1 Complete Bot Walkthrough
- Lab 7.1: Complete Bot Walkthrough
- 7.2 Your Level 1 Banking Bot: Summary
- 7.3 Best Practices
- Lab 7.2: Build Your Own Feature (Project)
- Lab 7.3: Best Practices Application

**Key Concepts**: Integration, summary, best practices

---

### Unit 8: Assessment and Next Steps
**Type**: Content Page  
**Assessment**: Knowledge Check (optional)

**Sections**:
- 8.1 Knowledge Check
- 8.2 What You've Learned
- 8.3 Limitations of Level 1
- 8.4 What's Next: Level 2 Preview
- 8.5 Course Completion Checklist

**Key Concepts**: Review, limitations, Level 2 preview

---

## File Organization

### Content Files (one per numbered subsection)
- **Unit 0**: `Level1_Unit0_Content_0.1_What-You-Need-Before-Starting.md`, `Level1_Unit0_Content_0.2_Project-Structure.md`, `Level1_Unit0_Content_0.3_Understanding-YAML-Syntax.md`, `Level1_Unit0_Content_0.4_Getting-Help.md`
- **Unit 1**: `Level1_Unit1_Content_1.1_What-is-a-Conversational-Bot.md` … `Level1_Unit1_Content_1.4_Test-Your-Knowledge.md`
- **Units 2–8**: `Level1_UnitN_Content_N.M_*.md` (see level1 folder for full list)

### Lab Content (student-facing)
- `Level1_Lab0.1_Content.md`, `Level1_Lab2.1_Content.md`, `Level1_Lab2.2_Content.md`, `Level1_Lab2.3_Content.md`
- `Level1_Lab3.1_Content.md` … `Level1_Lab3.4_Content.md`
- `Level1_Lab4.1_Content.md`, `Level1_Lab4.2_Content.md`
- `Level1_Lab5.1_Content.md`
- `Level1_Lab6.1_Content.md`, `Level1_Lab6.2_Content.md`, `Level1_Lab6.3_Content.md`
- `Level1_Lab7.1_Content.md`, `Level1_Lab7.2_Content.md`, `Level1_Lab7.3_Content.md`

### Assessment Setup (for implementers)
- `Level1_Lab0.1_Assessment_Setup.md`, `Level1_Lab6.1_Assessment_Setup.md`, `Level1_Lab7.2_Assessment_Setup.md`, `Level1_Lab7.3_Assessment_Setup.md` (one per graded lab that involves file manipulation)

### Implementation Files
- `Level1_Implementation_Overview.md` – Codio team guide
- `Level1_Course_Outline.md` – This file
- `CODIO_IMPLEMENTATION_GUIDE_OPTIMISED.md` – Full optimized guide (reference; content is split into the files above)

---

## Learning Path

```
Unit 0: Prerequisites and Setup ✓ Lab 0.1
    ↓
Unit 1: Introduction to Rasa Bots
    ↓
Unit 2: Understanding the Domain File ✓ Labs 2.1, 2.2, 2.3
    ↓
Unit 3: Understanding Flows ✓ Labs 3.1–3.4
    ↓
Unit 4: System Patterns ✓ Labs 4.1, 4.2
    ↓
Unit 5: Configuration Files ✓ Lab 5.1
    ↓
Unit 6: Training and Testing ✓ Lab 6.1, 6.2, 6.3
    ↓
Unit 7: Putting It All Together ✓ Labs 7.1–7.3
    ↓
Unit 8: Assessment and Next Steps
```

---

## Key Learning Outcomes

By the end of Level 1, students should be able to:

1. Explain what a conversational bot is and what Level 1 includes (responses only).
2. Edit the domain file to add and vary responses.
3. Create and modify flows and understand flow descriptions.
4. Configure system patterns (session start, pattern completed).
5. Train the bot and test it using Rasa Inspector.
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
