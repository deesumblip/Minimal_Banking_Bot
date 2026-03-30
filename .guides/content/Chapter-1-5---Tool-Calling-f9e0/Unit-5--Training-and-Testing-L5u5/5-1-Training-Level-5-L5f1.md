**Starting point:** Work in **`level5/`** with **Labs 2.0–4.1** complete (**`prompt_template`** + **`data/prompts/`**, **`tools/`**, **`endpoints.yml`** **`tools:`**, **`transfer_money_tools`**, **`action_process_transfer_with_tools`**).

After you add the **`tools/`** folder, **`tools:`** registration, and the **`transfer_money_tools`** flow and action, you need to **train** the Chapter 1.5 agent.

## Steps

1. From **project root**, activate the virtual environment (`source .venv/bin/activate` on Linux/macOS or `.\.venv\Scripts\Activate.ps1` on Windows).
2. Change to the **`level5`** folder: **`cd level5`**.
3. Run: **`python -m rasa train`** (use the venv’s Python from the project root so you use the same Rasa install as in earlier chapters).
4. The model is written under **`level5/models/`**. The trained assistant includes your domain, flows, and tool registration so the LLM can use tools when the flow runs **`action_process_transfer_with_tools`**.

If training fails, check: (1) **`domain/basics.yml`** lists **`action_process_transfer_with_tools`** under **`actions:`** and **`amount`**, **`recipient`**, and **`account_from`** each include **`active_flow: transfer_money_tools`** under **`from_llm`** (as in **Lab 4.1**); (2) **`endpoints.yml`** has **`tools:`** with **`tools_module: "tools"`**; (3) **`tools/banking_tools.py`** exists with valid Python and **`__all__`** defined; (4) **`config.yml`** still sets **`prompt_template`** to **`data/prompts/command_prompt_v3_slot_names.jinja2`** and that file exists (**Lab 2.0**—do not remove or rename it accidentally).
