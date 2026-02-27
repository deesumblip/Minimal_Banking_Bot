# Lab 0.1: Create Virtual Environment and Install Rasa Pro

**Objective**: Create a virtual environment in the **project root**, install Rasa Pro in it, set up **your own** Rasa Pro license (`RASA_LICENSE`), and verify the installation.

**Important**: This is your first step! You must create a virtual environment, install Rasa Pro, and set your **own** Rasa Pro license before you can proceed. This course uses only **RASA_LICENSE** (no OpenAI API key required).

---

> **📌 Create the virtual environment from the root folder first**  
> The terminal opens at the **project root** (the folder that contains `level1`, `level2`, and `.guides`). Create the virtual environment **there**; only **then** go into `level1` for the rest of this lab. One `.venv` in the root is used for **all levels** — do not create a separate venv inside `level1` or any other level folder.

---

**Before you start**: Open a terminal (in Codio or on your local machine). Stay in the **project root** for Steps 1–3. Do **not** run `cd level1` yet. You will set up your license and check project structure in Steps 4–5.

**Order of operations:** 1. Root → create venv & activate → 2. Root → install Rasa Pro → 3. Root → verify (`rasa --version`) → 4. Set **your own** `RASA_LICENSE` (Codio vs Local by OS) → 5. Check project structure in `level1`.

#### Steps

1. **Create a Virtual Environment (in the project root)**
   
   In the terminal, make sure you're in the **main project folder** (run `pwd`; path should **not** end in `level1`). Check Python 3.11:
   ```bash
   python3.11 -V
   ```
   Create and activate the venv:
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
   Your prompt should show `(.venv)`.

2. **Install Rasa Pro**
   
   With the venv activated (still in project root):
   ```bash
   pip install --no-cache-dir rasa-pro
   ```
   Expect 2–5 minutes; "Successfully installed rasa-pro-x.x.x" at the end.

3. **Verify Installation**
   
   ```bash
   rasa --version
   ```
   You should see version info like "Rasa 3.x.x" (no errors).

4. **Set Up Your Own RASA_LICENSE**
   
   You must provide **your own** Rasa Pro license. Follow the section for your environment.

   ---

   **On Codio**
   
   - **Option A – `.env` file (recommended)**  
     In the **project root** (e.g. `~/workspace`), create a file named `.env` with one line (use your real license; example is a placeholder):
     ```bash
     RASA_LICENSE=rasaxxx-your-license-here
     ```
     Do **not** commit `.env` (it is gitignored).  
     At the start of each new terminal session, from the project root:
     ```bash
     set -a
     source .env
     set +a
     ```
     Then `cd level1` (or any level) and run Rasa.
   
   - **Option B – Codio environment variables**  
     If your Codio project has an Environment Variables (or Settings) area, add `RASA_LICENSE` there with your license value. It will be available in every terminal session.

   ---

   **On your local machine (Windows)**
   
   - Create a file named `.env` in the **project root** with one line:
     ```
     RASA_LICENSE=rasaxxx-your-license-here
     ```
     Replace with your actual Rasa Pro license. Do not commit `.env`.
   
   - **Current PowerShell session:** Load the variable from `.env` (e.g. a one-liner that sets `$env:RASA_LICENSE` from the file, or use System → Environment Variables to set it for your user so it persists across sessions).

   ---

   **On your local machine (macOS / Linux)**
   
   - Create a file named `.env` in the **project root** with one line:
     ```bash
     RASA_LICENSE=rasaxxx-your-license-here
     ```
     Replace with your actual license. Do not commit `.env`.
   
   - At the start of each terminal session, from the project root:
     ```bash
     set -a
     source .env
     set +a
     ```
     Then `cd level1` (or any level) and run Rasa.

   ---

   **Verify RASA_LICENSE is set** (any environment):
   - **Linux / macOS / Codio:** `[ -n "$RASA_LICENSE" ] && echo "RASA_LICENSE is set" || echo "RASA_LICENSE is not set"`
   - **Windows PowerShell:** `if ($env:RASA_LICENSE) { "RASA_LICENSE is set" } else { "RASA_LICENSE is not set" }`  
   It should report "RASA_LICENSE is set" before you run Rasa in later labs.

5. **Check Project Structure** *(After installation)*
   
   ```bash
   cd level1
   ls -la domain/
   ls -la data/
   ls -la config.yml credentials.yml endpoints.yml
   ```
   Confirm: `domain/`, `data/`, and the config files exist.

**✅ Success Criteria**: You can run `rasa --version` successfully, **RASA_LICENSE is set**, and `level1` has the expected structure. Run the assessment for this lab to confirm. For later labs: **activate the venv from the project root**, ensure `RASA_LICENSE` is loaded, then `cd` into the level folder (e.g. `cd level1`).
