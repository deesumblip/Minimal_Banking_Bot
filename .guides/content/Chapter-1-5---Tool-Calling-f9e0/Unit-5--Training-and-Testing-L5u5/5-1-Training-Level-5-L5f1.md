**Starting point:** Work in **`level5/`** with **Labs 2.0–4.1** complete (**`prompt_template`**, **`data/prompts/`**, **`tools/`**, **`tools:`** in **`endpoints.yml`**, **`transfer_money_tools`**, **`action_process_transfer_with_tools`**).

With tools, endpoints, flow, and action in place, **train** the Chapter 1.5 agent.

## Steps

1. From **project root**, activate the virtual environment (`source .venv/bin/activate` on Linux/macOS or `.\.venv\Scripts\Activate.ps1` on Windows).
2. Change to the **`level5`** folder: **`cd level5`**.
3. Run: **`python -m rasa train`** (use the venv’s Python from the project root so you use the same Rasa install as in earlier chapters).
4. The model is written under **`level5/models/`**. The bundle includes your domain, flows, and tool registration so the LLM can use tools when **`action_process_transfer_with_tools`** runs.

If training fails, check:

1. **`domain/basics.yml`** — lists **`action_process_transfer_with_tools`**; **`amount`**, **`recipient`**, and **`account_from`** each include **`active_flow: transfer_money_tools`** under **`from_llm`** (**Lab 4.1**).
2. **`endpoints.yml`** — has **`tools:`** with **`tools_module: "tools"`**.
3. **`tools/banking_tools.py`** — valid Python with **`__all__`**.
4. **`config.yml`** and **`data/prompts/`** — **`prompt_template`** points at **`data/prompts/command_prompt_v3_slot_names.jinja2`** and the file exists (**Lab 2.0**).
