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
- **5.2:** Split into (a) *"The example: hours.yml"* (uses `action_bank_hours`) and (b) *"Your flow: holiday_hours.yml"* — create `data/basics/holiday_hours.yml` that uses `action_holiday_hours`, with a clear description so the LLM can match user questions about holiday hours.
- **5.3:** Optional: show mixing responses and actions; can still use `action_bank_hours` and `utter_contact` as the example.

**Lab 5.1 grader:**
- Keep checks for `hours.yml` and `action_bank_hours` (so the example flow stays).
- **Add** checks for `holiday_hours.yml`: file exists, has `flows:`, has a flow (e.g. `holiday_hours:`), has `name`, `description`, `steps:`, and uses `action_holiday_hours`. Allocate points (e.g. 4–5 for holiday_hours, rest for hours). Max_score can go from 10 to 14–16, or keep 10 and reallocate.

**Student-facing Lab 5.1 (Guide Content):**
- *"Create (or verify) the example flow `hours.yml` for `action_bank_hours`, and create a new flow `holiday_hours.yml` that uses your `action_holiday_hours`."*

---

## 3. Unit 6 (Training and Testing)

**Content changes:**
- **6.1:** No structural change; training still loads all actions and flows.
- **6.3 Testing:** Add a bullet: *"Test both flows: ask about regular hours and about holiday hours; confirm both your action and the example action run."*
- **6.2 / 6.4:** Keep error and debugging content; can add *"If your new action isn’t found, check it’s registered and the flow references it correctly."*

No grader change for Lab 6.1 (still "model exists, training succeeded"); the lab just benefits from students having both actions and flows.

---

## 4. Unit 7 (Putting It All Together)

**Content changes:**
- **7.1 Walkthrough:** Add a third turn: user asks about holiday hours → `holiday_hours` flow → `action_holiday_hours` runs. Keep the existing turns (greet, hours, contact).
- **7.2 Summary:** Under "Flows" list both `hours` and `holiday_hours`; under "Actions" list both `action_bank_hours` and `action_holiday_hours`. State that one is the example and one is the action they built.
- **7.3:** No change needed.

---

## 5. Unit 8 (Assessment and Next Steps)

**Content changes:**
- **8.2 What You've Learned:** Add a bullet: *"Can register your own action and create a flow that uses it."*
- **8.5 Course Completion Checklist:** Add:
  - *"[ ] Your action (`action_holiday_hours`) is registered in the domain"*
  - *"[ ] You have a flow (`holiday_hours.yml`) that uses your action"*

---

## 6. README (level2/README.md)

**Changes:**
- **"What this level adds":** Clarify: *"An example action and flow (`action_bank_hours`, `hours.yml`) so you can see how actions work. In Lab 3.1 you create your own action (`action_holiday_hours`); in Labs 4.1 and 5.1 you register it and add a flow for it."*
- **Exercises:** Align with the new path: (1) Modify `action_holiday_hours` message, (2) Add another action of your choice and register it, (3) Add a flow for that action.

---

## 7. Level 2 Starter / Repo (optional)

- **Starter (Codio):** Can still ship with `action_bank_hours.py` and `hours.yml` (and optionally `actions:` and `utter_goodbye` / `goodbye.yml`). Do **not** ship `action_holiday_hours.py` or `holiday_hours.yml` — students create those in Lab 3.1 and 5.1.
- **domain/basics.yml:** If the starter includes the `actions:` section, it can list only `action_bank_hours`; students add `action_holiday_hours` in Lab 4.1. If the starter has no `actions:` section, students add the section with both actions in Lab 4.1.

---

## 8. Summary Table

| Item | Change |
|------|--------|
| **Unit 4 content** | Say "register both action_bank_hours and action_holiday_hours"; 4.4 show both in list. |
| **Lab 4.1** | Grader: require `action_holiday_hours` in domain; student instructions: register both actions. |
| **Unit 5 content** | 5.2: add "Your flow: holiday_hours.yml" using action_holiday_hours. |
| **Lab 5.1** | Grader: require holiday_hours.yml + structure + action_holiday_hours; student instructions: create hours.yml (if needed) and holiday_hours.yml. |
| **Unit 6** | 6.3: add "test both regular and holiday hours." |
| **Unit 7** | 7.1: add holiday-hours turn; 7.2: list both actions and both flows. |
| **Unit 8** | 8.2 + 8.5: add bullets/checklist for "your action registered" and "your flow." |
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
