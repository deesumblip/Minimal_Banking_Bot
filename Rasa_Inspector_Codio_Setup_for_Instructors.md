# Rasa Inspector — Codio setup (instructors)

This document is **not** part of the student-facing Codio guide. It explains how to configure Codio so the terminal can auto-start Inspector when a student opens **6.3 Testing Your Agent** (Chapter 1.1, Unit 6), and how to use the **Start Rasa Inspector** link if auto-run is unavailable.

Codio supports running a terminal command when a section is displayed ([Codio docs: open tabs / section commands](https://docs.codio.com/instructors/authoring/guides/settings/opentabs.html)).

## In Codio Guide Editor

1. Open **Chapter 1.1** → **Unit 6** → **6.3 Testing Your Agent** (the command belongs on the **6.3** page layout in the Guide Editor, not on a separate student page).
2. Click **Layout** (top bar, next to Settings).
3. Under **Customize tabs within each panel** you should see a row with **TYPE** (e.g. Terminal), **FILENAME** (`#terminal`), **PANEL** (e.g. Panel A).
4. **Find the command field:**
   - It may appear in the same row (e.g. **Command** or **Run command**), or
   - Click the row / the **`#terminal`** cell to see if extra fields expand, or
   - When **TYPE** is **Terminal**, some Codio versions show a second field for the command.
5. In that command field, enter exactly:

   ```bash
   bash /home/codio/workspace/.guides/scripts/start_rasa_inspect.sh
   ```

6. **SAVE AND CLOSE SETTINGS**.

After that, when a student opens **6.3**, the terminal should open and run that script so Inspector starts automatically.

## If there is no command field

The repo’s **6.3** page JSON (`6-3-Testing-Your-Agent-f6a7.json`) already includes a `command` (and related `files` entry) for the terminal. If your Codio version ignores it, the fallback is the **“Start Rasa Inspector”** link in the **6.3** markdown (one click). You can also add **Start Rasa Inspector** to the Run menu via `.codio`.
