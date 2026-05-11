from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessTransfer(Action):
    """A custom action that processes a money transfer using multiple slots."""

    def name(self) -> Text:
        return "action_process_transfer"

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
        
        dispatcher.utter_message(
            text=f"Transfer of ${amount} from account {account_from} to {recipient} has been processed successfully."
        )
        return []
