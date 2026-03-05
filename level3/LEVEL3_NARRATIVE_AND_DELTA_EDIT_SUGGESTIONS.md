# Level 3: Suggested Edits for Narrative, Redundancy, and Full Delta Coding

This document suggests concrete edits to (1) improve narrative structure, (2) reduce redundancy, and (3) ensure students code the full delta between Level 3 and Level 2 under guidance.

---

## Part A: Narrative structure

### A1. State implementation order once (0.2)

**File:** `Level3_Unit0_Content_0.2_What-Level-3-Adds.md`

**Add** after the opening paragraph (after "You will just add memory on top."):

```markdown
You will implement in this order: **domain** (Lab 3.1), then **the action that uses the slot** (Lab 4.1), then **the flow that collects it** (Lab 5.1). That way you see how the action works before you wire it into a flow.
```

**Why:** Aligns the reader with the actual sequence (define → read → collect) and avoids confusion with the conceptual order "define, collect, read" from Unit 1.

---

### A2. Link Unit 3 to the "define" step (3.1)

**File:** `Level3_Unit3_Content_3.1_The-Slots-Section.md`

**Add** after the first sentence ("Slots are defined in the domain file, just like responses and actions."):

```markdown
This is the **define** step you saw in Unit 1.2: you add the slot and the ask response so that flows and actions can use them.
```

**Why:** Reinforces the three-step model and ties the domain page to the big picture.

---

### A3. Callback from Unit 5 to Unit 1 (5.1 and 5.2)

**File:** `Level3_Unit5_Content_5.1_The-Collect-Step.md`

**Replace** the first paragraph with:

```markdown
A flow can ask for information before running an action using a **collect step**. You saw how this works in **Unit 1.3**: the step tells Rasa to get the slot value before continuing; if the slot is empty, Rasa asks using `utter_ask_*`; once the slot has a value, the flow continues. In **Lab 5.1** you will add this step to your first flow.
```

**File:** `Level3_Unit5_Content_5.2_How-Collection-Works.md`

**Replace** the opening with:

```markdown
As in Unit 1.3, when the flow runs:
```

Then keep the numbered list as-is (or trim to two bullets: "Slot empty → ask and store" and "Slot has value → continue to action").

**Why:** Reduces repetition and makes Unit 5 the "apply it" moment instead of re-teaching collection.

---

## Part B: Reducing redundancy

### B1. Keep Unit 1 as the single place for "how collection works"

- **Unit 1.2** and **1.3** stay as the main explanation of define / collect / read and of collect-step behavior.
- **Unit 5.1**: Shortened as in A3 (syntax + callback to 1.3 + "in Lab 5.1 you'll add it").
- **Unit 5.2**: One sentence that references 1.3, then the short runtime list (or two bullets). Optionally remove 5.2 and fold that one sentence into 5.3.

### B2. Optional: Single "Collect in the flow" page in Unit 5

Instead of 5.1 and 5.2 as two pages, merge into one short page, e.g. **5.1 The collect step in your flow**:

- One sentence: You saw the collect step in Unit 1.3; in Lab 5.1 you'll add it to `check_balance.yml`.
- Syntax block (collect + description).
- One line: If the slot is empty the bot asks; if it has a value the flow continues to the action.
- Point to Lab 5.1.

**Why:** Less redundancy and a single place that "collect" is taught (Unit 1), with Unit 5 as application only.

---

## Part C: Students code the full delta (L3 − L2)

**Current gap:** The only L3−L2 code students do not write is `action_check_balance_simple.py`. They currently "explore" a provided file.

**Goal:** Students write the action themselves under guidance so they code the full delta.

### C1. Convert Lab 4.1 from "Explore" to "Write the action"

**File:** `Level3_Lab4.1_Content.md` (and .guides copy)

**Change the lab** from "open and explore the provided file" to **step-by-step creation** of `action_check_balance_simple.py`:

1. **Create** the file `level3/actions/action_check_balance_simple.py` (if it exists, replace or follow steps to match).
2. **Add** imports: `typing` (Any, Dict, List, Text), `rasa_sdk` (Action, Tracker, CollectingDispatcher).
3. **Define** the class `ActionCheckBalanceSimple(Action)` with:
   - `name(self)` returning `"action_check_balance_simple"`.
   - `run(self, dispatcher, tracker, domain)`:
     - Read the slot: `account = tracker.get_slot("account") or "<missing>"`.
     - Define a list of placeholder values, e.g. `["account number", "user_account_number", "<missing>"]`.
     - If `account` (lowercased) is in that list: call `dispatcher.utter_message(response="utter_ask_account")` and `return []`.
     - Otherwise: call `dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")` and `return []`.
4. **Verify** the file is in `level3/actions/` and the domain already lists `action_check_balance_simple` (from Lab 3.1).

