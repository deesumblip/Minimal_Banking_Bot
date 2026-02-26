# Lab 0.1 Setup: Students Provide Their Own License Keys

This guide describes how to set up Lab 0.1 (Level 1) so that **students provide their own RASA_LICENSE and OPENAI_API_KEY**, the **environment variables persist for the whole course**, and **keys never leave the student’s own sign-in** (no leaking).

---

## 1. Goals

- **Student-owned keys**: Each student uses their own Rasa Pro license and OpenAI API key.
- **Persistence**: Once set, the same keys work for Level 1, Level 2, and Level 3 without re-entering.
- **No leaking**: Keys are never committed to git, never in shared content, and only live in the student’s workspace or environment.

---

## 2. Keep Keys Out of the Repo (Already Done)

- **`.env` is in `.gitignore`** — Any file named `.env` is ignored by git, so students can create `.env` with real keys and it will never be committed or pushed.
- **Do not** put real keys in any guide content, assessment text, or solution files. Use placeholders only (e.g. `RASA_LICENSE=your-license-here`).

---

## 3. Option A: Single `.env` at Project Root (Recommended)

**Idea:** One `.env` file at the **project root** (the folder that contains `level1`, `level2`, `level3`, `.guides`). Students create it once in Lab 0.1. For every terminal session, they load it once from the root, then `cd` into any level and run Rasa; the process inherits the variables.

**Why it persists:** The file lives in the student’s workspace (Codio or local). It is not in git, so `git pull` never overwrites it. Same file is used for all levels.

**Why it doesn’t leak:** `.env` is gitignored. Only the student sees their own workspace; other students and the repo never see the file or its contents.

### Lab 0.1 steps (add or adjust)

1. **Create `.env` in the project root** (e.g. `~/workspace` on Codio, or `C:\Users\You\Minimal_Banking_Bot` locally).
2. **Add two lines** (no quotes around values):
   ```bash
   RASA_LICENSE=your-actual-rasa-license
   OPENAI_API_KEY=your-actual-openai-key
   ```
3. **Do not commit `.env`** — It is already ignored by git. Remind students not to add or commit it.
4. **Each time they open a new terminal** (or start a new Codio session), from the **project root** run:
   ```bash
   set -a
   source .env
   set +a
   ```
   Then they can `cd level1`, `cd level2`, or `cd level3` and run `rasa train`, `rasa inspect`, etc. Rasa and the shell will have the variables.

**Optional:** Add a one-line helper in the repo (e.g. `source_env.sh` at root) that only does `set -a && source .env && set +a`, and tell students to run `source source_env.sh` from root before working. The helper script does **not** contain any keys; it only sources `.env`, which remains gitignored.

### Codio-specific

- The workspace is **per student**. Files they create (like `.env`) exist only in their workspace and are not visible to other students or to the repo.
- So: one `.env` at project root, created once in Lab 0.1, and “source it from root at the start of each terminal session” gives persistence across the whole course without leaking.

---

## 4. Option B: Codio Environment Variables (If Available)

Some Codio plans let you set **environment variables** in the project or workspace settings. Those variables are then injected into the terminal for that workspace.

- **Student flow:** In Lab 0.1, the student pastes their RASA_LICENSE and OPENAI_API_KEY into Codio’s env-var UI (e.g. Project → Environment Variables or similar). No `.env` file is created.
- **Persistence:** Codio stores the values for that workspace; they apply to every terminal session and all levels.
- **No leaking:** Values are stored in Codio’s backend for that workspace only; they are not in any file in the repo and are not shared with other students.

**If your Codio instance supports this:** Prefer this for Codio so students never create a file with keys. Keep **Option A** for local (e.g. “Create `.env` in project root and source it”) and for Codio instances that don’t have workspace env vars.

---

## 5. Option C: One `.env` per Level (Current Pattern)

Your current docs sometimes say “create `.env` in the `level1` folder” (and similarly for level2/level3). That works too:

- **Persistence:** Student creates `level1/.env` in Lab 0.1. When they start Level 2, they **copy** the same file to `level2/.env`, and again to `level3/.env` when they start Level 3. Content is the same; they only enter keys once and copy.
- **No leaking:** All `.env` files are gitignored; keys never go into the repo.

Downside: three copies of the same keys. Option A (single root `.env` + source from root) avoids that and still keeps one place to edit if a key changes.

---

## 6. Lab 0.1 Assessment and Keys

- **Do not** require the assessment to **read** the contents of `.env` or env vars. Only check that:
  - A `.env` file exists in the expected place (e.g. project root for Option A), **or**
  - That required env vars are **set** (e.g. `[ -n "$RASA_LICENSE" ]`) without printing their values.
- **Do not** log or echo `RASA_LICENSE` or `OPENAI_API_KEY` in any script or instruction. Verification can be “is set” vs “is not set” only.

---

## 7. Short Checklist for Implementers

- [ ] `.env` is in `.gitignore` (already done in this repo).
- [ ] Lab 0.1 content tells students to create `.env` (or use Codio env vars) and add **their own** RASA_LICENSE and OPENAI_API_KEY; no real keys in the guide.
- [ ] Instructions say where to create `.env` (e.g. project root for Option A) and how to load it each session (e.g. `source .env` from root, then `cd` to level).
- [ ] Later labs (Level 1/2/3) say “ensure env vars are loaded” or “if RASA_LICENSE/OPENAI_API_KEY not set, see Lab 0.1” without ever echoing or storing key values.
- [ ] Lab 0.1 assessment only checks “.env exists” or “vars are set”, not their values.
- [ ] No keys in any committed file or shared content; Codio workspace remains the only place the student’s keys live (or Codio’s env-var storage if using Option B).

---

## Summary

- **Persistence:** Use one `.env` at **project root** and have students **source it at the start of each terminal session** (Option A), or use Codio env vars (Option B), or copy one `.env` to each level (Option C).
- **No leaking:** `.env` is gitignored; keys are never committed, never in guides/assessments, and only in the student’s workspace (or Codio’s env storage). That keeps setup persistent for the whole course while not leaking their license key outside their own sign-in.
