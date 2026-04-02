# Run the banking MCP server (Level 6). Streamable HTTP at http://127.0.0.1:8080/mcp
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mcp_server.banking import main
main()
