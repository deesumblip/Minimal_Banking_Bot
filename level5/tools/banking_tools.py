"""Banking tools for Level 5: Tool Calling.

Tools are functions that the LLM can dynamically call during conversations.
Unlike actions (which are explicitly called in flows), tools are selected
by the LLM based on the conversation context.

This allows the bot to:
- Dynamically choose which operations to perform
- Handle complex, multi-step tasks
- Adapt to user requests without hardcoding every scenario
"""

from typing import Dict, Any


def check_balance(account: str) -> Dict[str, Any]:
    """Check the balance for a given account.
    
    This is a tool function that the LLM can call dynamically.
    
    Args:
        account: The account number to check
        
    Returns:
        A dictionary with the balance information
    """
    # Demo implementation - in real life, this would query a database
    return {
        "account": account,
        "balance": 1234.56,
        "currency": "USD",
        "status": "active"
    }


def process_transfer(amount: float, from_account: str, to_account: str) -> Dict[str, Any]:
    """Process a money transfer between accounts.
    
    This is a tool function that the LLM can call dynamically.
    
    Args:
        amount: The amount to transfer
        from_account: Source account number
        to_account: Destination account number
        
    Returns:
        A dictionary with the transfer result
    """
    # Demo implementation - in real life, this would process a real transfer
    return {
        "success": True,
        "transaction_id": "TXN-12345",
        "amount": amount,
        "from_account": from_account,
        "to_account": to_account,
        "message": "Transfer processed successfully"
    }


def get_account_info(account: str) -> Dict[str, Any]:
    """Get information about an account.
    
    This is a tool function that the LLM can call dynamically.
    
    Args:
        account: The account number
        
    Returns:
        A dictionary with account information
    """
    # Demo implementation
    return {
        "account": account,
        "type": "checking",
        "owner": "John Doe",
        "opened": "2020-01-15",
        "status": "active"
    }


# Export all tools so Rasa can discover them
__all__ = ["check_balance", "process_transfer", "get_account_info"]
