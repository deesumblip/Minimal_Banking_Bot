A flow can ask for information before running an action using a **collect step**. **Section 1.3 (Slot collection)** in this chapter explained the behavior: the step tells Rasa to obtain the slot value before continuing. If the slot is empty, Rasa asks using the matching `utter_ask_*` response. Once the slot has a value, the flow continues. In **Lab 5.1** you will add this step to your first flow.

## Syntax

```yaml
steps:
  - collect: account
    description: "account number"
```

- **`collect: account`**: The slot to fill.
- **`description:`**: Helps the LLM understand what to extract. Optional, but recommended.

{Check It!|assessment}(multiple-choice-2502214147)
{Check It!|assessment}(fill-in-the-blanks-1454903744)
