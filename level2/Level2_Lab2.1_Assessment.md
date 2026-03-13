# Lab 2.1: Exploring the Actions Folder

## Guide Content (For Students)

**Placement**: This lab comes right after Unit 2 Test Your Knowledge. You should understand that every action is a Python class that inherits from `Action`, with required methods `name()` and `run()`.

---

#### Complete the action file (fill in the blanks)

Fill in the blanks to complete a **branch address** action that returns the bank's main branch address and the current day (so the message is dynamic and requires an action, not a static `utter_`). The structure is the same as the bank hours action: class name, `name()`, `run()` with `dispatcher`, `tracker`, `domain`, and sending a message.

*In the Codio guide this section has a Check It! assessment linked to `fill-in-the-blanks-1202100001` (`.guides/assessments/fill-in-the-blanks-1202100001.json`).*

---

### Your Task

Explore the `level2` folder, focusing on the `actions/` subfolder. Use the file tree and open the files to see how the structure you learned is implemented in code.

**What to do:**
1. Navigate to the `level2` folder in your workspace
2. Expand the `actions/` folder in the file tree
3. Open `actions/__init__.py` and `actions/action_bank_hours.py`
4. Read the code and compare it to the basic structure you learned
5. Answer the assessment questions below

---

### What You're Looking For

- **`actions/` folder** – Where all custom action files live
- **`__init__.py`** – Makes the folder a Python package so Rasa can find your actions
- **`action_bank_hours.py`** – An example action: imports (including `datetime`), class, `name()`, `run()` with conditional logic

Use what you see to answer the questions.

---

## Assessment Setup (For Implementers)

### Overview

This lab uses **Fill in the Blanks** only. The first assessment is a single fill-in-the-blanks task that completes a full action file (branch address)—see `.guides/assessments/fill-in-the-blanks-1202100001.json`. Students then explore the `level2/actions/` folder and answer the short fill-in-the-blanks questions below (taskIds 2658905168, 2658905169, 2658905170, 341339148, 235818681).

### Assessment Type

- **Fill in the Blanks** (short text, case-sensitive or case-insensitive as noted)

### Working Directory / Context

- Students work in `/home/codio/workspace/level2` (Codio)
- Files to explore: `actions/__init__.py`, `actions/action_bank_hours.py`

---

## Question Bank

### Fill in the Blanks Questions

**Question 9**  
The class in `action_bank_hours.py` is named ________.  
*Expected answer:* `ActionBankHours` (case-sensitive)

---

**Question 10**  
The action file that returns bank hours is named ________.  
*Expected answer:* `action_bank_hours.py` (case-sensitive)

---

**Question 11**  
To send a message to the user, the action calls `dispatcher.________(text="...")`.  
*Expected answer:* `utter_message` (case-sensitive)

---

**Question 12**  
The action uses the ________ module to check the current day of the week.  
*Expected answer:* `datetime` (case-sensitive)

---

**Question 13**  
The `CollectingDispatcher` is imported from `rasa_sdk.________`.  
*Expected answer:* `executor` (case-sensitive)

---

## Codio Setup Instructions

### Fill in the Blanks

1. The **complete action file** task is already in the guide: `fill-in-the-blanks-1202100001`.
2. Add or keep **Fill in the Blanks** assessments for each short fill-in question (Questions 9–13) with the expected answers below; configure case sensitivity as needed.
3. Set points (e.g., 1 per question for short FIBs; the complete-action-file task may carry more).
4. For AI-based grading: provide the question stem and expected answer in the rubric.

### Suggested Point Allocation

| Assessment | Type              | Points |
|------------|-------------------|--------|
| Complete action file (1202100001) | Fill in the blanks | e.g. 5 |
| Questions 9–13 (short FIB) | Fill in the blanks | 5 (1 each) |
| **Total**  |                   | **10** |

---

## Learning Objectives

- SWBAT complete the structure of a Rasa action file (imports, class, `name()`, `run()`, dispatcher, return)
- SWBAT recognize the structure of an action file (class, `name()`, `run()`) by exploring `actions/`
- SWBAT match action concepts (inheritance, dispatcher, return value, datetime) to their implementation
