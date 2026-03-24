After adding the tools folder, endpoints registration, and the transfer_money_tools flow and action, you need to **train** the Level 5 agent.

## Steps

1. From **project root**, activate the virtual environment (e.g. `source .venv/bin/activate` on Linux/macOS or `.\.venv\Scripts\Activate.ps1` on Windows).
2. Change to the level5 folder: `cd level5`.
3. Run: `rasa train`.
4. The model will be written to `level5/models/`. The assistant will include your domain, flows, and the ability to use tools when the flow runs action_process_transfer_with_tools.

If training fails, check: (1) domain/basics.yml lists `action_process_transfer_with_tools` in the actions list, (2) endpoints.yml has the `tools:` section with `tools_module: "tools"`, (3) the `tools/` folder exists and has `banking_tools.py` with valid Python and `__all__` defined.
