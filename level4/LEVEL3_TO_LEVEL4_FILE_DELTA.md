# Level 3 completion → Level 4 completion (reference)

Level 4 **starts** from **Level 3 completion**. The **`level3/`** folder is that reference agent; **`level4/`** in this repository begins at the **same** baseline (students do not assemble it by copying **`level3/`** into **`level4/`**). Labs **add** transfer domain fields, **`action_process_transfer.py`**, **`transfer_money.yml`**, then training and testing. Unit 0 pages spell this out. **Lab 5.1** produces **`level4/models/*.tar.gz`** for **Lab 5.2**.

---

## Pipeline

| File | Level 3 (`level3/`) | Level 4 (`level4/`) |
|------|-------------------------|-------------------------|
| `config.yml` | `SearchReadyLLMCommandGenerator`; `assistant_id: level3-agent` | `CompactLLMCommandGenerator`; `flow_retrieval`; `assistant_id: level4-agent` (see **Unit 0.2** section 2 in the Level 4 guide) |
| `endpoints.yml` | Course Level 3 pattern (same **`openai-gpt-5-1`** group id) | Same **`nlg`** / **`model_groups`** shape; **`openai-gpt-5-1`** group id → **`model: openai-gpt-5-1`**, **`temperature: 0.1`** |

---

## Domain, flows, actions

| Area | After Level 3 | Added in Level 4 (labs) |
|------|-------------------|------------------------------|
| **Domain** | `account`; `utter_ask_account`; `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple` | Slots `amount`, `recipient`, `account_from`; `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`; register `action_process_transfer` |
| **Flows** | `greet`, `help`, `contact`, `goodbye`, `hours`, `holiday_hours`, `check_balance` | **`transfer_money.yml`** |
| **Actions (Python)** | `action_bank_hours`, `action_holiday_hours`, `action_check_balance_simple` | **`action_process_transfer.py`** |

---

## Lab 5.2

Graded check: domain + action + flow + **trained model** + **`config.yml`** pipeline (**Compact**). **`endpoints.yml`** is not graded; align it with **`level4/endpoints.yml`** for reliable **recipient** in Inspector (**Unit 0.2**).
