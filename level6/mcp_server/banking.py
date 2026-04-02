"""
Banking MCP server for Level 6 (Streamable HTTP — required by Rasa's MCP client).

Rasa Pro connects via the official MCP Python SDK (`streamablehttp_client`); a plain
JSON-RPC `HTTPServer` is not compatible. This server uses FastMCP + uvicorn.

Run from level6:
  python mcp_server/banking.py

Default URL for endpoints.yml:
  http://127.0.0.1:8080/mcp
"""
from __future__ import annotations

import asyncio
import sys

from mcp.server.fastmcp import FastMCP

PORT = 8080
STREAMABLE_PATH = "/mcp"

mcp = FastMCP(
    "Banking",
    instructions="Demo banking tools for the Level 6 sub-agent lab.",
    host="127.0.0.1",
    port=PORT,
    streamable_http_path=STREAMABLE_PATH,
)


@mcp.tool()
def check_balance(account: str) -> str:
    """Check the balance for a bank account."""
    if not account or str(account).lower() in (
        "<missing>",
        "account number",
        "user_account_number",
    ):
        return "Please provide a valid account number."
    return f"(Demo) Balance for account {account} is $123.45."


@mcp.tool()
def process_transfer(amount: str, from_account: str, to_account: str) -> str:
    """Process a money transfer from one account to another."""
    if not amount or not from_account or not to_account:
        return "Missing required fields: amount, from_account, to_account."
    return (
        f"(Demo) Transfer of ${amount} from account {from_account} to {to_account} "
        "has been processed successfully."
    )


@mcp.tool()
def get_account_info(account: str) -> str:
    """Get information for a bank account (e.g. type, status)."""
    if not account or str(account).lower() in (
        "<missing>",
        "account number",
        "user_account_number",
    ):
        return "Please provide a valid account number."
    return f"(Demo) Account {account}: type Checking, status Active, opened 2020-01-15."


async def _run() -> None:
    print(
        f"Banking MCP (Streamable HTTP) at http://127.0.0.1:{PORT}{STREAMABLE_PATH}",
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
