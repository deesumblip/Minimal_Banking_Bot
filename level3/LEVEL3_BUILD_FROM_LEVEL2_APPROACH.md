# Level 3: Building from Level 2 — Approach

## Goal

Students should **start from their Level 2 bot as the baseline** and build Level 3 themselves under guidance. Level 3 = Level 2 + slots, new action, and new flow; the student does the adding.

**Course design (Chapter 1.3):** The **`level3/`** folder is a **ready-to-use Chapter 1.2–equivalent starter**: same Level 1/2 responses and flows, with **`action_bank_hours.py`** and **`action_holiday_hours.py` preloaded** in `actions/` from the first page of the chapter. Students **do not** recreate the holiday action in Level 3. They add `slots:`, `utter_ask_account`, register `action_check_balance_simple`, then create that `.py` file (Lab 4.1) and `check_balance.yml` (Lab 5.1).

---

## 1. Level 3 starter = Level 2 end state (+ no Level 3 wiring yet)

Target state when a student **opens** `level3/` at the start of Chapter 1.3:

- **level3/domain/basics.yml** — Match Level 2: same responses (including `utter_goodbye`), **`actions:`** lists **`action_bank_hours`** and **`action_holiday_hours`** only. The starter should omit `slots:`, `utter_ask_account`, and `action_check_balance_simple` until Lab 3.1; after Lab 3.1 the list includes all three action names.
- **level3/data/basics/** — Same flow files as Level 2: `greet.yml`, `help.yml`, `contact.yml`, `goodbye.yml`, `hours.yml`, `holiday_hours.yml`. **Do not** ship `check_balance.yml`; the student creates it in Lab 5.1.
- **level3/actions/** — **Preload** `action_bank_hours.py`, `action_holiday_hours.py` (and `__init__.py`). The student **creates** `action_check_balance_simple.py` in Lab 4.1; they register its name in the domain in Lab 3.1.
- **level3/config.yml** — Can stay as-is (e.g. `assistant_id: level3-bot`). Student does not edit it.

Result: opening `level3/` is “your Level 2 bot” plus **preloaded** custom action implementations. All Level 3–specific domain wiring and new files are added in the labs.

---

## 2. Add an explicit “Level 3 setup” in the chapter

**Where:** Unit 0 (e.g. new 0.0 or expand 0.1/0.2).

**Message:**

- “Level 3 uses the **level3** folder. We’ve set it up as a **copy of your Level 2 bot** (same domain, flows, and actions). Your job in this chapter is to **add** three things: (1) slots and an ask response in the domain, (2) the new action and its registration, (3) the check_balance flow.”
- Optional: “If you built Level 2 in your own repo and have different content (e.g. extra responses), copy your level2 folder to level3 so level3 matches your Level 2, then follow the labs.”

This makes it explicit that Level 3 = Level 2 + guided additions.

---

## 3. Lab 3.1: Student adds slots, ask response, and registers the new action

At Lab 3.1, **`domain/basics.yml`** already lists **`action_bank_hours`** and **`action_holiday_hours`** (preloaded `.py` files).

**Lab 3.1** instructs the student to:

1. Add the **`slots:`** section (with `account`) and the **`utter_ask_account`** response.
2. **Register** the new action: add **`action_check_balance_simple`** to the **`actions:`** list **alongside** the two existing entries.
3. Note that they will **create** **`actions/action_check_balance_simple.py`** in Lab 4.1; in Lab 3.1 they only add its name to the domain.

So the student performs all "domain and wiring" changes for the new action and writes the action file in Lab 4.1; that new action file is not in the repo until they create it.

**Assessment:** Lab 3.1 grader (or rubric) should require: `slots:` with `account`, `utter_ask_account`, and the three action names **`action_bank_hours`**, **`action_holiday_hours`**, **`action_check_balance_simple`** in `actions:`.

---

## 4. Lab 5.1: Student creates the flow (unchanged)

No change to the lab idea: student **creates** `data/basics/check_balance.yml` with the `check_balance` flow (`collect: account`, then `action_check_balance_simple`). They are building the only new flow.

---

## 5. Unit 0 and 0.2 wording

- **0.1** — Recap Level 2; state that **`level3/`** ships as a Chapter 1.2–equivalent starter with **`action_bank_hours.py`** and **`action_holiday_hours.py` preloaded**; students do not rebuild the holiday action in Chapter 1.3.
- **0.2** — Under “What’s new in Level 3,” state clearly:
  - “You’ll **add** in Lab 3.1: `slots:` and `utter_ask_account`, and you’ll **register** `action_check_balance_simple` alongside `action_bank_hours` and `action_holiday_hours` (you create the `.py` file in Lab 4.1).”
  - “You’ll **create** in Lab 4.1: `action_check_balance_simple.py`. You’ll **create** in Lab 5.1: `data/basics/check_balance.yml`.”
  - “Preloaded Level 2 actions and flows stay as-is; you add slots, the new action, and the check_balance flow.”

---

## 6. Summary of student actions

| What | Who | Where |
|------|-----|--------|
| Level 3 starter = copy of Level 2 | Provided (repo) | level3/ |
| Add `slots:`, `utter_ask_account`, register `action_check_balance_simple` | **Student** | Lab 3.1 |
| Create `action_check_balance_simple.py` | **Student** | Lab 4.1 |
| Create `check_balance.yml` | **Student** | Lab 5.1 |

No other project files are changed for them; they only add what the labs specify.

---

## 7. Repo / file changes checklist

- [ ] **level3/domain/basics.yml** — Replace with Level 2 domain (include `utter_goodbye`, `action_bank_hours`, `action_holiday_hours`). Remove any pre-added `slots:`, `utter_ask_account`, and `action_check_balance_simple` from `actions:`.
- [ ] **level3/data/basics/** — Ensure same flows as Level 2 (include `holiday_hours.yml`). Remove `check_balance.yml` from repo (student creates it in Lab 5.1).
- [ ] **level3/actions/** — Ensure `action_bank_hours.py` and `action_holiday_hours.py` exist (copy from Level 2 if needed). **Do not** ship `action_check_balance_simple.py`; the student creates it in Lab 4.1.
- [ ] **Unit 0** — Add or expand “Level 3 setup” so it’s explicit: Level 3 = Level 2 (in level3/) + what you add in Labs 3.1, 4.1, and 5.1.
- [ ] **Lab 3.1** — Add step: “Add `action_check_balance_simple` to the `actions:` list in the domain. You will create the file in Lab 4.1.”
- [ ] **Lab 3.1 assessment** — Require all three action names in `actions:` plus slots + utter_ask_account.
- [ ] **0.2 “What’s new”** — Say student **adds** slots and ask response and **registers** the new action name (file created in Lab 4.1); student **creates** action file in Lab 4.1 and check_balance flow in Lab 5.1.

This gives a single, consistent story: students build out Level 3 from their Level 2 baseline under guidance.
