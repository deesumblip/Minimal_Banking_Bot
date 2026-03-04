"""Banking tools callable by the LLM in Level 5 (and Level 6 main agent)."""
from typing import Any, Dict

__all__ = ["check_balance", "process_transfer", "get_account_info"]


def check_balance(account: str) -> Dict[str, Any]:
    """Check the balance for a bank account."""
    if not account or str(account).lower() in ("<missing>", "account number", "user_account_number"):
        return {"error": "Please provide a valid account number."}
    return {"account": account, "balance": "123.45", "currency": "USD"}


def process_transfer(amount: str, from_account: str, to_account: str) -> Dict[str, Any]:
    """Process a money transfer from one account to another."""
    if not amount or not from_account or not to_account:
        return {"error": "Missing required fields: amount, from_account, to_account."}
    return {
        "success": True,
        "message": f"Transfer of ${amount} from {from_account} to {to_account} processed.",
    }


def get_account_info(account: str) -> Dict[str, Any]:
    """Get information for a bank account (e.g. type, status)."""
    if not account or str(account).lower() in ("<missing>", "account number", "user_account_number"):
        return {"error": "Please provide a valid account number."}
    return {"account": account, "type": "Checking", "status": "Active", "opened": "2020-01-15"}
