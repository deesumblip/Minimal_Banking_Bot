from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransferWithTools(Action):
    """A custom action that works with tools.
    
    This demonstrates how actions can work alongside tool calling.
    The LLM can dynamically decide to call tools (like check_balance
    or process_transfer) based on the conversation context.
    """

    def name(self) -> Text:
        return "action_process_transfer_with_tools"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # This action can work with tools registered in endpoints.yml
        # The LLM will decide when to call tools based on the conversation
        
        amount = tracker.get_slot("amount")
        recipient = tracker.get_slot("recipient")
        account_from = tracker.get_slot("account_from")
        
        if not amount or not recipient or not account_from:
            dispatcher.utter_message(
                text="I'm missing some information. Please provide amount, recipient, and source account."
            )
            return []
        
        placeholder_values = ["amount", "recipient", "account number", "user_account_number"]
        if (amount.lower() in [p.lower() for p in placeholder_values] or
            recipient.lower() in [p.lower() for p in placeholder_values] or
            account_from.lower() in [p.lower() for p in placeholder_values]):
            dispatcher.utter_message(
                text="I need the actual values, not placeholders. Please provide the real amount, recipient name, and account number."
            )
            return []
        
        # In a real implementation, this action might call tools here
        # For now, we'll just show a message indicating tools are available
        dispatcher.utter_message(
            text=f"(Demo with Tools) Transfer of ${amount} from account {account_from} to {recipient} has been processed successfully. Tools are available for dynamic operations."
        )
        return []
