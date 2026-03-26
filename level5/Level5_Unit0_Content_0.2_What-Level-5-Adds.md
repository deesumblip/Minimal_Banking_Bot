Chapter 1.5 builds on the **final agent at the end of Chapter 1.4** described on the **previous page**.

Level 5 adds **tool calling**: the LLM can dynamically select and invoke **tools** (Python functions you register) based on conversation context—not only the fixed **action** steps named in your flows.

**How to read this page**

- Your **starting point** is **Chapter 1.4 completion** in **`level5/`**. In this course repo, **`level5/`** is already that baseline—you **add** the **`tools/`** module, **`tools:`** in **`endpoints.yml`**, the **`transfer_money_tools`** flow, and **`action_process_transfer_with_tools`**, then train and test. Complete every lab so *you* produce those files; when you are done, your tree should match the **Chapter 1.5 end state** summarized again at the **end of this chapter**.

Your Chapter 1.4 flows and actions stay in place; you **add** tools and the new flow so the LLM can call **`check_balance`**, **`process_transfer`**, **`get_account_info`**, and similar functions where the lab expects them.

**Implementation order:** **Lab 2.1** (tools folder + **`banking_tools.py`**) → **Lab 3.1** (register **`tools:`** in **`endpoints.yml`**) → **Lab 4.1** (flow + action) → **Labs 5.1–5.2** (train, completion check, Inspector). Step-by-step instructions live on each lab page.

---

## What you'll add (by lab)

**Lab 2.1 — Tools folder.** You create **`tools/`** and **`tools/banking_tools.py`** with at least three tool functions—**`check_balance(account)`**, **`process_transfer(amount, from_account, to_account)`**, and **`get_account_info(account)`**. Each returns a dict; you export them via **`__all__`**.

**Lab 3.1 — Register tools.** You add a **`tools:`** section to **`endpoints.yml`** with **`tools_module: "tools"`** so Rasa can load the module and expose those functions to the LLM.

**Lab 4.1 — Flow and action.** You create **`data/basics/transfer_money_tools.yml`** (collect **amount**, **recipient**, **account_from**, then **`action_process_transfer_with_tools`**) and **`actions/action_process_transfer_with_tools.py`**. In that flow step, the LLM can call the tools you defined, according to what the user said.

**Lab 5.1 — Training.** You train the Chapter 1.5 agent from **`level5/`** so the model includes domain, flows, tools registration, and the new action.

**Lab 5.2 — Testing.** You run the **completion check** and, in **Rasa Inspector**, exercise tool-calling behavior end-to-end.

**Unchanged in spirit.** All Chapter 1.4 responses, flows, and actions remain in **`level5/`**; you **add** the tools layer and the **`transfer_money_tools`** path described above.
