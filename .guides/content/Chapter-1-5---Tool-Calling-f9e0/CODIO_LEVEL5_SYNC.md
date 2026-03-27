# Chapter 1.5 - Tool Calling: Codio Sync

This folder mirrors the Level 5 content from `level5/` (unit content and lab content) so it can be synced to Codio the same way as Chapter 1.4 (Multiple Slots).

**Student working directory:** All Chapter 1.5 student steps assume the agent project lives under **`level5/`** in the workspace. Activate the venv at **project root**, then **`cd level5`** before **`python -m rasa …`** or editing domain, flows, actions, tools, and **`endpoints.yml`**.

## Structure

- **Chapter:** Chapter-1-5---Tool-Calling-f9e0
- **Units:** Unit 0 (Recap Level 4) through Unit 6 (Summary and Next Steps) — 7 units total. Folder names are **Unit-0--** through **Unit-6--**. Unit 1 has three pages (1.1, 1.2, 1.3 Test Your Knowledge). Unit 6 has seven pages: 6.1 Complete Agent Walkthrough, 6.2 What You've Learned, 6.3 What's Next, 6.4 Knowledge Check, 6.5 Limitations of Level 5, 6.6 What's Next Level 6 Preview, 6.7 Course Completion Checklist.
- **Labs:** Lab 2.1 (tools folder), Lab 3.1 (endpoints), Lab 4.1 (flow and action), Lab 5.1 (training), Lab 5.2 (completion check). **Unit 5 order (linear):** 5.1 Training → Lab 5.1 → 5.2 Testing → Lab 5.2 (concept then lab, then concept then lab).

Each unit has an `index.json` and each page has a `.md` and `.json`. **IDs use the f9e0/L5 suffix** so they do not collide with other chapters.

## Root index

The main guide index at `.guides/content/index.json` includes `Chapter-1-5---Tool-Calling-f9e0` in its `order` array so this chapter appears after Chapter 1.4.

## Assessments

- **Task IDs:** code-output-compare-501020001 (Lab 2.1), 501030001 (Lab 3.1), 501040001 (Lab 4.1), 501050001 (Lab 5.1), 501050002 (Lab 5.2).
- **Assessment JSONs:** `.guides/assessments/code-output-compare-501020001.json` through `code-output-compare-501050002.json`.
- **Graders:** `.guides/secure/level5_graders/` (lab_2.1_grader.py … lab_5.2_grader.py; lab_*_solution_reference.md for LLM Rubric).
- **Working directory:** `/home/codio/workspace`. Command uses venv Python and grader path, e.g. `/home/codio/workspace/.venv/bin/python3 /home/codio/workspace/.guides/secure/level5_graders/lab_2.1_grader.py`. Expect output contains `PASS` (substring match).

Lab pages in this chapter include `{Check It!|assessment}(code-output-compare-50XXXXXX)` with the taskId above.

## Re-import from Git

To refresh the guide in Codio (including Chapter 1.5), re-import or update the project from Git so Codio loads the current `.guides/content/` tree.
