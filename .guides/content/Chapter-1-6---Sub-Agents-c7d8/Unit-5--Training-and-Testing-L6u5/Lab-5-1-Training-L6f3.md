**Objective.** In Unit 5 you saw how to train the Level 6 agent. In this lab you will train from the `level6` folder, then **in Codio** use **Check It!** to submit the graded check.

## Step-by-Step Instructions

**Step 1.** From project root, activate the venv:

```bash
# Codio / Linux / macOS
source .venv/bin/activate

# Windows (PowerShell or CMD, from project root)
# .venv\Scripts\activate
```

**Step 2–3.** Train from **`level6/`**:

```bash
cd level6
rasa train
```

Wait for the model to be written to `level6/models/`.

**Step 4.** **In Codio**, use **Check It!** below. The grader will verify that training completed (e.g. model directory or success indicator).

{Check It!|assessment}(code-output-compare-501060004)

## Running locally

Same steps as **Steps 1–3** above when training locally. (Graded **Check It!** runs in the Codio guide, not on a local-only machine.)
