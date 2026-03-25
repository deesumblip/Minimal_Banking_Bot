**Starting point:** Chapter 1.4 assumes you begin with the **final banking agent at the end of Chapter 1.3** (your **`level3/`** project). You **add** work in **`level4/`**—see **`Level4_Unit0_Content_0.1_Your-Level-3-Banking-Agent.md`** and **`Level4_Unit0_Content_0.2_What-Level-4-Adds.md`**.

The order in which you list `collect:` steps in the flow is the order in which the agent will ask for values.

## Flow Steps Define the Order

In `transfer_money.yml` you will add steps like:

1. `collect: amount` — Agent asks for the amount first (using `utter_ask_amount`).
2. `collect: recipient` — Then asks who to send it to (`utter_ask_recipient`).
3. `collect: account_from` — Then asks which account to use (`utter_ask_account_from`).
4. `action: action_process_transfer` — Finally runs the action, which reads all three slots.

Rasa uses the **order of steps** to decide which slot to ask for next when one is still empty. So the order of your `collect:` steps should match what makes sense for the user (e.g. amount → recipient → source account) and match what your action expects (amount, recipient, account_from).

## Same Convention as Level 3

- Each collected slot needs a matching **response** in the domain: `utter_ask_<slot_name>` (e.g. `utter_ask_amount` for the `amount` slot).
- The action runs only after all collected slots have values (or after the user has been asked for each one in order).

In Lab 4.1 you will create the flow with the three collect steps in this order, then the action step.
