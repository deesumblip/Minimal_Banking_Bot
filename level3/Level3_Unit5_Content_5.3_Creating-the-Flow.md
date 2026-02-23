# 5.3 Creating the Flow

In the previous unit you wrote `action_check_balance_simple`, which reads the slot. Now you will create the flow that collects the slot and runs that action.

In **Lab 5.1** you will create the `check_balance` flow. That flow will collect the `account` slot so the bot asks for it when it's missing, then run `action_check_balance_simple`, which reads the slot and returns a balance.

You already defined the `account` slot and `utter_ask_account` and registered `action_check_balance_simple` in Lab 3.1, and you **wrote** the action in Lab 4.1. In Lab 5.1 you will create the flow file and follow the steps.