Keep the **Check Your Knowledge** section (and answer key) so they still reason about what the code does.

**Narrative:** "In Lab 4.1 you will write the action that reads the `account` slot and handles placeholders. The domain already registers this action from Lab 3.1; here you create the Python file."

### C2. Do not ship the action file (or ship only as reference)

- **Option A (recommended):** Remove `level3/actions/action_check_balance_simple.py` from the repo. Students create it in Lab 4.1. Keep a copy in `.guides/secure/level3_graders/` (e.g. `lab_4.1_solution_reference.md` or a reference `.py`) for grading only.
- **Option B:** Keep the file in the repo but rename to `action_check_balance_simple_solution.py` and instruct students to create `action_check_balance_simple.py` by following the lab (or copying and adapting the solution). Less clean.

### C3. Update all "provided" / "explore" wording

**Files to update:**

- **0.2:** Change "You'll explore how the provided action uses the slot" → "You'll **write** the action that uses the slot (Lab 4.1)". Change "Already provided" → "In Lab 3.1 you add the action **name** to the domain; in Lab 4.1 you will **write** the action file."
- **0.1:** Change "Provided for Level 3: … you will register it in the domain in Lab 3.1 and explore it in Lab 4.1" → "In Lab 3.1 you register **action_check_balance_simple** in the domain; in Lab 4.1 you will **write** the file `action_check_balance_simple.py`."
- **README:** Same idea: "In Lab 4.1 you **write** the action that reads the slot and handles placeholders" (not "explore").
- **Unit 4.1 and 4.2:** Keep teaching `tracker.get_slot`, placeholder handling, and re-prompting. Change "In Lab 4.1 you'll explore" → "In **Lab 4.1** you'll **write** this action in `action_check_balance_simple.py`."
- **Unit 5.3:** "You already … registered … in Lab 3.1, and you **wrote** the action in Lab 4.1" (not "explored").
- **Lab 5.1 intro:** "You have … defined the slot … (Lab 3.1) and **written** the action (Lab 4.1). Now create the flow…"

### C4. Lab 4.1 assessment

- **If Lab 4.1 is graded:** Use an LLM Rubric (or script) that checks for: file `level3/actions/action_check_balance_simple.py`; use of `tracker.get_slot("account")`; placeholder check and `utter_ask_account` re-prompt; balance message. Reference solution in `.guides/secure/level3_graders/` (e.g. `lab_4.1_solution_reference.md` with code snippet or full reference).
- **If Lab 4.1 stays ungraded:** No change to assessment; narrative still requires them to write the file.

### C5. Lab 3.1 wording (action registration)

**File:** `Level3_Lab3.1_Content.md`

**Add** one line in the objective or Step 4:

- "You will add the action **name** to the domain here; you will **create the action file** in Lab 4.1."

**Why:** Makes it explicit that 3.1 is "register the name" and 4.1 is "write the code," so the full delta is coded by them.

---

## Part D: Summary of suggested edits

| Area | File(s) | Edit |
|------|---------|------|
| **Narrative** | 0.2 | Add one short paragraph stating implementation order (domain → action → flow). |
| **Narrative** | 3.1 | Add one sentence linking domain to the "define" step from 1.2. |
| **Narrative** | 5.1, 5.2 | Shorten and add callbacks to Unit 1.3; avoid re-teaching collection. |
| **Redundancy** | 5.1, 5.2 | Treat Unit 1 as canonical for "how collection works"; Unit 5 = syntax + application only. Optionally merge 5.1 and 5.2 into one page. |
| **Full delta** | Lab 4.1 | Convert from "explore provided file" to "write `action_check_balance_simple.py`" with step-by-step instructions. |
| **Full delta** | Repo | Do not ship `action_check_balance_simple.py` (or only as grader reference). |
| **Full delta** | 0.1, 0.2, README, Unit 4, Unit 5.3, Lab 5.1 | Replace "explore" / "provided" with "write" / "create the action file" and clarify 3.1 = register name, 4.1 = write file. |
| **Full delta** | Lab 3.1 | Add one line: action name in domain here; action file created in Lab 4.1. |
| **Full delta** | Lab 4.1 assessment | If grading: add rubric or script for action file content; keep solution reference for graders. |

---

## Implementation order

1. **Narrative and redundancy (Parts A and B):** Low risk; improves flow and reduces repetition.
2. **Full-delta coding (Part C):** Requires rewriting Lab 4.1, updating 0.1/0.2/README/Unit 4/Unit 5.3/Lab 5.1/Lab 3.1, and deciding whether to remove or hide the provided action file and how to assess Lab 4.1.

If you want to implement only narrative and redundancy first, do Part A and B; then do Part C in a second pass.
