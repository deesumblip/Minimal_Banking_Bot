**Objective**: Create a virtual environment in the **project root**, install Rasa Pro in it, set up **your own** Rasa Pro license (`RASA_LICENSE`), and verify the installation.

**Important**: This is your first step! You must create a virtual environment, install Rasa Pro, and set your **own** Rasa Pro license before you can proceed. This course uses only **RASA_LICENSE** (no OpenAI API key required).

---

> **📌 Create the virtual environment from the root folder first**  
> The terminal opens at the **project root** (the folder that contains `level1`, `level2`, and `.guides`). Create the virtual environment **there**; only **then** go into `level1` for the rest of this lab. One `.venv` in the root is used for **all levels** — do not create a separate venv inside `level1` or any other level folder.

---

**Before you start**: Open a terminal. Stay in the **project root** for Steps 1–3 (create venv, install Rasa, verify). You will set up your license and check project structure in Steps 4–5.

**Order of operations:** 1. Root → create venv & activate → 2. Root → install Rasa Pro → 3. Root → verify (`rasa --version`) → 4. Set **your own** `RASA_LICENSE` (see Codio vs Local below) → 5. Check project structure in `level1`.

#### Steps

1. **Create a Virtual Environment (in the project root)**
   
   In the terminal, make sure you're in the **main project folder** (run `pwd`; you should see a path that does **not** end in `level1`). Then check that Python 3.11 is installed:
   ```bash
   python3.11 -V
   ```
   Create the virtual environment and activate it:
   - **Linux / macOS (Codio or local):**
     ```bash
     python3.11 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     py -3.11 -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   
   **What to expect**: Your command prompt should show `(.venv)` at the beginning. The `.venv` folder is in the **project root** and will be reused for every level.

2. **Install Rasa Pro**
   
   With the virtual environment activated (still in the project root), run:
   ```bash
   pip install --no-cache-dir rasa-pro
   ```
   
   **What to expect**: Installation takes 2–5 minutes. At the end you should see "Successfully installed rasa-pro-x.x.x" and dependencies.

3. **Verify Installation**
   
   Once installation completes:
   ```bash
   rasa --version
   ```
   **Expected output**: Version information like "Rasa 3.x.x" (no errors).

4. **Set Up Your Own RASA_LICENSE**
   
   You must provide **your own** Rasa Pro license. Use one of the following according to where you are working.

   ---

   **On Codio**
   
   - **Option A – `.env` file (recommended)**  
     In the **project root** (e.g. `~/workspace`), create a file named `.env` with one line (use your real license; this example is a placeholder):
     ```bash
     RASA_LICENSE=rasaxxx-your-license-here
     ```
     Do **not** commit `.env` (it is gitignored).  
     At the start of each new terminal session, from the project root run:
     ```bash
     set -a
     source .env
     set +a
     ```
     Then you can `cd level1` (or any level) and run Rasa; the process will have `RASA_LICENSE` set.
   
   - **Option B – Codio environment variables**  
     If your Codio project has an Environment Variables or Settings area where you can add variables, add `RASA_LICENSE` there with your license value. It will then be available in every terminal session without creating a file.

   ---

   **On your local machine (Windows)**
   
   - Create a file named `.env` in the **project root** (the folder that contains `level1`, `level2`, `.guides`). Put one line in it:
     ```
     RASA_LICENSE=rasaxxx-your-license-here
     ```
     Replace `rasaxxx-your-license-here` with your actual Rasa Pro license. Do not commit `.env`.
   
   - **Loading the variable in PowerShell (current session):**
     ```powershell
     Get-Content .env | ForEach-Object { if ($_ -match '^RASA_LICENSE=(.+)$') { [System.Environment]::SetEnvironmentVariable('RASA_LICENSE', $matches[1].Trim(), 'Process') } }
     ```
     Or, from project root, run a small script that reads `.env` and sets `$env:RASA_LICENSE` (never commit the script with a real key).
   
   - **Persistence across sessions:** You can set the user-level environment variable once (e.g. in System → Environment Variables, or `[System.Environment]::SetEnvironmentVariable('RASA_LICENSE', 'your-license', 'User')` in PowerShell). Then each new terminal will have `RASA_LICENSE` set.

   ---

   **On your local machine (macOS / Linux)**
   
   - Create a file named `.env` in the **project root** with one line:
     ```bash
     RASA_LICENSE=rasaxxx-your-license-here
     ```
     Replace with your actual license. Do not commit `.env`.
   
   - At the start of each terminal session, from the project root run:
     ```bash
     set -a
     source .env
     set +a
     ```
     Then `cd level1` (or any level) and run Rasa. The shell and child processes will have `RASA_LICENSE` set.

   ---

   **Verify RASA_LICENSE is set** (any environment):
   ```bash
   [ -n "$RASA_LICENSE" ] && echo "RASA_LICENSE is set" || echo "RASA_LICENSE is not set"
   ```
   (On Windows PowerShell, use `if ($env:RASA_LICENSE) { "RASA_LICENSE is set" } else { "RASA_LICENSE is not set" }`.)  
   It should report "RASA_LICENSE is set" before you run Rasa in later labs.

5. **Check Project Structure** *(After installation)*
   
   Go to the `level1` folder and confirm the bot structure is present:
   ```bash
   cd level1
   ls -la domain/
   ls -la data/
   ls -la config.yml credentials.yml endpoints.yml
   ```
   Confirm: `domain/` and `data/` exist, and the config files are present.

**✅ Success Criteria**: You can run `rasa --version` successfully, **RASA_LICENSE is set** (verified by the check above), and `level1` has the expected structure. Run the assessment for this lab to confirm your setup. For later labs: **activate the venv from the project root**, ensure `RASA_LICENSE` is loaded, then `cd` into the level folder you're working in (e.g. `cd level1`).

{Check It!|assessment}(code-output-compare-3333363688)
