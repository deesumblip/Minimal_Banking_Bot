Tool functions are plain Python functions that the LLM can call. They live in a **tools** module (e.g. `tools/banking_tools.py`).

## Requirements

- **Location**: Create a `tools/` folder in your bot directory (e.g. `level5/tools/`) with an `__init__.py` and a module file (e.g. `banking_tools.py`).
- **Signature**: Each tool is a function with a clear name, parameters, and a return value (typically a dict or string). Use type hints and a docstring so the LLM understands what the function does.
- **Discovery**: Export the functions that should be available as tools via `__all__` in the module (e.g. `__all__ = ["check_balance", "process_transfer", "get_account_info"]`).

## Example

In `tools/banking_tools.py` you might define:

- `check_balance(account: str)` — returns a dict with balance info.
- `process_transfer(amount: str, from_account: str, to_account: str)` — returns a dict with success/message.
- `get_account_info(account: str)` — returns a dict with account details.

Each function should have a docstring describing what it does; the LLM uses these to decide when to call each tool. In Lab 2.1 you will create this folder and file and add at least these three tools.
