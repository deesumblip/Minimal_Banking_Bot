**Starting point:** Work in **`level4/`** (see **Unit 0.1**).

You now have a **Level 4** assistant: the same **non-transfer** behavior as before, plus a **transfer** flow that collects **three** slots and runs **`action_process_transfer`**.

## What your agent can do

| Layer | What it does |
|-------|----------------|
| **Level 1** | Greet, help, contact, goodbye (responses). |
| **Level 2** | Bank hours, `action_bank_hours`. |
| **Level 3** | Check balance, collect `account`, then `action_check_balance_simple`. |
| **Level 4** | Transfer, collect **`amount` → `recipient` → `account_from`**, then **`action_process_transfer`** (demo confirmation). |

Train **once** from **`level4`**; one model serves all flows.

## Quick verification (same as Lab 5.2)

In **Rasa Inspector**, repeat the **scripted transfer** from **Lab 5.2** to see multi-slot collection and free-text **recipient** (capped at **100** characters in the action and flow). Example turns:

```text
1. Can I transfer some money?
2. let's say 300 dollars
3. Alice
4. savings
```

You should see a final line like **`(Demo) Transfer of $300 from account savings to Alice has been processed successfully.`**

For graded checks and troubleshooting, use **Lab 5.2** in Unit 5.
