**Starting point:** Work in **`level5/`** with **Labs 2.0–5.1** complete (**`prompt_template`** + **`data/prompts/`**, **`tools/`**, **`endpoints.yml`**, flow + action, **trained model**).

**Objective.** Run the **completion check** to confirm **`level5/`** contains **tools/**, **`banking_tools.py`**, **`tools:`** in **`endpoints.yml`**, **`transfer_money_tools.yml`**, **`action_process_transfer_with_tools`** (file and domain), and a model under **`level5/models/`** (partial credit if you have not trained yet).

## Step-by-Step Instructions

**Step 1.** Ensure **Labs 2.0–5.1** are done: **`prompt_template`** + **`data/prompts/`**, **`tools/`**, **`endpoints.yml`** **`tools:`**, flow and action, **training**.

**Step 2.** Optionally run the assistant in **Inspector** (recommended) so you can sanity-check tool calling end-to-end.

- Open **two terminals** with the venv active and your working directory set to **`level5/`**.
- In **Terminal A**, start the action server:
  - `python -m rasa run actions`
- In **Terminal B**, create a logs folder (if it does not exist yet):
  - `mkdir -p logs`
- In **Terminal B**, start Inspector **with debug logging enabled**:
  - `python -m rasa inspect --debug --log-file logs/inspect.log`

Then open Inspector in your browser and run a quick tool-calling smoke test.

### Optional: Tool-calling smoke test (Inspector)

Use prompts that reliably exercise the course setup. (You can also open `logs/inspect.log` and look for tool-related lines.)

- **Balance (`check_balance`)** — Ask: *“What’s my balance for account 123?”* You should get a short demo-style balance reply (this path is stable in Inspector).
- **`transfer_money_tools` flow** — Start with: *“Transfer 25 dollars to Alex from account 111.”* The assistant may still ask you to confirm **amount**, **recipient**, and **account_from** one at a time; answer plainly (e.g. *“25 dollars”*, *“Alex”*, then your **from** account when asked). You should end with a **demo transfer processed** message. That end-to-end path is what this lab expects you to verify—not that every slot is filled from the first user turn.

**Step 3.** **In Codio**, use **Check It!**.

{Check It!|assessment}(code-output-compare-501050002)

The grader inspects **`level5/tools/`**, **`banking_tools.py`** (with **`__all__`**), **`endpoints.yml`** (**`tools:`**), **Lab 2.0** files (**`data/prompts/command_prompt_v3_slot_names.jinja2`**, **`prompt_template`** in **`config.yml`**), **`transfer_money_tools.yml`**, **`action_process_transfer_with_tools.py`**, **`domain/basics.yml`** (action listed), and **`level5/models/`** (partial if domain passes but no model). **Lab 4.1** already enforced **`from_llm`** conditions for **`transfer_money_tools`** and a real **`run()`**—keep that work aligned when you run **Lab 5.2**.
