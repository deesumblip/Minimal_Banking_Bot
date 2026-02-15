# Level 1 chapter migration: Chapter-1-1 as ground truth

We use **Chapter-1-1---Just-Responses-d3b4** as the single source of truth for Level 1 (Just Responses) on both Codio and in the main repo. The old chapter **Level-1-1-d3b4** has been moved to **level1/old_duplicates/Level-1-1-d3b4** and is no longer referenced in the course.

---

## What was done

1. **Parked** `.guides/content/Level-1-1-d3b4` → **level1/old_duplicates/Level-1-1-d3b4** (no longer in the guide order).
2. **Course order** in `.guides/content/index.json` now points to **Chapter-1-1---Just-Responses-d3b4** instead of Level-1-1-d3b4.
3. **Placeholder** `.guides/content/Chapter-1-1---Just-Responses-d3b4/` exists in the repo (with a README). The actual page content lives on Codio until you complete the steps below.

---

## How to make the repo the ground truth (clone from Codio)

Chapter-1-1---Just-Responses-d3b4 already exists on Codio with full content (Units 0–6). To make the same content the ground truth in this repo so you can clone and edit it locally:

### Option A: Copy from Codio workspace (recommended)

1. **On Codio**, open the project and locate the chapter folder. It is usually under:
   - `guides/content/Chapter-1-1---Just-Responses-d3b4` or  
   - `.guides/content/Chapter-1-1---Just-Responses-d3b4`
2. **Download or copy** the entire folder (including all unit subfolders and `index.json`). You can:
   - Right-click the folder in the file tree → Download / Export, or  
   - Use the Codio terminal to zip it:  
     `cd guides/content && zip -r Chapter-1-1.zip "Chapter-1-1---Just-Responses-d3b4"` then download the zip.
3. **Locally**, open your cloned repo and go to `.guides/content/`.
4. **Replace** the contents of `.guides/content/Chapter-1-1---Just-Responses-d3b4/`:  
   - Remove the existing README (or keep it at the bottom of the folder if you like).  
   - Unzip or paste the Codio export so that `Chapter-1-1---Just-Responses-d3b4` contains:
     - `index.json` (chapter order)
     - `Unit-0--Prerequisites-and-Setup-1039/` (and its pages)
     - `Unit-1--Introduction-to-Rasa-Bots-06a7/`
     - … through **Unit-6--Training-and-Testing-6c70** (or the exact unit folder names you see on Codio).
5. **Commit and push:**
   ```bash
   git add .guides/content/Chapter-1-1---Just-Responses-d3b4
   git commit -m "Add Chapter-1-1 (Just Responses) as ground truth from Codio"
   git push
   ```
6. **On Codio**, re-import the project from Git (or pull and refresh). The course should still show the same chapter; from now on, edits in the repo under `.guides/content/Chapter-1-1---Just-Responses-d3b4/` are the ground truth for both Codio and any future clone.

### Option B: Codio Git push (if you use Codio → Git)

If Codio is set up to push to the same repo:

1. In Codio, ensure the chapter folder is under the path that maps to `.guides/content/` in the repo.
2. Commit and push from Codio so that `.guides/content/Chapter-1-1---Just-Responses-d3b4` is pushed to the main repo.
3. Pull locally; the repo now has the ground truth.

---

## After migration

- **Single source of truth:** Edit Level 1 (Just Responses) only under **`.guides/content/Chapter-1-1---Just-Responses-d3b4/`** in the repo. Sync to Codio by pushing and re-importing (or pulling) there.
- **Old content:** The previous chapter is archived at **level1/old_duplicates/Level-1-1-d3b4**. You can delete that folder later if you no longer need it for reference.
