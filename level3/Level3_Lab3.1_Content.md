# Lab 3.1: Defining a Slot in the Domain

**Objective**: Add the `account` slot and `utter_ask_account` response to your Level 3 domain so the bot can collect and remember an account number.

## Step-by-Step Instructions

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

---

## Part 1: In Codio

1. **Terminal**: From project root (`~/workspace`), run `source .venv/bin/activate`, then `cd level3`. Prompt should show `(.venv)` and you should be in `level3`.
2. **Open** `domain/basics.yml` in the editor.
3. **Follow Steps 2–3 above** to add the `slots:` section and `utter_ask_account` response.
4. **Verify** as in Step 4 above.

Run the assessment when done.

## Part 2: Running locally

1. Open your project in an editor. Go to the **main project folder** (root), activate the venv (e.g. `source .venv/bin/activate` or Windows `.venv\Scripts\Activate.ps1`), then `cd level3`.
2. Edit `level3/domain/basics.yml`: add `slots:` with `account` (type: text) and `utter_ask_account` under `responses:`.
3. Verify as above. Run the assessment when done (if your environment supports it).

**Success criteria**: `domain/basics.yml` contains a `slots:` section with `account` (type: text) and a `utter_ask_account` response.
