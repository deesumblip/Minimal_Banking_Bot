# Level 5: Content, Labs, and Assessments — Mapping and Task IDs

This document maps **Level 5** (Chapter 1.5 – Tool Calling) content files, labs, and assessment task IDs so implementers can sync with Codio and keep graders in one place.

---

## 1. Level 4 → Level 5 mapping

| Level 4 | Level 5 equivalent |
|---------|---------------------|
| **Starter** = Level 3 end state (level4 folder) | **Starter** = Level 4 end state (level5 folder) |
| Unit 0: Your Level 3 agent / What Level 4 adds | Unit 0: Your Level 4 agent / What Level 5 adds |
| Unit 1: Multiple slots (1.1, 1.2, 1.3) | Unit 1: Introduction to tools (1.1, 1.2, 1.3 Test Your Knowledge) |
| Unit 2 + Lab 2.1 (domain: slots + utter_ask_* + action) | Unit 2 + **Lab 2.1** (tools folder + banking_tools.py + __all__) |
| Unit 3 + Lab 3.1 (action_process_transfer) | Unit 3 + **Lab 3.1** (endpoints.yml tools section) |
| Unit 4 + Lab 4.1 (transfer_money flow) | Unit 4 + **Lab 4.1** (transfer_money_tools flow + action_process_transfer_with_tools) |
| Unit 5 + Lab 5.1 (train) + Lab 5.2 (test) | Unit 5 + **Lab 5.1** (train from level5) + **Lab 5.2** (completion check) |
| Unit 6: Walkthrough, summary, limitations, checklist | Unit 6: 6.1–6.7 (walkthrough, learned, next, knowledge check, limitations, Level 6 preview, checklist) |

**Lab numbering:** Level 5 uses Labs 2.1, 3.1, 4.1, 5.1, 5.2. Each is graded (10 points, 50 total).

---

## 2. Unit content files (source of truth in level5/)

| File | Purpose |
|------|---------|
| `Level5_Unit0_Content_0.1_Your-Level-4-Banking-Agent.md` | Recap: level5 = Level 4 agent; what's in domain, flows, actions. |
| `Level5_Unit0_Content_0.2_What-Level-5-Adds.md` | Level 5 adds: tools module, endpoints tools section, transfer_money_tools flow and action. |
| `Level5_Unit1_Content_1.1_Tools-vs-Actions.md` | Tools = LLM selects at runtime; actions = explicit in flow steps. |
| `Level5_Unit1_Content_1.2_When-to-Use-Tools.md` | When to use tools (dynamic selection) vs actions. |
| `Level5_Unit1_Content_1.3_Test-Your-Knowledge.md` | Quiz on Units 0–1 (tools vs actions, registration, __all__). |
| `Level5_Unit2_Content_2.1_Creating-Tool-Functions.md` | tools/ folder, banking_tools.py, __all__. Pointer to Lab 2.1. |
| `Level5_Unit3_Content_3.1_Registering-Tools.md` | endpoints.yml tools section, tools_module. Pointer to Lab 3.1. |
| `Level5_Unit4_Content_4.1_Using-Tools-in-a-Flow.md` | transfer_money_tools flow and action. Pointer to Lab 4.1. |
| `Level5_Unit5_Content_5.1_Training-Level-5.md` | Train from level5. Lab 5.1. |
| `Level5_Unit5_Content_5.2_Testing-Tool-Calling.md` | Completion check and optional Inspector test. Lab 5.2. |
| `Level5_Unit6_Content_6.1_Complete-Agent-Walkthrough.md` | Guided walkthrough of Level 5 agent. |
| `Level5_Unit6_Content_6.2_What-Youve-Learned.md` | Summary: tools module, registration, flow, action. |
| `Level5_Unit6_Content_6.3_Whats-Next.md` | What's next (Level 6, extensions). |
| `Level5_Unit6_Content_6.4_Knowledge-Check.md` | Quiz on Level 5 (tools, endpoints, flow, training). |
| `Level5_Unit6_Content_6.5_Limitations-of-Level-5.md` | What Level 5 cannot do; when to move to Level 6. |
| `Level5_Unit6_Content_6.6_Whats-Next-Level-6-Preview.md` | Sub-agents (Level 6) preview. |
| `Level5_Unit6_Content_6.7_Course-Completion-Checklist.md` | Checklist before Level 6. |

---

## 3. Lab content and assessment task IDs

| Lab | Content File | Assessment Setup File | Task ID (Codio) | Grader / Solution Ref |
|-----|--------------|------------------------|-----------------|------------------------|
| 2.1 | Level5_Lab2.1_Content.md | Level5_Lab2.1_Assessment_Setup.md | code-output-compare-501020001 | .guides/secure/level5_graders/lab_2.1_grader.py, lab_2.1_solution_reference.md |
| 3.1 | Level5_Lab3.1_Content.md | Level5_Lab3.1_Assessment_Setup.md | code-output-compare-501030001 | lab_3.1_grader.py, lab_3.1_solution_reference.md |
| 4.1 | Level5_Lab4.1_Content.md | Level5_Lab4.1_Assessment_Setup.md | code-output-compare-501040001 | lab_4.1_grader.py, lab_4.1_solution_reference.md |
| 5.1 | Level5_Lab5.1_Content.md | Level5_Lab5.1_Assessment_Setup.md | code-output-compare-501050001 | lab_5.1_grader.py, lab_5.1_solution_reference.md |
| 5.2 | Level5_Lab5.2_Content.md | Level5_Lab5.2_Assessment_Setup.md | code-output-compare-501050002 | lab_5.2_grader.py, lab_5.2_solution_reference.md |

**Assessment JSONs:** `.guides/assessments/code-output-compare-501020001.json` through `code-output-compare-501050002.json`. Each COMMAND uses venv Python and `.guides/secure/level5_graders/lab_X.X_grader.py`. Working Directory: `/home/codio/workspace`. Grading uses a **sequence** of `Check N: PASSED` substring matches (Lab 6.2 / Lab 3.1 style), **`showGuidanceAfterResponseOption`: Never**, **`showExpectedAnswerOption`: Always**.

---

## 4. Codio guide (Chapter 1.5)

- **Chapter ID:** Chapter-1-5---Tool-Calling-f9e0
- **Content path:** `.guides/content/Chapter-1-5---Tool-Calling-f9e0/`
- **Lab pages** in the guide include `{Check It!|assessment}(code-output-compare-50XXXXXX)` with the task IDs above.
- **Graders:** All in `.guides/secure/level5_graders/`. No grader scripts live under `.guides/assessments/`.

---

## 5. Summary table

| Item | Location / Value |
|------|------------------|
| Chapter | Chapter-1-5---Tool-Calling-f9e0 |
| Units | 0–6 (7 units) |
| Graded labs | 2.1, 3.1, 4.1, 5.1, 5.2 (10 points each, 50 total) |
| Task IDs | 501020001, 501030001, 501040001, 501050001, 501050002 |
| Graders | .guides/secure/level5_graders/lab_2.1_grader.py … lab_5.2_grader.py |
| Solution refs | .guides/secure/level5_graders/lab_*_solution_reference.md |
| Source content | level5/Level5_Unit*_Content_*.md, level5/Level5_Lab*_Content.md |

For step-by-step implementation (Codio vs local, COMMAND strings, grading tab setup), use **Level5_Lab*_Assessment_Setup.md** and **Level5_Implementation_Overview.md**.
