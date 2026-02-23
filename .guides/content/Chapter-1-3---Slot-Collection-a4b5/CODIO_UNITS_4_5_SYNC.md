# Units 4 and 5: Sync and Duplicate Issues in Codio

## Duplicate units (e.g. two Unit 5s)

If you see **two Unit 5s** in the Chapter 1.3 guide—e.g. `Unit-5--Collecting-Slots-in-Flows-8b9c` and **`Unit-5--Reading-Slots-in-Actions-0d1e`**—the extra one is a **Codio leftover** from an older structure. The repo has only one Unit 4 and one Unit 5:

- **Unit 4:** `Unit-4--Reading-Slots-in-Actions-0d1e`
- **Unit 5:** `Unit-5--Collecting-Slots-in-Flows-8b9c`

**Fix:** Re-import the project from Git (see below). That replaces the guide with the current repo and removes the duplicate. If you cannot re-import, in Codio’s Guide Editor remove or delete the duplicate section **Unit-5--Reading-Slots-in-Actions-0d1e** from the table of contents (it’s the wrong one; keep **Unit-5--Collecting-Slots-in-Flows-8b9c**).

---

## Units 4 and 5 not showing

If **Unit 4** (Reading Slots in Actions) and **Unit 5** (Collecting Slots in Flows) do not appear in the Chapter 1.3 guide in Codio after pulling from Git, the guide structure in Codio is likely still using an older snapshot.

## What’s in the repo

- **Chapter 1.3** (`.guides/content/Chapter-1-3---Slot-Collection-a4b5/`) includes:
  - `Unit-4--Reading-Slots-in-Actions-0d1e/` with `index.json` and page `.json` + `.md` for 4.1, 4.2, Lab 4.1
  - `Unit-5--Collecting-Slots-in-Flows-8b9c/` with `index.json` and page `.json` + `.md` for 5.1, 5.2, 5.3, Lab 5.1
- The chapter `index.json` lists both units in `order`.

So the repo is the source of truth and is complete.

## What to do in Codio

1. **Re-import the project from Git**  
   So Codio loads the **current** `.guides/content/` (including Units 4 and 5):
   - In Codio: **My Projects** → open the project (or the assignment that uses it).
   - Use **Update from Git** / **Re-import from Git** / **Replace content from Git** (wording depends on your Codio UI) so the workspace and guide content are replaced from the repo.
   - Or: create a **new project** from the same GitHub repo and use that; then point the assignment to the new project if needed.

2. **If you only pulled inside an existing box**  
   The workspace has the new files, but the Guide tab may still be showing the old table of contents. Re-import (step 1) is what refreshes the guide structure from the repo.

3. **If re-import is not available**  
   In **Tools → Guide → Edit**, open the Table of Contents (Index icon) and manually add **Unit 4** and **Unit 5** as sections, then add each page (4.1, 4.2, Lab 4.1, 5.1, 5.2, 5.3, Lab 5.1) and set each page’s content to the corresponding `.md` file under  
   `.guides/content/Chapter-1-3---Slot-Collection-a4b5/Unit-4--.../` and `.../Unit-5--.../`.

## Reference

- **CODIO_SYNC_GUIDE.md** (repo root): “In Codio, re-import the project from Git … so the updated `.guides/content/` is what Codio uses.”
