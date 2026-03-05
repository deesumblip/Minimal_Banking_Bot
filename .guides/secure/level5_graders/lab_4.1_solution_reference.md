# Lab 4.1 – Reference solution for LLM Rubric / Code Test

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 4.1 (Creating the transfer_money_tools Flow and Action), or as reference for the code-output-compare grader.

---

## Required artifacts

### 1. level5/data/basics/transfer_money_tools.yml

- **flows:** section with at least one flow (e.g. transfer_money_tools).
- Flow must use **collect:** to gather slots (e.g. amount, recipient, account_from) and include an **action** step that runs `action_process_transfer_with_tools` (or equivalent name registered in the domain).

### 2. level5/actions/action_process_transfer_with_tools.py

- Action class with **name()** returning the action name (e.g. `"action_process_transfer_with_tools"`).
- **run()** method that reads slots (amount, recipient, account_from), optionally validates, and returns at least one message (e.g. confirmation). Returns a list of events (e.g. `[SlotSet(...), BotMessage(...)]`).

### 3. level5/domain/basics.yml

- **actions:** list must include `action_process_transfer_with_tools` (so the flow can invoke it).

---

## Rubric summary for autograde

- **transfer_money_tools.yml** exists, is valid YAML, has a flow with collect and an action step.
- **action_process_transfer_with_tools.py** exists, defines the action name and run() with slot reads and at least one bot message.
- **domain/basics.yml** lists the action in the actions section.
