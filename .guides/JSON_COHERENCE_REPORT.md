# JSON Coherence Report: Content and Assessments by Level / Chapter

This report compares **content** (`.guides/content/` chapter and unit structure) with **assessments** (`.guides/assessments/*.json` and level Assessment_Setup docs) for each Level and its Codio chapter.

---

## 1. Root and chapter index coherence

### Root `.guides/content/index.json`
- **order**: Chapter-1-1, Chapter-1-2, Chapter-1-3, Chapter-1-4, Chapter-1-5. Coherent.

### Chapter index.json vs unit folders

| Chapter | index.json `order` | Unit folders present | Coherent? |
|---------|--------------------|----------------------|-----------|
| 1.1 Just Responses | Unit-0 … Unit-8 (9 units) | Yes (all match) | Yes |
| 1.2 Custom Actions | Unit-0 … Unit-8 (9 units) | Yes | Yes |
| 1.3 Slot Collection | Unit-0 … Unit-8 (9 units) | Yes | Yes |
| **1.4 Multiple Slots** | **Unit-1 … Unit-6 only (6 units)** | **No Unit-0 folder** | **No** |
| 1.5 Tool Calling | Unit-0 … Unit-6 (7 units) | Yes | Yes |

**Issue (Chapter 1.4):** The chapter **order** does not include **Unit-0** (Recap Level 3), and there is **no** `Unit-0--*` folder under `Chapter-1-4---Multiple-Slots-e5f6/`. The Level 4 course outline and content source (`level4/`) define Unit 0 (0.1 Your Level 3 Banking Bot, 0.2 What Level 4 Adds). So Chapter 1.4 is missing Unit 0 in both the chapter index and the filesystem.

---

## 2. Unit index.json vs page files

For each unit, the `order` array should list page ids that have a matching `.md` and `.json` in that unit folder.

### Spot checks
- **Chapter 1.3 Unit 1:** order = 1-1, 1-2, 1-3. Three pages; no 1-4. Coherent with current Unit 1 content.
- **Chapter 1.4 Unit 1:** order = 1-1, 1-2, 1-3, 1-4-Test-Your-Knowledge-e4f5. All four have corresponding .md and .json. Coherent.
- **Chapter 1.4 Unit 6:** order = 6-1 … 6-7 (all seven). All have .md and .json. Coherent.

No orphan `order` ids found in the checked units (i.e. every id in `order` has a matching page).

---

## 3. Assessment JSON vs content (Check It! tags)

Assessments are wired into the guide by **content**: markdown pages use `{Check It!|assessment}(taskId)`. Codio then looks up `.guides/assessments/<type>-<id>.json` by taskId.

### Level 1 (Chapter 1.1)
- Content references: multiple-choice-*, llm-based-auto-rubric-*, code-output-compare-3333363688, 2562507355, 7772000001, etc.
- Assessment JSONs: Present for the referenced taskIds (code-output-compare, multiple-choice, llm-based-auto-rubric). Coherent.

### Level 2 (Chapter 1.2)
- Content references: code-output-compare-2266471391, 1451983168, 1597644299, 389374509, 1070925386; multiple-choice-*.
- Assessment JSONs: Present. Coherent.

### Level 3 (Chapter 1.3)
- Content references: code-output-compare-3187585640, 2346557110, 1235165472, 1029038275; multiple-choice-*; fill-in-the-blanks-1454903744.
- Assessment JSONs: Present. Level 3 Implementation Overview and Lab Assessment_Setup docs state the taskIds; guide .md files contain the matching `{Check It!|assessment}(...)` tags. Coherent.

### Level 4 (Chapter 1.4)
- **Content references:** **None.** No `.md` file under `Chapter-1-4---Multiple-Slots-e5f6/` contains any `{Check It!|assessment}(...)` tag.
- **Assessment JSONs:** Present for Level 4 labs:
  - code-output-compare-401020001 (Lab 2.1)
  - code-output-compare-401030001 (Lab 3.1)
  - code-output-compare-401040001 (Lab 4.1)
  - code-output-compare-401050001 (Lab 5.1)
  - code-output-compare-401050002 (Lab 5.2)
- **Level 4 Assessment_Setup docs:** Describe Option A (LLM Rubric) and Option B (Standard Code Test) and grader paths but do **not** specify these taskIds in the repo (unlike Level 3, which explicitly documents taskId in the Assessment_Setup).

**Issue (Chapter 1.4):** The guide **content** does not link to the assessments. The lab pages (Lab 2.1, 3.1, 4.1, 5.1, 5.2) say “Run the assessment when done” but do **not** include `{Check It!|assessment}(code-output-compare-401020001)` etc. So the assessment JSONs exist and are correct, but students will not see a Check It! button unless the tags are added to the corresponding guide .md (and ideally to the level4 source Lab content as well).

---

## 4. Assessment JSON vs grader paths

Each code-output-compare assessment has a `source.command` that invokes a grader under `.guides/secure/levelN_graders/`.

