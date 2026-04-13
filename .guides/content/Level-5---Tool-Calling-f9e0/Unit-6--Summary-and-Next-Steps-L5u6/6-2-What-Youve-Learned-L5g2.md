**Starting point:** Work in **`level5/`** with the Level 4 baseline (**Unit 0.1**) plus the labs you finished in this chapter.

## What you added in Level 5

You added the **command prompt** (**Lab 2.0**), the **`tools/`** module (**Lab 2.1**), **`tools:`** registration (**Lab 3.1**), and the **`transfer_money_tools`** flow with **`action_process_transfer_with_tools`** (**Lab 4.1**), then trained and tested (**Labs 5.1–5.2**). The **full lab order and deliverables** are in **Unit 0.2** (summary table). Read there for filenames and steps. Do not treat this page as a second copy of that table.

## Key ideas

- **Tools** vs **actions**, **Unit 1.1** and **Unit 1.2**.
- **Where tools live**, Python under **`tools/`**, registered in **`endpoints.yml`**.
- **Flow + action + tools**, One **`action:`** step can run while the LLM still invokes tools. The flow does not list tool names.

Your assistant keeps every earlier flow and adds **`transfer_money_tools`** for model-chosen tool use alongside the classic **`transfer_money`** path.
