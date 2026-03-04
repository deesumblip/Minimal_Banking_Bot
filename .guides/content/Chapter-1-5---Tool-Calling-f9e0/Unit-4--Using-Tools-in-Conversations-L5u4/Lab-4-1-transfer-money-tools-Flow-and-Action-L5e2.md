**Objective.** In this lab you will create the flow `transfer_money_tools` and the action `action_process_transfer_with_tools`, and register the action in the domain so the LLM can call tools during this flow.

## Step-by-Step Instructions

**Step 1 — Flow file.** Create `level5/data/basics/transfer_money_tools.yml` with a flow that:
- Has a `name` and `description` (e.g. "transfer money with tools" — the description helps the LLM know when to trigger it).
- **steps:** collect amount (with description), collect recipient (with description), collect account_from (with description), then `action: action_process_transfer_with_tools`.

**Step 2 — Action file.** Create `level5/actions/action_process_transfer_with_tools.py` with a custom action class that:
- Inherits from `Action` (rasa_sdk).
- `name()` returns `"action_process_transfer_with_tools"`.
- `run()` can send a message and/or allow the LLM to use the registered tools in this context (implementation may call the tools or delegate to the LLM tool-calling mechanism per your Rasa version).

**Step 3 — Domain.** Open `level5/domain/basics.yml` and add `action_process_transfer_with_tools` to the `actions:` list (alongside the existing actions).

**Step 4.** Verify: the flow file exists and has the correct steps; the action file exists and is registered in the domain.

---

## In Codio / Locally

From project root activate venv, `cd level5`. Create the flow and action files and update the domain. Run the assessment when done.
