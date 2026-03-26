Chapter 1.4 builds on the **final agent at the end of Chapter 1.3** (see **Unit 0.1**).

Level 4 adds **multiple slots** in one flow: the agent remembers several values in a single conversation and uses them together in one action.

**How to read this page**

- Your **starting point** is always **Chapter 1.3 completion** (see **Unit 0.1** and **Chapter 1.3 end state** below). From there you **add** transfer-related domain fields, a new action, and a new flow, then align pipeline files in **`level4/`**, train, and test.
- **If you copied `level3/` → `level4/` yourself:** Work through **section 2** (pipeline), then **section 3** (lab deliverables), and use **section 4** as a final check.
- **If you are using this course repository:** **`level4/`** starts as the **Chapter 1.3 completion** snapshot (see **Unit 0.1**). You still complete every lab so *you* produce the pipeline files, domain, action, and flow. When you are done, your tree should match the **Chapter 1.4 end state** described here.

Your Level 3 behavior stays in place; you **add** the transfer flow and align **`level4/`** pipeline files so CALM can fill free-text slots reliably. The sections below are the **full checklist** from **Chapter 1.3 end** through **Chapter 1.4 end**. Step-by-step instructions live on each lab page.

**Implementation order:** pipeline (**Lab 0.1** — fill-in-the-blanks + paste **`config.yml`** / **`endpoints.yml`**), then domain (Lab 2.1), then action (Lab 3.1), then flow (Lab 4.1), then train and test (Labs 5.1 and 5.2). The table in **section 3** spells out files and changes. **Hands-on pipeline:** see **Lab 0.1** in Unit 0 (same pattern as Lab 3.1: blanks → paste → code test).

---

## Chapter 1.3 end state (what you bring forward)

At Chapter 1.3 completion you typically have:

- **`domain/basics.yml`:** an `account` slot, `utter_ask_account`, responses for greet, help, contact, and goodbye, and **`action_bank_hours`**, **`action_holiday_hours`**, and **`action_check_balance_simple`** under **`actions:`**
- **`data/basics/`:** flow files **`greet`**, **`help`**, **`contact`**, **`goodbye`**, **`hours`**, **`holiday_hours`**, **`check_balance`**
- **`actions/`:** **`action_bank_hours.py`**, **`action_holiday_hours.py`**, **`action_check_balance_simple.py`**
- **`config.yml`:** **`SearchReadyLLMCommandGenerator`** and **`FlowPolicy`** (Chapter 1.3 pattern)
- **`endpoints.yml`:** NLG rephrase and **`model_groups`** (your API keys in **`.env`**)

You do **not** delete that work. Chapter 1.4 **adds** the **transfer** pieces and adjusts **pipeline** files in **`level4/`**.

---

## 1. Use the `level4/` folder

- Do all Chapter 1.4 work under **`level4/`** (a copy of your Chapter 1.3–complete tree). Keep **`level3/`** as your Chapter 1.3 reference.
- If you copy **`level3/` → `level4/`** yourself, preserve **all** Chapter 1.3 files, then apply the **pipeline** and **lab** sections below.

---

## 2. Pipeline files (required for reliable CALM)

These differ from Chapter 1.3 **on purpose**. Skipping them often causes **“unable to understand you”** on **recipient** / **account_from** even when domain and flows are correct.

**Do the work yourself:** Finish **Lab 0.1** (Unit 0) **before Lab 2.1**. Fill in the blanks, paste into **`level4/config.yml`** and **`level4/endpoints.yml`**, then pass the **Code Test**. Skipping the exercise and only diffing against the repo shortchanges the learning; treat the repo as a reference for correct YAML, not a substitute for doing the work yourself.

### `config.yml` (in `level4/`)

| Setting | Chapter 1.3 (`level3/`) | Chapter 1.4 (`level4/`) |
|--------|-------------------------|-------------------------|
| **`assistant_id`** | e.g. `level3-agent` | e.g. **`level4-agent`** (distinct assistant) |
| **Command generator** | **`SearchReadyLLMCommandGenerator`** | **`CompactLLMCommandGenerator`** |
| **`minimize_num_calls`** | *(default / omitted)* | **`false`** (as in course repo) |
| **`flow_retrieval`** | *(often omitted)* | **`turns_to_embed: 5`**, **`num_flows: 20`** (keeps short turns in context) |

**What to do:** Align your copied **`level4/`** with the **`level4/config.yml`** in this repo, or edit your config to match the table. Further rationale for pipeline behavior is in **section 2** above on this page.

**After any `config.yml` change:** `python -m rasa train` from **`level4/`**.

### `endpoints.yml` (in `level4/`)

