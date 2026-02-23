Level 3 adds **slots**: the bot's memory. With slots, your bot will be able to remember what the user said, store it, and use it later.

Your Level 2 bot will still work. You will just add memory on top.

You will implement in this order: **domain** (Lab 3.1), then **the action that uses the slot** (Lab 4.1), then **the flow that collects it** (Lab 5.1). That way you see how the action works before you wire it into a flow.

## What You'll Add

**In Lab 3.1** you will update the domain:

- Add a `slots:` section with the `account` slot
- Add the response `utter_ask_account` so the bot can ask for the account number
- Add `action_check_balance_simple` to the `actions:` list (you will create the Python file in Lab 4.1)

**In Lab 4.1** you will **write** the action that uses the slot. **In Lab 5.1** you will create the flow file `data/basics/check_balance.yml`. That flow will collect the account number, then run `action_check_balance_simple`.

**In Lab 3.1** you add the action **name** to the domain; in **Lab 4.1** you will **write** the action file `action_check_balance_simple.py`.

**Unchanged.** All your Level 2 responses, flows, and actions will stay as they are. You will build Level 3 by adding these pieces.
