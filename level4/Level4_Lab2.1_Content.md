**Objective.** In Unit 2 you saw an example of the slots, ask responses, and action registration for the transfer flow. In this lab you will add your own version to `level4/domain/basics.yml`:

- Add the slots `amount`, `recipient`, and `account_from`
- Add the ask responses `utter_ask_amount`, `utter_ask_recipient`, and `utter_ask_account_from`
- Register the new action `action_process_transfer` (you will create the .py file in Lab 3.1)

## Step-by-Step Instructions

**Step 1.** Open `domain/basics.yml` in the `level4` folder. You should see your Level 3 content (slots with account, responses, actions).

**Step 2.** Add the three new slots under the existing `slots:` section (after `account`):

```yaml
slots:
  account:
    type: text
  amount:
    type: text
  recipient:
    type: text
  account_from:
    type: text
```

Use 2-space indentation. Each slot has `type: text`.

**Step 3.** Add the three ask responses under `responses:`:

```yaml
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
```

Use **`rephrase: False`** for these three `utter_ask_*` responses. With Rasa Pro CALM + LLM command generation, **`rephrase: True` on utter_ask during slot collection** can cause the bot to fail filling the next slot (e.g. recipient names) and reply with *“I’m sorry I am unable to understand you…”*. Keep `rephrase: True` on greetings/help if you like.

Naming: `utter_ask_<slot_name>` for each slot.

**Step 4.** Add `action_process_transfer` to the `actions:` list:

```yaml
actions:
  - action_bank_hours
  - action_check_balance_simple
  - action_process_transfer
```

You will create the file `action_process_transfer.py` in Lab 3.1; here you only add its name.

**Step 5.** Verify. Your domain should have:

- `slots:` with `account`, `amount`, `recipient`, `account_from`
- `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from` under `responses:`
- `action_process_transfer` in the `actions:` list
- Valid YAML and all Level 3 content unchanged

---

## Part 1: In Codio

You do **not** need to activate the virtual environment for this lab—**Check It!** only checks your saved file.

1. **Open** `level4/domain/basics.yml` in the editor (from the file tree).
2. **Follow Steps 2–4 above** to add the three slots, the three ask responses, and `action_process_transfer` to the actions list.
3. **Verify** as in Step 5.

Run the assessment when done.

{Check It!|assessment}(code-output-compare-401020001)

## Part 2: Running locally

1. Open your project in an editor. Go to the main project folder and open `level4/domain/basics.yml` (you do not need to activate the virtual environment for this lab—**Check It!** only checks your saved file).
2. Add the three slots, the three utter_ask_* responses, and `action_process_transfer` to the actions list.
3. Verify as above. Run the assessment when done if your environment supports it.

**Success criteria.** `domain/basics.yml` must contain:

- Slots: `amount`, `recipient`, `account_from` (each type text)
- Responses: `utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`
- `action_process_transfer` in the `actions:` list
