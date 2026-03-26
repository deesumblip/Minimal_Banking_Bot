# Level 4: Building from Level 3 — Setup Walkthrough

How **Chapter 1.4** relates to **Chapter 1.3** when you set up or teach the course.

---

## Goal

Students **start from Chapter 1.3 completion**—the same agent they finished in **`level3/`**—and **add** Level 4 content (transfer slots, `action_process_transfer`, `transfer_money.yml`) in guided labs, then align **`level4/`** pipeline files, train, and test.

**Chapter 1.4 instructional markdown** assumes that baseline everywhere (Unit 0, labs, guides).

---

## 1. Optional: “clean” `level4/` without transfer files

If you need a **minimal** `level4/` tree so students add every transfer file themselves:

- **`domain/basics.yml`:** `account` slot; `utter_ask_account`; responses; **`action_bank_hours`**, **`action_holiday_hours`**, **`action_check_balance_simple`** — **no** `amount` / `recipient` / `account_from`, **no** transfer `utter_ask_*`, **no** `action_process_transfer` in the list.
- **`data/basics/`:** `greet`, `help`, `contact`, `goodbye`, `hours`, `holiday_hours`, `check_balance` — **no** `transfer_money.yml`.
- **`actions/`:** `action_bank_hours.py`, `action_holiday_hours.py`, `action_check_balance_simple.py`, `__init__.py` — **no** `action_process_transfer.py`.
- Then apply **`level4/config.yml`** and **`level4/endpoints.yml`** from this repo (or the tables in Unit **0.2**) so multi-slot work behaves when students add it.

---

## 2. Pipeline files (Chapter 1.4)

See **Unit 0.2** (section 2) in the Chapter 1.4 guide. **`level4/config.yml`** uses **`CompactLLMCommandGenerator`**, **`flow_retrieval`**, etc.; **`level4/endpoints.yml`** aligns **`model_groups`** / **`temperature`** for FillSlot reliability.

---

## 3. Level 4 labs (student actions)

| What | Where (lab) |
|------|-------------|
| Add slots `amount`, `recipient`, `account_from` + `utter_ask_*` + register `action_process_transfer` | Lab 2.1 |
| Create `action_process_transfer.py` | Lab 3.1 |
| Create `transfer_money.yml` | Lab 4.1 |
| Train | Lab 5.1 |
| Completion check + Inspector | Lab 5.2 |

---

## 4. Codio and `.guides`

Sync **`level4/`** unit and lab content into **`.guides/content/Chapter-1-4-...`** so Codio matches the source-of-truth copy.

---

## 5. Summary

| Topic | Detail |
|-------|--------|
| **Student story** | Chapter 1.4 **starts** at Chapter 1.3 **completion**; labs **add** transfer + pipeline alignment + train/test. |
| **Optional minimal tree** | Strip transfer artifacts per §1 if you need a blank slate for learners. |
