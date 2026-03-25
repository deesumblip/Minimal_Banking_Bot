# Chapter 1.3 completion → Chapter 1.4 completion (reference)

Chapter 1.4 **starts** from **Chapter 1.3 completion** (your finished agent in **`level3/`**). Labs **add** transfer domain fields, **`action_process_transfer.py`**, **`transfer_money.yml`**, then training and testing. Unit 0 pages spell this out. **Lab 5.1** produces **`level4/models/*.tar.gz`** for **Lab 5.2**.

---

## Pipeline

| File | Chapter 1.3 (`level3/`) | Chapter 1.4 (`level4/`) |
|------|-------------------------|-------------------------|
| `config.yml` | `SearchReadyLLMCommandGenerator`; `assistant_id: level3-agent` | `CompactLLMCommandGenerator`; `flow_retrieval`; `assistant_id: level4-agent` (see **`PIPELINE_CHAPTER_1_3_AND_4.md`**) |
| `endpoints.yml` | Course Level 3 pattern (often literal mini) | Same **`nlg`** / **`model_groups`** shape; **`gpt-4o-mini`** group id → **`model: gpt-4o-2024-11-20`**, **`temperature: 0.1`** |

---

## Domain, flows, actions

| Area | After Chapter 1.3 | Added in Chapter 1.4 (labs) |
|------|-------------------|------------------------------|
| **Domain** | `account`; `utter_ask_account`; `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple` | Slots `amount`, `recipient`, `account_from`; `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`; register `action_process_transfer` |
| **Flows** | `greet`, `help`, `contact`, `goodbye`, `hours`, `holiday_hours`, `check_balance` | **`transfer_money.yml`** |
| **Actions (Python)** | `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple` | **`action_process_transfer.py`** |

---

## Lab 5.2

Graded check: domain + action + flow + **trained model** + **`config.yml`** pipeline (**Compact**). **`endpoints.yml`** is not graded; align it with **`level4/endpoints.yml`** for reliable **recipient** in Inspector (**Unit 0.2**).
