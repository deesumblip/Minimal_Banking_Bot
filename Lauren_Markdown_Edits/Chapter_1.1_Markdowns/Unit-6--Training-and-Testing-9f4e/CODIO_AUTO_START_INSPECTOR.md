# Auto-start Rasa Inspector when student opens 6.3 (Codio)

Codio supports running a terminal command when a section is displayed ([docs](https://docs.codio.com/instructors/authoring/guides/settings/opentabs.html)).

## In Codio Guide Editor

1. Open **Level 1** → **Unit 6** → **6.3 Testing Your Agent**.
2. Click **Layout** (top bar, next to Settings).
3. Under **Customize tabs within each panel** you should see a row with **TYPE** (e.g. Terminal), **FILENAME** (`#terminal`), **PANEL** (e.g. Panel A).
4. **Find the command field:**
   - It may appear in the same row (e.g. **Command** or **Run command**), or
   - Click the row / the **#terminal** cell to see if extra fields expand, or
   - When **TYPE** is **Terminal**, some Codio versions show a second field for the command.
5. In that command field, enter exactly:
   ```bash
   bash /home/codio/workspace/.guides/scripts/start_rasa_inspect.sh
   ```
6. **SAVE AND CLOSE SETTINGS**.

After that, when a student clicks 6.3, the terminal should open and run that script so Inspector starts automatically.

## If there is no command field

The repo’s 6.3 page JSON already includes a `command` (and `cmd`) for the terminal. If your Codio version ignores it, the only option is the **“Start Rasa Inspector now”** link in the 6.3 content (one click). You can also add **Start Rasa Inspector** to the Run menu via `.codio`.
