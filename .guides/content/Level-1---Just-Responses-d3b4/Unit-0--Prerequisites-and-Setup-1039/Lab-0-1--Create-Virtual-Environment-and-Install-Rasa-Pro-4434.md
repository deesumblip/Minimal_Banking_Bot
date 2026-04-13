Create a virtual environment in the **project root**, install Rasa Pro, configure **your own** Rasa Pro license using the **`RASA_LICENSE`** variable, and confirm the tools work. This is your first lab; complete it before any other hands-on work.

This course expects a valid **`RASA_LICENSE`** for Rasa Pro.

---

## In this lab you will

1. Check Python and pip.
2. Create a virtual environment named **`.venv`** in the **project root**. You reuse this same environment for **level1**, **level2**, **level3**, and the rest of the course.
3. Install Rasa Pro inside that virtual environment.
4. Create a **`.env`** file in the **project root** with your **`RASA_LICENSE`** (via the terminal).
5. Run **`rasa --version`** after loading the license from `.env` into your shell.
6. Confirm the **`level1`** project layout is present.

---

> **📌 Create the venv in the project root**
>
> The **project root** is the folder that contains every **level** folder used in this course. Create **`.venv`** there once. You reuse that single environment for all levels. Activate it from the project root, then change into the level you are working on, for example **`cd level1`**.

---

## Before you start

- Open a terminal on **Codio** or on your own computer.
- Run all setup steps from the **project root**. Use the section below that matches your environment: **Codio**, **Windows**, **macOS**, or **Linux**.

---

## On Codio

Follow these steps from the **project root**, often **`~/workspace`**. You do **not** need to create a new folder or **`cd`** away from the root before you begin.

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

**4. Create `.env` in the project root with `RASA_LICENSE`**

Stay in the **project root** (the folder that contains `level1/`, `level2/`, `.guides/` — **not** inside `level1`). Replace `YOUR_LICENSE_KEY` with your actual Rasa Pro license (paste the whole key):

```bash
echo 'RASA_LICENSE=YOUR_LICENSE_KEY' > .env
```

If your key contains characters that confuse the shell, use:

```bash
printf 'RASA_LICENSE=%s\n' 'YOUR_LICENSE_KEY' > .env
```

This creates **`.env`** next to `level1/`. The automated **Check It!** test reads this file (the grader never prints your key). Do **not** commit `.env` — it is listed in `.gitignore`.

**5. Verify installation**

Load the license into your **current** shell session, then run Rasa:

```bash
set -a
source .env
set +a
rasa --version
```

You should see version information with no errors.

**In Codio**, use **Check It!** for this lab after step 4 (`.env` exists) to confirm your setup.

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

**4. Create `.env` in the project root with `RASA_LICENSE`**

From the **project root** (the folder that contains `level1/`), create `.env` with your actual license:

```powershell
Set-Content -Path .env -Value "RASA_LICENSE=YOUR_LICENSE_KEY" -Encoding utf8
```

Or use a here-string if you prefer. Do **not** commit `.env` (it is in `.gitignore`).

**5. Verify installation**

Load the license for this PowerShell session, then run Rasa:

```powershell
Get-Content .env | ForEach-Object {
  if ($_ -match '^\s*RASA_LICENSE\s*=\s*(.+)\s*$') {
    $env:RASA_LICENSE = $matches[1].Trim([char]0x22, [char]0x27)
  }
}
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

**4. Create `.env` in the project root with `RASA_LICENSE`**

From the **project root**, create `.env` (same steps as **On Codio** above):

```bash
echo 'RASA_LICENSE=YOUR_LICENSE_KEY' > .env
```

Do **not** commit `.env` (it is in `.gitignore`).

**5. Verify installation**

```bash
set -a
source .env
set +a
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

**4. Create `.env` in the project root with `RASA_LICENSE`**

From the **project root**:

```bash
echo 'RASA_LICENSE=YOUR_LICENSE_KEY' > .env
```

Do **not** commit `.env` (it is in `.gitignore`).

**5. Verify installation**

```bash
set -a
source .env
set +a
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

- **Project-root `.env`** contains a real **`RASA_LICENSE=...`** line (not a placeholder), and you can run `rasa --version` successfully after loading `.env` in your shell.
- The `level1` folder has the expected structure (domain, data, config files).

For **later labs**: Use the same `.venv` from the project root for every level. Activate it from the root, load your license (`set -a; source .env; set +a` on bash, or your PowerShell equivalent), then `cd` into the level folder you're working in (e.g. `cd level1`).

---
