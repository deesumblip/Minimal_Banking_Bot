Level 3 introduces **slots**, the bot's memory. This enables remembering information from the conversation, storing user-provided data (like account numbers), asking for missing information, and using stored information in actions.

Your existing Level 2 bot continues to work. Level 3 adds memory on top of it.

## What's New in Level 3

**What you'll add in Lab 3.1.** In the domain you will add the `slots:` section with the `account` slot, the new response `utter_ask_account` (used when asking for the account number), and you will register the new action `action_check_balance_simple` in the `actions:` list. The action file is already in `level3/actions/`; you only add it to the domain.

**What you'll create in Lab 4.1.** You will create the flow file `data/basics/check_balance.yml`. That flow will collect the account number and then run `action_check_balance_simple`.

**Provided file.** The file `actions/action_check_balance_simple.py` is already in the project. You will register it in the domain in Lab 3.1 and explore how it works in Lab 5.1.

**Unchanged.** All Level 2 responses, flows, and actions remain. You are building Level 3 by adding these pieces to your Level 2 bot.
