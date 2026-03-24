**Objective.** In this lab you will run a completion check to verify that your Level 5 agent has all required components: tools folder and banking_tools.py, tools registration in endpoints.yml, transfer_money_tools flow, action_process_transfer_with_tools action and domain registration, and a trained model (or readiness to train).

## Step-by-Step Instructions

**Step 1.** Ensure you have completed Labs 2.1, 3.1, 4.1, and 5.1: tools folder, endpoints tools section, flow and action, and training.

**Step 2.** Optionally run the assistant: start the action server (`rasa run actions`) in one terminal and Rasa (`rasa run` or `rasa inspect`) in another. Open Inspector and trigger the transfer_money_tools flow; confirm the agent collects slots and that tool calling works (e.g. you get a balance or transfer confirmation).

**Step 3.** Run the assessment.

{Check It!|assessment}(code-output-compare-501050002)

The grader will verify the presence and validity of: level5/tools/, level5/tools/banking_tools.py with __all__, level5/endpoints.yml with tools section, level5/data/basics/transfer_money_tools.yml, level5/actions/action_process_transfer_with_tools.py, level5/domain/basics.yml with action_process_transfer_with_tools in actions, and optionally level5/models/ or successful train.
