**Starting point:** Work in **`level5/`** with **Labs 2.1–4.1** complete ( **`tools/`**, **`endpoints.yml`** **`tools:`**, **`transfer_money_tools`**, **`action_process_transfer_with_tools`** ).

After you add the **`tools/`** folder, **`tools:`** registration, and the **`transfer_money_tools`** flow and action, you need to **train** the Chapter 1.5 agent.

## Steps

1. From **project root**, activate the virtual environment (`source .venv/bin/activate` on Linux/macOS or `.\.venv\Scripts\Activate.ps1` on Windows).
2. Change to the **`level5`** folder: **`cd level5`**.
3. Run: **`python -m rasa train`** (use the venv’s Python so you pick up the same Rasa install as in Chapter 1.4).
4. The model is written under **`level5/models/`**. The trained assistant includes your domain, flows, and tool registration so the LLM can use tools when the flow runs **`action_process_transfer_with_tools`**.

If training fails, check: (1) **`domain/basics.yml`** lists **`action_process_transfer_with_tools`** under **`actions:`**; (2) **`endpoints.yml`** has **`tools:`** with **`tools_module: "tools"`**; (3) **`tools/banking_tools.py`** exists with valid Python and **`__all__`** defined.
