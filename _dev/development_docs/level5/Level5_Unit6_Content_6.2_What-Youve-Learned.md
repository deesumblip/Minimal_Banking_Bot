## Level 5 Summary

In this chapter you:

1. **Tools folder (Lab 2.1)** — Created `tools/` and `banking_tools.py` with tool functions (e.g. check_balance, process_transfer, get_account_info) and exported them via `__all__`.

2. **Register tools (Lab 3.1)** — Added a `tools:` section to `endpoints.yml` with `tools_module: "tools"` so Rasa discovers the tools.

3. **Flow and action (Lab 4.1)** — Created `transfer_money_tools.yml` (collect amount, recipient, account_from, then action_process_transfer_with_tools) and the action `action_process_transfer_with_tools`, and registered the action in the domain.

4. **Training and testing (Labs 5.1 and 5.2)** — Trained the Level 5 agent from the `level5` folder and ran the completion check and tested tool calling in Inspector.

## Key Ideas

- **Tools** are functions the LLM selects and calls at runtime; **actions** are steps explicitly named in flows.
- Tools are defined in a Python module (e.g. `tools/banking_tools.py`) and registered in `endpoints.yml`.
- A flow can run an action in a context where the LLM can call tools; the flow does not list the tools, the LLM decides.

Your Level 5 agent is a single assistant that supports all previous flows plus transfer_money_tools with dynamic tool use.
