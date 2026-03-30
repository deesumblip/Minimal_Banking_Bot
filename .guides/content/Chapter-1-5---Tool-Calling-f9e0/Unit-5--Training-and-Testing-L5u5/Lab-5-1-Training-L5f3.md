**Starting point:** Work in **`level5/`** with **Labs 2.0–4.1** complete.

**Objective.** Train from **`level5/`** so the model bundles your domain, flows, tool registration, and **`action_process_transfer_with_tools`**.

## Step-by-Step Instructions

**Step 1.** From **project root**, activate the virtual environment (`source .venv/bin/activate` on Linux/macOS or `.\.venv\Scripts\Activate.ps1` on Windows).

**Step 2.** Change to the **`level5`** folder: **`cd level5`**.

**Step 3.** Run: **`python -m rasa train`**.

**Step 4.** Confirm that training completes without errors and that a model is written to `level5/models/` (or the configured output path).

**Step 5.** **In Codio**, run **Check It!** below. The grader checks the venv, **`level5/`** layout (including **`tools/banking_tools.py`**), **Lab 2.0** (**`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`**), and a **`.tar.gz`** under **`level5/models/`**.

{Check It!|assessment}(code-output-compare-501050001)
