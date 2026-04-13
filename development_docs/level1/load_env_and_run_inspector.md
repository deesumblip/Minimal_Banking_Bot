# `load_env.ps1` and `run_inspector.ps1` (Level 1)

Two **optional** PowerShell helpers live in **`level1/`** (next to the Rasa project). They are **not** required for Codio and **not** invoked by the `.guides/` course content. They exist to make **local development on Windows** with PowerShell a little smoother.

---

## `load_env.ps1`

**What it does:** Reads **`level1/.env`** (same directory as the script) and sets each `KEY=value` pair on the **current** PowerShell process environment. It skips blank lines and `#` comments, then **requires** `RASA_LICENSE` to be set after loading.

**How to use:** From **`level1/`**, dot-source the script so variables apply to your session:

```powershell
cd path\to\Minimal_Banking_Bot\level1
. .\load_env.ps1
```

After that, commands you run in that terminal (e.g. `python -m rasa train`) can see `RASA_LICENSE` and any other keys you put in `.env`.

**Why use it:** On Windows, students often keep secrets in `.env` instead of exporting variables manually each time. This script avoids copy-paste errors for `RASA_LICENSE` (and optional keys like `OPENAI_API_KEY`).

**If it fails:** You must have a `.env` file in **`level1/`** and a line that defines `RASA_LICENSE=...`.

---

## `run_inspector.ps1`

**What it does:** A small **train + inspect** pipeline:

1. Dot-sources **`.\load_env.ps1`** (so `RASA_LICENSE` is loaded).
2. Creates **`level1/logs/`** if missing.
3. Runs **`python -m rasa train`** using the **repository root** virtualenv:  
   **`Minimal_Banking_Bot/.venv/Scripts/python.exe`** (parent of `level1/`).
4. Runs **`python -m rasa inspect --debug --log-file logs/logs.out`** with the same interpreter.

**How to use:** From **`level1/`**:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_inspector.ps1
```

**Why the repo-root `.venv`:** The script assumes you created **one** venv at the repo root (as in the root `README.md` / this folder’s quick start), not a separate venv inside `level1/`. If that path does not exist, the script will fail until you create `Minimal_Banking_Bot/.venv` and install Rasa Pro there.

**Equivalent without the script:** Activate your venv, ensure `RASA_LICENSE` is set, `cd` to `level1`, then run `rasa train` and `rasa inspect` with your usual flags.

---

## Codio vs local

| Environment | Need these scripts? |
|-------------|---------------------|
| **Codio** | **No.** The guide uses the terminal and environment Codio provides; these files are not referenced in `.guides/`. |
| **Local (Windows, PowerShell)** | **Optional.** Convenience only; same results with manual `rasa` commands and env setup. |
| **Local (macOS / Linux / bash)** | **No** — use `export` / `.env` tooling your shell supports; these are `.ps1` scripts. |

---

## Related docs

- **`development_docs/README.md`** — Quick start that mentions the same commands.
- **Root `README.md`** — Repo-wide local setup, including `load_env.ps1` / `run_inspector.ps1` for Level 1.
