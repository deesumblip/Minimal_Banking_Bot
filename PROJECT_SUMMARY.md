## Project Summary: Minimal Banking Agent (Codio + Rasa Pro)

This file captures high-level context and recent structural decisions so future collaborators (or AI sessions) can quickly re-orient on this repo, especially around **Chapter 1.2 – Custom Actions** and Codio integration.

---

### 1. Repository and Codio Overview

- **Repo:** `Minimal_Banking_Agent` – multi-level Rasa Pro + CALM course.
- **Codio guides:** Live under `.guides/content/` with:
  - Root chapter index: `.guides/content/index.json`.
  - Per-chapter folders, e.g. `Chapter-1-2---Custom-Actions-30d6/`.
  - Each unit has an `index.json` listing pages in `order`.
- **Assessments:** Live under `.guides/assessments/`:
  - Types: `code-output-compare`, `multiple-choice`, `fill-in-the-blanks`.
  - Pages reference assessments via `{Check It!|assessment}(taskId)`.
  - Task IDs and JSON filenames must match (e.g. `{Check It!|assessment}(code-output-compare-2266471391)` ↔ `.guides/assessments/code-output-compare-2266471391.json`).

For a full mapping of Level 2 (Chapter 1.2) content, labs, and graders, see `level2/LEVEL2_CONTENT_LABS_AND_ASSESSMENTS.md`.

---

### 2. Chapter 1.2 – Custom Actions (Current State)

#### 2.1 Structure (global JSONs)

- Root `.guides/content/index.json` includes:
  - `Chapter-1-2---Custom-Actions-30d6` in the `order` array.
- Chapter index: `.guides/content/Chapter-1-2---Custom-Actions-30d6/index.json`:
  - `type: "chapter"`, title `"Chapter 1.2 - Custom Actions"`.
  - `order` (units): Unit-0 … Unit-6 (7 units; Unit 6 closes with **6.4** then **6.5** — integration + knowledge check, then core ideas and Level 3 readiness):
    - `Unit-0--Recap--What-You-Built-in-Level-1-d9e8`
    - `Unit-1--Introduction-to-Actions-aa31`
    - `Unit-2--Understanding-the-Action-Class-6b66`
    - `Unit-3--Creating-Your-First-Action-5090`
    - `Unit-4--Registering-Actions-in-the-Domain-a7fc`
    - `Unit-5--Using-Actions-in-Flows-b1ff`
    - `Unit-6--Training-and-Testing-with-Actions-b86b` (includes **`6-4-Level-2-Wrap-Up-d798`**, **`6-5-Core-Ideas-and-Level-3-Readiness-b91a`**)
- **Unit 3 index** (`Unit-3--Creating-Your-First-Action-5090/index.json`) now uses:
  - `order`: `["Lab-3-1--Create-Your-Own-Action-04c0"]`.
  - Short duplicate `Lab-3-1-04c0` was removed (both `.md` and `.json`), and the index points only at the long-form Lab 3.1 page.
- **Unit 2 index** (`Unit-2--Understanding-the-Action-Class-6b66/index.json`):
  - `order`: `["2-1-The-Action-Class-Deep-Dive-49b9", "2-2-Understanding-the-Parameters-3f41", "2-3-Test-Your-Knowledge-5051", "Lab-2-1--Exploring-the-Actions-Folder-45a5"]`.
  - Lab 2.1 explicitly follows the 2.3 Test Your Knowledge page.

#### 2.2 Test Your Knowledge MCQs (1.4 and 2.3)

Unit 1.4 (Intro) and Unit 2.3 (Action Class Deep Dive) use multiple-choice assessments with task IDs:

- **Unit 1.4 – Test Your Knowledge** (`1-4-Test-Your-Knowledge-06fd.md`):
  - `{Check It!|assessment}(multiple-choice-1201400001)` – What is an action in Rasa?
  - `{Check It!|assessment}(multiple-choice-1201400002)` – How actions differ from responses (`utter_*`) – note: asterisk is escaped in JSON instructions.
  - `{Check It!|assessment}(multiple-choice-1201400003)` – When to use actions instead of simple responses (dynamic content, calculations, external data).
  - `{Check It!|assessment}(multiple-choice-1201400004)` – Flow calling an action.
  - `{Check It!|assessment}(multiple-choice-1201400005)` – Required methods (`name()` and `run()`).

