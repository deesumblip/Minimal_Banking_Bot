# Level 3: Slot Collection – Codio Implementation Guide (Implementers Only)

**Audience**: Codio team / course implementers. **Not** student-facing.

**Purpose**: Point to the canonical Level 3 content and assessment setup. Student-facing content lives elsewhere (see below).

---

## Where Student Content Lives

- **Source of truth (markdown)**: `level3/Level3_Unit*_Content_*.md` and `level3/Level3_Lab*_Content.md`
- **Codio guide (already populated)**: `.guides/content/Chapter-1-3---Slot-Collection-a4b5/` — Units 0–8 and all section/lab pages are copied from the `level3/` files. Sync this chapter for the Level 3 TOC; do not maintain duplicate tutorial text in this guide.

**Do not** copy the old long tutorial from this file into Codio. Use the unit/lab files above or the Chapter 1.3 guide content.

---

## Primary Implementer References

| Document | Use |
|----------|-----|
| **`Level3_Implementation_Overview.md`** | Venv (root), Codio vs local, file layout, grader locations, technical specs, alignment with L1/L2. |
| **`Level3_Course_Outline.md`** | Unit/lab list, which labs are graded, assessment summary. |
| **`Level3_Lab3.1_Assessment_Setup.md`** … **`Level3_Lab7.1_Assessment_Setup.md`** | Per-lab: Codio assessment config, COMMAND, Working Directory, LLM Rubric or grader script path, expected output. |

Use these for configuring the Codio course and assessments.

---

## Technical Summary (Quick Reference)

- **Venv**: One `.venv` in **project root** (from Lab 0.1). Students activate from root, then `cd level3`. Graders run from workspace root; script activates venv and `cd`s to `level3`.
- **Inspector on Codio**: **Rasa Inspect** tab only. Do not use Tools → Ports or port 5005 for students.
- **Graded labs**: Lab 3.1, 5.1 (LLM Rubric with solution references in `.guides/assessments/level3_graders/`), Lab 6.1 (Python grader `lab_6.1_grader.py`). Working Directory for assessments: `/home/codio/workspace`.
- **Success output**: Grader must print a line containing `PASS` or `Successfully passed!` for Codio’s expected-output match.

For full details, see **Level3_Implementation_Overview.md**.

---

## Auto-Grading and QA (Codio Team)

- **Lab 3.1 / 5.1**: Use LLM Rubric Autograde with the instructor-provided solution files in `.guides/assessments/level3_graders/` (see each lab’s Assessment_Setup.md). Option B: Standard Code Test with Bash scripts if you add `lab_3.1_grader.sh` / `lab_5.1_grader.sh`.
- **Lab 6.1**: Standard Code Test; run `lab_6.1_grader.py` from workspace root (see `Level3_Lab6.1_Assessment_Setup.md`).
- **QA**: Run course end-to-end in a clean Codio environment; confirm graded labs pass when requirements are met and fail with clear feedback when not. Confirm Rasa Inspect tab works for Inspector.

---

## AI Coach / Troubleshooting

- Point learners to the correct file and section (e.g. `domain/basics.yml` for slots, flow files for `collect:`).
- Common issues (slot not collected, slot always None) are covered in **Unit 6.4** content (`Level3_Unit6_Content_6.4_Common-Issues-with-Slots.md` and the same content in Chapter 1.3).

---

## Summary

1. **Student content**: `level3/Level3_Unit*_Content_*.md`, `level3/Level3_Lab*_Content.md`, and `.guides/content/Chapter-1-3---Slot-Collection-a4b5/`.
2. **Implementer setup**: **Level3_Implementation_Overview.md** + **Level3_Course_Outline.md** + each **Level3_Lab*_Assessment_Setup.md**.
3. **This file**: Implementer-only pointer and quick reference; no student tutorial content.
