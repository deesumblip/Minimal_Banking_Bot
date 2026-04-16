# Level 2: Content, Labs, and Assessments

This document maps Level 2 – Custom Actions unit content files, lab content files, and assessment task IDs / grader paths so implementers can sync with Codio.

---

## 1. Course structure

Level 2 uses **7 units** (0–6): Recap → Introduction to Actions → Action Class → Create Action (Lab 3.1) → Register Actions (Lab 4.1) → Flows (Lab 5.1) → Training and wrap-up (Labs 6.1, 6.2, pages 6.2–6.3, then **6.4** *See it all together*, then **6.5** *Before you continue*; former standalone Unit 7 and merged Unit 8 material are split across those two pages).

- **Course outline:** `level2/Level2_Course_Outline.md` — unit/section names, lab list, learning path.

---

## 2. Unit content files (source of truth in level2/)

| File | Purpose |
|------|---------|
| `Level2_Unit0_Content_0.1_Your-Level-1-Banking-Agent.md` | Recap Level 1; Level 2 preview under **What's new in Level 2** (single Unit 0 page) |
| `Level2_Unit1_Content_1.1_*.md` … `1.3_*.md` | What is an action, how they work, action class structure |
| `Level2_Unit2_Content_2.1_*.md`, `2.2_*.md` | Action class deep dive, parameters (dispatcher, tracker, domain) |
| `Level2_Unit3_Content_3.1_Step-by-Step-Creating-an-Action.md` | **Deprecated:** duplicate of Unit 2.1; Codio guide opens with **Lab 3.1** instead. Keep file as stub or delete locally. |
| `Level2_Unit3_Content_3.2_Understanding-Action-Execution.md` | **Deprecated:** merged into end of Lab 3.1 in the guide. |
| `Level2_Unit4_Content_4.1_Why-Register-Actions.md` | Domain registration, Lab 4.1 |
| `Level2_Unit5_Content_5.1_Actions-vs-Responses-in-Flows.md` | Actions vs responses in flows; mixing both in one flow (former 5.2 merged here) |
| `Level2_Unit6_Content_6.2_*.md`, `6.3_*.md` | Common training errors; testing and debugging (former **6.4 debugging** page merged into **6.3**); **Lab 6.1** is **`Level2_Lab6.1_Content.md`** only |
| `Level2_Unit6_Content_6.4_Level-2-Wrap-Up.md` | Codio title **6.4 See it all together** — walkthrough, structure, practices, **5× MC knowledge check** |
| `Level2_Unit6_Content_6.5_Core-Ideas-and-Level-3-Readiness.md` | Codio title **6.5 Before you continue** — short checkpoint; detailed Level 3 handoff is Level 3 **0-1** / **0-2** |
| `Level2_Troubleshooting_Content.md`, `Level2_AdditionalResources_Content.md` | Troubleshooting, extensions |

---

## 3. Lab content and assessment task IDs / graders

| Lab | Content File | Assessment Setup File | Task ID (Codio) | Grader Path |
|-----|--------------|------------------------|-----------------|-------------|
| 2.1 (optional) | — | Level2_Lab2.1_Assessment.md | — | Optional MC/FIB; explore actions folder |
| 3.1 | Level2_Lab3.1_Content.md | Level2_Lab3.1_Assessment_Setup.md | fill-in-the-blanks-201030010 → code-output-compare-2266471391 | .guides/secure/level2_graders/lab_3.2_grader.sh |
| 4.1 | Level2_Lab4.1_Content.md | Level2_Lab4.1_Assessment_Setup.md | — | .guides/secure/level2_graders/lab_4.1_grader.sh |
| 5.1 | Level2_Lab5.1_Content.md | Level2_Lab5.1_Assessment_Setup.md | — | .guides/secure/level2_graders/lab_5.1_grader.sh |
| 6.1 | Level2_Lab6.1_Content.md | Level2_Lab6.1_Assessment_Setup.md | — | .guides/secure/level2_graders/lab_6.1_grader.sh |
| 6.2 | Level2_Lab6.2_Content.md | Level2_Lab6.2_Assessment_Setup.md | code-output-compare-1597644299 | .guides/secure/level2_graders/lab_4.2_grader.sh |

**Execution:** Code Test graders are run from the workspace (e.g. `bash /home/codio/workspace/.guides/secure/level2_graders/lab_3.2_grader.sh` for Lab 3.1). Working directory for labs: `/home/codio/workspace/level2`. Do not upload grader scripts into the assessment; run from workspace so `git pull` updates them.

---

## 4. Summary table

| Item | Location / Value |
|------|------------------|
| Course outline | level2/Level2_Course_Outline.md |
| Units | 0–6 |
| Graded labs | 3.1, 4.1, 5.1, 6.1, 6.2 |
| Task ID (example) | code-output-compare-1597644299 (Lab 6.2) |
| Graders | .guides/secure/level2_graders/lab_*.sh |
| Source content | level2/Level2_Unit*_Content_*.md, level2/Level2_Lab*_Content.md |

For step-by-step implementation (COMMAND strings, grading tab), use **Level2_Lab*_Assessment_Setup.md** and **Level2_Implementation_Overview.md**.
