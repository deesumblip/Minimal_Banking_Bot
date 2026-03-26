**Starting point:** Work in **`level5/`** with the Chapter 1.4 completion baseline plus the additions you made in this chapter’s labs. The summary below lists what you **added** on top of that baseline.

## Chapter 1.5 summary

In this chapter you:

1. **Tools folder (Lab 2.1).** Created **`tools/`** and **`tools/banking_tools.py`** with tool functions (for example **`check_balance`**, **`process_transfer`**, **`get_account_info`**) and exported them via **`__all__`**.

2. **Register tools (Lab 3.1).** Added a **`tools:`** section to **`endpoints.yml`** with **`tools_module: "tools"`** so Rasa discovers the tools.

3. **Flow and action (Lab 4.1).** Created **`transfer_money_tools.yml`** (collect **amount**, **recipient**, **account_from**, then **`action_process_transfer_with_tools`**) and **`action_process_transfer_with_tools.py`**, and registered the action in the domain.

4. **Training and testing (Labs 5.1 and 5.2).** Trained from **`level5/`**, ran the **completion check**, and tested tool calling in **Rasa Inspector**.

## Key ideas

- **Tools** are functions the LLM selects and calls at runtime; **actions** are steps explicitly named in flows.
- Tools are defined in a Python module (for example **`tools/banking_tools.py`**) and registered in **`endpoints.yml`**.
- A flow can run one **action** in a context where the LLM calls **tools**; the flow does not list each tool—the LLM decides.

Your Chapter 1.5 agent is one assistant that still supports all earlier flows and adds **`transfer_money_tools`** with dynamic tool use.
