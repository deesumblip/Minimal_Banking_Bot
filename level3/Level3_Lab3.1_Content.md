# Lab 3.1: Defining a Slot in the Domain

**Objective**: Add the `account` slot and `utter_ask_account` response to your Level 3 domain so the bot can collect and remember an account number.

## Part 1: In Codio

1. **Terminal**: From project root (`~/workspace`), run `source .venv/bin/activate`, then `cd level3`. Prompt should show `(.venv)` and you should be in `level3`.
2. **Open** `domain/basics.yml` in the editor.
3. **Add** the `slots:` section before `responses:` with the `account` slot (type: text). See Unit 3.1–3.2.
4. **Add** the `utter_ask_account` response under `responses:` (e.g. "What is your account number?").
5. **Verify**: YAML is valid; all Level 2 content remains; `slots:` and `utter_ask_account` are present.

Run the assessment when done.

## Part 2: Running locally

1. Open your project in an editor. Go to the **main project folder** (root), activate the venv (e.g. `source .venv/bin/activate` or Windows `.venv\Scripts\Activate.ps1`), then `cd level3`.
2. Edit `level3/domain/basics.yml`: add `slots:` with `account` (type: text) and `utter_ask_account` under `responses:`.
3. Verify as above. Run the assessment when done (if your environment supports it).

**Success criteria**: `domain/basics.yml` contains a `slots:` section with `account` (type: text) and a `utter_ask_account` response.
