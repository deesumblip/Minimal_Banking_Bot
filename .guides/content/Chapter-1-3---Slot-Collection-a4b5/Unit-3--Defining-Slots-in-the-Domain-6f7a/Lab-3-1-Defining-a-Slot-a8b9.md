**Objective.** In this lab you will:

- Add the `account` slot and `utter_ask_account` response to your Level 3 domain
- Register the new action `action_check_balance_simple` so the agent can collect and remember an account number

You will add the action **name** to the domain here; you will **create the action file** in Lab 4.1.

**Starter reminder.** The `level3` folder already includes **`action_holiday_hours.py`** and **`action_bank_hours.py`**. When you finish Lab 3.1, **`actions:`** should list **`action_bank_hours`**, **`action_holiday_hours`**, and **`action_check_balance_simple`** so **holiday_hours** and training (e.g. Lab 6.1) stay consistent.

## Step-by-Step Instructions

**Step 1.** Open `domain/basics.yml` in the `level3` folder. You should see Level 1 responses and an `actions:` list with **`action_bank_hours`** and **`action_holiday_hours`**.

**Step 2.** Add the `slots:` section before `responses:`.

```yaml
version: "3.1"

slots:
  account:
    type: text

responses:
  # ... existing responses
```

- Use 2-space indentation
- `account:` goes under `slots:`; `type: text` goes under `account:`

**Step 3.** Add the ask response. When collecting a slot, Rasa needs a response to ask for it.

- Add `utter_ask_account` under `responses:` with the YAML below
- Naming convention: `utter_ask_<slot_name>`. For the slot `account`, the response is `utter_ask_account`


  utter_ask_account:
    - text: "What is your account number?"
      metadata:
        rephrase: True

**Step 4.** Register the new action.

- Add `action_check_balance_simple` to the `actions:` list. You will create `action_check_balance_simple.py` in Lab 4.1; for now you only add its name to the domain. Those files pair with the entries already in the starter domain.

Your `actions:` block should look like this when you are done:

```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
  - action_check_balance_simple
```

**Step 5.** Verify. Your domain should have:

- A `slots:` section with `account`
- An `utter_ask_account` response
- **`action_bank_hours`**, **`action_holiday_hours`**, and **`action_check_balance_simple`** under `actions:`
- Valid YAML and all other responses unchanged

---

## Part 1: In Codio

This lab only asks you to edit the domain file in the file tree. You do **not** need the terminal or a virtual environment for this step. Later labs use `source .venv/bin/activate` and `cd level3` when you run Rasa commands.

1. In the file tree, open **`level3/domain/basics.yml`** in the editor.
2. **Follow Steps 2–4 above** to add:
   - The `slots:` section
   - The `utter_ask_account` response
   - `action_check_balance_simple` to the `actions:` list **while keeping** `action_bank_hours` and `action_holiday_hours`
3. **Verify** as in Step 5 above.

**Use Check It!** below when done (Codio).

{Check It!|assessment}(code-output-compare-3187585640)

## Part 2: Running locally

1. Open your project in an editor. Go to the main project folder (root), activate the venv, then `cd level3`.
2. Edit `level3/domain/basics.yml`. Add:
   - `slots:` with `account` (type text)
   - `utter_ask_account` under `responses:`
   - `action_check_balance_simple` to the `actions:` list together with `action_bank_hours` and `action_holiday_hours`
3. Verify as above.

**Success criteria.** `domain/basics.yml` must contain:

- A `slots:` section with `account` (type text)
- An `utter_ask_account` response
- Under `actions:`: `action_bank_hours`, `action_holiday_hours`, and `action_check_balance_simple`
