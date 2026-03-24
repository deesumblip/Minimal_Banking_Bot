Level 6 uses the **level6** folder, which extends your Level 5 agent. Everything from Level 5 remains:

- **Domain**: Slots (account, amount, recipient, account_from), utter_ask_* responses, actions including action_process_transfer and action_process_transfer_with_tools
- **Flows**: greet, help, contact, goodbye, hours, check_balance, transfer_money, transfer_money_tools
- **Actions**: action_bank_hours, action_check_balance_simple, action_process_transfer, action_process_transfer_with_tools
- **Tools**: tools/banking_tools.py with check_balance, process_transfer, get_account_info; registered in endpoints.yml

Level 6 does not remove or replace these. It adds **sub-agents** so the main agent can delegate whole tasks to another agent (e.g. a banking assistant) that runs until it completes.
