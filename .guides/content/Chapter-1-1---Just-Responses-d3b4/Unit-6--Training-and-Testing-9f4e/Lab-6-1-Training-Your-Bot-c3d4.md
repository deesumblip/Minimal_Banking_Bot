**Objective**: Train your bot and verify it works.

## Part 1: In Codio

1. **Virtual environment**: In the terminal window (it opens at `~/workspace`; your prompt may show `~/workspace$`), go to the main project folder (the one that contains `level1`, `level2`, and `.guides`). Run `ls -la .venv`. If it exists: `source .venv/bin/activate`. If not: `python3.11 -m venv .venv` then `source .venv/bin/activate`. Prompt should show `(.venv)`.
2. **Navigate to level1**: Go to the `level1` folder: `cd level1`. Confirm with `pwd` (path should end in `level1`).
3. **Rasa**: Run `python -m rasa --version`. If error, install: `python -m pip install --no-cache-dir rasa-pro`.
4. **Train**: From `level1` with venv active: `python -m rasa train`. Wait for "Successfully saved model" (1–3 minutes).
5. **Verify**: Terminal shows "Successfully saved model to 'models/...'". In the file tree, `level1/models/` should contain a new `.tar.gz` file.

**Common errors**: YAML syntax → use 2 spaces, colons, dashes. Response not found → add response in domain or fix flow typo. No module 'rasa' → activate venv, install rasa-pro. RASA_LICENSE not set → check Lab 0.1 (set RASA_LICENSE) or ask instructor.

Run the assessment when done.

## Part 2: Running locally

Follow the same logic as Part 1, but use your own terminal and OS-specific commands.

1. **Open a terminal** (PowerShell, Command Prompt, or Terminal.app / your Linux terminal).
2. **Go to the main project folder** (the one that contains `level1`, `level2`, and `.guides`).  
   Example: `cd C:\Users\You\Minimal_Banking_Bot` or `cd ~/Minimal_Banking_Bot`.
3. **Activate the virtual environment** (the `.venv` folder is in the main project folder):
   - **Windows (PowerShell)**: `.venv\Scripts\Activate.ps1`
   - **Windows (Command Prompt)**: `.venv\Scripts\activate.bat`
   - **macOS / Linux**: `source .venv/bin/activate`  
   Your prompt should show `(.venv)`.
4. **Navigate to level1**: Go to the `level1` folder: `cd level1` (the one that contains `config.yml`, `domain/`, and `data/`).
5. **Ensure RASA_LICENSE is set**: Create a `.env` file in the **project root** (folder containing `level1`) with `RASA_LICENSE=your-license-key` (no quotes), then source it from root before `cd level1`. Or see Lab 0.1 for Codio vs local (Windows/macOS/Linux).
6. **Train**: With venv active and from the `level1` folder, run: `python -m rasa train`. Wait for "Successfully saved model".
7. **Verify**: A new `.tar.gz` file appears in `level1/models/`.

**Success criteria**: Training completes with no errors; a new model file appears in `models/`.
