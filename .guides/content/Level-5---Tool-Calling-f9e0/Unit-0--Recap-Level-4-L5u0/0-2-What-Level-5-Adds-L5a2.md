**Work in `level5/`:** Every lab path in this chapter sits under **`level5/`** in the repo.

Level 5 builds on the **Level 4 completion** agent (see **Unit 0.1**).

**Tool calling** is the new layer. The LLM can choose and run **tools**, which are Python functions you register. It picks tools based on context. That goes beyond only following **action** steps named in your flows.

**How to read this page**

Your **starting point** is **Level 4 completion** in **`level5/`**. Until you finish the labs, that baseline does **not** yet include:

- **`prompt_template`** in **`config.yml`** (the Jinja2 file to copy is in **`resources/`**, not yet under **`data/prompts/`**)
- A **`tools/`** module
- A **`tools:`** block in **`endpoints.yml`**
- **`transfer_money_tools`** flow YAML or **`action_process_transfer_with_tools`**

The sections below are the **checklist** from that baseline through **Level 5 end**. Step-by-step instructions live on each lab page.

**Implementation order** (each lab page has the full steps):

1. **Lab 2.0**, copy from **`resources/`** into **`data/prompts/`**, then **`prompt_template`** in **`config.yml`**
2. **Lab 2.1**, fill-in-the-blanks, then **`tools/banking_tools.py`**
3. **Lab 3.1**, register **`tools:`** in **`endpoints.yml`**
4. **Lab 4.1**, fill-in-the-blanks for **domain slot conditions**. Add **`action_process_transfer_with_tools`** to **`actions:`**. Then **flow YAML**, then **custom action** Python
5. **Lab 5.1**, train from **`level5/`**
6. **Lab 5.2**, completion check. Optional **Rasa Inspector**

---

## Lab deliverables (summary)

| Lab | What you add |
|-----|----------------|
| **2.0** | Copy **`command_prompt_v3_slot_names.jinja2`** into **`data/prompts/`**. Set **`prompt_template`** on **`SearchReadyLLMCommandGenerator`** in **`config.yml`**. That keeps **`set slot`** aligned with domain names. SearchReady vs Compact in **`level4/`** is explained in **Unit 0.1** and **`level5/config.yml`**. |
| **2.1** | **`tools/`**, **`tools/banking_tools.py`** with **`check_balance`**, **`process_transfer`**, **`get_account_info`**, **`__all__`**. |
| **3.1** | **`tools:`** / **`tools_module: "tools"`** in **`endpoints.yml`**. |
| **4.1** | **`from_llm`** conditions for **`transfer_money_tools`**. **`transfer_money_tools.yml`**. **`action_process_transfer_with_tools.py`**. Register the action under **`actions:`**. |
| **5.1** | Train. The model is written under **`level5/models/`**. |
| **5.2** | Completion check. Optionally run an Inspector smoke test. |

**Unchanged in spirit.** Level 4 responses, flows, and actions remain in **`level5/`**. You **add** the rows above, including the **`transfer_money_tools`** path.

**Done when:** Labs **2.0** through **5.2** pass, **`level5/`** matches the deliverables in the table (including a trained model from **Lab 5.1**), and you can exercise **`transfer_money_tools`** as described on **Lab 5.2** (optional).
