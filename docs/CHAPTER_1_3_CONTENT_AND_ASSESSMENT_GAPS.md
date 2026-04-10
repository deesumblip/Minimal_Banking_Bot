# Chapter 1.3: Content and Assessment Progression — Gap Analysis

This document summarizes gaps and inconsistencies found in Chapter 1.3 (Slot Collection) content and assessment progression. Recommendations are at the end.

**Resolved in repo (items 1–5):** (1) 4.2 now states Lab 4.1 has a graded code assessment. (2) 3.1 domain example includes all three actions (`action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple`) with prose that the starter preloads the Level 2 actions. (3) Lab 6.1 references **Lab 0.1 in Chapter 1.1** for venv/Rasa Pro and `.env`. (4) Unit 5.2 uses new MCQ `multiple-choice-5130520013` (slot already filled); Unit 2.3 still uses `multiple-choice-3629141196` (empty slot). (5) Unit 0.1 states **`action_holiday_hours.py`** is **preloaded** at the start of Chapter 1.3; Lab 3.1 grader and rubric expect all three action names in `domain/basics.yml`.

---

## 1. Content gaps

### 1.1 Unit 4.2 says Lab 4.1 has “no graded assessment” (incorrect) — fixed

- **Where:** `Unit-4--Reading-Slots-in-Actions-0d1e/4-2-Placeholder-Handling-a4b5.md`
- **Issue:** The page states: “That lab has no graded assessment.”
- **Reality:** Lab 4.1 includes `{Check It!|assessment}(fill-in-the-blanks-2346557111)` and `{Check It!|assessment}(code-output-compare-2346557110)` and instructs students to complete both.
- **Gap:** Content contradicts the presence of a graded assessment and can confuse students or instructors.

**Recommendation:** In 4.2, remove or rephrase the sentence about “no graded assessment” (e.g. “Lab 4.1 includes a code assessment that checks the action file.”) so it matches the lab.

---

### 1.2 Unit 3.1 domain example — fixed (three actions + preload story)

- **Where:** `Unit-3--Defining-Slots-in-the-Domain-6f7a/3-1-The-Slots-Section-4b5c.md` (and Lab 3.1).
- **Former issue:** Example sometimes showed only `action_bank_hours` + `action_check_balance_simple`, which encouraged dropping **`action_holiday_hours`** and breaking training.
- **Current:** The unit snippet lists **`action_bank_hours`**, **`action_holiday_hours`**, and **`action_check_balance_simple`**. Unit 0.1 and Lab 3.1 state that **`action_holiday_hours.py`** is **preloaded** with the Chapter 1.3 starter; assessments expect the full three-name `actions:` list.

---

### 1.3 Cross-chapter reference to “Lab 0.1” (prerequisites) — fixed in Lab 6.1

- **Where:** `Unit-6--Training-and-Testing-with-Slots-2f3a/Lab-6-1-Training-and-Testing-d7e8.md` (and similarly in Ch 1.4)
- **Issue:** Lab 6.1 says: “If RASA_LICENSE or OPENAI_API_KEY is not set, check Lab 0.1 or ask your instructor.” Lab 0.1 lives in **Chapter 1.1** (Just Responses), not in Chapter 1.3.
- **Gap:** If the course is taken out of order or 1.3 is used standalone, “Lab 0.1” is ambiguous (which chapter? which unit?).

**Recommendation:** Either (a) add a short prerequisite note at the start of Chapter 1.3 (e.g. in Unit 0) that “Lab 0.1 in Chapter 1.1 covers venv and Rasa Pro setup,” or (b) phrase the reference as “Lab 0.1 in Chapter 1.1 (Prerequisites)” so the location is clear.

---

### 1.4 Duplicate assessment ID in Unit 2 and Unit 5 — fixed

- **2.3** still uses `multiple-choice-3629141196` (when slot is **empty**, agent asks with `utter_ask_account`).
- **5.2** now uses `multiple-choice-5130520013` (when slot **already has a value**, agent skips asking and continues). Assessment file: `.guides/assessments/multiple-choice-5130520013.json`.

---

## 2. Assessment progression

### 2.1 Overall flow (no structural gap)

- **Unit 0–2:** Conceptual (slots, types, naming). Assessments: multiple-choice in 1.1 and 2.3.
- **Unit 3:** Define slot in domain. Lab 3.1 has a **code-output-compare** assessment; content prepares students for it.
- **Unit 4:** Read slots and placeholders. Lab 4.1 has a **code-output-compare**; 4.1 and 4.2 explain the logic first; 4.2 now matches the lab on grading.
- **Unit 5:** Collect in flows. Lab 5.1 has **code-output-compare**; 5.1–5.3 explain collect steps and flow before the lab. Progression is correct.
- **Unit 6:** Lab 6.1 has **code-output-compare** (training); Lab 6.2 and page 6.2 state “no graded assessment” / “completion-based” but include multiple-choice “Check Your Knowledge” items. So “no graded assessment” means no code test, which is consistent.
- **Unit 7:** Lab 7.1 is completion-based with multiple-choice only; stated as “no graded assessment.” Consistent.
- **Unit 8:** 8.1 reuses earlier multiple-choice IDs (recap); 8.2–8.5 are summary, limitations, next steps, checklist. No missing step.

Conclusion: **Content teaches concepts before labs; labs then have code or knowledge checks.** The only assessment-related content gap is the “no graded assessment” claim in 4.2.

---

### 2.2 “Graded” vs “completion-based” wording

- **Labs 6.2 and 7.1** say they have “no graded assessment” or are “completion-based,” but both include multiple-choice assessments.
- **Gap:** “No graded assessment” could be read as “no points” or “no Check It! at all.” In practice it means “no code-output-compare / code test.”
- **Recommendation:** Use consistent wording, e.g. “This lab has no code assessment; it is completion-based and includes knowledge-check questions.”

---

## 3. Content-to-lab dependency check

| Lab    | Depends on content / prior labs                    | Status |
|--------|----------------------------------------------------|--------|
| Lab 3.1 | Unit 3.1 (slots section, utter_ask_account)       | OK     |
| Lab 4.1 | Lab 3.1 (domain), Unit 4.1 (get_slot), Unit 4.2 (placeholders) | OK     |
| Lab 5.1 | Lab 3.1 (slot + action in domain), Lab 4.1 (action file), Unit 5.1–5.3 (collect step) | OK     |
| Lab 6.1 | Domain + flow + action from 3.1, 4.1, 5.1         | OK (references Lab 0.1 for env) |
| Lab 6.2 | Lab 6.1 (trained model)                            | OK     |
| Lab 7.1 | Full agent (all prior labs)                          | OK     |

No missing dependencies; only the Lab 0.1 reference needs clarification (1.3).

---

## 4. Summary of recommendations

1. ~~**4.2 Placeholder-Handling:**~~ Done.
2. ~~**3.1 The-Slots-Section:**~~ Done.
3. ~~**Lab 6.1:**~~ Done (Chapter 1.1 cited). Optional: add the same Chapter 1.1 pointer in **Unit 0** for students who jump straight to Chapter 1.3.
4. ~~**Assessment ID 3629141196 / 5.2:**~~ Done — 5.2 uses `multiple-choice-5130520013` (already-filled slot); 2.3 keeps `multiple-choice-3629141196` (empty slot).
5. **Labs 6.2 and 7.1:** Optionally clarify that “no graded assessment” means no code test but may include knowledge-check questions.

Chapter 1.3 content and assessments for items 1–4 are now aligned as described above.
