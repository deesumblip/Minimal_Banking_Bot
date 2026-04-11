# Pre-commit checks – result

Run date: (generated when checks were run)

---

## 1. Global course JSON

- **File:** `.guides/content/index.json`
- **Check:** `order` lists six level guide folder ids; each must have a matching folder with `index.json`.
- **Result:** **PASS** – All six levels (Levels 1–6) exist with `index.json`. Order matches.

---

## 2. Level 5 – Unit 6 (no orphans)

- **Check:** Unit 6 should have no orphan files; only 6.1–6.7 as in index order (6.5 = Limitations, 6.7 = Checklist).
- **Result:** **PASS** – Only `6-5-Limitations-of-Level-5-L5g5` present (no old `6-5-Course-Completion-Checklist-L5g5`). Unit 6 index order lists 7 pages; all have .md and .json.

---

## 3. Level 5 – Unit 1 (1.3 Test Your Knowledge)

- **Check:** Unit 1 `order` includes `1-3-Test-Your-Knowledge-L5b3`; matching .md and .json must exist.
- **Result:** **PASS** – Missing files were created: `1-3-Test-Your-Knowledge-L5b3.md` and `1-3-Test-Your-Knowledge-L5b3.json` in `Unit-1--Introduction-to-Tools-L5u1/`.

---

## 4. Level 5 assessment JSONs

- **Check:** Level 5 code-output assessments exist: `code-output-compare-501020000.json` through `code-output-compare-501050002.json`.
- **Result:** **PASS** – All 5 files present in `.guides/assessments/`. Commands point to `.guides/secure/level5_graders/lab_*.py`.

---

## 5. Level 5 graders

- **Check:** `.guides/secure/level5_graders/` contains lab_2.1 through lab_5.2 grader scripts and solution references.
- **Result:** **PASS** – 5 grader .py files and 5 solution_reference.md files present.

---

## 6. Secrets / .env

- **Check:** No committed files should contain real API keys or secrets. Assessment JSONs reference `.env` only in preExecuteCommand (file itself is gitignored).
- **Result:** **PASS** – No secrets found in assessment JSONs. Level 5 assessment commands do not source .env; other levels’ use of .env is configuration only.

---

## 7. .gitignore

- **Check:** desktop.ini and other OS/editor cruft should be ignored.
- **Result:** **PASS** – `desktop.ini` added to `.gitignore` (already applied).

---

## Summary

| Check                    | Status |
|--------------------------|--------|
| Global course JSON       | PASS   |
| Level 5 Unit 6       | PASS   |
| Level 5 Unit 1 (1.3)| PASS (files created) |
| Level 5 assessment JSONs | PASS   |
| Level 5 graders          | PASS   |
| Secrets / .env           | PASS   |
| .gitignore               | PASS   |

**Action taken during run:** Created missing `1-3-Test-Your-Knowledge-L5b3.md` and `.json` in Level 5 Unit 1 so index order is coherent.

You can commit and push after reviewing `git status` and staging the intended files.
