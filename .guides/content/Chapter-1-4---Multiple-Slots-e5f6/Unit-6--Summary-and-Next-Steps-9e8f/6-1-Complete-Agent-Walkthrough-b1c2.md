**Starting point:** Work in **`level4/`** (see **Unit 0.1**).

You now have one assistant under **`level4/`** that keeps Levels **1–3** behavior and adds the **transfer** path: ordered **`collect:`** steps for **`amount`**, **`recipient`**, **`account_from`**, then **`action_process_transfer`**. Train **once**; one model covers every flow.

## What your agent can do

| Layer | What it does |
|-------|----------------|
| **Level 1** | Greet, help, contact, goodbye (responses). |
| **Level 2** | Bank hours, `action_bank_hours`. |
| **Level 3** | Check balance, collect `account`, then `action_check_balance_simple`. |
| **Level 4** | Transfer, collect **`amount` → `recipient` → `account_from`**, then **`action_process_transfer`** (demo confirmation). |

## Verify in Inspector

Use the **scripted transfer**, expected turns, and troubleshooting from **Lab 5.2** (Unit 5)—that page is the single place for the example dialogue and confirmation line. This walkthrough is the **layer map** only.
