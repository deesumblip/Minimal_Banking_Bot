# Level 4: Building from Level 3 — Setup Walkthrough

This document walks through how to set up **Level 4** so that the **starting bot files are the same as what the student has built at the end of Level 3**, and students add Level 4 content (multiple slots, transfer flow) in guided labs. It mirrors the approach used for Level 3.

---

## Goal

Students should **start from their Level 3 bot as the baseline** and build Level 4 themselves under guidance. Level 4 = Level 3 + more slots, more ask responses, one new action, and one new flow; the student does the adding.

---

## 1. Make the Level 4 starter = Level 3 end state

**level4/** in the repo should be a **true copy of the Level 3 end state** (what the student has after completing all Level 3 labs). Do **not** pre-add any Level 4–only content.

### 1.1 level4/domain/basics.yml

- **Include everything from Level 3:**  
  - **slots:** `account` (type: text).  
  - **responses:** utter_greet, utter_help, utter_contact, utter_goodbye, **utter_ask_account**.  
  - **actions:** `action_bank_hours`, `action_check_balance_simple`.
- **Do not** add: `amount`, `recipient`, `account_from` slots; `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`; or `action_process_transfer` in the actions list.  
- Add a short comment at the top: e.g. “Level 4 starts as your Level 3 bot. In Level 4 you will add slots and ask responses for transfer, and register/create `action_process_transfer`.”

### 1.2 level4/data/basics/

- **Same flow files as Level 3:**  
  `greet.yml`, `help.yml`, `contact.yml`, `goodbye.yml`, `hours.yml`, `check_balance.yml`.  
- **Do not** ship `transfer_money.yml`; the student creates it in a Level 4 lab (e.g. Lab 4.1 or equivalent).

### 1.3 level4/actions/

- **Same as Level 3:**  
  `action_bank_hours.py`, `action_check_balance_simple.py`, `__init__.py`.  
- **Do not** ship `action_process_transfer.py`; the student creates it in a Level 4 lab (e.g. Lab 3.1).

### 1.4 level4/config.yml (and credentials, endpoints)

- **config.yml:** Same structure as Level 3; only change `assistant_id` to something like `level4-bot` so the assistant identity is distinct.  
- **credentials.yml / endpoints.yml:** Can match Level 3 (no Level 4-specific changes required for a minimal setup).

### 1.5 level4/ — other files

- Copy over from Level 3: `credentials.yml`, `endpoints.yml`, `data/system/patterns/patterns.yml`, `load_env.ps1`, `run_inspector.ps1` if you use them.  
- **.env** is gitignored; do not commit. Students use their existing keys (same as Level 3).

**Result:** Opening **level4/** is “your Level 3 bot.” All Level 4–specific content is added by the student in the labs.

---

## 2. Add an explicit “Level 4 setup” in the chapter (Unit 0)

**Where:** Unit 0 (e.g. 0.1 “Your Level 3 bot” and 0.2 “What Level 4 adds”).

**Message:**

- “Level 4 uses the **level4** folder. We’ve set it up as a **copy of your Level 3 bot** (same domain, flows, and actions). Your job in this chapter is to **add** multiple slots and a transfer flow: (1) new slots and ask responses in the domain, (2) the new action and its registration, (3) the transfer_money flow.”
- Optional: “If you built Level 3 in your own repo and have different content, copy your level3 folder to level4 so level4 matches your Level 3, then follow the labs.”

---

## 3. Level 4 labs (student actions)

Following the Level 3 pattern, students **add** domain content and **create** new files; they do not delete or replace Level 3 content.

| What | Who | Where (lab) |
|------|-----|-------------|
| Level 4 starter = copy of Level 3 | Provided (repo) | level4/ |
| Add slots: `amount`, `recipient`, `account_from` | **Student** | Lab 2.1 (domain) |
| Add responses: `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from` | **Student** | Lab 2.1 (domain) |
| Register `action_process_transfer` in domain | **Student** | Lab 2.1 (domain) |
| Create `action_process_transfer.py` | **Student** | Lab 3.1 (actions) |
| Create `transfer_money.yml` (flow with multiple collect steps + action) | **Student** | Lab 4.1 (data/basics) |
| Train and test | **Student** | Lab 5.1 / Lab 5.2 |

- **Lab 2.1 (domain):** Add the three new slots, the three new utter_ask_* responses, and `action_process_transfer` to the `actions:` list. Note that the action **file** is created in Lab 3.1.  
- **Lab 3.1 (action):** Create `actions/action_process_transfer.py` that reads `amount`, `recipient`, and `account_from` from the tracker and sends a confirmation (and optionally validates or re-prompts).  
- **Lab 4.1 (flow):** Create `data/basics/transfer_money.yml` with a flow that has multiple `collect:` steps (e.g. amount, recipient, account_from) in order, then `action: action_process_transfer`.  
- **Lab 5.1 (or integrated into a “Training and testing” unit):** Train from level4, run Inspector, test the transfer flow.

Numbering (2.1 vs 3.1 vs 4.1) can be adjusted to match your course; the important part is the **order**: domain first, then action file, then flow, then train/test.

---

## 4. Assessments (mirror Level 3)

- **Lab 2.1:** Grader or rubric checks: domain has slots `amount`, `recipient`, `account_from`; has `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`; has `action_process_transfer` in `actions:`.  
- **Lab 3.1:** Grader checks: `action_process_transfer.py` exists; has required structure (Action subclass, `name()` returning `"action_process_transfer"`, `run()` reading the three slots).  
- **Lab 4.1:** Grader checks: `transfer_money.yml` exists; valid YAML; flow has multiple `collect:` steps and `action: action_process_transfer`.  
- **Training/test lab:** Optional completion or automated check (e.g. model exists, or transfer flow runs in Inspector).

Use **Python graders** (like Level 3) for Labs 2.1–4.1: scripts that parse YAML and check structure, with **substring match** for “PASS” in Codio if the script prints detailed output before “PASS”.

---

## 5. Codio and .guides (mirror Level 3)

- **Chapter structure:** Either a new chapter for Level 4 (e.g. “Chapter 1.4: Multiple Slots”) or a dedicated “Level 4” section in the same guide.  
- **Units:** Unit 0 (recap Level 3, what Level 4 adds), Unit 1 (multiple slots in the domain), Unit 2 (actions that use multiple slots), Unit 3 (flows with multiple collect steps), Unit 4 (creating the transfer flow), Unit 5–6 (training and testing). Adjust to your narrative.  
- **Sync:** Keep **source content** in something like `level4/Level4_Unit*_Content_*.md` and `level4/Level4_Lab*_Content.md`, and sync (or copy) into `.guides/content/...` so Codio shows the same content. Remove leading H1 from synced markdown if Codio adds its own page title (avoid double headers).  
- **Assessment setup docs:** For each graded lab, maintain a `Level4_LabX_Y_Assessment_Setup.md` with Option A (LLM rubric) and Option B (Standard Code Test + Python grader), including Codio details: COMMAND (venv Python path), Working Directory, Timeout, EXPECTED OUTPUT “PASS”, **enable substring match**, rationale text.

---

## 6. Repo / file checklist for Level 4

- [ ] **level4/domain/basics.yml** — Replace with Level 3 end state (slots: account; utter_ask_account; actions: action_bank_hours, action_check_balance_simple). Add a short “Level 4 starts from Level 3” comment. Do **not** add amount/recipient/account_from slots, transfer ask responses, or action_process_transfer.
- [ ] **level4/data/basics/** — Same as Level 3: greet, help, contact, goodbye, hours, check_balance. Remove **transfer_money.yml** from the repo (student creates it in a lab).
- [ ] **level4/actions/** — Same as Level 3: action_bank_hours.py, action_check_balance_simple.py, __init__.py. Remove **action_process_transfer.py** from the repo (student creates it in a lab).
- [ ] **level4/config.yml** — Same as Level 3 except `assistant_id: level4-bot` (or your convention).
- [ ] **Unit 0** — “Level 4 setup”: level4 folder = copy of your Level 3 bot; you will add multiple slots and the transfer flow in the labs.
- [ ] **Labs 2.1–4.1 and 5.1–5.2 (or your numbering)** — Domain lab, action lab, flow lab; each with content + assessment setup + optional Python grader in `.guides/secure/level4_graders/` (or equivalent).
- [ ] **.guides** — New chapter or section for Level 4; index.json updated if needed; unit/lab pages and assessments linked.

---

## 7. Summary

| Item | Action |
|------|--------|
| **level4 starter** | = Level 3 end state (domain with account slot + utter_ask_account + two actions; flows greet, help, contact, goodbye, hours, check_balance; actions action_bank_hours, action_check_balance_simple). No transfer slots, no transfer flow, no action_process_transfer. |
| **Students add** | In labs: (1) domain: amount, recipient, account_from slots and utter_ask_* and register action_process_transfer; (2) create action_process_transfer.py; (3) create transfer_money.yml; (4) train and test. |
| **Persistence** | One level4 folder; same venv and .env as Level 3 (no new env setup). |
| **No leaking** | Students never commit .env; keys stay in their workspace (same as Level 3). |

This gives a single, consistent story: **Level 4 = Level 3 (in level4/) + multiple slots and transfer flow**, added by the student in guided labs, with starting bot files identical to what they have at the end of Level 3.
