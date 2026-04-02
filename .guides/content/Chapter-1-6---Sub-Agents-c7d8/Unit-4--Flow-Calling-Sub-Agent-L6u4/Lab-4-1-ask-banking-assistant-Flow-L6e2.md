**Objective.** Add the **`ask_banking_assistant`** flow so the main agent can **`call: banking_assistant`**. **Same pattern as Chapter 1.4 / 1.5:** fill-in-the-blanks for the full flow file, save under **`data/basics/`**, then **Code Test**.

## Step-by-Step Instructions

**Step 1.** Create **`level6/data/basics/`** if needed (it usually exists from the Level 6 starter).

**Step 2.** Complete the **Fill in the blanks** below. It includes the top-level **`flows:`** key, flow id **`ask_banking_assistant`**, **`name`**, **`description`**, and **`steps`** with **`call:`** and **`action:`**.

{Check It!|assessment}(fill-in-the-blanks-501060110)

**Step 3.** Copy your **passed** YAML into **`level6/data/basics/ask_banking_assistant.yml`**. Save. (You may refine **`description`** later for SearchReady; the fill-in gives a course-correct baseline.)

**Step 4.** **Use Check It!** below for the graded **Code Test** (Codio).

{Check It!|assessment}(code-output-compare-501060003)

## Running locally

From project root activate the venv. Paste the completed flow into **`ask_banking_assistant.yml`**, then validate from **`level6/`**:

```bash
cd level6
python -m rasa data validate
```
