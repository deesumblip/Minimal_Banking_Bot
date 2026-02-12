# Syncing Course Content to Codio

This guide explains how Codio content is structured and how to **sync your edits** from this repo (e.g. `level2/` sections and labs) so that **each page in Codio equals one lab or section**.

---

## How Codio content is organized

Codio Guides use a **hierarchy of JSON + Markdown** under `.guides/content/`:

1. **Root**  
   - `.guides/content/index.json` — lists **chapters** (e.g. Level 1.1, Level 2.1) and their order.

2. **Chapter** (e.g. Level 2.1)  
   - A folder like `Level-2-1-<id>/` with an `index.json` that lists **sections** (units) and their order.

3. **Section (Unit)** (e.g. Unit 4)  
   - A folder like `Unit-4--Registering-Actions-in-the-Domain-<id>/` with:
   - `index.json` — lists **pages** (individual content/lab files) and their order.
   - One **page** = one `.md` file + one `.json` metadata file (e.g. `4-4-Multiple-Actions-a1b2.md` and `4-4-Multiple-Actions-a1b2.json`).

So: **one Codio “page” = one section or one lab**. You keep editing the source files in `level2/` (or `level1/`); a sync process copies them into `.guides/content/` in this shape.

---

## Two ways to populate Codio

### Option A: Sync script (recommended for many edits)

Use the script that copies **Level 2** source files into `.guides/content` so each section/lab becomes one page:

```bash
# From repo root
python sync_level2_to_codio.py
```

- **Reads from:** `level2/Level2_Unit*_Content_*.md` and `level2/Level2_*_Assessment.md`.
- **Writes to:** `.guides/content/Level-2-1-<id>/Unit-<N>--<Title>-<id>/` with one `.md` + `.json` per page.
- **Result:** Each of your Level 2 content files and each assessment becomes one Codio page; order follows the course outline.
- **Preserves Codio assessments:** If a page `.json` already exists (e.g. you attached an AI-generated assessment in Codio), the script **merges** instead of overwriting: it updates only the page **title** from your local content and keeps all other fields (assessment links, `taskId`, `files`, layout, etc.). The `.md` content is always updated from local so your edits sync; only the metadata is preserved where it already exists.

After running the script:

- Commit and push the changes under `.guides/content/`.
- In Codio, **re-import the project from Git** (or use Codio’s content import if you use it), so the updated `.guides/content/` is what Codio uses.

**When to run:** Whenever you change one or more sections or labs in `level2/` and want those changes reflected in Codio.

---

### Option B: Manual in Codio

If you prefer not to use the script:

1. In Codio, open **Guides** (or **Content** / **Curriculum**).
2. Create or open the **Level 2** chapter and the **Units** (sections).
3. For each **page** (one section or one lab):
   - Create a new page.
   - Paste or type the content (or upload the markdown); you can copy from the corresponding `level2/*.md` file.

This gives you full control but is slower when you change many sections. The script is meant to avoid re-pasting after each edit.

---

## Making “one page = one section or lab”

- **Sections:** Each `Level2_Unit<N>_Content_<X>.<Y>_<Name>.md` is intended to become **one** Codio page (e.g. “4.4 Multiple Actions”).
- **Labs:** Each assessment file (e.g. `Level2_Unit4_Assessment.md`) is intended to become **one** Codio page (e.g. “Lab 4.1”).

The sync script maps these files into the Unit folders and sets the page order in each unit’s `index.json` so that the Codio order matches the course outline. No need to manually split or merge unless you want a different page structure.

---

## Level 1 content

Level 1 is already under `.guides/content/Level-1-1-d3b4/`. If you later add a similar script for Level 1 (e.g. `sync_level1_to_codio.py`), it would:

- Read from `level1/` (or the Level 1 source files you use).
- Write into the same `Level-1-1-*` structure so each section/lab stays one page.

For now, Level 1 can be updated by editing the markdown files under `.guides/content/Level-1-1-d3b4/` directly, or by restoring a Level 1 sync script if you had one.

---

## Summary

| Goal | Approach |
|------|----------|
| One page = one section or lab | Structure under `.guides/content/` so each unit has one `.md` (and `.json`) per section/lab; the sync script does this for Level 2. |
| Sync after editing sections | Run `python sync_level2_to_codio.py`, then commit/push and re-import in Codio (or use Codio’s import). |
| Populate Codio from this repo | Use the script to fill `.guides/content/`, then use Codio’s Git import or content import so Codio loads that structure. |
