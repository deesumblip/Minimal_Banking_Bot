**Open in \`level5/\`:** All labs and paths in this chapter are under **`level5/`** in the repository.

Chapter 1.5 builds on the **final agent at the end of Chapter 1.4** described on the **previous page**.

Level 5 adds **tool calling**: the LLM can dynamically select and invoke **tools** (Python functions you register) based on conversation context—not only the fixed **action** steps named in your flows.

**How to read this page**

- Your **starting point** is **Chapter 1.4 completion** in **`level5/`**: **no** command-generator **`prompt_template`**, **no** **`tools/`** module, **no** **`tools:`** in **`endpoints.yml`**, **no** **`transfer_money_tools`** flow file, **no** **`action_process_transfer_with_tools`**. You **build** the full delta in the labs. When you are done, your **`level5/`** tree matches the **Chapter 1.5 end state** summarized at the **end of this chapter**.

Your Chapter 1.4 flows and actions stay in place; you **add** the prompt file, **tools**, **`endpoints`** registration, the new flow and action, and domain slot conditions so the LLM can call **`check_balance`**, **`process_transfer`**, **`get_account_info`**, and similar functions where the lab expects them.

**Implementation order:** **Lab 2.0** ( **`data/prompts/`** + **`prompt_template`** in **`config.yml`** ) → **Lab 2.1** (fill-in-the-blanks + **`tools/banking_tools.py`**) → **Lab 3.1** (register **`tools:`** in **`endpoints.yml`**) → **Lab 4.1** (fill-in-the-blanks for **domain slot conditions**, add **`action_process_transfer_with_tools`** to **`actions:`**, then **flow YAML**, then **custom action** Python) → **Labs 5.1–5.2** (train, completion check, Inspector). Step-by-step instructions live on each lab page.

---

## What you'll add (by lab)

**Lab 2.0 — Command-generator prompt.** You copy **`command_prompt_v3_slot_names.jinja2`** from **`.guides/content/Chapter-1-5---Tool-Calling-f9e0/resources/`** in the repository into **`level5/data/prompts/`**, then set **`prompt_template`** on **`SearchReadyLLMCommandGenerator`** in **`config.yml`**. This keeps **`set slot`** commands aligned with **domain slot names**.

**Lab 2.1 — Tools folder.** You create **`tools/`** and **`tools/banking_tools.py`** with at least three tool functions—**`check_balance(account)`**, **`process_transfer(amount, from_account, to_account)`**, and **`get_account_info(account)`**. Each returns a dict; you export them via **`__all__`**.

**Lab 3.1 — Register tools.** You add a **`tools:`** section to **`endpoints.yml`** with **`tools_module: "tools"`** so Rasa can load the module and expose those functions to the LLM.

**Lab 4.1 — Flow, action, and domain slots.** You complete the **fill-in-the-blanks** exercise for **`from_llm`** conditions (**`active_flow: transfer_money_tools`** on **amount**, **recipient**, **account_from**), create **`data/basics/transfer_money_tools.yml`**, create **`actions/action_process_transfer_with_tools.py`**, and register the action in the domain. In that flow step, the LLM can call the tools you defined, according to what the user said.

**Lab 5.1 — Training.** You train the Chapter 1.5 agent from **`level5/`** so the model includes domain, flows, tools registration, prompt, and the new action.

**Lab 5.2 — Testing.** You run the **completion check** and, in **Rasa Inspector**, exercise tool-calling behavior end-to-end.

**Unchanged in spirit.** All Chapter 1.4 responses, flows, and actions remain in **`level5/`**; you **add** the layers above and the **`transfer_money_tools`** path described here.