- **Unit 2.3 – Test Your Knowledge** (`2-3-Test-Your-Knowledge-5051.md`):
  - `{Check It!|assessment}(multiple-choice-1202300001)` – Parameters of `run()` (dispatcher, tracker, domain).
  - `{Check It!|assessment}(multiple-choice-1202300002)` – How an action sends messages (`dispatcher.utter_message`).
  - `{Check It!|assessment}(multiple-choice-1202300003)` – `name()` must match domain `actions:`.
  - `{Check It!|assessment}(multiple-choice-1202300004)` – Why `action_bank_hours` uses `datetime` (dynamic by day).
  - `{Check It!|assessment}(multiple-choice-1202300005)` – `run()` return value (`[]`).

All corresponding JSONs exist under `.guides/assessments/` with matching `taskId` fields.

---

### 3. Labs 2.1 and 3.1 – Current Design

#### 3.1 Lab 2.1 – Exploring the Actions Folder (Unit 2)

- **Guide page:** `.guides/content/Chapter-1-2---Custom-Actions-30d6/Unit-2--Understanding-the-Action-Class-6b66/Lab-2-1--Exploring-the-Actions-Folder-45a5.md`.
- **Placement:** Immediately after `2-3-Test-Your-Knowledge-5051` in the Unit 2 `index.json`.
- **Current content design:**
  - Lab now consists of:
    - A **complete action file** fill-in-the-blanks task (branch address + current day) linked via:
      - `{Check It!|assessment}(fill-in-the-blanks-1202100001)`.
    - No additional MCQs and no additional short FIB Check It! tags on this page.
  - Old “Your Task”, “What You're Looking For”, and extra FIB Check It! tags for Lab 2.1 were removed from the guide.
- **Assessment JSON:** `.guides/assessments/fill-in-the-blanks-1202100001.json`.
  - Students complete an action class `ActionBranchAddress(Action)` that:
    - Imports `datetime`, `Action`, `Tracker`, `CollectingDispatcher`.
    - Implements `name()` returning `"action_branch_address"`.
    - Implements `run(self, dispatcher, tracker, domain)`:
      - Uses `datetime.now().weekday()` to map to day names.
      - Builds a dynamic message like: `"Our main branch is at 123 High Street. Today is Mon."`.
      - Sends the message with `dispatcher.utter_message(text=message)`.
      - Returns `[]`.
  - Blanks in the FIB align with Level 2 learning goals:
    - `CollectingDispatcher`, `ActionBranchAddress`, `Action`, `action_branch_address`,
      `dispatcher`, `tracker`, `domain`, `utter_message`, `[]`.

**Note:** The lab still has **short-answer FIB JSONs** in `.guides/assessments/` (IDs like 2658905168, 2658905169, 2658905170, 341339148, 235818681), but they are no longer referenced from this guide. They can be reused later if needed or deleted if we decide they are permanently out-of-scope.

#### Lab 3.1 – Creating Your First Action (Unit 3)

- **Guide page (canonical):** `Unit-3--Creating-Your-First-Action-5090/Lab-3-1--Create-Your-Own-Action-04c0.md` (+ matching `.json`).
  - **Unit 3** contains **this page only** (removed: “3.1 Step-by-Step: Creating an Action”, “3.2 Understanding Action Execution”; execution steps moved to the **end of Lab 3.1**).
  - Segue from **Unit 2.1** (`action_bank_hours`); task: `level2/actions/action_holiday_hours.py`.
  - **Check It! order:** `{Check It!|assessment}(fill-in-the-blanks-201030010)` → paste → `{Check It!|assessment}(code-output-compare-2266471391)`.
  - Page ends with prose section **When Rasa executes your action** (seven steps + key point).
- **Unit 3 `index.json` `order`:** `["Lab-3-1--Create-Your-Own-Action-04c0"]` only.
- **Assessment JSONs:** `.guides/assessments/fill-in-the-blanks-201030010.json` (5 pts); `.guides/assessments/code-output-compare-2266471391.json` (8 pts).
  - Code test runs `bash .../level2_graders/lab_3.2_grader.sh` (filename in repo; banner says Lab 3.1).
  - Checks file, imports, `datetime`, `ActionHolidayHours`, `name()`, `run()`, `dispatcher.utter_message`, `return []`.

