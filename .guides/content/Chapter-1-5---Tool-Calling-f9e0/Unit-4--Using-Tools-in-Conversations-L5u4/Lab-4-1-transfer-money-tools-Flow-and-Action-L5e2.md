**Starting point:** Work in **`level5/`** with **Labs 2.0–3.1** complete (**`prompt_template`**, **`data/prompts/`**, **`tools/banking_tools.py`**, **`tools:`** in **`endpoints.yml`**).

**Objective.** Add the **`transfer_money_tools`** flow, the **`action_process_transfer_with_tools`** custom action, and **domain** updates so the LLM can fill **`amount`**, **`recipient`**, and **`account_from`** while that flow runs, then execute the action step. You create every artifact: a **fill-in-the-blanks** exercise for **domain slot conditions**, pasted **YAML** for the **flow**, and **Python** for the **action** (or your own equivalent that satisfies the grader).

You do **not** need the venv for the fill-in-the-blanks; you need it when you **train** later in the chapter.

---

## Why the domain step matters

Chapter 1.4 already maps **`amount`**, **`recipient`**, and **`account_from`** when **`transfer_money`** is active (in this repo’s **`level5/`** baseline, that means **`from_llm`** + **`active_flow: transfer_money`**—see **`level5/domain/basics.yml`** if your hand-built **`level4/`** domain used only plain **`type: text`** slots). **`transfer_money_tools`** reuses those slot names. Each **`from_llm`** mapping needs a **`conditions`** entry with **`active_flow: transfer_money_tools`** as well. Without it, slot updates can fail while **`transfer_money_tools`** is running.

---

## Part A — Domain slot conditions (fill in the blanks)

Complete the exercise, then open **`level5/domain/basics.yml`** and align the **`amount`**, **`recipient`**, and **`account_from`** blocks with your answers (so **`transfer_money`** and **`transfer_money_tools`** both appear under **`conditions`**). If the file already matches, skim to confirm.

{Check It!|assessment}(fill-in-the-blanks-501040010)

---

## Part B — Register the action name in the domain

In **`level5/domain/basics.yml`**, under **`actions:`**, add **`action_process_transfer_with_tools`** if it is missing—keep all existing action names.

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

Save the file. Tools stay registered in **`endpoints.yml`**; the flow lists only the **action** step, not individual tool names.

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

**In Codio**, run **Check It!** below when Parts A–D are saved. The grader checks flow YAML, the action, the domain **`actions:`** list, and **`from_llm`** conditions for **`transfer_money_tools`**.

{Check It!|assessment}(code-output-compare-501040001)

---

## Running locally

From project root, activate the venv, then **`cd level5`**. After Parts A–D, run **`python -m rasa train`** in **Lab 5.1**. On Windows PowerShell, use **`.\.venv\Scripts\Activate.ps1`** before **`cd level5`**.

---

**Success criteria.** Fill-in-the-blanks passed, code test **10/10**, then go to **Unit 5** (training and testing).
