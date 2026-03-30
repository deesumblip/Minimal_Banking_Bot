# Chapter 1.5 - Tool Calling: Codio Sync

This folder mirrors Level 5 teaching content (aligned with `level5/`) for Codio sync, same pattern as Chapter 1.4.

**Student working directory:** All steps assume the agent under **`level5/`**. For training and CLI runs, activate the venv at **project root**, then **`cd level5`** before **`python -m rasa …`**. Graded labs use on-disk checks (fill-in-the-blanks and code tests read `level5/`); the venv is **not** required to pass Lab 2.1 file checks.

**Lab order (from Chapter 1.4 completion to Chapter 1.5 done):** **Lab 2.0** — copy **`command_prompt_v3_slot_names.jinja2`** from **`level5/resources/`** to **`level5/data/prompts/`**, set **`prompt_template`** in **`config.yml`** → **Lab 2.1** (tools) → **Lab 3.1** (endpoints) → **Lab 4.1** (flow + action) → **Lab 5.1** (train) → **Lab 5.2** (completion check). **Lab 2.0** uses **`code-output-compare-501020000`**; **Lab 5.1** and **Lab 5.2** graders still include **Check 3** for the same prompt file and **`prompt_template`**.

**Guide page JSON (`*.json` next to each `.md`):** Pages use **`"path": ["level5"]`** (and **`"layout": "2-panels-tree-guides-left"`** where set) so the IDE tree highlights **`level5/`**, like **`level4/`** in Chapter 1.4.

## Structure

- **Chapter:** Chapter-1-5---Tool-Calling-f9e0
- **Units:** Unit 0 (Recap Level 4) through Unit 6 (Summary and Next Steps) — 7 units total. Folder names are **Unit-0--** through **Unit-6--**. Unit 1 has three pages (1.1, 1.2, 1.3 Test Your Knowledge). Unit 6 has seven pages: 6.1 Complete Agent Walkthrough, 6.2 What You've Learned, 6.3 What's Next, 6.4 Knowledge Check, 6.5 Limitations of Level 5, 6.6 What's Next Level 6 Preview, 6.7 Course Completion Checklist.
- **Labs:** Lab 2.0 (command prompt), Lab 2.1 (tools folder), Lab 3.1 (endpoints), Lab 4.1 (flow and action), Lab 5.1 (training), Lab 5.2 (completion check). **Unit 5 (linear):** page 5.1 → Lab 5.1 → page 5.2 → Lab 5.2.

Each unit has an `index.json` and each page has a `.md` and `.json`. **IDs use the f9e0/L5 suffix** so they do not collide with other chapters.

## Root index

The main guide index at `.guides/content/index.json` includes `Chapter-1-5---Tool-Calling-f9e0` in its `order` array so this chapter appears after Chapter 1.4.

## Assessments

- **Task IDs:** **code-output-compare-501020000** (Lab 2.0); **fill-in-the-blanks-501020010** + **code-output-compare-501020001** (Lab 2.1); 501030001 (Lab 3.1); **fill-in-the-blanks-501040010** + **code-output-compare-501040001** (Lab 4.1); 501050001 (Lab 5.1); 501050002 (Lab 5.2). **501050001** / **501050002** graders still include a **Lab 2.0** check (prompt file + **`prompt_template`**).
- **Assessment JSONs:** `.guides/assessments/fill-in-the-blanks-501020010.json`, `fill-in-the-blanks-501040010.json`; `code-output-compare-501020000.json` through `code-output-compare-501050002.json`.
- **Graders:** `.guides/secure/level5_graders/` (lab_2.0_grader.py, lab_2.1_grader.py … lab_5.2_grader.py; lab_*_solution_reference.md for LLM Rubric).
- **Working directory:** `/home/codio/workspace`. Command uses venv Python and grader path, e.g. `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level5_graders/lab_2.1_grader.py`. Expect output contains `PASS` (substring match).

Lab 2.0 includes `{Check It!|assessment}(code-output-compare-501020000)`. Lab 2.1 includes `{Check It!|assessment}(fill-in-the-blanks-501020010)` then `{Check It!|assessment}(code-output-compare-501020001)`. Lab 4.1 includes `{Check It!|assessment}(fill-in-the-blanks-501040010)` then `{Check It!|assessment}(code-output-compare-501040001)`. Other lab pages use `{Check It!|assessment}(code-output-compare-50XXXXXX)` with the task IDs above.

## Re-import from Git

Re-import or pull the project so Codio picks up the latest `.guides/content/` tree.
