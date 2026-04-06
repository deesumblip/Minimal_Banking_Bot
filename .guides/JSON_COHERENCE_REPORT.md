# JSON Coherence Report: Content and Assessments by Level / Chapter

This report compares **content** (`.guides/content/` chapter and unit structure) with **assessments** (`.guides/assessments/*.json` and level Assessment_Setup docs) for each level and its Codio chapter. Last run: re-check across all levels.

---

## 1. Root and chapter index coherence

### Root `.guides/content/index.json`

- **order**: `Chapter-1-1---Just-Responses-d3b4`, `Chapter-1-2---Custom-Actions-30d6`, `Chapter-1-3---Slot-Collection-a4b5`, `Chapter-1-4---Multiple-Slots-e5f6`, `Chapter-1-5---Tool-Calling-f9e0`, `Chapter-1-6---Sub-Agents-c7d8`. **Fixed:** Chapter 1.6 added to order.

### Chapter index.json vs unit folders

| Chapter | index.json `order` | Unit folders / notes | Coherent? |
|---------|--------------------|----------------------|-----------|
| 1.1 Just Responses | Unit-0 … Unit-8 (9 units) | Present (see §8 for trimmed pages) | Yes |
| 1.2 Custom Actions | Unit-0 … Unit-8 (9 units) | Present | Yes |
| 1.3 Slot Collection | Unit-0 … Unit-8 (9 units) | Present | Yes |
| 1.4 Multiple Slots | Unit-0 … Unit-6 (7 units) | Unit-0 folder present; order matches | Yes |
| 1.5 Tool Calling | Unit-0 … Unit-6 (7 units) | Present | Yes |
| 1.6 Sub-Agents | Unit-0 … Unit-6 (7 units) | Chapter index.json and all unit index.json + page .json added | Yes |

**Chapter 1.4:** Unit 0 present; chapter `id` placeholder replaced with valid UUID.

**Chapter 1.6:** **Fixed.** Chapter `index.json` created; each unit has `index.json` and every page has a matching `.json` (21 page .json files added).

---

## 2. Unit index.json vs page files

For each unit, the `order` array should list page ids that have a matching `.md` and `.json` in that unit folder.

**Chapter 1.1:** Eight pages were removed from the guide TOC; stems are listed in **§8**. Unit **0.4** (Getting Help) was restored. Optional `level1/` mirror markdown for some topics may still exist.

### Spot checks (sample units)

- **Chapter 1.4 Unit 0:** `order` = `["0-1-Your-Level-3-Banking-Agent-e4f5","0-2-What-Level-4-Adds-f5a6"]`; Unit-0 folder has matching .md and .json for both. Coherent.
- **Chapter 1.4 Unit 1:** order includes 1-1, 1-2, 1-3, 1-4-Test-Your-Knowledge-e4f5; all have .md and .json. Coherent.
- **Chapter 1.6:** Each unit has `index.json`; every listed page stem has matching `.md` and `.json`. Coherent for Codio expectations.

---

## 3. Assessment JSON vs content (Check It! tags)

Assessments are wired by **content**: markdown pages use `{Check It!|assessment}(taskId)`. Codio looks up `.guides/assessments/<type>-<id>.json` by taskId.

### By level

| Level | Referenced taskIds (from Assessment_Setup docs) | Assessment JSONs on disk | Coherent? |
|-------|--------------------------------------------------|---------------------------|-----------|
| 1.1 | code-output-compare-2562507355, 3333363688, 7772000001, etc. | Present | Yes |
| 1.2 | 1597644299, 1451983168, 2266471391, 389374509, 1070925386 | Present | Yes |
| 1.3 | 3187585640, 2346557111, 2346557110, 1235165472, 1029038275 | Present | Yes |
| 1.4 | fill-in-the-blanks-401010010, 401010001, 401020001, fill-in-the-blanks-401030010, 401030001, 401040001, 401050001, 401050002 | Present | Yes |
| 1.5 | 501020000, fill-in-the-blanks-501020010, 501020001, 501030001, fill-in-the-blanks-501040010, 501040001, 501050001, 501050002 | Present | Yes |
| 1.6 | fill-in-the-blanks-501060110–501060112; code-output-compare-501060001–501060005; multiple-choice-501060100–501060107 | Present | Yes |

**Chapter 1.4:** Lab .md files under `Chapter-1-4---Multiple-Slots-e5f6/` include `{Check It!|assessment}(code-output-compare-40XXXXXX)` for Labs 2.1, 4.1, 5.1, 5.2; **Lab 0.1** uses `fill-in-the-blanks-401010010` then `code-output-compare-401010001`; **Lab 3.1** also includes `fill-in-the-blanks-401030010` before the code test. Both fill-in-the-blanks JSONs use the **Chapter 1.3 Lab 4.1** `tokens.text` pattern (literal `0` for each blank, sequential). Coherent.

