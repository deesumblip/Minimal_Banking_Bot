# 4.3 Creating the Flow

Now that you've seen how collection works, you'll learn how to build it. In **Lab 4.1** you'll create the `check_balance` flow. That flow will do two things. It will collect the `account` slot so the bot asks for it when it's missing. Then it will run the action `action_check_balance_simple`, which reads the slot and returns a balance.

You already defined the `account` slot and `utter_ask_account` and registered `action_check_balance_simple` in Lab 3.1. In Lab 4.1 you'll create the flow file and follow the steps.
