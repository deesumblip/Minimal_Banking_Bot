**Work in \`level5/\`:** All Level 5 files and Rasa commands use **`level5/`** as the agent directory.

Use **tools** when you want the LLM to decide what to do based on context: for example, the user might ask for a balance check, a transfer, or both in one conversation. The LLM selects which tool(s) to call and with what arguments.

Use **actions** when you need a fixed sequence: for example, "after collecting amount, recipient, and account_from, always run action_process_transfer." The flow guarantees that step runs.

In Level 5 you use both: the flow collects slots and then runs one action (action_process_transfer_with_tools). Inside that action's context, the **LLM** can call one or more **tools** (check_balance, process_transfer, get_account_info) depending on the dialogue. So the flow is predictable (collect then action), and the flexibility is inside the action (which tools the LLM calls).