**Chapter 1.5:** **Lab 2.0** (command-generator prompt) uses **`code-output-compare-501020000`** (`lab_2.0_grader.py`); **`prompt_template`** and the prompt file are **also checked by Lab 5.1 and Lab 5.2** (`501050001`, `501050002`, grader Check 3). **Lab 2.1** uses `fill-in-the-blanks-501020010` then `code-output-compare-501020001`; **Lab 4.1** uses `fill-in-the-blanks-501040010` (domain slot conditions for `transfer_money_tools`) then `code-output-compare-501040001`. Coherent.

**Chapter 1.6:** **Unit 1.3** uses `multiple-choice-501060105`–`501060107`. **Unit 6.4** uses `multiple-choice-501060100`–`501060104`. **Labs 2.1–4.1** each use **fill-in-the-blanks** then **code-output-compare**, mirroring Chapter 1.5: **`501060111`** (sub-agent `config.yml`) → **`501060001`**; **`501060112`** (`mcp_servers`) → **`501060002`**; **`501060110`** (full `ask_banking_assistant` flow) → **`501060003`**.

---

## 4. Assessment JSON vs grader paths

Each code-output-compare assessment uses a `source.command` that invokes a grader under `.guides/secure/levelN_graders/`. Spot-checked assessment JSONs reference the correct grader paths (e.g. level6_graders/lab_2.1_grader.py for 501060001). Coherent.

---

## 5. JSON validity

- Root `index.json`, chapter `index.json` (1.1–1.5), and sampled assessment JSONs (e.g. code-output-compare-501060001, 401020001) **parse** as valid JSON.
- **Chapter 1.4** `index.json`: placeholder id replaced with valid UUID `e5f6c7d8-9a1b-4c2d-b3e4-5f6a7b8c9d0e`.

---

## 6. Summary of issues (all fixed)

| # | Level / Chapter | Issue | Status |
|---|------------------|--------|--------|
| 1 | Root | `order` did not include Chapter 1.6 | **Fixed** – added to order |
| 2 | 1.6 | No chapter index.json | **Fixed** – created |
| 3 | 1.6 | No unit index.json or page .json | **Fixed** – 7 unit index.json + 21 page .json added |
| 4 | 1.4 | Placeholder UUID in chapter id | **Fixed** – replaced with valid UUID |

---

## 7. Actions taken

1. **Root index** – Added `"Chapter-1-6---Sub-Agents-c7d8"` to `.guides/content/index.json` order.
2. **Chapter 1.6** – Created `Chapter-1-6---Sub-Agents-c7d8/index.json` with title and unit order. Created `index.json` in each unit (Unit-0 … Unit-6) and a matching `.json` for every guide page in units. **Unit 5:** Labs 5.1 and 5.2 are merged into pages **5.1** and **5.2** (two guide pages, not four).
3. **Chapter 1.4** – Replaced placeholder id with `e5f6c7d8-9a1b-4c2d-b3e4-5f6a7b8c9d0e`.
4. **Chapter 1.1** – Removed eight guide pages from TOC (see §8); **Unit 0.4** later restored. Updated affected unit `index.json` files and deleted matching page `.md`/`.json` pairs (except restored 0.4).

---

*Report updated after fixing all incoherences; Chapter 1.1 guide trim is documented in §8.*

---

## 8. Chapter 1.1 guide trim (Codio)

The following **Chapter 1.1** pages were removed from unit `index.json` `order` arrays and their `.md`/`.json` pairs were deleted under `Chapter-1-1---Just-Responses-d3b4/`: Unit **0.3**; Unit **1.3**, **1.4**; **Lab 2.1**; Unit **6.4** (Understanding Agent Behavior); Unit **8.2**, **8.4**, **8.5**. **Unit 0.4** (Getting Help, stem `0-4-Getting-Help-8218`) was **restored** to the TOC and files.

**Deleted page stems (filename ids):** `0-3-Understanding-YAML-Syntax-0971`, `1-3-Real-World-Use-Cases-d20d`, `1-4-Test-Your-Knowledge-3412`, `Lab-2-1--YAML-Syntax-for-Responses-2906`, `6-4-Understanding-Agent-Behavior-b8c9`, `8-2-What-Youve-Learned-e8f9`, `8-4-Whats-Next-Level-2-Preview-8a04`, `8-5-Course-Completion-Checklist-8a05`.

Assessment JSON files referenced only by deleted pages may remain on disk as orphans until cleaned up separately.
