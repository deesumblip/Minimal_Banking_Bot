# Lab 0.1: Create Virtual Environment and Install Rasa Pro

Create a virtual environment in the **project root**, install Rasa Pro, set up **your own** Rasa Pro license (`RASA_LICENSE`), and verify everything works. This is your first step—you need this setup before any other lab.

This course uses:

- `RASA_LICENSE` (Rasa Pro license)

---

## In this lab you will

1. Check Python and pip (`python --version`, `pip --version`)
2. Create a virtual environment (`.venv`) in the **project root** — this same `.venv` is used across **all levels** (level1, level2, level3, etc.)
3. Install Rasa Pro in that venv
4. Set up **RASA_LICENSE** (your own Rasa Pro license)
5. Verify the installation with `rasa --version` (after your environment variable is loaded)
6. Confirm the `level1` project structure is present

---

> **📌 Create the venv in the project root**
>
> The **project root** is the folder that contains all levels used in this course. Create `.venv` there. You'll use this single `.venv` for every level. Activate it from the project root, then `cd` into the level you're working in (e.g. `cd level1`).

---

## Before you start

- Open a terminal (Codio or your local machine).
- **On Codio:** You are already in the project directory (e.g. `~/workspace`); you do **not** need to run `mkdir` or `cd` into a new folder.
- Stay in the **project root** for Steps 1–5. You will set up **RASA_LICENSE** in Step 4 according to your environment (Codio, Windows, or macOS/Linux).

---

## Step 1: Check Python and pip

From the **project root**, run:

**Linux / macOS (Codio or local):**
```bash
python --version
pip --version
```

**Windows (PowerShell):**
```powershell
py -3.11 --version
py -m pip --version
```

You should see Python 3.11.x (or 3.10+) and pip. If either command is not found, install Python 3.11 for your OS.

---

## Step 2: Create a virtual environment (project root)

1. Confirm you are in the **main project folder** (run `pwd` — the path should **not** end in `level1`).
2. Create and activate the virtual environment:

   **Linux / macOS (Codio or local):**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows (PowerShell):**
   ```powershell
   py -3.11 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

**What you'll see:** Your prompt should show `(.venv)` at the start. The `.venv` folder is in the project root and is used across all levels — activate it from the root whenever you work in level1, level2, or any other level.

---

## Step 3: Install Rasa Pro

With the virtual environment activated and still in the project root:

```bash
pip install rasa-pro
```

**What you'll see:** Installation takes 2–5 minutes.

---

## Step 4: Set up your own RASA_LICENSE

You must provide your **own** Rasa Pro license (`RASA_LICENSE`). Replace `YOUR_LICENSE_KEY` with your actual key.

### On Codio / Linux / macOS

With the virtual environment activated, from the **project root** run:

```bash
export RASA_LICENSE=YOUR_LICENSE_KEY
```

This sets RASA_LICENSE for the current terminal session. Then run `rasa --version` (Step 5).

**To have RASA_LICENSE in every new terminal:** Create a `.env` file in the project root with `RASA_LICENSE=your-license`, then at the start of each session run `set -a; source .env; set +a`. Do **not** commit `.env` (it is in `.gitignore`). On Codio, you can also add `RASA_LICENSE` in **Environment Variables** / **Settings** if available.

---

### On your local machine (Windows)

In PowerShell, with the virtual environment activated, from the **project root** run (replace with your actual license):

```powershell
$env:RASA_LICENSE = "YOUR_LICENSE_KEY"
```

This sets RASA_LICENSE for the current session. Then run `rasa --version` (Step 5). To have it in every new terminal, set the user environment variable (e.g. **System → Environment Variables**) or use a `.env` file and load it in your profile.

---

## Step 5: Verify installation (after loading RASA_LICENSE)

With the virtual environment active **and** RASA_LICENSE loaded (Step 4), run:

```bash
rasa --version
```

**What you'll see:** Version information with no errors.

---

## Step 6: Check project structure

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

**On Codio:** Run the assessment for this lab (use the Check It! button in the guide) to confirm your setup.
