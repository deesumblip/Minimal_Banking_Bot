# Lab 3.1: Defining a Slot in the Domain

**Objective.** Add the `account` slot and `utter_ask_account` response to your Level 3 domain, and register the new action `action_check_balance_simple`, so the bot can collect and remember an account number. The action file is already in `level3/actions/`; you will add it to the domain here.

## Step-by-Step Instructions

**Step 1.** Open `domain/basics.yml` in the `level3` folder. You should see your Level 2 content (responses and actions).

**Step 2.** Add the `slots:` section before `responses:`.

```yaml
version: "3.1"

slots:
  account:
    type: text

responses:
  # ... existing responses
```

Use 2-space indentation. `account:` is under `slots:`; `type: text` is under `account:`.

**Step 3.** Add the ask response. When collecting a slot, Rasa needs a response to ask for it. Add `utter_ask_account` under `responses:`.

```yaml
  utter_ask_account:
    - text: "What is your account number?"
      metadata:
        rephrase: True
```

The naming convention is `utter_ask_<slot_name>`. For the slot `account`, the response is `utter_ask_account`.

**Step 4.** Register the new action. Add `action_check_balance_simple` to the `actions:` list in the domain. The file `actions/action_check_balance_simple.py` is already in the project; you are only adding its name to the domain so Rasa can use it.

Example: under `actions:` add a line so the list includes both your Level 2 actions and the new one, for example:

```yaml
actions:
  - action_bank_hours
  - action_check_balance_simple
```

(If your domain already lists `action_holiday_hours`, keep it and add `action_check_balance_simple` as well.)

**Step 5.** Verify. The domain has a `slots:` section with `account`, an `utter_ask_account` response, and `action_check_balance_simple` in the `actions:` list. All Level 2 content remains and the YAML is valid.

---

## Part 1: In Codio

1. **Terminal.** From project root (`~/workspace`), run `source .venv/bin/activate`, then `cd level3`. The prompt should show `(.venv)` and you should be in `level3`.
2. **Open** `domain/basics.yml` in the editor.
3. **Follow Steps 2–4 above** to add the `slots:` section, `utter_ask_account` response, and `action_check_balance_simple` to the `actions:` list.
4. **Verify** as in Step 5 above.

Run the assessment when done.

## Part 2: Running locally

1. Open your project in an editor. Go to the main project folder (root), activate the venv, then `cd level3`.
2. Edit `level3/domain/basics.yml`. Add `slots:` with `account` (type text), add `utter_ask_account` under `responses:`, and add `action_check_balance_simple` to the `actions:` list.
3. Verify as above. Run the assessment when done if your environment supports it.

**Success criteria.** `domain/basics.yml` contains a `slots:` section with `account` (type text), an `utter_ask_account` response, and `action_check_balance_simple` in the `actions:` list.