---

### 4. Other Chapter 1.2 Lab Assessments

- **Lab 4.1 – Registering Actions in the Domain**
  - Guide: `Unit-4--Registering-Actions-in-the-Domain-a7fc/Lab-4-1--Registering-Actions-in-the-Domain-3406.md`.
  - Assessment: `{Check It!|assessment}(code-output-compare-1451983168)`.
  - JSON: `.guides/assessments/code-output-compare-1451983168.json`.
- **Lab 6.2 – Verify Domain and Training** (Unit 6, right after Lab 6.1)
  - Guide: `Unit-6--Training-and-Testing-with-Actions-b86b/Lab-6-2--Verify-Domain-and-Training-2289.md`.
  - Assessment: `{Check It!|assessment}(code-output-compare-1597644299)`.
  - JSON: `.guides/assessments/code-output-compare-1597644299.json`.
- **Lab 5.1 – Using Actions in Flows**
  - Guide: `Unit-5--Using-Actions-in-Flows-b1ff/Lab-5-1--Using-Actions-in-Flows-e512.md`.
  - Assessment: `{Check It!|assessment}(code-output-compare-389374509)`.
  - JSON: `.guides/assessments/code-output-compare-389374509.json`.
- **Lab 6.1 – Training and Testing with Actions**
  - Guide: `Unit-6--Training-and-Testing-with-Actions-b86b/Lab-6-1--Training-and-Testing-with-Actions-7710.md`.
  - Assessment: `{Check It!|assessment}(code-output-compare-1070925386)`.
  - JSON: `.guides/assessments/code-output-compare-1070925386.json`.

All of these are confirmed in `.guides/JSON_COHERENCE_REPORT.md` as coherent: each taskId used in content has a JSON with matching `taskId`, and the grader paths are valid.

---

### 5. Git / Branching and Codio Integration Notes

- **Git branches:**
  - Primary dev branch: `main`.
  - There is a `codio-main` branch configured to track `origin/main` in `.git/config`, but the canonical upstream is `origin/main`.
- **Current deployment flow (manual):**
  1. Edit in local dev (or Cursor) and commit to `main`.
  2. Push to GitHub (`origin/main`).
  3. In Codio assignment:
     - Open terminal in `/home/codio/workspace`.
     - Run `git fetch origin && git pull origin main`.
     - If needed, reload the guide (or re-import/update from Git) so Codio reflects `.guides/` updates.
- **Future option – GitHub Actions → Codio:**
  - Codio supports automatic publishing from GitHub via a workflow using [`codio/codio-assignment-publish-action`](https://docs.codio.com/develop/develop/ide/tools/ghapi.html#implementing-workflow-actions).
  - Setup (not yet implemented in this repo):
    - Codio org admin creates a GitHub API integration and captures `client-id` and `secret-id`.
    - Add these as GitHub Actions secrets:
      - `CODIO_PRODUCTION_CLIENT_ID`
      - `CODIO_PRODUCTION_SECRET_ID`
    - Add `.github/workflows/codio-publish.yml` that:
      - Runs on `push` to `main`.
      - Uses the Codio publish action to push this repo to the appropriate `course-id` / `assignment-id`.
  - This would eliminate manual Codio pulls and keep the assignment in sync on every merge to `main`.

---

### 6. How to Re-Prime an AI Assistant for This Project

When opening this repo in a new Cursor / AI session, you can quickly re-establish context by:

- Pointing the assistant to:
  - This file: `PROJECT_SUMMARY.md` (for high-level decisions).
  - `level2/LEVEL2_CONTENT_LABS_AND_ASSESSMENTS.md` (for detailed Level 2 mapping).
  - `.guides/JSON_COHERENCE_REPORT.md` (for global content/assessment coherence).
- Mentioning key constraints:
  - **Do not** reintroduce removed Lab 2.1 MCQs or the duplicate Lab 3.1 page pair.
  - Always keep `{Check It!|assessment}(taskId)` in sync with `.guides/assessments/` JSON filenames and `taskId` fields.
  - Maintain the current Chapter 1.2 unit order and Lab placements as reflected in the chapter and unit `index.json` files.

