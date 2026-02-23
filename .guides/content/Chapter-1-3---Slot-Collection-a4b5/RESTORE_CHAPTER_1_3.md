# Restoring Chapter 1.3 (Slot Collection) in Codio

If you've deleted Chapter 1.3 from the guide or the workspace, sync it back from the repo as follows.

## 1. Get the files back from Git

- In Codio, open the project and go to the **Terminal**.
- Run:
  ```bash
  cd /home/codio/workspace
  git fetch origin
  git checkout origin/main -- .guides/content/Chapter-1-3---Slot-Collection-a4b5
  ```
  That restores the entire `Chapter-1-3---Slot-Collection-a4b5` folder (and all **9 unit subfolders** and their `.json`/`.md` files) from the current `main` branch without touching the rest of the project.

- **If the chapter folder exists but has no unit folders inside:** the same `git checkout` command above will populate it from the repo. After running it, you should see `Unit-0--...` through `Unit-8--...` under `Chapter-1-3---Slot-Collection-a4b5`.

- Or do a full refresh from Git:
  ```bash
  git pull origin main
  ```
  Use this if you want the whole project (including Chapter 1.3) to match the repo.

## 2. Make sure the guide shows Chapter 1.3

- The course index is in **`.guides/content/index.json`**. It should list:
  - `Chapter-1-1---Just-Responses-d3b4`
  - `Chapter-1-2---Custom-Actions-30d6`
  - `Chapter-1-3---Slot-Collection-a4b5`

- If Chapter 1.3 still doesn’t appear in the Guide tab after pulling:
  - Use **Tools → Guide → Edit** and check the Table of Contents (index).
  - If the chapter is missing from the list, add a section that points to the folder **`Chapter-1-3---Slot-Collection-a4b5`** (or re-import the project from Git so Codio rebuilds the guide from the repo).

## 3. Re-import (alternative)

- **My Projects** → your project → **Update from Git** / **Re-import from Git**.
- That replaces the workspace (and guide) with the repo and restores Chapter 1.3 with all 9 units (0–8).

## What’s in the repo

- **`.guides/content/Chapter-1-3---Slot-Collection-a4b5/`**
  - `index.json` (chapter with 9 units in order)
  - `Unit-0--Recap-What-You-Built-in-Level-2-c2a1/` … through `Unit-8--Assessment-and-Next-Steps-6d7e/`
  - Each unit has `index.json` and page `.json` + `.md` files.

The repo is the source of truth; restoring that folder (and the parent `content/index.json` if needed) brings Chapter 1.3 back.
