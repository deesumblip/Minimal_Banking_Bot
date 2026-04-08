# Narrative Structure Examination: All Levels / Chapters

This document examines the narrative structure of Levels 1–6 (Chapters 1.1–1.6) and suggests where things could be improved.

---

## 1. Unit 0 (Opening) — Consistency

| Level | Unit 0 title | Content |
|-------|----------------|--------|
| **1** | Prerequisites and Setup | 0.1 What You Need, 0.2 Environment Setup, 0.3 YAML, 0.4 File Structure, 0.5 Verifying, 0.6 Getting Help — **no “recap previous level”** (first level) |
| **2** | Recap - What you built in Level 1 | 0.1 Your Level 1 Agent, 0.2 What Level 2 Adds |
| **3** | Recap - What you built in Level 2 | 0.1 Your Level 2 Agent, 0.2 What Level 3 Adds |
| **4** | Recap - What you built in Level 3 | 0.1 Your Level 3 Agent, 0.2 What Level 4 Adds |
| **5** | Recap - What you built in Level 4 | 0.1 Your Level 4 Agent, 0.2 What Level 5 Adds |
| **6** | Recap - What you built in Level 5 | 0.1, 0.2 in **unit content**; **TUTORIAL** has only one short paragraph for Unit 0 (no 0.1/0.2) |

**Improvements**

- **Level 6 TUTORIAL:** Add explicit **0.1 Your Level 5 Banking Agent** and **0.2 What Level 6 Adds** subsections (with bullet lists of what remains and what’s added) so Unit 0 matches Level 4/5 and the unit content.

---

## 2. Unit Count — Two Patterns

| Pattern | Levels | Structure |
|---------|--------|-----------|
| **Long (9 units)** | 1, 3 | 0: Setup/Recap → 1–5: Concepts + labs → 6: Training → 7: Putting It All Together → 8: Assessment (Knowledge Check, Learned, Limitations, Next Preview, Checklist) |
| **Short (7 units)** | 4, 5, 6 | 0: Recap → 1–4: Concepts + labs → 5: Training and Testing → 6: Summary (6.1 Walkthrough … 6.7 Checklist) |

Level 2 uses 8 units (0–8) with a similar “Putting It All Together” and “Assessment” close.

**Improvements**

- **Optional:** Add a one-line design note in the course outline or CONTENT_LABS doc explaining why Level 1/2/3 use 7–9 units (more concepts, first exposure) and Level 4/5/6 use 7 (0–6) with a single “Summary and Next Steps” unit. No structural change required; this only clarifies intent.
- **Level 2:** Chapter 1.2 ends with **Unit 7** only; the final page (**7.1**) includes integration, review, knowledge check, and Level 3 preview (former Unit 8 merged into Unit 7).

---

## 3. Unit 6 / 8 Closing Block — Consistency

| Level | Last unit | Sections |
|-------|------------|----------|
| **1** | Unit 8 | 8.1 Knowledge Check, 8.2 What You've Learned, 8.3 Limitations, 8.4 What's Next Level 2, 8.5 Checklist |
| **2** | Unit 7 (7.1) | Single wrap-up page: walkthrough, review, 8.1-style MCs, recap, limitations, Level 3 preview, checklist (no separate Unit 8) |
| **3** | Unit 8 | 8.1–8.5 same |
| **4** | Unit 6 | 6.1 Walkthrough, 6.2 Learned, 6.3 Next, 6.4 Knowledge Check, 6.5 Limitations, 6.6 Level 5 Preview, 6.7 Checklist |
| **5** | Unit 6 | 6.1–6.7 same |
| **6** | Unit 6 | 6.1–6.7 (in content); 6.6 = “What’s Next Beyond Course” (no Level 7) |

Levels 4–6 use a **7-part closing** (walkthrough, learned, next, knowledge check, limitations, next-level preview / beyond course, checklist); Levels 1–3 use a **5-part closing** (knowledge check, learned, limitations, next preview, checklist) and put “Complete Agent Walkthrough” and “Summary” in Unit 7.

**Improvements**

- **Optional:** In Level 1/2/3, add an explicit “Complete Agent Walkthrough” subsection inside the closing block (or point to Unit 7) so the “review what you built” moment is clearly part of the same narrative block as Knowledge Check and Checklist. This is a light wording/pointer change, not a restructure.

---

## 4. TUTORIAL.md — Gaps and Depth

| Level | TUTORIAL present? | Depth |
|-------|-------------------|--------|
| **1** | Yes | Very long (2500+ lines), many subsections per unit |
| **2** | **No** | — |
| **3** | Yes | Full Unit 0–8 with subsections |
| **4** | Yes | Unit 0–6 with 0.1/0.2, 1.1–1.4, 2.1, 3.1, 4.1, 5.1–5.2, 6.1–6.7 |
| **5** | Yes | Same style as 4 |
| **6** | Yes | **Thin:** Unit 0 one paragraph; Units 1–5 one paragraph each; Unit 6 only a pointer to Unit 6 files |

**Improvements**

- **Level 2:** Add **level2/TUTORIAL.md** with Table of Contents (Units 0–8 or 0–6 depending on how Level 2 is numbered in .guides) and short summaries per unit, plus a Quick Reference table. Align section names with Level2_Course_Outline and Level2_Unit* content so the narrative path is clear.
- **Level 6:** Expand **level6/TUTORIAL.md** so Unit 0 has 0.1 and 0.2 subsections (matching unit content), and Unit 6 lists 6.1–6.7 with one line each (like Level 4/5) instead of only “See Level6_Unit6_Content_6.1… through 6.7.”

---

## 5. “Examples Before Labs” / Lab Objective Wording

