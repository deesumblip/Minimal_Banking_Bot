Level 3 adds **slots**: the bot's memory. With slots, your bot will be able to remember what the user said, store it, and use it later.

Your Level 2 bot will still work. You will just add memory on top.

## What You'll Add

**In Lab 3.1** you will update the domain:

- Add a `slots:` section with the `account` slot
- Add the response `utter_ask_account` so the bot can ask for the account number
- Add `action_check_balance_simple` to the `actions:` list (the Python file is already in the project)

**In Lab 4.1** you will create the flow file `data/basics/check_balance.yml`. That flow will collect the account number, then run `action_check_balance_simple`.

**Already provided.** The file `action_check_balance_simple.py` is in `level3/actions/`. You will register it in the domain; you won't write it. You'll explore how it works in Lab 5.1.

**Unchanged.** All your Level 2 responses, flows, and actions will stay as they are. You will build Level 3 by adding these pieces.
