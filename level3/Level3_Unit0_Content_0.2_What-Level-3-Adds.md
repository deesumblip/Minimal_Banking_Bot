Level 3 adds **slots**. A slot is a named place in the domain where Rasa can store something the user said so the bot can use it again later.

Your Level 2 bot still works. You are only adding memory on top of what you already have.

You will work in a fixed order on purpose. First you change the **domain** so Rasa knows about the new slot and the new action name. Next you **write the action** that reads the slot. Last you **add the flow** that collects the slot before it runs that action. That order lets you understand the action on its own before you connect it to a flow.

## What you will add

### Lab 3.1: domain

You will update `domain/basics.yml` in the `level3` folder.

- Add a `slots:` section with an `account` slot.
- Add the response `utter_ask_account` so the bot can ask for the account number when the slot is empty.
- Add `action_check_balance_simple` to the `actions:` list. You will create the matching Python file in Lab 4.1.

### Lab 4.1: action

You will create `level3/actions/action_check_balance_simple.py`. That action reads the `account` slot from the tracker and handles placeholder values the model might fill in by mistake.

### Lab 5.1: flow

You will create `level3/data/basics/check_balance.yml`. The flow will collect the account number into the slot, then run `action_check_balance_simple`.

### What stays the same

All Level 2 responses, flows, and actions stay in your project. Level 3 only adds the items above.
