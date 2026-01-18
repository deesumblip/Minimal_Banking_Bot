from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalanceSimple(Action):
    """A deliberately tiny custom action for learning.

    - Reads a slot ('account')
    - Returns a deterministic response (no DB, no external calls)
    """

    def name(self) -> Text:
        return "action_check_balance_simple"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        account = tracker.get_slot("account") or "<missing>"
        dispatcher.utter_message(text=f"(Demo) Balance for account {account} is $123.45.")
        return []

