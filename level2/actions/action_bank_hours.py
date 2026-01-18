from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A simple custom action that returns bank hours.
    
    This action doesn't use any slots (memory) - it just returns
    a hardcoded message. Perfect for learning how actions work!
    """

    def name(self) -> Text:
        """Return the name of this action.
        
        This name must match what you put in domain/basics.yml
        under the 'actions:' list.
        """
        return "action_bank_hours"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """Execute the action.
        
        Args:
            dispatcher: Used to send messages back to the user
            tracker: Contains the conversation history and slots
            domain: The bot's domain configuration
            
        Returns:
            A list of events (usually empty for simple actions)
        """
        # This is where your custom logic goes!
        # For now, we just return a hardcoded message.
        dispatcher.utter_message(
            text="Our bank hours are Monday-Friday 9am-5pm, Saturday 10am-2pm. We're closed on Sundays."
        )
        return []
