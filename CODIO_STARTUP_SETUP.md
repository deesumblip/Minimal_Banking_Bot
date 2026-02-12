# Codio: Setting Up startup.sh for This Project

This document is for the **Codio implementer** (instructor or course author) who is configuring the Minimal_Banking_Bot project on Codio. It explains how to set up the startup script so that `RASA_LICENSE` and `OPENAI_API_KEY` are loaded in **every terminal** for students (and for you).

---

## What the startup script does

- **File:** `.guides/startup.sh` (must be **directly** under `.guides/`, not inside `.guides/secure/`).
- **When it runs:** Automatically when the Codio box starts (e.g. when a user opens the project or assignment).
- **What it does:** If it finds an env file at `.guides/secure/rasa_env` or `secure/rasa_env`, it adds a single line to the user’s `~/.bashrc` so that **every new terminal** sources that file. That way `RASA_LICENSE` and `OPENAI_API_KEY` are set in all terminals without users having to run anything.

---

## Required folder and file structure

In the project workspace on Codio you should have:

```
Minimal_Banking_Bot/
├── .guides/
│   ├── startup.sh          ← Script Codio runs on box start (must be here)
│   └── secure/
│       └── rasa_env         ← Env vars (you create this; see below)
├── ...
```

- **`.guides/startup.sh`** — Should already be in the repo. Codio runs this when the box starts.
- **`.guides/secure/rasa_env`** — You create this in Codio and put your Rasa env vars in it. Do not commit real values to Git; this file is for the Codio workspace only (or use a template and fill in when setting up the course).

---

## Step-by-step setup

### 1. Ensure `.guides/startup.sh` is in the project

- In your Codio project (or in the repo), confirm that **`.guides/startup.sh`** exists **directly** under `.guides/` (not inside `.guides/secure/`).
- If you’re using Git: pull the latest from the repo; the file is at `.guides/startup.sh`.
- **Do not** put a copy of the script inside `.guides/secure/`; Codio only runs `.guides/startup.sh`.

### 2. Create the env file `.guides/secure/rasa_env`

- In the Codio file tree, under **`.guides`**, create a folder named **`secure`** if it does not exist.
- Inside **`.guides/secure/`**, create a file named **`rasa_env`** (no extension).
- Put the following in `rasa_env`, **with your real values** (no quotes unless a value contains spaces):

  ```bash
  export RASA_LICENSE=your-actual-rasa-pro-license
  export OPENAI_API_KEY=your-actual-openai-api-key
  ```

- Save the file.  
- **Security:** This file will be in the workspace, so students can open it if they look. Do not commit real keys to the repo; keep them only in Codio (or in a secure place you use when building the assignment).

### 3. (Optional) Make the script executable

- In a Codio terminal you can run:
  ```bash
  chmod +x /home/codio/workspace/.guides/startup.sh
  ```
- Many Codio setups run the script without this; if the script doesn’t run after a restart, try this step.

### 4. Restart the box so the script runs

- In Codio: **Project** → **Restart Box**.
- Wait for the box to come back up. The startup script runs once at box start and, if it finds `rasa_env`, adds the source line to `~/.bashrc`.

### 5. Verify in a new terminal

- Open a **new** terminal (close any old one).
- Run:
  ```bash
  echo $RASA_LICENSE
  echo $OPENAI_API_KEY
  ```
- You should see the values (or at least non-empty output). If you see nothing, see **Troubleshooting** below.

---

## Troubleshooting

| Issue | What to do |
|-------|------------|
| Variables still empty after restart | 1) Confirm `.guides/secure/rasa_env` exists and contains the two `export` lines. 2) Open a **new** terminal (the script only affects new shells). 3) Check that the line was added: `grep "Codio Rasa env" ~/.bashrc` — you should see one line. |
| No `.guides/startup.sh` in project | Get it from the repo (path: `.guides/startup.sh`) and add it under `.guides/` in Codio. Do not put it inside `.guides/secure/`. |
| Script not running at all | Run it once by hand, then open a new terminal: `bash /home/codio/workspace/.guides/startup.sh` |
| Wrong path for env file | The script looks for (1) `/home/codio/workspace/.guides/secure/rasa_env`, then (2) `/home/codio/workspace/secure/rasa_env`. Use one of these two paths for your env file. |

---

## Summary checklist for implementer

- [ ] `.guides/startup.sh` exists directly under `.guides/` (not inside `secure/`).
- [ ] `.guides/secure/rasa_env` exists and contains `export RASA_LICENSE=...` and `export OPENAI_API_KEY=...` with real values.
- [ ] Box has been restarted at least once after the above was in place.
- [ ] In a **new** terminal, `echo $RASA_LICENSE` and `echo $OPENAI_API_KEY` show the values.

After this, every new terminal in that project/assignment will have the Rasa env vars loaded automatically.
