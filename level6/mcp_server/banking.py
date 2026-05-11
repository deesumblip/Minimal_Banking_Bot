"""
Banking MCP server for Level 6 (Streamable HTTP — required by Rasa's MCP client).

Rasa Pro connects via the official MCP Python SDK (streamablehttp_client); a plain
JSON-RPC HTTPServer is not compatible. This server uses FastMCP + uvicorn.

Run from level6:
  python mcp_server/banking.py

Default URL for endpoints.yml:
  http://127.0.0.1:8080/mcp
"""
import asyncio
import json
import sys
from typing import Optional

from mcp.server.fastmcp import FastMCP

PORT = 8080
STREAMABLE_PATH = "/mcp"

mcp = FastMCP(
    "Banking",
    instructions="Demo banking tools for the Level 6 financial advisor sub-agent.",
    host="0.0.0.0",
    port=PORT,
    streamable_http_path=STREAMABLE_PATH,
)


def _as_json(obj) -> str:
    return json.dumps(obj, ensure_ascii=False)


@mcp.tool()
def get_account_options(goal: str, user_profile: Optional[str] = None) -> str:
    """
    Return product options for a given financial goal.
    goal: e.g. "loan", "savings account", "product comparison"
    user_profile: optional free-text context (income, credit score band, etc.)
    """
    goal_norm = (goal or "").strip().lower()
    if not goal_norm:
        return _as_json({"error": "Missing required field: goal"})

    if "loan" in goal_norm:
        options = [
            {"product": "Personal Loan", "min_apr": 8.9, "max_apr": 18.9, "term_months": [24, 36, 60]},
            {"product": "Auto Loan", "min_apr": 6.4, "max_apr": 14.9, "term_months": [36, 48, 60, 72]},
        ]
    elif "savings" in goal_norm:
        options = [
            {"product": "High-Yield Savings", "apy": 4.10, "min_balance": 0},
            {"product": "Money Market", "apy": 4.35, "min_balance": 1000},
            {"product": "CD (12 mo)", "apy": 4.60, "min_balance": 500},
        ]
    else:
        options = [
            {"product": "Checking", "monthly_fee": 0, "notes": "No-fee with direct deposit"},
            {"product": "High-Yield Savings", "apy": 4.10, "notes": "Variable APY"},
            {"product": "Personal Loan", "apr_range": "8.9-18.9%", "notes": "APR depends on credit"},
        ]

    return _as_json({
        "goal": goal,
        "options": options,
        "disclaimer": "Demo data only. Not real rates.",
        "context_used": bool(user_profile),
    })


@mcp.tool()
def get_current_rates(product: str) -> str:
    """
    Return current demo rates for a product category.
    product: e.g. "personal loan", "auto loan", "savings", "cd"
    """
    product_norm = (product or "").strip().lower()
    if not product_norm:
        return _as_json({"error": "Missing required field: product"})

    demo_rates = {
        "personal loan": {"apr_min": 8.9, "apr_max": 18.9},
        "auto loan":     {"apr_min": 6.4, "apr_max": 14.9},
        "savings":       {"apy": 4.10},
        "cd":            {"apy_12mo": 4.60, "apy_24mo": 4.40},
    }

    for key, val in demo_rates.items():
        if key in product_norm:
            return _as_json({
                "product": key,
                "rates": val,
                "disclaimer": "Demo data only. Not real rates.",
            })

    return _as_json({
        "product": product,
        "error": "Unknown product. Try: personal loan, auto loan, savings, cd",
    })


@mcp.tool()
def calculate_loan_repayment(
    principal: float,
    apr_percent: float,
    term_months: int,
) -> str:
    """
    Calculate monthly payment and totals for a fixed-rate loan.
    principal: loan amount in dollars
    apr_percent: annual percentage rate, e.g. 8.9 for 8.9%
    term_months: loan term in months, e.g. 36 for 3 years
    """
    if not principal or principal <= 0:
        return _as_json({"error": "principal must be > 0"})
    if apr_percent is None or apr_percent < 0:
        return _as_json({"error": "apr_percent must be >= 0"})
    if not term_months or term_months <= 0:
        return _as_json({"error": "term_months must be > 0"})

    r = (apr_percent / 100.0) / 12.0
    n = term_months
    payment = principal / n if r == 0 else principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    total_paid = payment * n

    return _as_json({
        "principal": round(principal, 2),
        "apr_percent": round(apr_percent, 4),
        "term_months": n,
        "monthly_payment": round(payment, 2),
        "total_paid": round(total_paid, 2),
        "total_interest": round(total_paid - principal, 2),
        "disclaimer": "Demo calculation. Does not include fees, insurance, or taxes.",
    })


async def _run() -> None:
    print(
        f"Banking MCP (Streamable HTTP)\n"
        f"URL for endpoints.yml:\n  http://127.0.0.1:{mcp.settings.port}{STREAMABLE_PATH}",
        flush=True,
    )
    await mcp.run_streamable_http_async()


def main() -> None:
    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    mcp.settings.port = port
    asyncio.run(_run())


if __name__ == "__main__":
    main()