| Level | Pattern |
|-------|--------|
| **4, 5, 6** | Unit content includes **full examples** of what students create; lab objectives say **“In Unit X you saw an example… In this lab you will create your own version…”** |
| **1, 2, 3** | Some labs use “In this lab you will”; **no consistent** “you saw an example… create your own version” or full example-before-lab pattern in every create lab. |

Level 2’s narrative assessment already calls out “example vs. yours” (action_bank_hours vs action_holiday_hours) and suggests small bridges (e.g. Unit 2.2 → Lab 3.1, Unit 4.1 reminder).

**Improvements**

- **Level 1:** For any lab that asks students to **create** a new artifact (e.g. flow, response), ensure the preceding unit shows a **concrete example** of that artifact and the lab objective says something like “You saw…; in this lab create your own version.” Apply the same principle as in Level 4/5.
- **Level 2:** Implement the bridges in LEVEL2_NARRATIVE_STRUCTURE_ASSESSMENT (Unit 2.2, 3.2, 4.1, 5.1, 6.1, outline). Optionally add “In Unit X you saw…; in this lab you create your own version” where the lab is “create action_holiday_hours / holiday_hours flow.”
- **Level 3:** For domain/action/flow labs, ensure the unit immediately before each “create” lab has a **full example** (e.g. domain snippet, action class, flow YAML) and the lab objective ties to it (“you saw…; create your own version”).

---

## 6. Forward and Backward References

- **Level 2:** LEVEL2_NARRATIVE_STRUCTURE_ASSESSMENT already lists strong handoffs and gaps (Unit 2.2, 3.2, 4.1, 5.1, 6.1, Lab 2.1 in outline). Implementing those one-line bridges would strengthen the narrative.
- **Levels 4–6:** “In Unit X you saw… In this lab you will…” provides clear forward references; Unit 0 “What Level Y Adds” sets the journey. No major gaps identified.
- **Level 1:** Prerequisites and Setup (Unit 0) could end with a single sentence: “In the next units you will add responses, flows, and patterns, then train and test your agent.” So the reader sees the full arc up front.

**Improvements**

- Add the recommended one-line bridges in Level 2 (see LEVEL2_NARRATIVE_STRUCTURE_ASSESSMENT).
- In Level 1 Unit 0 (e.g. end of 0.2 or 0.5), add one sentence that previews the rest of the level (responses → flows → patterns → config → training → walkthrough → assessment).

---

## 7. CONTENT_LABS_AND_ASSESSMENTS / Course Outline

| Level | Has CONTENT_LABS (or equivalent)? | Has Course Outline? |
|-------|-----------------------------------|-----------------------|
| **1** | Unclear (other docs) | — |
| **2** | — | Level2_Course_Outline.md |
| **3** | — | — |
| **4** | LEVEL4_CONTENT_LABS_AND_ASSESSMENTS.md | — |
| **5** | LEVEL5_CONTENT_LABS_AND_ASSESSMENTS.md | Level5_Course_Outline.md |
| **6** | LEVEL6_CONTENT_LABS_AND_ASSESSMENTS.md | — |

**Improvements**

- **Level 1, 2, 3:** Consider adding a **LEVELn_CONTENT_LABS_AND_ASSESSMENTS.md** (or single “Content and Labs” doc per level) that lists unit content files, lab content, task IDs, and grader paths. That would align narrative structure with assessment and make it easier to keep .guides and level folders in sync.
- **Level 4, 6:** If useful for implementers, add a short **Course Outline** (like Level 5) with unit titles, section names, and key concepts so the narrative structure is documented in one place.

---

## 8. Summary: Priority Improvements

| Priority | Improvement |
|----------|-------------|
| **High** | **Level 6 TUTORIAL:** Add Unit 0 subsections 0.1 and 0.2; expand Unit 6 to list 6.1–6.7 with one line each. |
| **High** | **Level 2:** Add **level2/TUTORIAL.md** (ToC + unit summaries + Quick Reference). |
| **Medium** | **Level 2:** Apply the small narrative edits in LEVEL2_NARRATIVE_STRUCTURE_ASSESSMENT (Unit 2.2, 3.2, 4.1, 6.1, 5.1, outline). |
| **Medium** | **Level 1, 2, 3:** Where a lab asks students to **create** something, ensure the preceding unit has a **full example** and the lab objective says “you saw… create your own version” (align with Level 4/5/6). |
| **Low** | **Level 1 Unit 0:** Add one sentence at the end of setup that previews the level (responses → flows → … → assessment). |
| **Low** | **Level 1, 2, 3:** Add LEVELn_CONTENT_LABS_AND_ASSESSMENTS (or one Content and Labs doc) for consistency with 4/5/6. |
| **Low** | **Level 4, 6:** Add a short Course Outline doc if useful for implementers. |

---

## 9. What’s Already Working Well

- **Levels 4, 5, 6:** Clear pattern: Recap (0.1, 0.2) → Concepts with full examples → Labs that “create your own version” → Training/Testing → Unit 6 with 6.1–6.7 closing block. TUTORIAL (4, 5) and unit content are aligned.
- **Level 2:** Narrative arc and “example vs. yours” are documented and coherent; only small bridges and a TUTORIAL are missing.
- **Level 3:** TUTORIAL has full Unit 0–8 and a clear recap → slots → domain → flows → actions → training → walkthrough → assessment.
- **Level 1:** Very detailed TUTORIAL and prerequisites; only a brief “what’s ahead” sentence and example-before-lab consistency could be tightened.
- **Graders and paths:** All levels that use code-output-compare use `.guides/secure/level*_graders/`; assessment JSONs are consistent for 4/5/6.

This document can be used to prioritize edits and keep narrative structure consistent across all levels/chapters.
