**Starting point:** Work in **`level5/`** with the Chapter 1.4 baseline plus the labs you completed here. The list below is what you **added** on top of that baseline.

## Chapter 1.5 summary

In this chapter you:

1. **Command-generator prompt (Lab 2.0).** Added **`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`** so **`set slot`** uses domain slot names.

2. **Tools folder (Lab 2.1).** Created **`tools/`** and **`tools/banking_tools.py`** defining **`check_balance`**, **`process_transfer`**, and **`get_account_info`**, listed in **`__all__`**.

3. **Register tools (Lab 3.1).** Added **`tools:`** to **`endpoints.yml`** with **`tools_module: "tools"`** so Rasa loads the package.

4. **Flow and action (Lab 4.1).** Finished the fill-in-the-blanks for **`from_llm`** (**`active_flow: transfer_money_tools`** on **amount**, **recipient**, **account_from**), added **`transfer_money_tools.yml`**, **`action_process_transfer_with_tools.py`** (**`run()`**, slot reads, **`utter_message`**), and listed the action in the domain.

5. **Training and testing (Labs 5.1 and 5.2).** Trained from **`level5/`**, passed the **completion check**, and tried tool calling in **Rasa Inspector**.

## Key ideas

- **Tools** are functions the LLM may call at runtime; **actions** are what the flow names at each step.
- Tools live in a Python module (for example **`tools/banking_tools.py`**) and are registered in **`endpoints.yml`**.
- A flow can run one **action** while the LLM still invokes **tools**; the flow does not enumerate tools—the model chooses.

Your assistant keeps every earlier flow and adds **`transfer_money_tools`** for dynamic tool use.
