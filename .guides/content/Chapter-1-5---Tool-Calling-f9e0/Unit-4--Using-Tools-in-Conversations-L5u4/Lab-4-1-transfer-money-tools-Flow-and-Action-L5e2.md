**Starting point:** Work in **`level5/`** with **Labs 2.0–3.1** complete (**`prompt_template`** + **`data/prompts/`**, **`tools/banking_tools.py`**, **`tools:`** in **`endpoints.yml`**).

**Objective.** Add the **`transfer_money_tools`** flow, the **`action_process_transfer_with_tools`** custom action, and the **domain** updates so the LLM can fill **`amount`**, **`recipient`**, and **`account_from`** when that flow is active, then run the action step. Nothing in this lab appears without you creating or editing it: you will use a **fill-in-the-blanks** exercise for the **domain slot conditions**, paste **structured YAML** for the **flow**, and paste **Python** for the **action** (you may type it yourself if you prefer, as long as it matches the grader).

You do **not** need the virtual environment for the **fill-in-the-blanks** exercise; you need it for **training** later in the chapter.

---

## Why the domain step matters

Chapter 1.4 already maps **`amount`**, **`recipient`**, and **`account_from`** when the active flow is **`transfer_money`**. The new flow **`transfer_money_tools`** uses the **same** slot names. For **`from_llm`** mappings with **`conditions`**, each of those three slots must also list **`active_flow: transfer_money_tools`**. Without that line, the assistant may not set slots correctly while the new flow is running.

---

## Part A — Domain slot conditions (fill in the blanks)

Complete the exercise below. Then open **`level5/domain/basics.yml`** and ensure the **`slots`** section for **`amount`**, **`recipient`**, and **`account_from`** matches your answers (merge or replace those three blocks so **`transfer_money`** and **`transfer_money_tools`** both appear under **`conditions`**). If your file already matched the completed exercise, you only need to confirm it.

{Check It!|assessment}(fill-in-the-blanks-501040010)

---

## Part B — Register the action name in the domain

In **`level5/domain/basics.yml`**, under **`actions:`**, add **`action_process_transfer_with_tools`** if it is not already listed (keep every existing action in the list).

---

## Part C — Create the flow file

Create **`level5/data/basics/transfer_money_tools.yml`** with the following content. The flow **`id`** (**`transfer_money_tools`**) must match the **`active_flow`** values you set in Part A. The **`collect:`** descriptions help the LLM fill slots in one turn when the user already gave part of the information.

```yaml
flows:
  transfer_money_tools:
    name: transfer money with tools
    description: |
      Demonstrates tool calling in a flow.
      The agent collects the necessary information, then the LLM
      can dynamically decide to call tools (like check_balance
      or process_transfer) based on the conversation context.
    steps:
      - collect: amount
        description: |
          The transfer amount in dollars. Extract from this message if the user already said it
          (same turn as starting the flow). Accept digits with or without $; commas may appear;
          phrases like "hundred" or "twenty dollars" are acceptable.
      - collect: recipient
        description: |
          Name or account identifier of who receives the money. Short reply (e.g. "Jamie" or an account number).
          Extract from this turn if they already named the recipient.
      - collect: account_from
        description: |
          Source account number or ID the money is sent from. Digits or short label;
          extract from this turn if the user already gave the source account.
      - action: action_process_transfer_with_tools
```

Save the file. (Tools remain registered in **`endpoints.yml`**; the flow does not list tool names—only the action step.)

---

## Part D — Create the custom action

Create **`level5/actions/action_process_transfer_with_tools.py`**. The grader expects a real **`run()`** that reads **`amount`**, **`recipient`**, and **`account_from`** from the tracker and sends at least one **`dispatcher.utter_message`** (for example a short demo confirmation). Use the script below as your reference implementation, or type an equivalent yourself.

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransferWithTools(Action):
    """Custom action used with registered tools in endpoints.yml."""

    def name(self) -> Text:
        return "action_process_transfer_with_tools"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        amount = tracker.get_slot("amount")
        recipient = tracker.get_slot("recipient")
        account_from = tracker.get_slot("account_from")

        if not amount or not recipient or not account_from:
            dispatcher.utter_message(
                text="I'm missing some information. Please provide amount, recipient, and source account."
            )
            return []

        placeholder_values = ["amount", "recipient", "account number", "user_account_number"]
        if (
            amount.lower() in [p.lower() for p in placeholder_values]
            or recipient.lower() in [p.lower() for p in placeholder_values]
            or account_from.lower() in [p.lower() for p in placeholder_values]
        ):
            dispatcher.utter_message(
                text="I need the actual values, not placeholders. Please provide the real amount, recipient name, and account number."
            )
            return []

        dispatcher.utter_message(
            text=(
                f"(Demo with Tools) Transfer of ${amount} from account {account_from} to {recipient} "
                "has been processed successfully. Tools are available for dynamic operations."
            )
        )
        return []
```

Save the file.

---

## Part E — Run the code assessment

**In Codio**, use **Check It!** below when Parts A–D are saved. The grader checks the flow YAML, the action implementation, the domain **`actions:`** list, and the **`from_llm`** slot conditions for **`transfer_money_tools`**.

{Check It!|assessment}(code-output-compare-501040001)

---

## Running locally

From the project root, activate the venv, then **`cd level5`**. Complete Parts A–D, then run **`python -m rasa train`** when you reach **Lab 5.1**. (On Windows PowerShell, use **`.\.venv\Scripts\Activate.ps1`** before **`cd level5`**.)

---

**Success criteria.** Fill-in-the-blanks passed, code test **10/10**, then continue to **Unit 5** (training and testing).
