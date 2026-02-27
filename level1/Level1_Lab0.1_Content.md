# Lab 0.1: Create Virtual Environment and Install Rasa Pro

Create a virtual environment in the **project root**, install Rasa Pro, set up **your own** Rasa Pro license (`RASA_LICENSE`), and verify everything works. This is your first step—you need this setup before any other lab.

**This course uses only RASA_LICENSE** (no OpenAI API key required).

---

## In this lab you will

1. Create a virtual environment (`.venv`) in the **project root** — this same `.venv` is used across **all levels** (level1, level2, level3, etc.)
2. Install Rasa Pro in that venv
3. Verify the installation with `rasa --version`
4. Set your **own** Rasa Pro license (`RASA_LICENSE`) — instructions by environment below
5. Confirm the `level1` project structure is present

---

> **📌 Create the venv in the project root**
>
> The **project root** is the folder that contains all levels used in this course. Create `.venv` there. You'll use this single `.venv` for every level. Activate it from the project root, then `cd` into the level you're working in (e.g. `cd level1`).

---

## Before you start

- Open a terminal (Codio or your local machine).
- Stay in the **project root** for Steps 1–3.
- You will set up `RASA_LICENSE` in Step 4 according to your environment (Codio, Windows, or macOS/Linux).

---

## Step 1: Create a virtual environment (project root)

1. Confirm you are in the **main project folder** (run `pwd` — the path should **not** end in `level1`).
2. Check Python 3.11:
   ```bash
   python3.11 -V
   ```
3. Create and activate the virtual environment:

   **Linux / macOS (Codio or local):**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows (PowerShell):**
   ```powershell
   py -3.11 -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

**What you'll see:** Your prompt should show `(.venv)` at the start. The `.venv` folder is in the project root and is used across all levels — activate it from the root whenever you work in level1, level2, or any other level.

---

## Step 2: Install Rasa Pro

With the virtual environment activated and still in the project root:

```bash
pip install --no-cache-dir rasa-pro
```

**What you'll see:** Installation takes 2–5 minutes.

---

## Step 3: Verify installation

Run:

```bash
rasa --version
```

**What you'll see:** Version information such as "Rasa 3.x.x" with no errors.

---

## Step 4: Set up your own RASA_LICENSE

You must provide **your own** Rasa Pro license. Follow the section for **your** environment: Codio, Windows, or macOS/Linux.

### On Codio

1. In the **project root** (e.g. `~/workspace`), create a file named `.env` from the terminal (replace the placeholder with your real license):
   ```bash
   cd ~/workspace
   cat > .env <<'EOF'
   RASA_LICENSE=rasaxxx-your-license-here
   EOF
   ```
2. Do **not** commit `.env` (it is in `.gitignore`).
3. At the start of **each new terminal session**, from the project root run:
   ```bash
   set -a
   source .env
   set +a
   ```
4. Then you can `cd level1` (or any level) and run Rasa; the process will have `RASA_LICENSE` set.

**Alternative – Codio environment variables**

If your Codio project has an **Environment Variables** (or **Settings**) area where you can add variables, add `RASA_LICENSE` there with your license value. It will then be available in every terminal session without creating a `.env` file.

---

### On your local machine (Windows)

1. Create a file named `.env` in the **project root** (the folder that contains all levels). From PowerShell, run (replace the placeholder with your real license):
   ```powershell
   Set-Content -Path .env -Value "RASA_LICENSE=rasaxxx-your-license-here"
   ```
   Do **not** commit `.env`.

2. **Load the variable in the current PowerShell session:**
   ```powershell
   Get-Content .env | ForEach-Object { if ($_ -match '^RASA_LICENSE=(.+)$') { [System.Environment]::SetEnvironmentVariable('RASA_LICENSE', $matches[1].Trim(), 'Process') } }
   ```
   Alternatively, use a small script that reads `.env` and sets `$env:RASA_LICENSE` (do not commit the script with a real key).

3. **To have it in every new terminal:** Set the user-level environment variable once (e.g. **System → Environment Variables**, or `[System.Environment]::SetEnvironmentVariable('RASA_LICENSE', 'your-license', 'User')` in PowerShell).

---

### On your local machine (macOS / Linux)

1. Create a file named `.env` in the **project root** from your terminal (replace the placeholder with your real license):
   ```bash
   cat > .env <<'EOF'
   RASA_LICENSE=rasaxxx-your-license-here
   EOF
   ```
   Do **not** commit `.env`.

2. At the start of **each terminal session**, from the project root run:
   ```bash
   set -a
   source .env
   set +a
   ```
   Then `cd level1` (or any level) and run Rasa; the shell and child processes will have `RASA_LICENSE` set.

---

### Verify RASA_LICENSE is set (all environments)

**Windows / Linux / macOS / Codio:** Run `rasa --version` again to ensure that the license has been correctly set.

---

## Step 5: Check project structure

In your file tree, go into `level1` and confirm the bot structure is present. You should see something like this:

```
level1/
├── config.yml
├── credentials.yml
├── endpoints.yml
├── domain/
│   └── basics.yml
└── data/
    └── basics/
        ├── greet.yml
        ├── help.yml
        └── contact.yml
```

Confirm that the **domain/** and **data/** directories exist and that the three config files (`config.yml`, `credentials.yml`, `endpoints.yml`) are present in `level1`.

---

## Success criteria

- **RASA_LICENSE is set** and you can run `rasa --version` successfully.
- The `level1` folder has the expected structure (domain, data, config files).

For **later labs**: Use the same `.venv` from the project root for every level. Activate it from the root, ensure `RASA_LICENSE` is loaded, then `cd` into the level folder you're working in (e.g. `cd level1`).

**Run the assessment for this lab** to confirm your setup.