| taskId | command path | Grader file expected | Exists? |
|--------|----------------|----------------------|---------|
| L1 3333363688 | (not in sampled file) | level1 | — |
| L1 2562507355 | level1_graders/lab_6.1_grader.sh | level1 | Yes |
| L2 2266471391 | level2_graders/lab_3.1_grader.sh | level2 | Yes |
| L2 1451983168 | level2_graders/lab_4.1_grader.sh | level2 | Yes |
| L2 1597644299 | level2_graders/lab_5.1_grader.sh | level2 | Yes |
| L2 389374509 | level2_graders/lab_5.1_grader.sh | level2 | Yes |
| L2 1070925386 | level2_graders/lab_6.1_grader.sh | level2 | Yes |
| L3 3187585640 | level3_graders/lab_3.1_grader.py | level3 | Yes |
| L3 2346557110 | level3_graders/lab_4.1_grader.py | level3 | Yes |
| L3 1235165472 | level3_graders/lab_5.1_grader.py | level3 | Yes |
| L3 1029038275 | level3_graders/lab_6.1_grader.py | level3 | Yes |
| L4 401020001 | level4_graders/lab_2.1_grader.py | level4 | Yes |
| L4 401030001 | level4_graders/lab_3.1_grader.py | level4 | Yes |
| L4 401040001 | level4_graders/lab_4.1_grader.py | level4 | Yes |
| L4 401050001 | level4_graders/lab_5.1_grader.py | level4 | Yes |
| L4 401050002 | level4_graders/lab_5.2_grader.py | level4 | Yes |
| L5 501020001 | level5_graders/lab_2.1_grader.py | level5 | Yes |
| L5 501030001 | level5_graders/lab_3.1_grader.py | level5 | Yes |
| L5 501040001 | level5_graders/lab_4.1_grader.py | level5 | Yes |
| L5 501050001 | level5_graders/lab_5.1_grader.py | level5 | Yes |
| L5 501050002 | level5_graders/lab_5.2_grader.py | level5 | Yes |

Grader paths in assessment JSONs match the documented level and lab numbers and the existing `.guides/secure/levelN_graders/` files. Coherent.

### Level 5 (Chapter 1.5)
- **Content references:** Chapter 1.5 lab .md files contain `{Check It!|assessment}(code-output-compare-501020001)` … `501050002`. level5 Level5_Lab*_Content.md and Level5_Lab*_Assessment_Setup.md document the same taskIds.
- **Assessment JSONs:** Present for all five labs (501020001, 501030001, 501040001, 501050001, 501050002).
- **Unit 6 pages:** 6.1–6.7 (6.4 Knowledge Check, 6.5 Limitations, 6.6 What's Next Level 6 Preview, 6.7 Course Completion Checklist) have matching .md and .json in Unit-6--Summary-and-Next-Steps-L5u6; unit index order lists all seven. Unit 1 has three pages (1.3 Test Your Knowledge added). Coherent.

---

## 5. Level 4 vs Level 3 pattern (documentation)

- **Level 3:** Lab Assessment_Setup docs explicitly state: “The Lab X.X page in the Chapter 1.3 guide includes: `{Check It!|assessment}(code-output-compare-XXXXX)`.” So implementers and content stay in sync.
- **Level 4:** Lab Assessment_Setup docs describe how to configure the assessment in Codio (Option A/B, command, working directory) but do **not** document the taskId or the exact Check It! tag to embed in the guide. So content and assessment wiring are not documented in one place for Level 4.

---

## 6. Summary of issues

| # | Level / Chapter | Issue | Severity |
|---|------------------|--------|----------|
| 1 | 1.4 | Chapter index has no Unit-0; no Unit-0 folder. Unit 0 (Recap Level 3) content is missing from the guide. | High |
| 2 | 1.4 | No `{Check It!|assessment}(...)` tags in any Chapter 1.4 .md. Lab pages don’t link to code-output-compare-401020001, 401030001, 401040001, 401050001, 401050002. | High |
| 3 | 1.4 | Level 4 Lab Assessment_Setup docs do not state the taskIds or the exact Check It! tag for each lab (unlike Level 3). | Low (documentation) |

---

## 7. Recommended actions

1. **Chapter 1.4 – Unit 0**
   - Add a unit folder, e.g. `Unit-0--Recap-What-You-Built-in-Level-3-e5f6`, under `Chapter-1-4---Multiple-Slots-e5f6/`.
   - Add pages for 0.1 (Your Level 3 Banking Bot) and 0.2 (What Level 4 Adds) (content from `level4/Level4_Unit0_Content_0.1_*.md` and `0.2_*.md`).
   - Prepend `Unit-0--...` to the chapter `index.json` **order** so Unit 0 appears first.

2. **Chapter 1.4 – Assessment tags**
   - Add to the **guide** Lab .md (and optionally to `level4/Level4_Lab*_Content.md`):
     - Lab 2.1: `{Check It!|assessment}(code-output-compare-401020001)`
     - Lab 3.1: `{Check It!|assessment}(code-output-compare-401030001)`
     - Lab 4.1: `{Check It!|assessment}(code-output-compare-401040001)`
     - Lab 5.1: `{Check It!|assessment}(code-output-compare-401050001)`
     - Lab 5.2: `{Check It!|assessment}(code-output-compare-401050002)`
   - Place each tag where the lab says “Run the assessment when done” (or equivalent).

3. **Level 4 Assessment_Setup docs**
   - In each `Level4_Lab*_Assessment_Setup.md`, add a short line similar to Level 3: “The Lab X.X page in the Chapter 1.4 guide includes: `{Check It!|assessment}(code-output-compare-40XXXXXX)`.” with the correct taskId. Optionally add the assessment JSON path (e.g. `.guides/assessments/code-output-compare-401020001.json`).

---

*Report generated from inspection of `.guides/content/`, `.guides/assessments/`, and level implementation/assessment docs.*
