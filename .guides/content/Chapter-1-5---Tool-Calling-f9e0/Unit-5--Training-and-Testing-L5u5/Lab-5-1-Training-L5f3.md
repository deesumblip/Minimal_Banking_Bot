**Objective.** In this lab you will train the Level 5 bot from the `level5` folder so that the model includes your domain, flows, and tool registration.

## Step-by-Step Instructions

**Step 1.** From **project root**, activate the virtual environment (`source .venv/bin/activate` on Linux/macOS or `.\.venv\Scripts\Activate.ps1` on Windows).

**Step 2.** Change to the level5 folder: `cd level5`.

**Step 3.** Run: `rasa train`.

**Step 4.** Confirm that training completes without errors and that a model is written to `level5/models/` (or the configured output path).

**Step 5.** **In Codio**, use **Check It!** below. The grader will check that training can be run from level5 (or that the required files and config are present so training would succeed).

{Check It!|assessment}(code-output-compare-501050001)
