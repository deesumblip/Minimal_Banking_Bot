# Level 6: Content, Labs, and Assessments — Mapping and Task IDs

This document maps **Level 6** (Chapter 1.6 – Sub-Agents) content files, labs, and assessment task IDs.

---

## 1. Level 5 → Level 6 mapping

| Level 5 | Level 6 equivalent |
|---------|---------------------|
| **Starter** = Level 5 end state (level6 folder) | level6 = Level 5 agent + sub-agent layer |
| Unit 0: Recap - What you built in Level 4 / What Level 5 adds | Unit 0: Recap - What you built in Level 5 / What Level 6 adds |
| Unit 1: Introduction to tools | Unit 1: Sub-agents concept (what they are, when to use) |
| Unit 2 + Lab 2.1 (tools folder) | Unit 2 + **Lab 2.1** (sub_agents/banking_assistant config) |
| Unit 3 + Lab 3.1 (endpoints tools) | Unit 3 + **Lab 3.1** (endpoints mcp_servers) |
| Unit 4 + Lab 4.1 (transfer_money_tools flow) | Unit 4 + **Lab 4.1** (ask_banking_assistant flow) |
| Unit 5 + Labs 5.1, 5.2 | Unit 5 + **Lab 5.1** (train), **Lab 5.2** (completion check) |
| Unit 6: 6.1–6.7 | Unit 6: 6.1–6.7 (walkthrough, learned, next, knowledge check, limitations, beyond course, checklist) |

**Lab numbering:** Level 6 uses Labs 2.1, 3.1, 4.1, 5.1, 5.2. Each is graded (10 points, 50 total).

---

## 2. Unit content files (source of truth in level6/)

| File | Purpose |
|------|---------|
| Level6_Unit0_Content_0.1_Your-Level-5-Banking-Agent.md | Recap: level6 = Level 5 agent; what remains. |
| Level6_Unit0_Content_0.2_What-Level-6-Adds.md | Level 6 adds: sub-agent, flow that calls it, MCP registration. |
| Level6_Unit1_Content_1.1_What-Are-Sub-Agents.md | Sub-agents = flow step call: agent_name; hand off, run until done, return. |
| Level6_Unit1_Content_1.2_When-to-Use-Sub-Agents.md | When to use sub-agents vs tools in main agent. |
| Level6_Unit2_Content_2.1_Sub-Agent-Layout-and-Config.md | sub_agents/<name>/config.yml; full example. Pointer to Lab 2.1. |
| Level6_Unit3_Content_3.1_MCP-and-ReAct-Config.md | endpoints.yml mcp_servers; full example. Pointer to Lab 3.1. |
| Level6_Unit4_Content_4.1_Flow-that-Calls-Sub-Agent.md | ask_banking_assistant flow YAML; full example. Pointer to Lab 4.1. |
| Level6_Unit5_Content_5.1_Training-Level-6.md | Train from level6. Lab 5.1. |
| Level6_Unit5_Content_5.2_Testing-Sub-Agents.md | Run MCP server, actions, Rasa; Inspector. Lab 5.2. |
| Level6_Unit6_Content_6.1 through 6.7 | Walkthrough, learned, next, knowledge check, limitations, beyond course, checklist. |

---

## 3. Lab content and assessment task IDs

| Lab | Content File | Assessment Setup File | Task ID (Codio) | Grader |
|-----|--------------|------------------------|-----------------|--------|
| 2.1 | Level6_Lab2.1_Content.md | Level6_Lab2.1_Assessment_Setup.md | code-output-compare-501060001 | .guides/secure/level6_graders/lab_2.1_grader.py |
| 3.1 | Level6_Lab3.1_Content.md | Level6_Lab3.1_Assessment_Setup.md | code-output-compare-501060002 | lab_3.1_grader.py |
| 4.1 | Level6_Lab4.1_Content.md | Level6_Lab4.1_Assessment_Setup.md | code-output-compare-501060003 | lab_4.1_grader.py |
| 5.1 | Level6_Lab5.1_Content.md | Level6_Lab5.1_Assessment_Setup.md | code-output-compare-501060004 | lab_5.1_grader.py |
| 5.2 | Level6_Lab5.2_Content.md | Level6_Lab5.2_Assessment_Setup.md | code-output-compare-501060005 | lab_5.2_grader.py |

**Assessment JSONs:** `.guides/assessments/code-output-compare-501060001.json` through `501060005.json`. COMMAND uses `.guides/secure/level6_graders/lab_*.py`. Working Directory: `/home/codio/workspace`. **Sequence:** `Check 1: PASSED` … (per lab), Lab 6.2 / Lab 3.1 style; **`showGuidanceAfterResponseOption`: Never**; **`showExpectedAnswerOption`: Always**.

---

## 4. Codio guide (Chapter 1.6)

- **Chapter ID:** Chapter-1-6---Sub-Agents-c7d8
- **Content path:** `.guides/content/Chapter-1-6---Sub-Agents-c7d8/`
- **Graders:** All in `.guides/secure/level6_graders/`.

---

## 5. Summary table

| Item | Location / Value |
|------|------------------|
| Chapter | Chapter-1-6---Sub-Agents-c7d8 |
| Units | 0–6 |
| Graded labs | 2.1, 3.1, 4.1, 5.1, 5.2 (10 points each, 50 total) |
| Task IDs | 501060001 – 501060005 |
| Graders | .guides/secure/level6_graders/lab_2.1_grader.py … lab_5.2_grader.py |
| Source content | level6/Level6_Unit*_Content_*.md, level6/Level6_Lab*_Content.md |
