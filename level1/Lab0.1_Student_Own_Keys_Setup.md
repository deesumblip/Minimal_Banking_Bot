# Lab 0.1 Setup: Students Provide Their Own Rasa Pro License

This guide describes how to set up Lab 0.1 (Level 1) so that **students provide their own RASA_LICENSE**, the **environment variable persists for the whole course**, and **the license never leaves the student's own sign-in** (no leaking).

**Scope**: This course uses only **RASA_LICENSE**. No OpenAI API key is required.

---

## 1. Goals

- **Student-owned license**: Each student uses their own Rasa Pro license.
- **Persistence**: Once set, the same license works for Level 1, Level 2, Level 3, and Level 4 without re-entering.
- **No leaking**: The license is never committed to git, never in shared content, and only lives in the student's workspace or environment.

---

## 2. Keep the License Out of the Repo (Already Done)

- **`.env` is in `.gitignore`** — Students can create `.env` with their real license and it will never be committed or pushed.
- **Do not** put real licenses in any guide content, assessment text, or solution files. Use placeholders only (e.g. `RASA_LICENSE=rasaxxx-your-license-here`).

---

## 3. Option A: Single `.env` at Project Root (Recommended)

**Idea:** One `.env` file at the **project root** (the folder that contains `level1`, `level2`, `level3`, `.guides`). Students create it once in Lab 0.1. For every terminal session, they load it once from the root, then `cd` into any level and run Rasa; the process inherits `RASA_LICENSE`.

**Why it persists:** The file lives in the student's workspace (Codio or local). It is not in git, so `git pull` never overwrites it. Same file is used for all levels.

**Why it doesn't leak:** `.env` is gitignored. Only the student sees their own workspace.

### Lab 0.1 steps (add or adjust)

1. **Create `.env` in the project root** (e.g. `~/workspace` on Codio, or `C:\Users\You\Minimal_Banking_Bot` locally).
2. **Add one line** (no quotes around the value):
   ```
   RASA_LICENSE=rasaxxx-your-license-here
   ```
   Students replace the placeholder with their actual Rasa Pro license.
3. **Do not commit `.env`** — It is already ignored by git. Remind students not to add or commit it.
4. **Each time they open a new terminal** (or start a new Codio session), from the **project root** run:
   - **Linux / macOS / Codio:** `set -a` then `source .env` then `set +a`
   - **Windows PowerShell:** Load `RASA_LICENSE` from `.env` (e.g. read the file and set `$env:RASA_LICENSE`), or set it once in System → Environment Variables.
   Then they can `cd level1`, `cd level2`, etc. and run Rasa.

### Codio-specific

- The workspace is **per student**. Files they create (like `.env`) exist only in their workspace.
- One `.env` at project root, created once in Lab 0.1, and "source it from root at the start of each terminal session" gives persistence across the whole course without leaking.

---

## 4. Option B: Codio Environment Variables (If Available)

Some Codio plans let you set **environment variables** in the project or workspace settings.

- **Student flow:** In Lab 0.1, the student pastes their RASA_LICENSE into Codio's env-var UI (e.g. Project → Environment Variables). No `.env` file is created.
- **Persistence:** Codio stores the value for that workspace; it applies to every terminal session and all levels.
- **No leaking:** The value is stored in Codio's backend for that workspace only; it is not in any file in the repo.

**If your Codio instance supports this:** You can use this for Codio so students never create a file with the license. Keep **Option A** for local (create `.env` in project root and source it) and for Codio instances that don't have workspace env vars.

---

## 5. Option C: One `.env` per Level

- **Persistence:** Student creates `level1/.env` in Lab 0.1. When they start Level 2, they **copy** the same file to `level2/.env`, and so on. Content is the same; they only enter the license once and copy.
- **No leaking:** All `.env` files are gitignored.

Downside: multiple copies. Option A (single root `.env` + source from root) avoids that.

---

## 6. Lab 0.1 Assessment and the License

- **Do not** require the assessment to **read** the contents of `.env` or the value of `RASA_LICENSE`. Only check that:
  - A `.env` file exists in the expected place (e.g. project root for Option A), **or**
  - That `RASA_LICENSE` is **set** (e.g. `[ -n "$RASA_LICENSE" ]`) without printing its value.
- **Do not** log or echo `RASA_LICENSE` in any script or instruction. Verification can be "is set" vs "is not set" only.

---

## 7. Short Checklist for Implementers

- [ ] `.env` is in `.gitignore` (already done in this repo).
- [ ] Lab 0.1 content tells students to create `.env` (or use Codio env vars) and add **their own** RASA_LICENSE; no real license in the guide.
- [ ] Instructions say where to create `.env` (e.g. project root for Option A) and how to load it each session (e.g. `source .env` from root, then `cd` to level).
- [ ] Instructions are split by environment: **Codio** vs **Local (Windows / macOS / Linux)** as appropriate.
- [ ] Later labs say "ensure RASA_LICENSE is loaded" or "if RASA_LICENSE not set, see Lab 0.1" without ever echoing or storing the value.
- [ ] Lab 0.1 assessment only checks ".env exists" or "RASA_LICENSE is set", not its value.
- [ ] No license in any committed file or shared content; Codio workspace (or local `.env`) remains the only place the student's license lives.

---

## Summary

- **Persistence:** Use one `.env` at **project root** and have students **source it at the start of each terminal session** (Option A), or use Codio env vars (Option B), or copy one `.env` to each level (Option C).
- **No leaking:** `.env` is gitignored; the license is never committed, never in guides/assessments, and only in the student's workspace (or Codio's env storage). This keeps setup persistent for the whole course while not leaking their license outside their own sign-in.
