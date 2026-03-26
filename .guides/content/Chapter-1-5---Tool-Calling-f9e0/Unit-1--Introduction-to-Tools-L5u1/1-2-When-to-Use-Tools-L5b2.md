**Starting point:** Work in **`level5/`** (see **Units 0.1–0.2**). This page is a rule-of-thumb for when to model behavior as a **tool** versus an **action**.

## When to use tools

Use **tools** when you want the **LLM** to decide what to do from context: the user might ask for a balance check, a transfer, or both in one conversation. The LLM selects which tool(s) to call and with what arguments.

## When to use actions

Use **actions** when you need a **fixed sequence**: for example, after collecting **amount**, **recipient**, and **account_from**, the flow should **always** run **`action_process_transfer`**. The flow guarantees that step runs.

## How Chapter 1.5 combines both

In this chapter you use **both** patterns. The **flow** collects slots, then runs one **action** (`action_process_transfer_with_tools`). Inside that action’s context, the **LLM** can call one or more **tools** (`check_balance`, `process_transfer`, `get_account_info`, …) depending on the dialogue. So the **flow** stays predictable (collect, then action), and the **flexibility** lives inside that action step—which tools the LLM invokes.
