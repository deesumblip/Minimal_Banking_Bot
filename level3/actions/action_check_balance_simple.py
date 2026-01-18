from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalanceSimple(Action):
    """A custom action that reads a slot and returns a balance.
    
    This demonstrates:
    - How to read slots (conversation memory) from the tracker
    - How to handle placeholder values that the LLM might extract incorrectly
    - How to re-prompt the user if needed
    """

    def name(self) -> Text:
        return "action_check_balance_simple"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Read the 'account' slot from conversation memory
        account = tracker.get_slot("account") or "<missing>"
        
        # Check if the account is a placeholder value
        # Sometimes the LLM extracts "account number" or "user_account_number"
        # as the value, which isn't a real account number
        placeholder_values = ["account number", "user_account_number", "<missing>"]
        if account.lower() in [p.lower() for p in placeholder_values]:
            # Ask for the account number instead
            dispatcher.utter_message(response="utter_ask_account")
            return []
        
        # If we have a real account number, show the balance
        dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")
        return []
