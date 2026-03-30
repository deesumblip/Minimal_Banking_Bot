**Starting point:** Work in **`level5/`** with the Chapter 1.4 completion baseline plus the additions you made in this chapter’s labs. The summary below lists what you **added** on top of that baseline.

## Chapter 1.5 summary

In this chapter you:

1. **Command-generator prompt (Lab 2.0).** Added **`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`** so the LLM uses domain slot names in **`set slot`** commands.

2. **Tools folder (Lab 2.1).** Created **`tools/`** and **`tools/banking_tools.py`** with tool functions (for example **`check_balance`**, **`process_transfer`**, **`get_account_info`**) and exported them via **`__all__`**.

3. **Register tools (Lab 3.1).** Added a **`tools:`** section to **`endpoints.yml`** with **`tools_module: "tools"`** so Rasa discovers the tools.

4. **Flow and action (Lab 4.1).** Completed the **fill-in-the-blanks** exercise for **`from_llm`** slot conditions (**`active_flow: transfer_money_tools`** on **amount**, **recipient**, **account_from**), created **`transfer_money_tools.yml`**, created **`action_process_transfer_with_tools.py`** (with **`run()`**, slot reads, and **`utter_message`**), and registered the action in the domain.

5. **Training and testing (Labs 5.1 and 5.2).** Trained from **`level5/`**, ran the **completion check**, and tested tool calling in **Rasa Inspector**.

## Key ideas

- **Tools** are functions the LLM selects and calls at runtime; **actions** are steps explicitly named in flows.
- Tools are defined in a Python module (for example **`tools/banking_tools.py`**) and registered in **`endpoints.yml`**.
- A flow can run one **action** in a context where the LLM calls **tools**; the flow does not list each tool—the LLM decides.

Your Chapter 1.5 agent is one assistant that still supports all earlier flows and adds **`transfer_money_tools`** with dynamic tool use.
