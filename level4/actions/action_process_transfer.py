from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransfer(Action):
    """A custom action that processes a money transfer using multiple slots.
    
    This demonstrates:
    - Reading multiple slots from the tracker
    - Validating slot values
    - Using all collected information to perform an action
    """

    def name(self) -> Text:
        return "action_process_transfer"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Read all the slots we need
        amount = tracker.get_slot("amount")
        recipient = tracker.get_slot("recipient")
        account_from = tracker.get_slot("account_from")
        
        # Validate that we have all required information
        if not amount or not recipient or not account_from:
            dispatcher.utter_message(
                text="I'm missing some information. Please provide amount, recipient, and source account."
            )
            return []
        
        # Check for placeholder values
        placeholder_values = ["amount", "recipient", "account number", "user_account_number"]
        if (amount.lower() in [p.lower() for p in placeholder_values] or
            recipient.lower() in [p.lower() for p in placeholder_values] or
            account_from.lower() in [p.lower() for p in placeholder_values]):
            dispatcher.utter_message(
                text="I need the actual values, not placeholders. Please provide the real amount, recipient name, and account number."
            )
            return []
        
        # Process the transfer (demo - no real transfer happening)
        dispatcher.utter_message(
            text=f"(Demo) Transfer of ${amount} from account {account_from} to {recipient} has been processed successfully."
        )
        return []
