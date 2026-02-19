You will do this in **Lab 3.1: Defining a Slot in the Domain**. The steps below are the detailed walkthrough for that lab.

**Step 1:** Open `domain/basics.yml` (in the `level3` folder). You should see your Level 2 content (responses and actions).

**Step 2:** Add the `slots:` section before `responses:`:

```yaml
version: "3.1"

slots:
  account:
    type: text

responses:
  # ... existing responses
```

Important: `slots:` and `account:` and `type: text` use 2-space indentation. `account:` is under `slots:`; `type: text` is under `account:`.

**Step 3:** Add the ask response. When collecting a slot, Rasa needs a response to ask for it. Add `utter_ask_account` under `responses:`:

```yaml
  utter_ask_account:
    - text: "What is your account number?"
      metadata:
        rephrase: True
```

**Naming convention**: `utter_ask_<slot_name>` — e.g. slot `account` → response `utter_ask_account`.

**Step 4:** Verify: `slots:` with `account`, `utter_ask_account` exists, all Level 2 content remains, YAML is valid.
