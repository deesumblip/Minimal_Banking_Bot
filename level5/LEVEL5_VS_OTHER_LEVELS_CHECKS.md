# Level 5 vs Other Levels: Comparison and Recommended Checks

This document compares Level 5 (Tool Calling) to Levels 1-4 and lists **additional checks or additions** so Level 5 matches the same standards and patterns.

---

## 1. Unit 1: Test Your Knowledge page

| Level | Unit 1 (or early unit) | Test Your Knowledge page |
|-------|------------------------|--------------------------|
| 1.1   | Unit 1 Intro to Rasa Bots | 1.4 Test Your Knowledge |
| 1.2   | Unit 1 Intro to Actions   | 1.4 Test Your Knowledge |
| 1.3   | Unit 2 Slot Types         | 2.3 Test Your Knowledge |
| 1.4   | Unit 1 Multiple Slots     | 1.4 Test Your Knowledge |
| **1.5** | **Unit 1 Introduction to Tools** | **None** - only 1.1, 1.2 |

**Check needed:** Add **Unit 1.3 or 1.4 Test Your Knowledge** for Level 5 (e.g. short Q&A on tools vs actions, when to use tools, __all__, tools_module). Add to both level5/ source and .guides Unit 1 (new page .md + .json, update index order).

---

## 2. Unit 6: Summary unit page count and types

| Level | Unit 6 pages | Extra pages beyond 6.1-6.4 + Checklist |
|-------|--------------|----------------------------------------|
| 1.4   | 7            | 6.5 Limitations of Level 4, 6.6 What's Next (Level 5 Preview), 6.7 Course Completion Checklist |
| **1.5** | **5**     | 6.4 Knowledge Check, 6.5 Course Completion Checklist only |

**Check needed:** Consider adding for parity with Level 4: **6.5 Limitations of Level 5**, **6.6 What's Next Level 6 Preview**, and renumber current 6.5 Checklist to 6.7. Optional: keep Level 5 Unit 6 shorter and document the decision.

---

## 3. Unit 6 source-of-truth in level5/

Level 4 has all Unit 6 content files (6.1-6.7) in level4/. Level 5 has only 6.1, 6.2, 6.3 in level5/; 6.4 and 6.5 exist in .guides but not in level5/ as canonical source.

**Check needed:** Add Level5_Unit6_Content_6.4_Knowledge-Check.md and Level5_Unit6_Content_6.5_Course-Completion-Checklist.md in level5/ and keep in sync with .guides.

---

## 4. TUTORIAL.md

Level 4 has level4/TUTORIAL.md (table of contents, module-by-module summary). Level 5 has no TUTORIAL.md.

**Check needed:** Add level5/TUTORIAL.md with ToC and module summaries aligned with Level 4 style.

---

## 5. Supporting docs

Level 4 has LEVEL4_CONTENT_LABS_AND_ASSESSMENTS.md, LEVEL4_BUILD_FROM_LEVEL3_APPROACH.md. Level 5 has LEVEL5_BUILD_FROM_LEVEL4_APPROACH.md and CODIO_IMPLEMENTATION_GUIDE but no LEVEL5_CONTENT_LABS_AND_ASSESSMENTS equivalent.

**Check needed:** Optional. Add LEVEL5_CONTENT_LABS_AND_ASSESSMENTS.md if you want one-place mapping of content to labs and taskIds.

---

## 6. Grader script behavior (Windows / Unicode)

Graders use /home/codio/workspace and Unicode symbols in print(); on Windows this can fail (path and cp1252 encoding).

**Check needed:** Document that graders are Codio-only, or make them Windows-friendly (env var for workspace root, ASCII-only output).

---

## Summary: What Level 5 still needs

| # | Check | Priority | Action |
|---|--------|----------|--------|
| 1 | Unit 1 Test Your Knowledge | Medium | Add 1.3 or 1.4 Test Your Knowledge in level5 + .guides Unit 1. |
| 2 | Unit 6 Limitations + What's Next | Low | Optionally add 6.5 Limitations, 6.6 Level 6 Preview; renumber Checklist to 6.7. |
| 3 | Unit 6.4/6.5 source in level5/ | High | Add Level5_Unit6_Content_6.4 and 6.5 .md in level5/; sync with .guides. |
| 4 | TUTORIAL.md | Medium | Add level5/TUTORIAL.md (ToC + module summary). |
| 5 | LEVEL5_CONTENT_LABS_AND_ASSESSMENTS | Low | Optional doc mapping content to labs and taskIds. |
| 6 | Grader Windows/Unicode | Low | Document Codio-only or make graders env/ASCII-safe. |
