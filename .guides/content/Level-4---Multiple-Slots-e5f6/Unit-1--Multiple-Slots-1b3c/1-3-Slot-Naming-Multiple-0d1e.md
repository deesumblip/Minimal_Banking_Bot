Each slot needs a matching ask response in the domain. The convention is `utter_ask_<slot_name>`:
 
| Slot | Ask response | Status in Level 4 |
|---|---|---|
| `account` | `utter_ask_account` | Already exists from Level 3 |
| `amount` | `utter_ask_amount` | New in Level 4 |
| `recipient` | `utter_ask_recipient` | New in Level 4 |
 
The action reads each slot by the same name with `tracker.get_slot("<slot_name>")`. A mismatch between the slot name in the domain, the flow, and the action is the most common source of broken behavior.