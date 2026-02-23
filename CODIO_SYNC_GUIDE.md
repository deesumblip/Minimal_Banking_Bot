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
- In Codio, **re-import the project from Git** (or use Codio’s content import if you use it), so the updated `.guides/content/` is what Codio uses. **Without re-import, the Guide tab may keep showing an older table of contents** (e.g. new units like Chapter 1.3 Units 4 and 5 won't appear even after a pull). See `.guides/content/Chapter-1-3---Slot-Collection-a4b5/CODIO_UNITS_4_5_SYNC.md` if those units don't show.

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
- **Labs:** Each `Level2_Lab*_Content.md` file is synced to **one** student-facing Codio lab page; each `Level2_Lab*_Assessment_Setup.md` is synced to `Lab-Implementation/` (instructor-only) (e.g. “Lab 4.1”).

The sync script maps these files into the Unit folders and sets the page order in each unit’s `index.json` so that the Codio order matches the course outline. No need to manually split or merge unless you want a different page structure.

---

## Level 1 content

Level 1 (Just Responses) uses **Chapter-1-1---Just-Responses-d3b4** as the single source of truth. It lives at `.guides/content/Chapter-1-1---Just-Responses-d3b4/`. The old chapter **Level-1-1-d3b4** has been moved to **level1/old_duplicates/Level-1-1-d3b4**.

- **On Codio:** The full chapter (Units 0–6) already exists. Keep using it there.
- **In the repo:** To make the repo the ground truth, copy the chapter from Codio into `.guides/content/Chapter-1-1---Just-Responses-d3b4/` and push. See **level1/MIGRATION_LEVEL1_CHAPTER.md** for step-by-step instructions.

After that, edit Level 1 by changing the markdown and JSON under `.guides/content/Chapter-1-1---Just-Responses-d3b4/`, then commit, push, and re-import in Codio.

---

## Summary

| Goal | Approach |
|------|----------|
| One page = one section or lab | Structure under `.guides/content/` so each unit has one `.md` (and `.json`) per section/lab; the sync script does this for Level 2. |
| Sync after editing sections | Run `python sync_level2_to_codio.py`, then commit/push and re-import in Codio (or use Codio’s import). |
| Populate Codio from this repo | Use the script to fill `.guides/content/`, then use Codio’s Git import or content import so Codio loads that structure. |
