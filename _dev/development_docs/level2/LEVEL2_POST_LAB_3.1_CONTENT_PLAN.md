# Level 2: Content Modifications After Lab 3.1

**Goal:** After Lab 3.1, students have created **action_holiday_hours**. The rest of Level 2 should require them to **register** that action and **create a flow** for it, so the narrative is "you built it → you wire it in → you train and test it."

**Status:** Implemented (see below for what was changed).

---

## 1. Unit 4 (Registering Actions) + Lab 4.1

**Content changes:**
- **4.1 / 4.2 / 4.3:** Keep the explanation and step-by-step for the `actions:` section. Add one clear line: *"Register both the example action (`action_bank_hours`) and the action you created in Lab 3.1 (`action_holiday_hours`)."*
- **4.4 Multiple Actions:** Use as the main example: list both `action_bank_hours` and `action_holiday_hours` so students see "multiple actions" in practice.

**Lab 4.1 grader:**
- Keep existing checks for `actions:` section and `action_bank_hours` (so the example stays wired).
- **Add** a check that `action_holiday_hours` is registered under `actions:` (e.g. 2 points). Adjust max_score (e.g. 10 → 12) or reallocate so both registrations are required to pass.

**Student-facing Lab 4.1 (Guide Content):**
- *"Add an `actions:` section to `domain/basics.yml` and register both `action_bank_hours` and the action you created in Lab 3.1 (`action_holiday_hours`)."*

---

## 2. Unit 5 (Using Actions in Flows) + Lab 5.1

**Content changes:**
- **5.1:** Keep the comparison of responses vs actions; keep `hours` / `action_bank_hours` as the example.
- **Lab 5.1:** Create both flows — (a) *"The example: hours.yml"* (uses `action_bank_hours`) and (b) *"Your flow: holiday_hours.yml"* (`action_holiday_hours`), with clear descriptions so the LLM can match user questions. Full steps in the lab.
- **5.1:** Mixing responses and actions (same page as actions vs responses); use `action_bank_hours` and `utter_contact` as the example.

**Lab 5.1 grader:**
- Keep checks for `hours.yml` and `action_bank_hours` (so the example flow stays).
- **Add** checks for `holiday_hours.yml`: file exists, has `flows:`, has a flow (e.g. `holiday_hours:`), has `name`, `description`, `steps:`, and uses `action_holiday_hours`. Allocate points (e.g. 4–5 for holiday_hours, rest for hours). Max_score can go from 10 to 14–16, or keep 10 and reallocate.

**Student-facing Lab 5.1 (Guide Content):**
- *"Create the flow `hours.yml` for `action_bank_hours`, and create `holiday_hours.yml` that uses your `action_holiday_hours`."*

---

## 3. Unit 6 (Training and Testing)

**Content changes:**
- **6.1:** No structural change; training still loads all actions and flows.
- **Lab 6.2 testing:** Add a bullet: *"Test both flows: ask about regular hours and about holiday hours; confirm both your action and the example action run."*
- **6.2 / Lab 6.2:** Error content in 6.2; testing + debugging in **Lab 6.2**.

No grader change for Lab 6.1 (still "model exists, training succeeded"); the lab just benefits from students having both actions and flows.

---

## 4. Unit 6 — page 6.4 (Level 2 wrap-up; former Unit 7)

**Content changes:**
- **6.4 (single page):** Walkthrough includes holiday hours → `holiday_hours` → `action_holiday_hours` plus greet, hours, contact. Same page summarizes domain/flows/actions (both `hours` / `holiday_hours` and example vs student action), future levels, and best practices (former 7.2 / 7.3-style material merged here).

---

## 5. Unit 6 wrap-up (former Unit 8 merged into 6.4)

**Content changes:**
- End of **6.4** should include recap, limitations, Level 3 preview, and readiness items that reference **`action_holiday_hours`** and **`holiday_hours`** alongside the example action and **`hours`** flow.

---

## 6. README (level2/README.md)

**Changes:**
- **"What this level adds":** Clarify: *"An example action file (`action_bank_hours.py`) so you can see how actions work. In Lab 3.1 you create your own action (`action_holiday_hours`); in Labs 4.1 and 5.1 you register both actions and add `hours.yml` and `holiday_hours.yml`."*
- **Exercises:** Align with the new path: (1) Modify `action_holiday_hours` message, (2) Add another action of your choice and register it, (3) Add a flow for that action.

---

## 7. Level 2 Starter / Repo (optional)

- **Starter (Codio):** Ship **`action_bank_hours.py`** and Level 1 responses/flows; **do not** ship `action_holiday_hours.py`, **`actions:`** in the domain, **`hours.yml`**, or **`holiday_hours.yml`** — students add those in Labs 3.1, 4.1, and 5.1. See **`LEVEL2_STARTER_STATE.md`**.
- **domain/basics.yml:** Starter has **no** `actions:` section; students add the section and **both** action names in Lab 4.1.

---

## 8. Summary Table

| Item | Change |
|------|--------|
| **Unit 4 content** | Say "register both action_bank_hours and action_holiday_hours"; 4.4 show both in list. |
| **Lab 4.1** | Grader: require `action_holiday_hours` in domain; student instructions: register both actions. |
| **Unit 5 content** | Lab 5.1: add "Your flow: holiday_hours.yml" using action_holiday_hours. |
| **Lab 5.1** | Grader: require holiday_hours.yml + structure + action_holiday_hours; student instructions: create hours.yml (if needed) and holiday_hours.yml. |
| **Unit 6** | Lab 6.2: add "test both regular and holiday hours." |
| **Unit 6 (6.4)** | Single page: walkthrough, both actions/flows, practices, MC check, recap, limitations, L3 preview, readiness (former Unit 7 and Unit 8 merged). |
| **README** | Clarify example vs. your action; align exercises. |

---

## 9. Domain and flow for `action_holiday_hours` (reference)

**domain/basics.yml** (excerpt):
```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
```

**data/basics/holiday_hours.yml** (example):
```yaml
flows:
  holiday_hours:
    name: holiday hours
    description: Tell the user when the bank is closed or has limited hours for holidays.
    steps:
      - action: action_holiday_hours
```

Students can choose different description text; the grader should check for the flow name and the action reference, not the exact wording of `description`.
