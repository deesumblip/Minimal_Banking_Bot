from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalanceSimple(Action):
    """A custom action that reads a slot and returns a balance."""

    def name(self) -> Text:
        return "action_check_balance_simple"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        account = tracker.get_slot("account") or "<missing>"
        
        placeholder_values = ["account number", "user_account_number", "<missing>"]
        if account.lower() in [p.lower() for p in placeholder_values]:
            dispatcher.utter_message(response="utter_ask_account")
            return []
        
        dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")
        return []
