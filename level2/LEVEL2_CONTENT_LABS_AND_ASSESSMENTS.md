# Level 2: Content, Labs, and Assessments

This document maps Level 2 (Chapter 1.2 – Custom Actions) unit content files, lab content files, and assessment task IDs / grader paths so implementers can sync with Codio.

---

## 1. Course structure

Level 2 uses **9 units** (0–8): Recap → Introduction to Actions → Action Class → Create Action (Lab 3.1) → Register Actions (Lab 4.1) → Flows (Lab 5.1) → Training (Labs 6.1, 6.2) → Putting It All Together → Assessment.

- **Course outline:** `level2/Level2_Course_Outline.md` — unit/section names, lab list, learning path.

---

## 2. Unit content files (source of truth in level2/)

| File | Purpose |
|------|---------|
| `Level2_Unit0_Content_0.1_*.md`, `0.2_*.md` | Recap Level 1, What Level 2 adds |
| `Level2_Unit1_Content_1.1_*.md` … `1.3_*.md` | What is an action, how they work, action class structure |
| `Level2_Unit2_Content_2.1_*.md`, `2.2_*.md` | Action class deep dive, parameters (dispatcher, tracker, domain) |
| `Level2_Unit3_Content_3.1_Step-by-Step-Creating-an-Action.md` | Full action_bank_hours example, pointer to Lab 3.1 |
| `Level2_Unit3_Content_3.2_Understanding-Action-Execution.md` | How Rasa executes actions |
| `Level2_Unit4_Content_4.1_Why-Register-Actions.md` | Domain registration, Lab 4.1 |
| `Level2_Unit5_Content_5.1_Actions-vs-Responses-in-Flows.md` | Actions in flows, hours example |
| `Level2_Unit6_Content_6.1_Training-with-Actions.md` | Training with actions, holiday_hours.yml |
| Units 7–8 | Putting It All Together, Assessment, Next Steps |
| `Level2_Troubleshooting_Content.md`, `Level2_AdditionalResources_Content.md` | Troubleshooting, extensions |

---

## 3. Lab content and assessment task IDs / graders

| Lab | Content File | Assessment Setup File | Task ID (Codio) | Grader Path |
|-----|--------------|------------------------|-----------------|-------------|
| 2.1 (optional) | — | Level2_Lab2.1_Assessment.md | — | Optional MC/FIB; explore actions folder |
| 3.1 | Level2_Lab3.1_Content.md | Level2_Lab3.1_Assessment_Setup.md | — | .guides/secure/level2_graders/lab_3.1_grader.sh |
| 4.1 | Level2_Lab4.1_Content.md | Level2_Lab4.1_Assessment_Setup.md | — | .guides/secure/level2_graders/lab_4.1_grader.sh |
| 5.1 | Level2_Lab5.1_Content.md | Level2_Lab5.1_Assessment_Setup.md | — | .guides/secure/level2_graders/lab_5.1_grader.sh |
| 6.1 | Level2_Lab6.1_Content.md | Level2_Lab6.1_Assessment_Setup.md | — | .guides/secure/level2_graders/lab_6.1_grader.sh |
| 6.2 | Level2_Lab6.2_Content.md | Level2_Lab6.2_Assessment_Setup.md | code-output-compare-1597644299 | .guides/secure/level2_graders/lab_4.2_grader.sh |

**Execution:** Graders are run from the workspace (e.g. `bash /home/codio/workspace/.guides/secure/level2_graders/lab_3.1_grader.sh`). Working directory for labs: `/home/codio/workspace/level2`. Do not upload grader scripts into the assessment; run from workspace so `git pull` updates them.

---

## 4. Summary table

| Item | Location / Value |
|------|------------------|
| Course outline | level2/Level2_Course_Outline.md |
| Units | 0–8 |
| Graded labs | 3.1, 4.1, 5.1, 6.1, 6.2 |
| Task ID (example) | code-output-compare-1597644299 (Lab 6.2) |
| Graders | .guides/secure/level2_graders/lab_*.sh |
| Source content | level2/Level2_Unit*_Content_*.md, level2/Level2_Lab*_Content.md |

For step-by-step implementation (COMMAND strings, grading tab), use **Level2_Lab*_Assessment_Setup.md** and **Level2_Implementation_Overview.md**.
