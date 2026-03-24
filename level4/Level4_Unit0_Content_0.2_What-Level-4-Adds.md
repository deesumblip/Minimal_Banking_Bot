Level 4 adds **multiple slots** in one flow: the bot will remember several values in a single conversation and use them together in one action.

**How to read this page**

- **Using the course repo’s `level4/` folder:** Skim **§1** and the **§4** summary, then follow the labs. Open **§2** (pipeline) if you change config/endpoints or hit FillSlot / “can’t understand” issues on free-text slots.
- **You copied `level3/` → `level4/` yourself:** Apply **§2** (pipeline) and **§3** (lab deliverables), then use **§4** as a final check.

Your Level 3 bot will still work. You will add the transfer flow on top—**and** align **`level4/`** pipeline files so CALM can fill free-text slots reliably. Everything below is the **full checklist** from **Chapter 1.3 end state** → **Chapter 1.4 end state** (use it when you build or verify `level4/`). Step-by-step instructions for each lab are on the lab pages.

**Implementation order:** domain (Lab 2.1) → action (Lab 3.1) → flow (Lab 4.1) → train and test (Labs 5.1 and 5.2). The table in **§3** spells out files and changes.

---

## Chapter 1.3 end state (what you bring forward)

Typically includes:

- **`domain/basics.yml`:** `account` slot; `utter_ask_account`; responses and actions for greet, help, contact, goodbye; **`action_bank_hours`**, **`action_check_balance_simple`** (and anything else you added in Chapter 1.2 / 1.3, e.g. holiday hours).
- **`data/basics/`:** Flow YAMLs such as **`greet`**, **`help`**, **`contact`**, **`goodbye`**, **`hours`**, **`check_balance`** (plus optional flows).
- **`actions/`:** e.g. **`action_bank_hours.py`**, **`action_check_balance_simple.py`** (plus optional actions).
- **`config.yml`:** **`SearchReadyLLMCommandGenerator`** + **`FlowPolicy`** (Chapter 1.3 pattern).
- **`endpoints.yml`:** NLG rephrase + **`model_groups`** (your API keys via **`.env`**).

You do **not** delete that work. Chapter 1.4 adds the **transfer** pieces and adjusts **pipeline** files in **`level4/`**.

---

## 1. Use the `level4/` folder

- Do all Chapter 1.4 work under **`level4/`** (a copy of your Level 3 tree). Keep **`level3/`** as your Chapter 1.3 reference.
- If you copy **`level3/` → `level4/`** yourself, preserve **all** Level 3 files, then apply the **pipeline** and **lab** sections below.

---

## 2. Pipeline files (required for reliable CALM)

These differ from Chapter 1.3 **on purpose**. Skipping them often causes **“unable to understand you”** on **recipient** / **account_from** even when domain and flows are correct.

### `config.yml` (in `level4/`)

| Setting | Chapter 1.3 (`level3/`) | Chapter 1.4 (`level4/`) |
|--------|-------------------------|-------------------------|
| **`assistant_id`** | e.g. `level3-bot` | e.g. **`level4-bot`** (distinct assistant) |
| **Command generator** | **`SearchReadyLLMCommandGenerator`** | **`CompactLLMCommandGenerator`** |
| **`minimize_num_calls`** | *(default / omitted)* | **`false`** (as in course repo) |
| **`flow_retrieval`** | *(often omitted)* | **`turns_to_embed: 5`**, **`num_flows: 20`** (keeps short turns in context) |

**What to do:** Start from the **`level4/config.yml`** in this repo, or edit your copied config to match the table. Details and rationale: **`level4/PIPELINE_CHAPTER_1_3_AND_4.md`**.

**After any `config.yml` change:** `python -m rasa train` from **`level4/`**.

### `endpoints.yml` (in `level4/`)

- Keep the same **structure** as Level 3 (**`action_endpoint`**, **`nlg`**, **`model_groups`**).
- For **reliable FillSlot** on free-text names, the course **`level4/endpoints.yml`** points the shared **`gpt-4o-mini`** **group id** at a **capable chat model** (e.g. **`gpt-4o-2024-11-20`**) and uses a **lower `temperature`** (e.g. **0.1**) than a minimal mini-only setup.

**What to do:** Compare your file to **`level4/endpoints.yml`** in this repo and align **`model_groups`** / **`temperature`** if your transfer flow mis-fills slots.

---

## 3. Lab deliverables (guided steps)

| Step | What you change | Where |
|------|-----------------|-------|
| **Lab 2.1** | Add slots **`amount`**, **`recipient`**, **`account_from`**; add **`utter_ask_amount`**, **`utter_ask_recipient`**, **`utter_ask_account_from`** with **`metadata: rephrase: False`**; register **`action_process_transfer`** in **`actions:`** | `level4/domain/basics.yml` |
| **Lab 3.1** | Create **`action_process_transfer.py`** (read three slots, cap **recipient** at **100** characters, placeholders, demo confirmation) | `level4/actions/action_process_transfer.py` |
| **Lab 4.1** | Create **`transfer_money.yml`** — **`collect:`** amount → recipient → account_from (with **`description:`** text for CALM), then **`action: action_process_transfer`** | `level4/data/basics/transfer_money.yml` |
| **Lab 5.1** | Train — produces **`level4/models/*.tar.gz`** | Terminal |
| **Lab 5.2** | Completion check + Inspector (**scripted transfer** on the Lab 5.2 page) | Grader + Rasa Inspect |

**Unchanged in spirit.** All your Level 3 responses, flows, and actions stay in **`level4/`**; you **add** the transfer domain pieces, action, and flow.

**Optional:** If your Chapter 1.3 bot included **extra** flows (e.g. holiday hours), keep them when you copy to **`level4/`**. The course **`level4`** snapshot may not include every optional Level 3 file.

---

## 4. Summary: Chapter 1.3 end → Chapter 1.4 end

| Area | Chapter 1.3 end | Chapter 1.4 end adds / changes |
|------|-----------------|------------------------------|
| **Config** | SearchReady | **CompactLLM** + **flow_retrieval** + **`assistant_id`** for level4 |
| **Endpoints** | Your mini/keys | Align **model_groups** / **temperature** with course **`level4/endpoints.yml`** if needed |
| **Domain** | account + check_balance pieces | **+** three transfer slots, three **`utter_ask_*`**, **`action_process_transfer`** |
| **Actions** | bank + check_balance | **+** **`action_process_transfer.py`** |
| **Flows** | no transfer | **+** **`transfer_money.yml`** |
| **Train** | level3 model | **Retrain** from **`level4/`** after domain/data/config changes |

**Done when:** Labs 2.1–5.2 pass, **`level4/config.yml`** and **`level4/endpoints.yml`** match the course pattern, and the **scripted transfer** in Lab 5.2 reaches a **`(Demo) Transfer of $…`** confirmation.
