**Objective**: Train your bot and verify it works.

## Part 1: In Codio

1. **Terminal**: Open **Tools** → **Terminal**. Go to the `level1` folder: `cd level1`. Confirm with `pwd` (path should end in `level1`).
2. **Virtual environment**: Run `ls -la .venv`. If it exists: `source .venv/bin/activate`. If not: `python3.11 -m venv .venv` then `source .venv/bin/activate`. Prompt should show `(.venv)`.
3. **Rasa**: Run `python -m rasa --version`. If error, install: `python -m pip install --no-cache-dir rasa-pro`.
4. **Train**: From `level1` with venv active: `python -m rasa train`. Wait for "Successfully saved model" (1–3 minutes).
5. **Verify**: Terminal shows "Successfully saved model to 'models/...'". In the file tree, `level1/models/` should contain a new `.tar.gz` file.

**Common errors**: YAML syntax → use 2 spaces, colons, dashes. Response not found → add response in domain or fix flow typo. No module 'rasa' → activate venv, install rasa-pro. RASA_LICENSE/OPENAI_API_KEY not set → check Lab 0.1 step 5 or ask instructor.

## Part 2: Running locally

Same steps as above, but: use your OS terminal; on Windows use `.venv\Scripts\Activate.ps1` or `activate.bat`. Create a `.env` in the same folder as `config.yml` with `RASA_LICENSE=...` and `OPENAI_API_KEY=...` (no quotes). Run `python -m rasa train` from that folder.

**Success criteria**: Training completes with no errors; a new model file appears in `models/`. Run the assessment when done.
