**Starting point:** Work in **`level5/`** with the Chapter 1.4 baseline and the Chapter 1.5 overview on the previous pages. This page is a practical rule of thumb for **tool** versus **action**.

## When to use tools

Choose **tools** when the **LLM** should pick what to do from context—the user might ask for a balance, a transfer, or both in one turn. The model selects which tool(s) to run and with which arguments.

## When to use actions

Choose **actions** when you need a **fixed step**: after **amount**, **recipient**, and **account_from** are collected, the flow should **always** run **`action_process_transfer`**. The flow enforces that order.

## How Chapter 1.5 combines both

This chapter uses **both**. The **flow** collects slots, then runs one **action** (`action_process_transfer_with_tools`). Inside that action’s context, the **LLM** may call one or more **tools** (`check_balance`, `process_transfer`, `get_account_info`, …) depending on the dialogue. The **flow** stays predictable (collect, then action); **flexibility** sits in that action step—which tools run and when.
