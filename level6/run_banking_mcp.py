# Run the banking MCP server (Level 6). Listens on http://localhost:8080.
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mcp_server.banking import main
main()
