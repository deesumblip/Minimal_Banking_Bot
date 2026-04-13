**Starting point:** Work in **`level5/`** with **Labs 2.0–5.1** complete (**`prompt_template`** + **`data/prompts/`**, **`tools/`**, **`endpoints.yml`**, flow + action, **trained model**).

**Objective.** Run the **completion check** so **`level5/`** is confirmed to contain:

- **`tools/`** and **`banking_tools.py`**
- **`tools:`** in **`endpoints.yml`**
- **`transfer_money_tools.yml`** and **`action_process_transfer_with_tools`** (file and domain listing)
- A trained model under **`level5/models/`** (partial credit if you have not trained yet)

## Step-by-Step Instructions

**Step 1.** Ensure you meet the **Objective** above (same artifacts as **Labs 2.0–5.1**).

**Step 2.** Optionally run the assistant in **Inspector** (recommended) so you can sanity-check tool calling end-to-end.

- Open **two terminals** with the venv active and your working directory set to **`level5/`**.
- In **Terminal A**, start the action server:
 - `python -m rasa run actions`
- In **Terminal B**, create a logs folder (if it does not exist yet):
 - Linux / macOS / Codio: `mkdir -p logs`
 - Windows (PowerShell): `if (-not (Test-Path logs)) { New-Item -ItemType Directory -Path logs }`
- In **Terminal B**, start Inspector **with debug logging enabled**:
 - `python -m rasa inspect --debug --log-file logs/inspect.log`

Then open Inspector in your browser and run a quick tool-calling smoke test.

### Optional: Tool-calling smoke test (Inspector)

Use prompts that reliably exercise the course setup. (You can also open `logs/inspect.log` and look for tool-related lines.)

- **Balance (`check_balance`)**, Ask: *“What’s my balance for account 123?”* You should get a short demo-style balance reply (this path is stable in Inspector).
- **`transfer_money_tools` flow**, Start with: *“Transfer 25 dollars to Alex from account 111.”* The assistant may still ask you to confirm **amount**, **recipient**, and **account_from** one at a time. Answer plainly (e.g. *“25 dollars”*, *“Alex”*, then your **from** account when asked). You should end with a **demo transfer processed** message. That end-to-end path is what this lab expects you to verify. Not that every slot is filled from the first user turn.

**Step 3.** **In Codio**, use **Check It!**.

{Check It!|assessment}(code-output-compare-501050002)

The grader inspects:

- **`level5/tools/`** and **`banking_tools.py`** (with **`__all__`**)
- **`endpoints.yml`** (**`tools:`**)
- **Lab 2.0** wiring: **`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`**
- **`transfer_money_tools.yml`**, **`action_process_transfer_with_tools.py`**, and **`domain/basics.yml`** (action listed)
- **`level5/models/`** (partial credit if domain passes but there is no model yet)

**Lab 4.1** already enforced **`from_llm`** conditions for **`transfer_money_tools`** and a real **`run()`**. Keep that work aligned when you run **Lab 5.2**.
