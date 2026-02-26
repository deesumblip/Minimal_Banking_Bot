# Chapter 1.4 - Multiple Slots: Codio Sync

This folder mirrors the Level 4 content from `level4/` (unit content and lab content) so it can be synced to Codio the same way as Chapter 1.3 (Slot Collection).

## Structure

- **Chapter:** Chapter-1-4---Multiple-Slots-e5f6
- **Units:** Unit 0 (Recap Level 3) through Unit 8 (Summary and Next Steps)
- **Labs:** Lab 4.1 (domain), Lab 4.2 (action), Lab 4.3 (flow), Lab 4.4 (training), Lab 4.5 (completion check)

Each unit has an `index.json` (section title and order of pages) and each page has a `.md` (content) and `.json` (page metadata: title, type page, contentType markdown).

## Root index

The main guide index at `.guides/content/index.json` includes `Chapter-1-4---Multiple-Slots-e5f6` in its `order` array so this chapter appears after Chapter 1.3 when the project is loaded or re-imported from Git in Codio.

## Assessments

Graders and solution references live in `.guides/assessments/level4_graders/` (lab_4.1_grader.py through lab_4.5_grader.py and corresponding solution_reference.md files). Configure each lab assessment in Codio using the Level4_Lab*_Assessment_Setup.md files in `level4/` (Option A: LLM Rubric, Option B: Standard Code Test with substring match for PASS).

## Re-import from Git

To refresh the guide in Codio (including Chapter 1.4), re-import or update the project from Git so Codio loads the current `.guides/content/` tree.
