Create a virtual environment in the **project root**, install Rasa Pro, configure **your own** Rasa Pro license using the **`RASA_LICENSE`** variable, and confirm the tools work. This is your first lab. Complete it before any other hands-on work.

This course expects a valid **`RASA_LICENSE`** for Rasa Pro.

Install the **`rasa-pro`** package at version **3.16.3** (pinned in the commands below) so your environment matches the course materials.

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
pip install --no-cache-dir rasa-pro==3.16.3
```

Installation takes 2–5 minutes.

**4. Create `.env` in the project root with `RASA_LICENSE`**

Stay in the **project root** (the folder that contains `level1/`, `level2/`, `.guides/`, **not** inside `level1`). Replace `YOUR_LICENSE_KEY` with your actual Rasa Pro license (paste the whole key):

```bash
echo 'RASA_LICENSE=YOUR_LICENSE_KEY' > .env
```

This creates **`.env`** next to `level1/`. The automated **Check It!** test reads this file (the grader never prints your key).

**5. Verify installation**

Now load the license into your current shell session, then run Rasa by running the following:

```bash
set -a
source .env
set +a
rasa --version
```

You should see version information with no errors.

**In Codio**, use **Check It!** for this lab after step 4 (`.env` exists) to confirm your setup.

{Check It!|assessment}(code-output-compare-3333363688)


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

---
