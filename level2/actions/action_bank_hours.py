from datetime import datetime
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A custom action that returns bank hours based on the current day.
    
    Uses datetime to tailor the message—this can't be done with a simple
    utter response because the message changes depending on when the user asks.
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
        
        Returns different messages based on the current day of the week.
        """
        weekday = datetime.now().weekday()  # 0=Monday, 5=Saturday, 6=Sunday

        if weekday == 6:  # Sunday
            message = "Today is Sunday—we're closed."
        elif weekday == 5:  # Saturday
            message = "Today is Saturday—we're open 10am-2pm."
        else:  # Monday–Friday
            message = (
                "Our bank hours are Monday-Friday 9am-5pm, "
                "Saturday 10am-2pm. We're closed on Sundays."
            )

        dispatcher.utter_message(text=message)
        return []
