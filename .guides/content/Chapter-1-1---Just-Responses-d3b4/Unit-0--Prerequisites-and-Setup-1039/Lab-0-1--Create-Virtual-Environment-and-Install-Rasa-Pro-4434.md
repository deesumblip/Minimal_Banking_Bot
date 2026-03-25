Create a virtual environment in the **project root**, install Rasa Pro, set up **your own** Rasa Pro license (`RASA_LICENSE`), and verify everything works. This is your first step, you need this setup before any other lab.

This course uses:

- `RASA_LICENSE` (Rasa Pro license)

---

## In this lab you will

1. Check Python and pip
2. Create a virtual environment (`.venv`) in the **project root**, this same `.venv` is used across **all levels** (level1, level2, level3, etc.)
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
- Stay in the **project root** for all setup steps below. Choose the section that matches your environment: **Codio**, **Windows**, **macOS**, or **Linux**.

---

## On Codio

Follow these steps from the **project root** (e.g. `~/workspace`). You do **not** need to run `mkdir` or `cd` into a new folder.

**1. Check Python and pip**

```bash
python --version
pip --version
```

You should see Python 3.11.x (or 3.10+) and pip. **If Python is not found,** install it in the terminal (Codio is usually Ubuntu-based):

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

Then run `python3.11 --version` and `pip --version` again. If your environment doesn't allow `sudo` or the packages aren't available, ask your instructor or course support for how to enable Python 3.11 on your Codio box.

**If pip is not found** but Python is, install pip with:

```bash
python3.11 -m ensurepip --upgrade
```

(or use `python -m ensurepip --upgrade` if `python` points to 3.11). Then run `pip --version` again.

**2. Create and activate the virtual environment**

Confirm you're in the project root (run `pwd`, the path should **not** end in `level1`). Then:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Your prompt should show `(.venv)` at the start.

**3. Install Rasa Pro**

```bash
pip install --no-cache-dir rasa-pro
```

Installation takes 2–5 minutes.

**4. Set RASA_LICENSE**

Replace `YOUR_LICENSE_KEY` with your actual Rasa Pro license key:

```bash
export RASA_LICENSE=YOUR_LICENSE_KEY
```

Then run `rasa --version` (step 5).

**To have RASA_LICENSE in every new terminal:** Create a `.env` file in the project root with `RASA_LICENSE=your-license`, then at the start of each session run `set -a; source .env; set +a`. Do **not** commit `.env` (it is in `.gitignore`). On Codio you can also add `RASA_LICENSE` in **Environment Variables** / **Settings** if available.

**5. Verify installation**

```bash
rasa --version
```

You should see version information with no errors.

**In Codio**, use **Check It!** for this lab to confirm your setup.

{Check It!|assessment}(code-output-compare-3333363688)

---

## On Windows

Follow these steps from the **project root** in **PowerShell**.

**1. Check Python and pip**

```powershell
py -3.11 --version
py -m pip --version
```

You should see Python 3.11.x (or 3.10+) and pip. **If Python is not found,** install Python 3.11 (or 3.10+):

- Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3.11 (or 3.10+) installer for Windows.
- Run the installer and check **"Add python.exe to PATH"** (and **"Install pip"** if offered). Restart your terminal, then run the version commands again.
- Alternatively, install from Microsoft Store ("Python 3.11") or with `winget install Python.Python.3.11` (if you use winget).

**If pip is not found** but Python is installed, bootstrap pip with:

```powershell
py -3.11 -m ensurepip --upgrade
```

Then run `py -m pip --version` again.

**2. Create and activate the virtual environment**

Confirm you're in the project root. Then:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Your prompt should show `(.venv)` at the start.

**3. Install Rasa Pro**

```powershell
pip install --no-cache-dir rasa-pro
```

Installation takes 2–5 minutes.

**4. Set RASA_LICENSE**

Replace `YOUR_LICENSE_KEY` with your actual license:

```powershell
$env:RASA_LICENSE = "YOUR_LICENSE_KEY"
```

