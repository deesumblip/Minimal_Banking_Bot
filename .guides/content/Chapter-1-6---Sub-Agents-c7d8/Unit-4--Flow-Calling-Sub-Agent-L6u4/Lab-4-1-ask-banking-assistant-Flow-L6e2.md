**Objective.** In Unit 4 you saw an example of the ask_banking_assistant flow (YAML with `call: banking_assistant` and a follow-up action). In this lab you will create your own version: the file `level6/data/basics/ask_banking_assistant.yml` with a flow that calls the banking_assistant sub-agent, then (optionally) an action such as utter_help.

## Step-by-Step Instructions

**Step 1.** Create `level6/data/basics/ask_banking_assistant.yml` (create the `data/basics/` directory if needed).

**Step 2.** Add a flow with:
- **name** and **description** (e.g. "ask banking assistant" — the description helps the LLM know when to trigger it).
- **steps:** at least one step `call: banking_assistant`, and optionally a follow-up step (e.g. `action: utter_help`).

**Step 3.** Verify: the file exists and the flow has `call: banking_assistant` (name must match the sub-agent from Lab 2.1). Run the assessment when done.

{Check It!|assessment}(code-output-compare-501060003)

## Running locally

From project root activate the venv, `cd level6`. Create the flow file as above. Run the assessment when done.
