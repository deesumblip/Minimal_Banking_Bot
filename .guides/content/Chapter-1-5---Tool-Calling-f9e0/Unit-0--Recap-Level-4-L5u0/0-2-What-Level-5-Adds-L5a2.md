**Work in `level5/`:** Every lab path in this chapter sits under **`level5/`** in the repo.

Chapter 1.5 builds on the **Chapter 1.4 completion** agent (see **Unit 0.1**).

**Tool calling** is the new layer: the LLM can choose and run **tools**—Python functions you register—based on context, instead of only following **action** steps named in your flows.

**How to read this page**

Your **starting point** is **Chapter 1.4 completion** in **`level5/`**. Until you finish the labs, that baseline does **not** yet include:

- **`prompt_template`** in **`config.yml`** (the Jinja2 file to copy is in **`resources/`**, not yet under **`data/prompts/`**)
- A **`tools/`** module
- A **`tools:`** block in **`endpoints.yml`**
- **`transfer_money_tools`** flow YAML or **`action_process_transfer_with_tools`**

The sections below are the **checklist** from that baseline through **Chapter 1.5 end**. Step-by-step instructions live on each lab page.

**Implementation order** (each lab page has the full steps):

1. **Lab 2.0** — copy from **`resources/`** into **`data/prompts/`**, then **`prompt_template`** in **`config.yml`**
2. **Lab 2.1** — fill-in-the-blanks, then **`tools/banking_tools.py`**
3. **Lab 3.1** — register **`tools:`** in **`endpoints.yml`**
4. **Lab 4.1** — fill-in-the-blanks for **domain slot conditions**; add **`action_process_transfer_with_tools`** to **`actions:`**; then **flow YAML**, then **custom action** Python
5. **Lab 5.1** — train from **`level5/`**
6. **Lab 5.2** — completion check; optional **Rasa Inspector**

---

## Lab deliverables (summary)

| Lab | What you add |
|-----|----------------|
| **2.0** | **`command_prompt_v3_slot_names.jinja2`** in **`data/prompts/`**; **`prompt_template`** on **`SearchReadyLLMCommandGenerator`** in **`config.yml`** (keeps **`set slot`** aligned with domain names). SearchReady vs Compact in **`level4/`** is explained in **Unit 0.1** and **`level5/config.yml`**. |
| **2.1** | **`tools/`**, **`tools/banking_tools.py`** with **`check_balance`**, **`process_transfer`**, **`get_account_info`**, **`__all__`**. |
| **3.1** | **`tools:`** / **`tools_module: "tools"`** in **`endpoints.yml`**. |
| **4.1** | **`from_llm`** conditions for **`transfer_money_tools`**; **`transfer_money_tools.yml`**; **`action_process_transfer_with_tools.py`**; action under **`actions:`**. |
| **5.1** | Train; model under **`level5/models/`**. |
| **5.2** | Completion check; optional Inspector smoke test. |

**Unchanged in spirit.** Chapter 1.4 responses, flows, and actions remain in **`level5/`**; you **add** the rows above, including the **`transfer_money_tools`** path.

**Done when:** Labs **2.0** through **5.2** pass, **`level5/`** matches the deliverables in the table (including a trained model from **Lab 5.1**), and you can exercise **`transfer_money_tools`** as described on **Lab 5.2** (optional).
