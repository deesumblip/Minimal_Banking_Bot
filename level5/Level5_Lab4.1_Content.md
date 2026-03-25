**Objective.** In Unit 4.1 you saw examples of the transfer_money_tools flow (YAML) and the action_process_transfer_with_tools action (Python). In this lab you will create your own version: the flow file and action file following those patterns, and register the action in the domain so the LLM can call tools during this flow.

## Step-by-Step Instructions

**Step 1 — Flow file.** Create `level5/data/basics/transfer_money_tools.yml` with a flow that:
- Has a `name` and `description` (e.g. "transfer money with tools" — the description helps the LLM know when to trigger it).
- **steps:** collect amount (with description), collect recipient (with description), collect account_from (with description), then `action: action_process_transfer_with_tools`.

**Step 2 — Action file.** Create `level5/actions/action_process_transfer_with_tools.py` with a custom action class that inherits from `Action` (rasa_sdk), implements `name()` returning `"action_process_transfer_with_tools"`, and implements `run()` returning a list of events (e.g. `[]`). For this lab the action can be minimal: when this step runs, the LLM will use the registered tools in this flow step; you do not need to call the tools from inside the action. A minimal valid action looks like this:

```python
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransferWithTools(Action):
    def name(self) -> Text:
        return "action_process_transfer_with_tools"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Optional: send a message, then return. The LLM can use tools in this step.
        return []
```

**Step 3 — Domain.** Open `level5/domain/basics.yml` and add `action_process_transfer_with_tools` to the `actions:` list (alongside the existing actions).

**Step 4.** Verify: the flow file exists and has the correct steps; the action file exists and is registered in the domain.

---

## In Codio / Locally

From the project root, activate the venv, then work in `level5`:

```bash
source .venv/bin/activate   # Linux / macOS / Codio
cd level5
```

On Windows PowerShell, use `.\.venv\Scripts\Activate.ps1` before `cd level5`.

Create the flow and action files and update the domain. Run the assessment when done.

{Check It!|assessment}(code-output-compare-501040001)
