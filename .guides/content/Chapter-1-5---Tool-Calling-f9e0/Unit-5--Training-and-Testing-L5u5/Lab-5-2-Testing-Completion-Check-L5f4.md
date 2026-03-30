**Starting point:** Work in **`level5/`** with **Labs 2.0–5.1** complete (**`prompt_template`** + **`data/prompts/`**, **`tools/`**, **`endpoints.yml`**, flow + action, **trained model**).

**Objective.** Run the **completion check** to confirm **`level5/`** contains **tools/**, **`banking_tools.py`**, **`tools:`** in **`endpoints.yml`**, **`transfer_money_tools.yml`**, **`action_process_transfer_with_tools`** (file and domain), and a model under **`level5/models/`** (partial credit if you have not trained yet).

## Step-by-Step Instructions

**Step 1.** Ensure **Labs 2.0–5.1** are done: **`prompt_template`** + **`data/prompts/`**, **`tools/`**, **`endpoints.yml`** **`tools:`**, flow and action, **training**.

**Step 2.** Optionally run the assistant: **`python -m rasa run actions`** in one terminal and **`python -m rasa run`** or **`python -m rasa inspect`** in another (from **`level5/`** with venv active). Open **Inspector** and trigger **`transfer_money_tools`**; confirm slots collect and tools behave as expected.

**Step 3.** **In Codio**, use **Check It!**.

{Check It!|assessment}(code-output-compare-501050002)

The grader inspects **`level5/tools/`**, **`banking_tools.py`** (with **`__all__`**), **`endpoints.yml`** (**`tools:`**), **Lab 2.0** files (**`data/prompts/command_prompt_v3_slot_names.jinja2`**, **`prompt_template`** in **`config.yml`**), **`transfer_money_tools.yml`**, **`action_process_transfer_with_tools.py`**, **`domain/basics.yml`** (action listed), and **`level5/models/`** (partial if domain passes but no model). **Lab 4.1** already enforced **`from_llm`** conditions for **`transfer_money_tools`** and a real **`run()`**—keep that work aligned when you run **Lab 5.2**.