- Keep the same **structure** as Level 3 (**`action_endpoint`**, **`nlg`** with **`type: rephrase`**, **`model_groups`**). Your **`.env`** still supplies API keys.

- **`config.yml`** uses **`model_group: gpt-4o-mini`** for the LLM components. That value is the **`id`** under **`model_groups`**—it is a **label**, not a requirement to call OpenAI’s **`gpt-4o-mini`** model literally.

- **What you should set (course pattern):** Under **`model_groups`**, the entry with **`id: gpt-4o-mini`** must use **`model: gpt-4o-2024-11-20`** and **`temperature: 0.1`**. **`nlg.llm.model_group`** stays **`gpt-4o-mini`** so it picks up that same group. Example (matches **`level4/endpoints.yml`** in this repo):

```yaml
nlg:
  type: rephrase
  llm:
    model_group: gpt-4o-mini

model_groups:
  - id: gpt-4o-mini
    models:
      - provider: openai
        model: gpt-4o-2024-11-20
        temperature: 0.1
```

- **What to avoid:** Using **`model: gpt-4o-mini-2024-07-18`** (or similar) together with a **higher** **`temperature`** (e.g. **0.3**) under that group. That combination often **mis-fills** free-text **recipient** or produces flaky **FillSlot** commands—even when **`config.yml`** is already **`CompactLLMCommandGenerator`**.

- **What to do:** Copy or diff against **`level4/endpoints.yml`** in this repository. After any change, run **`python -m rasa train`** from **`level4/`** before re-testing in Inspector.

---

## 3. Lab deliverables (guided steps)

| Step | What you change | Where |
|------|-----------------|-------|
| **Lab 0.1** | **`config.yml`**: **`CompactLLMCommandGenerator`**, **`flow_retrieval`**, **`assistant_id`**; **`endpoints.yml`**: **`model_groups`** / **`temperature`** (fill-in-the-blanks → paste → code test) | `level4/config.yml`, `level4/endpoints.yml` |
| **Lab 2.1** | Add slots **`amount`**, **`recipient`**, **`account_from`**; add **`utter_ask_amount`**, **`utter_ask_recipient`**, **`utter_ask_account_from`** with **`metadata: rephrase: False`**; register **`action_process_transfer`** in **`actions:`** | `level4/domain/basics.yml` |
| **Lab 3.1** | Create **`action_process_transfer.py`** (read three slots, cap **recipient** at **100** characters, placeholders, demo confirmation) | `level4/actions/action_process_transfer.py` |
| **Lab 4.1** | Create **`transfer_money.yml`** with **`collect:`** steps for amount, then recipient, then account_from (with **`description:`** text for CALM), then **`action: action_process_transfer`** | `level4/data/basics/transfer_money.yml` |
| **Lab 5.1** | Train so you get **`level4/models/*.tar.gz`** | Terminal |
| **Lab 5.2** | Completion check + Inspector (**scripted transfer** on the Lab 5.2 page) | **Check It!** + Rasa Inspect |

**Unchanged in spirit.** All Chapter 1.3 responses, flows, and actions remain in **`level4/`**; you **add** the transfer domain pieces, action, and flow.

---

## 4. Summary: Chapter 1.3 end → Chapter 1.4 end

| Area | Chapter 1.3 end | Chapter 1.4 end adds / changes |
|------|-----------------|--------------------------------|
| **Config** | SearchReady | **CompactLLM** + **flow_retrieval** + **`assistant_id`** for level4 |
| **Endpoints** | NLG + **`model_groups`** (often literal mini) | Same structure, but **`gpt-4o-mini`** group uses **`model: gpt-4o-2024-11-20`**, **`temperature: 0.1`** (see **`level4/endpoints.yml`**) |
| **Domain** | account + asks + bank / holiday / check_balance actions | **+** three transfer slots, three **`utter_ask_*`**, **`action_process_transfer`** |
| **Actions (Python)** | bank + holiday + check_balance | **+** **`action_process_transfer.py`** |
| **Flows** | no transfer | **+** **`transfer_money.yml`** |
| **Train** | level3 model | **Retrain** from **`level4/`** after domain/data/config changes |

**Done when:** **Lab 0.1** (pipeline YAML) and Labs 2.1–5.2 pass, **`level4/config.yml`** matches the **Compact** pipeline pattern, **`level4/endpoints.yml`** matches the course **`model_groups`** / **`temperature`** ( **`gpt-4o`** model under the **`gpt-4o-mini`** group id—see section 2), and the **scripted transfer** in Lab 5.2 reaches a **`(Demo) Transfer of $…`** confirmation.
