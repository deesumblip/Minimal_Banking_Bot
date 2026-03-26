**Starting point:** Work in **`level5/`** (see **Units 0.1–0.2**). You will add **`tools/banking_tools.py`** in **Lab 2.1**; this page explains the pattern.

Tool functions are plain Python functions that the LLM can call. They live in a **`tools`** module (for example **`tools/banking_tools.py`**).

## Requirements

- **Location:** Create a **`tools/`** folder under your agent directory (for example **`level5/tools/`**) with **`__init__.py`** and a module file (for example **`banking_tools.py`**).
- **Signature:** Each tool is a function with a clear name, parameters, and a return value (typically a **dict** or string). Use type hints and a docstring so the LLM understands what the function does.
- **Discovery:** Export the functions that should be available as tools via **`__all__`** in the module (for example **`__all__ = ["check_balance", "process_transfer", "get_account_info"]`**).

## Example: One complete tool function

Below is one full example. The LLM uses the **function name** and **docstring** to decide when to call it. You will create a module with at least three tools (**`check_balance`**, **`process_transfer`**, **`get_account_info`**); this shows the pattern for one of them.

In **`tools/banking_tools.py`** you might define:

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

You will add two more functions following the same pattern: **`process_transfer(amount, from_account, to_account)`** (returns a dict with success/message) and **`get_account_info(account)`** (returns a dict with account details). Each needs a clear docstring so the LLM knows when to call it. The **`__all__`** list at the top tells Rasa which functions to expose as tools. In **Lab 2.1** you will create the **`tools/`** folder and **`banking_tools.py`** with all three tools and **`__all__`**.