Then run `rasa --version` (step 5). To have it in every new terminal, set the user environment variable (e.g. **System → Environment Variables**) or use a `.env` file and load it in your profile.

**5. Verify installation**

```powershell
rasa --version
```

You should see version information with no errors.

---

## On macOS

Follow these steps from the **project root** in Terminal.

**1. Check Python and pip**

```bash
python3.11 --version
pip --version
```

(If needed, try `python --version` or `python3 --version`.) You should see Python 3.11.x (or 3.10+). **If Python is not found,** install Python 3.11 (or 3.10+):

- **Option A:** Download the macOS installer from [python.org/downloads](https://www.python.org/downloads/) and run it. The installer adds Python (and pip) to your path.
- **Option B:** With Homebrew installed, run `brew install python@3.11`. Then use `python3.11` and `pip3` (or ensure `python3` points to 3.11 via your PATH).

**If pip is not found** but Python is installed, install pip with:

```bash
python3.11 -m ensurepip --upgrade
```

Then run `pip --version` (or `pip3 --version`) again. After any install, close and reopen your terminal, then repeat the version commands from the project root.

**2. Create and activate the virtual environment**

Confirm you're in the project root (run `pwd`, the path should **not** end in `level1`). Then:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Your prompt should show `(.venv)` at the start.

**3. Install Rasa Pro**

```bash
pip install --no-cache-dir rasa-pro
```

Installation takes 2–5 minutes.

**4. Set RASA_LICENSE**

Replace `YOUR_LICENSE_KEY` with your actual license:

```bash
export RASA_LICENSE=YOUR_LICENSE_KEY
```

Then run `rasa --version` (step 5). **To have RASA_LICENSE in every new terminal:** Create a `.env` file in the project root with `RASA_LICENSE=your-license`, then at the start of each session run `set -a; source .env; set +a`. Do **not** commit `.env` (it is in `.gitignore`).

**5. Verify installation**

```bash
rasa --version
```

You should see version information with no errors.

---

## On Linux

Follow these steps from the **project root** in your terminal.

**1. Check Python and pip**

```bash
python3.11 --version
pip --version
```

You should see Python 3.11.x (or 3.10+). **If Python is not found,** install Python 3.11 (or 3.10+):

- **Ubuntu/Debian:** `sudo apt update` then `sudo apt install python3.11 python3.11-venv python3-pip`
- **Fedora/RHEL:** `sudo dnf install python3.11 python3-pip` (or `python3.11-pip` if available)
- If 3.11 isn't in your repos, use the deadsnakes PPA (Ubuntu) or install from [python.org/downloads](https://www.python.org/downloads/) and adjust your PATH.

**If pip is not found** but Python 3.11 is installed, install pip with your package manager (`sudo apt install python3-pip` or `sudo dnf install python3-pip`) or bootstrap it:

```bash
python3.11 -m ensurepip --upgrade
```

Then run `pip --version` again. After any install, close and reopen your terminal, then repeat the version commands from the project root.

**2. Create and activate the virtual environment**

Confirm you're in the project root (run `pwd`, the path should **not** end in `level1`). Then:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Your prompt should show `(.venv)` at the start.

**3. Install Rasa Pro**

```bash
pip install --no-cache-dir rasa-pro
```

Installation takes 2–5 minutes.

**4. Set RASA_LICENSE**

Replace `YOUR_LICENSE_KEY` with your actual license:

```bash
export RASA_LICENSE=YOUR_LICENSE_KEY
```

Then run `rasa --version` (step 5). **To have RASA_LICENSE in every new terminal:** Create a `.env` file in the project root with `RASA_LICENSE=your-license`, then at the start of each session run `set -a; source .env; set +a`. Do **not** commit `.env` (it is in `.gitignore`).

**5. Verify installation**

```bash
rasa --version
```

You should see version information with no errors.

---

## Step 6: Check project structure (all environments)

In your file tree, go into `level1` and confirm the agent structure is present. You should see something like this:

```text
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

---
