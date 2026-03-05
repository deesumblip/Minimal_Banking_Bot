# Lab 1.1: Exploring Actions

## Guide Content (For Students)

**Placement**: This lab comes right after the section on the Action Class Structure. Before starting, you should understand that every action is a Python class that inherits from `Action`, with required methods `name()` and `run()`.

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

This lab uses **Multiple Choice** and **Fill in the Blanks** assessments. Students explore the `level2/actions/` folder and answer questions based on what they observe. Use Codio's AI Generation feature or manually create assessments from the question bank below.

### Assessment Type

- **Multiple Choice** (select one correct answer)
- **Fill in the Blanks** (short text, case-sensitive or case-insensitive as noted)

### Working Directory / Context

- Students work in `/home/codio/workspace/level2` (Codio)
- Files to explore: `actions/__init__.py`, `actions/action_bank_hours.py`

---

## Question Bank

### Multiple Choice Questions

**Question 1: Actions folder location**  
*What is the main folder where custom Rasa actions live in this project?*

- [ ] `domain/`
- [x] `actions/`
- [ ] `data/`
- [ ] `config/`

---

**Question 2: Purpose of `__init__.py`**  
*Why does the `actions/` folder contain an `__init__.py` file?*

- [ ] To define the action logic
- [ ] To store the action name
- [x] To make the folder a Python package so Rasa can find your actions
- [ ] To configure the domain

---

**Question 3: Class inheritance**  
*What must every custom action class inherit from?*

- [ ] `CollectingDispatcher`
- [ ] `Tracker`
- [x] `Action`
- [ ] `rasa_sdk`

---

**Question 4: What `name()` returns**  
*In `action_bank_hours.py`, what does the `name()` method return?*

- [ ] `ActionBankHours`
- [ ] `bank_hours`
- [x] `action_bank_hours`
- [ ] The filename

---

**Question 5: Sending messages**  
*How does the action send a message to the user?*

- [ ] `tracker.utter_message(...)`
- [ ] `domain.utter_message(...)`
- [x] `dispatcher.utter_message(...)`
- [ ] `return "message text"`

---

**Question 6: Required parameters for `run()`**  
*Which parameters does the `run()` method receive? (Select the most accurate list)*

- [ ] `self` only
- [ ] `self` and `domain`
- [x] `self`, `dispatcher`, `tracker`, and `domain`
- [ ] `self` and `dispatcher` only

---

**Question 7: Return value of `run()`**  
*What should `run()` return for a simple action that only sends a message?*

- [ ] `None`
- [ ] A string
- [x] An empty list `[]`
- [ ] The message text

---

**Question 8: Why an action (not an utter)?**  
*Why is `action_bank_hours` implemented as an action instead of a simple `utter_*` response?*

- [ ] Actions are faster than responses
- [ ] The domain file doesn't support hours
- [x] The message changes based on the current day—it uses `datetime` and conditional logic
- [ ] Actions are required for all bank-related messages

---

### Fill in the Blanks Questions

**Question 9**  
The class in `action_bank_hours.py` is named ________.  
*Expected answer:* `ActionBankHours` (case-sensitive)

---

**Question 9**  
The action file that returns bank hours is named ________.  
*Expected answer:* `action_bank_hours.py` (case-sensitive)

---

**Question 10**  
To send a message to the user, the action calls `dispatcher.________(text="...")`.  
*Expected answer:* `utter_message` (case-sensitive)

---

**Question 11**  
Actions are imported from the ________ module.  
*Expected answer:* `rasa_sdk` (case-sensitive)

---

**Question 12**  
The `CollectingDispatcher` is imported from `rasa_sdk.________`.  
*Expected answer:* `executor` (case-sensitive)

---

## Codio Setup Instructions

### Multiple Choice

1. Add a **Multiple Choice** assessment for each multiple-choice question (Questions 1–7).
2. Copy the question text and options from the Question Bank above.
3. Mark the correct answer (indicated with [x]).
4. Set points (e.g., 1–2 per question, total ~10–14).
5. Use Codio's AI Generation if available: provide the question and correct answer as context.

### Fill in the Blanks

1. Add a **Fill in the Blanks** (or short-answer) assessment for each fill-in question (Questions 8–12).
2. Use the expected answers provided; configure case sensitivity as needed.
3. Set points (e.g., 1 per question, total 5).
4. For AI-based grading: provide the question stem and expected answer in the rubric.

### Suggested Point Allocation

| Questions | Type              | Points |
|----------|-------------------|--------|
| 1–7      | Multiple choice   | 14 (2 each) |
| 8–12     | Fill in the blanks| 5 (1 each) |
| **Total**|                   | **19** |

---

## Learning Objectives

- SWBAT locate the `actions/` folder in a Rasa project
- SWBAT identify the purpose of `__init__.py` in the actions folder
- SWBAT recognize the structure of an action file (class, `name()`, `run()`)
- SWBAT match action concepts (inheritance, dispatcher, return value) to their implementation
