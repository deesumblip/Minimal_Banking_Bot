**Starting point:** Work in **`level5/`** with **Labs 2.0–5.1** complete (**`prompt_template`** + **`data/prompts/`**, **`tools/`**, **`endpoints.yml`**, flow + action, **trained model**).

**Objective.** Run the **completion check** to verify **`level5/`** has **tools/**, **`banking_tools.py`**, **`tools:`** in **`endpoints.yml`**, **`transfer_money_tools.yml`**, **`action_process_transfer_with_tools`** (file + domain), and a model under **`level5/models/`** (or readiness to train).

## Step-by-Step Instructions

**Step 1.** Ensure **Labs 2.0–5.1** are done: **`prompt_template`** + **`data/prompts/`**, **`tools/`**, **`endpoints.yml`** **`tools:`**, flow and action, **training**.

**Step 2.** Optionally run the assistant: **`python -m rasa run actions`** in one terminal and **`python -m rasa run`** or **`python -m rasa inspect`** in another (from **`level5/`** with venv active). Open **Inspector** and trigger **`transfer_money_tools`**; confirm slots collect and tools behave as expected.

**Step 3.** **In Codio**, use **Check It!**.

{Check It!|assessment}(code-output-compare-501050002)

The grader checks **`level5/tools/`**, **`level5/tools/banking_tools.py`** with **`__all__`**, **`level5/endpoints.yml`** with a **`tools:`** section, **Lab 2.0** (**`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`**), **`level5/data/basics/transfer_money_tools.yml`**, **`level5/actions/action_process_transfer_with_tools.py`**, **`level5/domain/basics.yml`** listing **`action_process_transfer_with_tools`**, and **`level5/models/`** (partial score if the domain is correct but you have not trained yet). **Lab 4.1** (code test) additionally verifies **`from_llm`** slot conditions for **`transfer_money_tools`** and a complete **`run()`** on **`action_process_transfer_with_tools`**; keep those in sync with **Lab 5.2**.
