# Bridging Lab 4.2 → Lab 6.1: Walk-Through and Assessment

**Problem**: Students hit validation errors at Lab 6.1 (e.g. "utter_balance not in domain") because (1) Lab 3.4 leaves domain updates optional/vague, (2) Lab 5.1 is only multiple choice, and (3) there is no coding checkpoint between Lab 4.2 and Lab 6.1 to verify project readiness.

**Goal**: Walk students through the file setup so that by the time they run Lab 6.1, domain and flows are complete, and add enough content/coding assessment between Lab 4.2 and Lab 6.1.

---

## 1. Tighten Lab 3.4 (domain + flows in one place)

Make Lab 3.4 the **single place** where students add the two new responses and the two new flows, in a fixed order so domain is always complete before flows reference it.

**Suggested structure**

- **Step 1 – Add responses to the domain (required first)**  
  - Open `domain/basics.yml`.  
  - Under `responses:`, add two new responses: `utter_hours` and `utter_balance`.  
  - Provide exact YAML blocks (or a copy-paste snippet) so every student has the same keys.  
  - Explain: "Every `utter_*` used in a flow must exist here. We add these first so the flows we create next are valid."

- **Step 2 – Create `data/basics/hours.yml`**  
  - One flow: `hours`, with `name`, `description`, and `steps` containing `- action: utter_hours`.  
  - Optional: give a full file template so structure is correct.

- **Step 3 – Create `data/basics/balance.yml`**  
  - One flow: `balance`, with `name`, `description`, and `steps` containing `- action: utter_balance`.  
  - Same idea: template or minimal example.

- **Step 4 – Verify before moving on**  
  - "From the `level1` folder, run: `python -m rasa train`."  
  - "If you see errors about an action not in the domain, go back to Step 1 and check that `utter_hours` and `utter_balance` are under `responses:` in `domain/basics.yml`."  
  - "When training completes (or at least passes validation), you’re ready for Unit 4 and later for Lab 6.1."

This makes Lab 3.4 the **bridge** that guarantees a trainable project.

---

## 2. Add a “project readiness” step between Lab 4.2 and Lab 6.1

Introduce one coding/check step so there is something concrete between Lab 4.2 and Lab 6.1.

**Option A – Extend Lab 5.1 with Part 2 (recommended)**

- **Part 1 (unchanged)**  
  - Multiple-choice / short-answer questions about config (language, LLM model, actions module, temperature).

- **Part 2 – Project readiness for training**  
  - Short checklist:
    - "I have added `utter_hours` and `utter_balance` to `domain/basics.yml` (Lab 3.4)."
    - "I have `data/basics/hours.yml` and `data/basics/balance.yml`."
  - One command: "From `level1`, run `python -m rasa train`. Does it pass validation and start training (or finish)? If not, fix the reported error (usually a missing response in the domain)."
  - Success criterion: "Training runs without 'action not in domain' (or similar) errors."

This keeps one “Lab 5.1” but adds a small coding/verification part so there is a clear step between 4.2 and 6.1.

**Option B – New “Lab 5.2: Ready for training”**

- Dedicated short lab after Lab 5.1:
  - Explain that training requires every `utter_*` used in flows to exist in the domain.
  - Checklist: list flow files in `data/basics/`, list responses in `domain/basics.yml`, confirm they match.
  - Run `rasa train` once as a self-check.
  - Optional: simple auto-grader (e.g. “model file exists after `rasa train`” or “no validation error in last run”).

Use Option A if you want to avoid extra lab numbers; use Option B if you want a separate, assessable “readiness” lab.

---

## 3. Short content page before Lab 6.1

Add a short content page (e.g. under Unit 6, before “Lab 6.1: Training Your Agent”) that sets expectations and points back to the bridge.

**Suggested title**: “What training needs” or “Before you run Lab 6.1”.

**Suggested content (short)**:

- Training reads `domain/`, `data/`, and `config.yml`.  
- Every `utter_*` or action used in any flow must appear in the domain (responses or actions).  
- If you completed Lab 3.4, you added `utter_hours` and `utter_balance` and the `hours` and `balance` flows.  
- If `rasa train` reports “action 'utter_XYZ' is used in flow … but it is not listed in the domain”, add that response (or action) to the domain, then run `rasa train` again.  
- Optional: one sentence on “validation runs at the start of `rasa train`; fixing domain/flow mismatches fixes most errors.”

This doesn’t replace the walk-through; it reinforces it and gives a place to point students who hit errors at Lab 6.1.

---

## 4. Summary: what to change

| Item | Change |
|------|--------|
| **Lab 3.4** | Turn it into a strict sequence: (1) Add `utter_hours` and `utter_balance` to domain (with given YAML), (2) Create `hours.yml`, (3) Create `balance.yml`, (4) Run `rasa train` to verify. |
| **Lab 5.1** | Add Part 2: “Project readiness” checklist + one `rasa train` run (and fix any “not in domain” error). |
| **Unit 6 (content)** | Add one short page before Lab 6.1: “What training needs” / “Before you run Lab 6.1” (domain–flow match, where to fix errors). |
| **Optional** | New Lab 5.2 “Ready for training” if you prefer a separate, assessable step instead of extending 5.1. |

Result: students are walked through the file setup in Lab 3.4, have a coding/verification step in Lab 5.1 (or 5.2), and see a clear explanation before Lab 6.1, so the path from Lab 4.2 to Lab 6.1 is bridged with content and at least one concrete coding/assessment task.
