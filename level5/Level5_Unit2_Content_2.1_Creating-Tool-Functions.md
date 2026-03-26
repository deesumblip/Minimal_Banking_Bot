**Starting point:** Work in **`level5/`** with the Chapter 1.4 completion baseline. The **next lab** in this unit has you add **`tools/banking_tools.py`**; this page explains the pattern first.

Tool functions are plain Python functions that the LLM can call. They live in a **tools** module (e.g. `tools/banking_tools.py`).

## Requirements

- **Location**: Create a `tools/` folder in your agent directory (e.g. `level5/tools/`) with an `__init__.py` and a module file (e.g. `banking_tools.py`).
- **Signature**: Each tool is a function with a clear name, parameters, and a return value (typically a dict or string). Use type hints and a docstring so the LLM understands what the function does.
- **Discovery**: Export the functions that should be available as tools via `__all__` in the module (e.g. `__all__ = ["check_balance", "process_transfer", "get_account_info"]`).

## Example: One complete tool function

Below is a full example of one tool function. The LLM uses the function name and docstring to decide when to call it. You will create a module with at least three tools (check_balance, process_transfer, get_account_info); this example shows the pattern for one of them.

In `tools/banking_tools.py` you might define:

```python
__all__ = ["check_balance", "process_transfer", "get_account_info"]


def check_balance(account: str):
    """Check the balance for a given bank account.
    
    Use this when the user asks for their balance or how much is in an account.
    
    Args:
        account: The account number or identifier to check.
        
    Returns:
        A dict with keys such as account, balance, currency, status.
    """
    # Demo: in production you would query a real system
    return {
        "account": account,
        "balance": 1234.56,
        "currency": "USD",
        "status": "active"
    }
```

You will add two more functions following the same pattern: **process_transfer(amount, from_account, to_account)** (returns a dict with success/message) and **get_account_info(account)** (returns a dict with account details). Each needs a clear docstring so the LLM knows when to call it. The `__all__` list at the top tells Rasa which functions to expose as tools. The **lab at the end of this unit** has you create the `tools/` folder and `banking_tools.py` with all three tools and `__all__`.
