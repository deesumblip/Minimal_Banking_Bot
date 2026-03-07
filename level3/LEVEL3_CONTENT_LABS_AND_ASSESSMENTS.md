# Level 3: Content, Labs, and Assessments

This document maps Level 3 (Chapter 1.3 – Slot Collection) unit content files, lab content files, and assessment task IDs / grader paths so implementers can sync with Codio.

---

## 1. Course structure

Level 3 uses **9 units** (0–8): Recap → Slots intro → Slot types → Domain (Lab 3.1) → Actions (Lab 4.1) → Flows with collect (Lab 5.1) → Training (Lab 6.1, 6.2) → Walkthrough (Lab 7.1) → Assessment.

- **Course outline:** `level3/Level3_Course_Outline.md` — unit/section names, lab list, assessment summary.

---

## 2. Unit content files (source of truth in level3/)

| File | Purpose |
|------|---------|
| `Level3_Unit0_Content_0.1_Your-Level-2-Banking-Bot.md`, `0.2_What-Level-3-Adds.md` | Recap Level 2, What Level 3 adds (slots, check_balance) |
| `Level3_Unit1_Content_1.1_*.md` … `1.3_*.md` | What is a slot, how slots work, slot collection |
| `Level3_Unit2_Content_2.1_*.md`, `2.2_*.md`, `2.3_Test-Your-Knowledge.md` | Slot types, naming, quiz |
| `Level3_Unit3_Content_3.1_The-Slots-Section.md` | Domain slots section, full domain example; Lab 3.1 |
| `Level3_Unit4_Content_4.1_Accessing-Slots-in-Actions.md`, `4.2_Placeholder-Handling.md` | tracker.get_slot, placeholder handling; Lab 4.1 |
| `Level3_Unit5_Content_5.1_*.md`, `5.2_*.md`, `5.3_Creating-the-Flow.md` | Collect step, flow with collect; Lab 5.1 |
| `Level3_Unit6_Content_6.1_*.md` … `6.4_*.md` | Training, testing, slot state, common issues |
| `Level3_Unit7_Content_7.1_*.md` … `7.3_*.md` | Walkthrough, summary, best practices |
| `Level3_Unit8_Content_8.1_*.md` … `8.5_*.md` | Knowledge check, learned, limitations, Level 4 preview, checklist |

---

## 3. Lab content and assessment task IDs / graders

| Lab | Content File | Assessment Setup File | Task ID (Codio) | Grader Path |
|-----|--------------|------------------------|-----------------|-------------|
| 3.1 | Level3_Lab3.1_Content.md | Level3_Lab3.1_Assessment_Setup.md | code-output-compare-3187585640 | .guides/secure/level3_graders/lab_3.1_grader.py |
| 4.1 | Level3_Lab4.1_Content.md | Level3_Lab4.1_Assessment_Setup.md | code-output-compare-2346557110 | .guides/secure/level3_graders/lab_4.1_grader.py |
| 5.1 | Level3_Lab5.1_Content.md | Level3_Lab5.1_Assessment_Setup.md | code-output-compare-1235165472 | .guides/secure/level3_graders/lab_5.1_grader.py |
| 6.1 | Level3_Lab6.1_Content.md | Level3_Lab6.1_Assessment_Setup.md | code-output-compare-1029038275 | .guides/secure/level3_graders/lab_6.1_grader.py |
| 6.2 | Level3_Lab6.2_Content.md | Level3_Lab6.2_Assessment_Setup.md | — | Ungraded (testing slot collection) |
| 7.1 | Level3_Lab7.1_Content.md | Level3_Lab7.1_Assessment_Setup.md | — | Ungraded (walkthrough) |

**Execution:** Use venv Python in COMMAND (e.g. `/home/codio/workspace/.venv/bin/python3 .../lab_3.1_grader.py`). Working directory: `/home/codio/workspace`. Do not upload grader scripts; run from workspace so `git pull` updates them.

**Solution references:** `.guides/secure/level3_graders/lab_*_solution_reference.md` (3.1, 4.1, 5.1) for implementers.

---

## 4. Summary table

| Item | Location / Value |
|------|------------------|
| Course outline | level3/Level3_Course_Outline.md |
| Units | 0–8 |
| Graded labs | 3.1 (8 pts), 4.1 (10 pts), 5.1 (8 pts), 6.1 (12 pts) |
| Task IDs | 3187585640, 2346557110, 1235165472, 1029038275 |
| Graders | .guides/secure/level3_graders/lab_*.py |
| Source content | level3/Level3_Unit*_Content_*.md, level3/Level3_Lab*_Content.md |

For step-by-step implementation (COMMAND, rubric, solution refs), use **Level3_Lab*_Assessment_Setup.md** and **Level3_Implementation_Overview.md**.
