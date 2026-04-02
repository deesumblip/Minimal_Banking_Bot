**Objective.** In Unit 2 you saw what belongs in the sub-agent config. In this lab you will create **`level6/sub_agents/banking_assistant/config.yml`** so the main agent can call the **`banking_assistant`** sub-agent. **Same pattern as Chapter 1.5 Lab 2.1:** fill-in-the-blanks first, copy the completed file into the project, then **Code Test**.

## Step-by-Step Instructions

**Step 1.** Complete the **Fill in the blanks** exercise below. It produces the full **`config.yml`** skeleton for this course (agent, **`configuration.module`** for **`BankingAssistantLiteAgent`**, **`mcp_servers`** name).

{Check It!|assessment}(fill-in-the-blanks-501060111)

**Step 2.** Create the folder **`level6/sub_agents/banking_assistant/`** if it does not exist (the starter may already include **`.gitkeep`** only).

**Step 3.** Copy your **passed** fill-in YAML into **`level6/sub_agents/banking_assistant/config.yml`**. Save the file. Confirm indentation is two spaces (YAML-sensitive).

**Step 4.** **Use Check It!** below for the graded **Code Test** (Codio).

{Check It!|assessment}(code-output-compare-501060001)

## Running locally

From project root activate the venv, complete the fill-in in the guide, and paste into **`config.yml`**. Then validate from **`level6/`**:

```bash
cd level6
python -m rasa data validate
```
