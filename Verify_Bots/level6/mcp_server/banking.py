"""
Banking MCP server for Level 6.
Exposes check_balance, process_transfer, get_account_info as MCP tools.
Run from repo root: python -m level6.mcp_server.banking
Or from level6: python mcp_server/banking.py
Listens on http://localhost:8080 by default.
"""
import json
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

PORT = 8080

TOOLS = [
    {
        "name": "check_balance",
        "description": "Check the balance for a bank account.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "account": {"type": "string", "description": "Account number or identifier"}
            },
            "required": ["account"],
            "additionalProperties": False,
        },
    },
    {
        "name": "process_transfer",
        "description": "Process a money transfer from one account to another.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "amount": {"type": "string", "description": "Transfer amount"},
                "from_account": {"type": "string", "description": "Source account number"},
                "to_account": {"type": "string", "description": "Recipient account or name"},
            },
            "required": ["amount", "from_account", "to_account"],
            "additionalProperties": False,
        },
    },
    {
        "name": "get_account_info",
        "description": "Get information for a bank account (e.g. type, status).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "account": {"type": "string", "description": "Account number or identifier"}
            },
            "required": ["account"],
            "additionalProperties": False,
        },
    },
]


def handle_check_balance(arguments: dict) -> str:
    account = arguments.get("account", "<missing>")
    if not account or str(account).lower() in ("<missing>", "account number", "user_account_number"):
        return "Please provide a valid account number."
    return f"(Demo) Balance for account {account} is $123.45."


def handle_process_transfer(arguments: dict) -> str:
    amount = arguments.get("amount", "")
    from_account = arguments.get("from_account", "")
    to_account = arguments.get("to_account", "")
    if not amount or not from_account or not to_account:
        return "Missing required fields: amount, from_account, to_account."
    return f"(Demo) Transfer of ${amount} from account {from_account} to {to_account} has been processed successfully."


def handle_get_account_info(arguments: dict) -> str:
    account = arguments.get("account", "<missing>")
    if not account or str(account).lower() in ("<missing>", "account number", "user_account_number"):
        return "Please provide a valid account number."
    return f"(Demo) Account {account}: type Checking, status Active, opened 2020-01-15."


HANDLERS = {
    "check_balance": handle_check_balance,
    "process_transfer": handle_process_transfer,
    "get_account_info": handle_get_account_info,
}


def json_rpc_tools_list() -> dict:
    return {"tools": TOOLS, "nextCursor": None}


def json_rpc_tools_call(name: str, arguments: dict) -> dict:
    if name not in HANDLERS:
        return {"content": [{"type": "text", "text": f"Unknown tool: {name}"}], "isError": True}
    try:
        text = HANDLERS[name](arguments or {})
        return {"content": [{"type": "text", "text": text}], "isError": False}
    except Exception as e:
        return {"content": [{"type": "text", "text": str(e)}], "isError": True}


class MCPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b""
        try:
            req = json.loads(body.decode("utf-8"))
        except Exception:
            self._send_json_rpc_error(None, -32700, "Parse error")
            return
        req_id = req.get("id")
        method = req.get("method")
        params = req.get("params") or {}
        if method == "tools/list":
            result = json_rpc_tools_list()
            self._send_json_rpc_result(req_id, result)
        elif method == "tools/call":
            name = params.get("name", "")
            arguments = params.get("arguments") or {}
            result = json_rpc_tools_call(name, arguments)
            self._send_json_rpc_result(req_id, result)
        else:
            self._send_json_rpc_error(req_id, -32601, "Method not found: " + str(method))

    def _send_json_rpc_result(self, req_id, result):
        resp = {"jsonrpc": "2.0", "id": req_id, "result": result}
        self._send_json(200, resp)

    def _send_json_rpc_error(self, req_id, code, message):
        resp = {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}
        self._send_json(200, resp)

    def _send_json(self, status, obj):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(obj).encode("utf-8"))

    def log_message(self, format, *args):
        pass


def main():
    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    server = HTTPServer(("", port), MCPHandler)
    print("Banking MCP server listening on http://localhost:" + str(port))
    server.serve_forever()


if __name__ == "__main__":
    main()
