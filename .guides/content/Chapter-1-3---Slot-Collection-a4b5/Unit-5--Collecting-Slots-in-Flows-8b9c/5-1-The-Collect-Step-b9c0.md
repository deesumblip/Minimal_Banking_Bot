A flow can ask for information before running an action using a **collect step**. You saw how this works in **Unit 1.3**: the step tells Rasa to get the slot value before continuing; if the slot is empty, Rasa asks using `utter_ask_*`; once the slot has a value, the flow continues. In **Lab 5.1** you will add this step to your first flow.

## Syntax


steps:
  - collect: account
    description: "account number"

- **`collect: account`**. The slot to collect.
- **`description:`**. Helps the LLM understand what to extract. Optional, but recommended.

{Check It!|assessment}(multiple-choice-2502214147)
{Check It!|assessment}(fill-in-the-blanks-1454903744)
