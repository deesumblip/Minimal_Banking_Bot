# Lab 4.1 – Reference solution for LLM Rubric / Code Test

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 4.1 (Creating the transfer_money_tools Flow and Action), or as reference for the code-output-compare grader.

---

## Required artifacts

### 1. `level5/domain/basics.yml`

- **`actions:`** includes **`action_process_transfer_with_tools`**.
- **`slots:`** For **`amount`**, **`recipient`**, and **`account_from`**, each **`from_llm`** mapping lists **`conditions`** that include **both** **`active_flow: transfer_money`** and **`active_flow: transfer_money_tools`** (students complete this in **fill-in-the-blanks-501040010**).

### 2. `level5/data/basics/transfer_money_tools.yml`

- **`flows:`** contains **`transfer_money_tools`** with **`collect:`** for **amount**, **recipient**, **account_from**, and **`action: action_process_transfer_with_tools`**.

### 3. `level5/actions/action_process_transfer_with_tools.py`

- Action class with **`name()`** returning **`"action_process_transfer_with_tools"`**.
- **`run()`** uses **`tracker.get_slot`** for **amount**, **recipient**, and **account_from**, and calls **`dispatcher.utter_message`** at least once (demo confirmation).

---

## Rubric summary for autograde

- Flow file exists; flow collects the three slots and runs **`action_process_transfer_with_tools`**.
- Action file implements **`run()`** with slot reads and **`utter_message`**.
- Domain lists the action and maps **`from_llm`** for the three slots when **`transfer_money_tools`** is active.
