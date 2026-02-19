# Codio Implementation Overview (All Levels)

**Audience**: Codio team / course implementers. Single entry point for implementation docs across levels.

---

## Level 1: Just Responses (Chapter 1.1)

- **Content**: `.guides/content/Chapter-1-1---Just-Responses-d3b4/`
- **Implementer docs**: `level1/Level1_Implementation_Overview.md`
- **Course outline**: See Level 1 unit/lab structure in repo; assessments per `Level1_Lab*_Assessment_Setup.md`

---

## Level 2: Custom Actions (Chapter 1.2)

- **Content**: `.guides/content/Chapter-1-2---Custom-Actions-30d6/`
- **Implementer docs**: `level2/Level2_Implementation_Overview.md`
- **Course outline**: See Level 2 unit/lab structure; assessments per `Level2_Lab*_Assessment_Setup.md`

---

## Level 3: Slot Collection (Chapter 1.3)

- **Content**: `.guides/content/Chapter-1-3---Slot-Collection-a4b5/` (populated from `level3/Level3_Unit*_Content_*.md` and `level3/Level3_Lab*_Content.md`)
- **Implementer docs**: `level3/Level3_Implementation_Overview.md` (primary); `level3/CODIO_IMPLEMENTATION_GUIDE.md` (short implementer-only pointer)
- **Course outline**: `level3/Level3_Course_Outline.md`
- **Assessments**: Per `level3/Level3_Lab*_Assessment_Setup.md`; graders in `.guides/assessments/level3_graders/` (LLM Rubric solution refs for 3.1/4.1, Python grader for 6.1). Venv in project root; Working Directory `/home/codio/workspace`; use **Rasa Inspect** tab only (no Ports).

---

## Conventions (All Levels)

- One `.venv` in **project root** (created in Level 1 Lab 0.1). For Level 2/3, activate from root then `cd level2` or `cd level3`.
- Codio: **Rasa Inspect** tab for Inspector (no Tools → Ports / port 5005 for students).
- Graders: run from workspace root; scripts activate venv and `cd` to the level folder; print `PASS` / `Successfully passed!` on success.
