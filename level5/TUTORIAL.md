# Level 5: Tool Calling - Tutorial

**A guide to adding LLM-driven tool selection to your Level 4 banking bot.**

---

## Table of Contents

0. [Recap: What You Built in Level 4](#module-0-recap-what-you-built-in-level-4)
1. [Introduction to Tools](#module-1-introduction-to-tools)
2. [Creating Tool Functions](#module-2-creating-tool-functions)
3. [Registering Tools](#module-3-registering-tools)
4. [Using Tools in Conversations](#module-4-using-tools-in-conversations)
5. [Training and Testing](#module-5-training-and-testing)
6. [Summary and Next Steps](#module-6-summary-and-next-steps)

---

## Module 0: Recap - What You Built in Level 4

### 0.1 Your Level 4 Banking Bot

Level 5 uses the **level5** folder, which extends your Level 4 bot. Everything from Level 4 remains:

- **Domain**: Slots (account, amount, recipient, account_from), utter_ask_* responses, actions including action_process_transfer
- **Flows**: greet, help, contact, goodbye, hours, check_balance, transfer_money
- **Actions**: action_bank_hours, action_check_balance_simple, action_process_transfer

### 0.2 What Level 5 Adds

Level 5 adds **tool calling**: functions the LLM can choose to call at runtime (check_balance, process_transfer, get_account_info). You will add:

- **Tools module (Lab 2.1):** `level5/tools/` with `banking_tools.py` and `__all__`
- **Registration (Lab 3.1):** `tools:` section in `endpoints.yml` with `tools_module: "tools"`
- **Flow and action (Lab 4.1):** `transfer_money_tools.yml` and `action_process_transfer_with_tools.py`
- **Training and testing (Labs 5.1, 5.2):** Train from level5 and run the completion check

---

## Module 1: Introduction to Tools

### 1.1 Tools vs Actions

**Actions** are explicitly called in flow steps (e.g. `action: action_process_transfer`). **Tools** are Python functions the LLM can decide to call based on conversation context. You register tools in endpoints.yml; the LLM discovers and invokes them when relevant.

### 1.2 When to Use Tools

Use tools when you want the LLM to dynamically choose which function to call (e.g. "check my balance" vs "transfer $50") instead of hard-coding one action per flow step.

### 1.3 Test Your Knowledge

See **Level5_Unit1_Content_1.3_Test-Your-Knowledge.md** for a short quiz on Units 0–1.

---

## Module 2: Creating Tool Functions

### 2.1 Creating Tool Functions

In **Lab 2.1** you create `level5/tools/` and `tools/banking_tools.py` with at least three functions: `check_balance(account)`, `process_transfer(amount, from_account, to_account)`, and `get_account_info(account)`. Each returns a dict and has a docstring. You add `__all__` so Rasa can discover them.

---

## Module 3: Registering Tools

### 3.1 Registering Tools

In **Lab 3.1** you add a `tools:` section to `level5/endpoints.yml` with `tools_module: "tools"`. Rasa then discovers the functions exported in your tools module.

---

## Module 4: Using Tools in Conversations

### 4.1 Using Tools in a Flow

In **Lab 4.1** you create the flow `transfer_money_tools` (collect amount, recipient, account_from, then `action: action_process_transfer_with_tools`) and the action file. When that action runs, the LLM can call the registered tools. You also add the action to the domain `actions:` list.

---

## Module 5: Training and Testing

### 5.1 Training Level 5

From **project root**, activate the venv and run:

- `cd level5`
- `rasa train`

A model is created in `level5/models/`. Use the same venv as Level 1–4 (no new venv in level5).

### 5.2 Testing Tool Calling

Run the completion check (Lab 5.2). Optionally run `rasa run actions` and `rasa inspect` to trigger the transfer_money_tools flow and confirm the LLM can call tools. On Codio use the **Rasa Inspect** tab.

**Lab 5.1** is graded (training); **Lab 5.2** is the completion check (tools, endpoints, flow, action, domain, and optionally model).

---

## Module 6: Summary and Next Steps

### 6.1 Complete Bot Walkthrough

Your Level 5 bot supports all Level 1–4 flows plus **transfer_money_tools**, where the LLM can call check_balance, process_transfer, and get_account_info. See **Level5_Unit6_Content_6.1_Complete-Bot-Walkthrough.md**.

### 6.2 What You've Learned

You added a tools module with `__all__`, registered it in endpoints.yml, created a flow and action that run in a tool-calling context, and trained from level5.

### 6.3 What's Next

See **Level5_Unit6_Content_6.3_Whats-Next.md** for next steps.

### 6.4 Knowledge Check

See **Level5_Unit6_Content_6.4_Knowledge-Check.md** for a short quiz on Level 5.

### 6.5 Limitations of Level 5

See **Level5_Unit6_Content_6.5_Limitations-of-Level-5.md** for what Level 5 cannot do and when to move to Level 6.

### 6.6 What's Next: Level 6 Preview

See **Level5_Unit6_Content_6.6_Whats-Next-Level-6-Preview.md** for an overview of sub-agents (Level 6).

### 6.7 Course Completion Checklist

See **Level5_Unit6_Content_6.7_Course-Completion-Checklist.md** before moving to Level 6.

---

## Quick Reference

| Item | Location |
|------|----------|
| Virtual environment | Project root (same as Level 1–4). Activate from root, then `cd level5`. |
| Tools module | level5/tools/ and level5/tools/banking_tools.py |
| Tools registration | level5/endpoints.yml — `tools:` section with `tools_module: "tools"` |
| Transfer-with-tools flow | level5/data/basics/transfer_money_tools.yml |
| Transfer-with-tools action | level5/actions/action_process_transfer_with_tools.py |
| Inspector on Codio | Use **Rasa Inspect** tab only (no port 5005 / Ports view) |

For step-by-step lab instructions and assessment setup, use the **Level5_Lab*_Content.md** and **Level5_Lab*_Assessment_Setup.md** files in level5/.
