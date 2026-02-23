# Level 3: Building from Level 2 — Approach

## Goal

Students should **start from their Level 2 bot as the baseline** and build Level 3 themselves under guidance. Level 3 = Level 2 + slots, new action, and new flow; the student does the adding.

---

## 1. Make the Level 3 starter = Level 2

**Current gap:** `level3/` is a pre-made variant (e.g. no `utter_goodbye`, no `action_holiday_hours`, `action_check_balance_simple` already in domain). So the student is not starting from “their” Level 2.

**Change:** Make the **level3/** starter a **true copy of the Level 2 end state**:

- **level3/domain/basics.yml** — Match Level 2: same responses (include `utter_goodbye`), same actions list (`action_bank_hours`, `action_holiday_hours`). **Do not** pre-add `slots:`, `utter_ask_account`, or `action_check_balance_simple`. The student adds those in the labs.
- **level3/data/basics/** — Same flow files as Level 2: `greet.yml`, `help.yml`, `contact.yml`, `hours.yml`, `holiday_hours.yml`. **Do not** ship `check_balance.yml`; the student creates it in Lab 4.1.
- **level3/actions/** — Same as Level 2: `action_bank_hours.py`, `action_holiday_hours.py` (and `__init__.py`). **Add** `action_check_balance_simple.py` as a **provided file** (student does not write it, but they **do** register it in the domain in Lab 3.1).
- **level3/config.yml** — Can stay as-is (e.g. `assistant_id: level3-bot`). Student does not edit it.

Result: opening `level3/` is “your Level 2 bot.” All Level 3-specific content is added by the student in the labs.

---

## 2. Add an explicit “Level 3 setup” in the chapter

**Where:** Unit 0 (e.g. new 0.0 or expand 0.1/0.2).

**Message:**

- “Level 3 uses the **level3** folder. We’ve set it up as a **copy of your Level 2 bot** (same domain, flows, and actions). Your job in this chapter is to **add** three things: (1) slots and an ask response in the domain, (2) the new action and its registration, (3) the check_balance flow.”
- Optional: “If you built Level 2 in your own repo and have different content (e.g. extra responses), copy your level2 folder to level3 so level3 matches your Level 2, then follow the labs.”

This makes it explicit that Level 3 = Level 2 + guided additions.

---

## 3. Lab 3.1: Student adds slots, ask response, and registers the new action

**Current:** Student adds only `slots:` and `utter_ask_account`. The domain already lists `action_check_balance_simple`.

**Change:**

- **Lab 3.1** instructs the student to:
  1. Add the **`slots:`** section (with `account`) and the **`utter_ask_account`** response (unchanged).
  2. **Register** the new action: add **`action_check_balance_simple`** to the **`actions:`** list in `domain/basics.yml`.
  3. Note that the file **`actions/action_check_balance_simple.py`** is already in the project (provided); they only need to register it in the domain.

So the student performs all “domain and wiring” changes for the new action; they don’t write the Python.

**Assessment:** Lab 3.1 grader (or rubric) should require: `slots:` with `account`, `utter_ask_account`, and `action_check_balance_simple` in `actions:`.

---

## 4. Lab 4.1: Student creates the flow (unchanged)

No change to the lab idea: student **creates** `data/basics/check_balance.yml` with the `check_balance` flow (`collect: account`, then `action_check_balance_simple`). They are building the only new flow.

---

## 5. Unit 0 and 0.2 wording

- **0.1** — Keep “what you built in Level 2.” Optionally add: “Level 3 is that same bot in the **level3** folder; you’ll add memory (slots) and a new flow.”
- **0.2** — Under “What’s new in Level 3,” state clearly:
  - “You’ll **add** in Lab 3.1: `slots:` and `utter_ask_account`, and you’ll **register** the new action `action_check_balance_simple` (the file is provided).”
  - “You’ll **create** in Lab 4.1: `data/basics/check_balance.yml`.”
  - “Everything else is your Level 2 bot.”

---

## 6. Summary of student actions

| What | Who | Where |
|------|-----|--------|
| Level 3 starter = copy of Level 2 | Provided (repo) | level3/ |
| Add `slots:`, `utter_ask_account`, register `action_check_balance_simple` | **Student** | Lab 3.1 |
| Use provided `action_check_balance_simple.py` | Provided (repo) | level3/actions/ |
| Create `check_balance.yml` | **Student** | Lab 4.1 |

No other project files are changed for them; they only add what the labs specify.

---

## 7. Repo / file changes checklist

- [ ] **level3/domain/basics.yml** — Replace with Level 2 domain (include `utter_goodbye`, `action_bank_hours`, `action_holiday_hours`). Remove any pre-added `slots:`, `utter_ask_account`, and `action_check_balance_simple` from `actions:`.
- [ ] **level3/data/basics/** — Ensure same flows as Level 2 (include `holiday_hours.yml`). Remove `check_balance.yml` from repo (student creates it in Lab 4.1).
- [ ] **level3/actions/** — Ensure `action_bank_hours.py` and `action_holiday_hours.py` exist (copy from Level 2 if needed). Keep `action_check_balance_simple.py` as provided.
- [ ] **Unit 0** — Add or expand “Level 3 setup” so it’s explicit: Level 3 = Level 2 (in level3/) + what you add in Labs 3.1 and 4.1.
- [ ] **Lab 3.1** — Add step: “Add `action_check_balance_simple` to the `actions:` list in the domain. The file is already in `level3/actions/`.”
- [ ] **Lab 3.1 assessment** — Require `action_check_balance_simple` in `actions:` (and slots + utter_ask_account).
- [ ] **0.2 “What’s new”** — Say student **adds** slots and ask response and **registers** the new action (file provided); student **creates** check_balance flow.

This gives a single, consistent story: students build out Level 3 from their Level 2 baseline under guidance.
