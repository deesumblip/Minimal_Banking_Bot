In Lab 2.1 you will update the domain so the agent can collect amount, recipient, and account_from for the transfer flow.

## What You Will Add

1. **Three slots** under `slots:` (in addition to your existing `account` slot):
   - `amount` (type text)
   - `recipient` (type text)
   - `account_from` (type text)

2. **Three ask responses** under `responses:`:
   - `utter_ask_amount`, e.g. "How much would you like to transfer?"
   - `utter_ask_recipient`, e.g. "Who would you like to transfer money to?"
   - `utter_ask_account_from`, e.g. "Which account would you like to transfer from?"

3. **One new action name** in the `actions:` list:
   - `action_process_transfer`, You will create the `.py` file in Lab 3.1; here you only register the name so Rasa can call it.

## Domain Structure (concept)

After Lab 2.1 your domain will have the existing Level 3 content plus:

- Under `slots:`: `account` (from Level 3), and `amount`, `recipient`, `account_from`
- Under `responses:`: the existing utter_* and `utter_ask_account`, plus `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- Under `actions:`: `action_bank_hours`, `action_check_balance_simple`, and `action_process_transfer`

## Example: What you will add to the domain

Below is an example of the **new** pieces you will add. Your existing `slots:` already has `account`; you add the three slots below. Under `responses:` you add the three ask responses. Under `actions:` you add `action_process_transfer` (you will create the `.py` file in Lab 3.1).

**New slots (add under existing slots:):**

  amount:
    type: text
  recipient:
    type: text
  account_from:
    type: text

**New ask responses (add under responses:):**

  utter_ask_amount:
    - text: "How much would you like to transfer?"
      metadata:
        rephrase: False
  utter_ask_recipient:
    - text: "Who would you like to transfer money to?"
      metadata:
        rephrase: False
  utter_ask_account_from:
    - text: "Which account would you like to transfer from?"
      metadata:
        rephrase: False

Use **`rephrase: False`** on these three asks so prompts stay stable during slot collection (see Lab 2.1 note, `rephrase: True` here can break CALM slot filling and trigger “unable to understand you”).

**Updated actions list (include the new action):**

actions:
  - action_bank_hours
  - action_check_balance_simple
  - action_process_transfer

In **Lab 2.1** you will add your own version of these to `level4/domain/basics.yml`. When you are done, **in Codio** use **Check It!** for Lab 2.1.
