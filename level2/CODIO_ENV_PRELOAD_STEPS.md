# Preloading environment variables in Codio (instructor + students)

**Goal:** Env vars (e.g. `RASA_LICENSE`, `OPENAI_API_KEY`) are loaded in every terminal for the course, and kept as hidden as possible from students.

**Important Codio limitation:** Environment variables you set in **Codio > Preferences > Environment Variables** are **not** passed to student assignments. So students do **not** get those vars unless you use one of the workarounds below.

---

## Part 1: Your own (instructor) environment — fully hidden

Use this so **your** terminals always have the vars and students never see them in the repo.

### Step 1: Set variables in Codio Preferences

1. Open your **Codio project** (the one you use to build the course).
2. In the menu bar: **Codio** → **Preferences** → **Environment Variables**.
3. Click **Add** (or similar) and add:
   - **Name:** `RASA_LICENSE`  
     **Value:** your actual Rasa Pro license.
   - **Name:** `OPENAI_API_KEY`  
     **Value:** your actual OpenAI API key.
4. Save.
5. **Restart the box** so the vars take effect: **Project** → **Restart Box**.

After this, every **new** terminal you open in that project will have these variables. They are stored in Codio’s config, not in the project files, so students never see them.

---

## Part 2: Students’ environment — loaded in every terminal

Because Codio does **not** give students the instructor’s Preferences env vars, the only way to have vars loaded automatically in **student** terminals is to **source a file** from the project when the box starts. That file will exist in the student’s workspace, so they *could* open it if they look for it. So “completely hidden” is **not** possible with standard Codio; the steps below give “loaded for every exercise” and “as hidden as we can make it” (e.g. in a non-obvious path).

### Step 1: Put the env file in the project (instructor only)

1. In your project, ensure you have a file that **only you** maintain (e.g. `secure/rasa_env`), **not** in Git:
   - Create `secure/rasa_env` in the project root (or use your existing path).
   - Contents (no quotes unless the value has spaces):
     ```bash
     export RASA_LICENSE=your-actual-license
     export OPENAI_API_KEY=your-actual-key
     ```
2. The repo has **`secure/rasa_env`** in `.gitignore` (so real keys are never committed) and **`secure/rasa_env.template`** committed as a placeholder. Copy the template to `rasa_env` and add your real values.
3. When you **publish** the assignment: do **not** add `secure/` to `.assignmentignore`. Ensure `secure/rasa_env` (with real values) is present in the project in Codio when you publish—e.g. copy from template and fill in, or upload your existing file. Then students’ boxes will have the file and the startup script will load it. Students could open the file if they look.

So: with standard Codio you can have **either** “loaded for every exercise” **or** “completely hidden,” not both.

### Step 2: Load the env file in every new terminal (startup)

So that **every** terminal (including students’) loads the vars when the box starts:

1. Create or edit the **startup script** Codio runs when the box starts.
   - **If your project uses Guides:** use **`.guides/startup.sh`** (in the project root).
   - **Otherwise:** use **`/home/codio/startup.sh`** (you may need to create it from **Tools > Install Software** or your stack so it’s in the image).
2. In that startup script, add a line that sources your env file **only if it exists** (so it doesn’t error if the file was excluded):

   **For `.guides/startup.sh`** (path relative to workspace):

   ```bash
   # Load env vars for Rasa (if present)
   [ -f "/home/codio/workspace/secure/rasa_env" ] && source "/home/codio/workspace/secure/rasa_env"
   ```

   **For `/home/codio/startup.sh`** (same idea):

   ```bash
   # Load env vars for Rasa (if present)
   [ -f "/home/codio/workspace/secure/rasa_env" ] && source "/home/codio/workspace/secure/rasa_env"
   ```

3. If you use **`.guides/startup.sh`**, ensure it’s **included** in the assignment (not in `.assignmentignore`), so students’ boxes run it when they open the assignment.
4. **Restart the box** once: **Project** → **Restart Box**. After that, every **new** terminal should have the variables (as long as `secure/rasa_env` exists in that box, i.e. you didn’t exclude it with `.assignmentignore`).

### Step 3: Make sure students start in the right directory (optional)

If your exercises assume a specific folder (e.g. `level2`), you can add to the same startup script:

```bash
# Optional: default to level2 when terminal opens (adjust path if different)
# This is often set in Codio’s terminal settings instead; see your stack/docs.
```

Or configure the **default terminal directory** in your Codio stack/box so that when students open a terminal, they’re already in the right folder.

---

## Summary

| Who        | How vars are loaded                    | Hidden from students? |
|-----------|----------------------------------------|------------------------|
| Instructor| **Codio > Preferences > Environment Variables** + Restart Box | Yes (not in project)   |
| Students  | **startup script** sources `secure/rasa_env` (file must be in their workspace) | No (file is in project) |

- For **you**: use **Part 1** only; no need to put secrets in the repo.
- For **students**: use **Part 2** so vars are preloaded in every terminal; “completely hidden” is not possible without Codio passing instructor env vars to student boxes (which Codio does not do). To minimize visibility, keep the file in a single place (e.g. `secure/rasa_env`) and don’t reference it in student-facing instructions.

---

## References

- [Codio: Environment Variables](https://docs.codio.com/common/settings/env-variables.html)  
- [Codio: Autostart / startup.sh](https://docs.codio.com/common/develop/ide/boxes/startup.html)  
- [Codio: Excluding files (.assignmentignore)](https://docs.codio.com/instructors/authoring/guides/excludingfiles.html)
