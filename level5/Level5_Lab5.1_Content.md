**Objective.** In this lab you will train the Level 5 agent from the `level5` folder so that the model includes your domain, flows, and tool registration.

## Step-by-Step Instructions

**Step 1.** From **project root**, activate the virtual environment (`source .venv/bin/activate` on Linux/macOS or `.\.venv\Scripts\Activate.ps1` on Windows).

**Step 2.** Change to the level5 folder: `cd level5`.

**Step 3.** Run: `rasa train`.

**Step 4.** Confirm that training completes without errors and that a model is written to `level5/models/` (or the configured output path).

**Step 5.** Run the assessment. The grader checks the venv, **`level5/`** structure, **Lab 2.0** (**`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`**), and a trained model under **`level5/models/`**.

{Check It!|assessment}(code-output-compare-501050001)
