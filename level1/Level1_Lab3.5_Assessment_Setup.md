# Lab 3.5: Complete Your Bot for Training - Assessment Setup

## Guide Content (For Students)

**Placement**: After Lab 3.4 (Flow Descriptions and LLM Matching), before Unit 4 and Lab 6.1.

**Objective**: Add flows that use `utter_hours` and `utter_balance` by pasting pre-written response text and flow files so the assessment for this section can verify the project. (If Lab 3.4 passed, students' own responses were valid; here they use the exact versions required to pass the Lab 3.5 assessment.)

Students paste the provided YAML into `domain/basics.yml` and create `data/basics/hours.yml` and `data/basics/balance.yml`, then run the assessment.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student has completed Lab 3.5: domain contains `utter_hours` and `utter_balance`, and `hours.yml` and `balance.yml` exist with the correct flow structure.

### Assessment Type

**Code Test** (Python grader script)

### Grader Script Location

```
.guides/secure/level1_graders/lab_3.5_grader.py
```

### Command (Codio)

From **workspace root** (`/home/codio/workspace`):

```
python3 /home/codio/workspace/.guides/secure/level1_graders/lab_3.5_grader.py
```

Working Directory: `/home/codio/workspace` (or project root).

### Expected Output

- **Step 1: PASSED** – Domain has utter_hours and utter_balance  
- **Step 2: PASSED** – hours.yml has correct structure  
- **Step 3: PASSED** – balance.yml has correct structure  
- Final line: **PASS**

### Test Cases (Codio Code Test)

| # | Expected output (substring) | Points |
|---|----------------------------|--------|
| 1 | Step 1: PASSED             | 1      |
| 2 | Step 2: PASSED             | 1      |
| 3 | Step 3: PASSED             | 1      |

**Total**: 3 points. Allow partial points; substring match ON.

### Task ID

Create or use a code-output-compare assessment with a unique taskId (e.g. `code-output-compare-lab-3-5`) and attach it to the Lab 3.5 section in the Chapter 1.1 guide.
