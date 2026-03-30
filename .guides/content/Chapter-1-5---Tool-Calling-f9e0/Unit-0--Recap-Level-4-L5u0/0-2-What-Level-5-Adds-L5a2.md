**Work in `level5/`:** Every lab path in this chapter sits under **`level5/`** in the repo.

Chapter 1.5 extends the **Chapter 1.4 completion** agent from the **previous page**.

**Tool calling** is the new layer: the LLM can choose and run **tools**—Python functions you register—based on context, instead of only following **action** steps named in your flows.

**How to read this page**

- You start from **Chapter 1.4 completion** in **`level5/`** with **no** **`prompt_template`**, **no** **`data/prompts/`** install yet (the template to copy sits in **`resources/`**), **no** **`tools/`** module, **no** **`tools:`** in **`endpoints.yml`**, **no** **`transfer_money_tools`** flow file, and **no** **`action_process_transfer_with_tools`**. The labs walk you from that baseline to the finished Chapter 1.5 layout (summarized again in Unit 6).

Existing flows and responses stay; you **add** the command-generator prompt, the **tools** package, **`endpoints`** registration, the new flow and action, and domain slot conditions so the model can call **`check_balance`**, **`process_transfer`**, **`get_account_info`**, and the other tools as the labs specify.

**Implementation order** (each lab page has the full steps):

1. **Lab 2.0** — copy from **`resources/`** into **`data/prompts/`**, then **`prompt_template`** in **`config.yml`**
2. **Lab 2.1** — fill-in-the-blanks, then **`tools/banking_tools.py`**
3. **Lab 3.1** — register **`tools:`** in **`endpoints.yml`**
4. **Lab 4.1** — fill-in-the-blanks for **domain slot conditions**; add **`action_process_transfer_with_tools`** to **`actions:`**; then **flow YAML**, then **custom action** Python
5. **Lab 5.1** — train from **`level5/`**
6. **Lab 5.2** — completion check; optional **Rasa Inspector**

---

## What you'll add (by lab)

**Lab 2.0 — Command-generator prompt.** Copy **`command_prompt_v3_slot_names.jinja2`** from **`level5/resources/`** to **`level5/data/prompts/`**, then set **`prompt_template`** on **`SearchReadyLLMCommandGenerator`** in **`config.yml`**. That keeps **`set slot`** aligned with **domain slot names**.

**Lab 2.1 — Tools folder.** You create **`tools/`** and **`tools/banking_tools.py`** with at least three tool functions—**`check_balance(account)`**, **`process_transfer(amount, from_account, to_account)`**, and **`get_account_info(account)`**. Each returns a dict; you export them via **`__all__`**.

**Lab 3.1 — Register tools.** You add a **`tools:`** section to **`endpoints.yml`** with **`tools_module: "tools"`** so Rasa can load the module and expose those functions to the LLM.

**Lab 4.1 — Flow, action, and domain slots.** You complete the **fill-in-the-blanks** exercise for **`from_llm`** conditions (**`active_flow: transfer_money_tools`** on **amount**, **recipient**, **account_from**), create **`data/basics/transfer_money_tools.yml`**, create **`actions/action_process_transfer_with_tools.py`**, and register the action in the domain. In that flow step, the LLM can call the tools you defined, according to what the user said.

**Lab 5.1 — Training.** You train the Chapter 1.5 agent from **`level5/`** so the model includes domain, flows, tools registration, prompt, and the new action.

**Lab 5.2 — Testing.** You run the **completion check** and, in **Rasa Inspector**, exercise tool-calling behavior end-to-end.

**What stays the same.** Chapter 1.4 responses, flows, and actions remain in **`level5/`**; you **add** the layers above, including the **`transfer_money_tools`** path.
