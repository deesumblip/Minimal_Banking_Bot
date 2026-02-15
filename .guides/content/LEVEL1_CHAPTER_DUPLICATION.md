# Level 1 chapter duplication: Chapter-1-1 vs Level-1-1

**Status: Resolved.** Level-1-1-d3b4 has been moved to **level1/old_duplicates/Level-1-1-d3b4**. The course now uses **Chapter-1-1---Just-Responses-d3b4** as the single source of truth. See **level1/MIGRATION_LEVEL1_CHAPTER.md** for how to populate that chapter in the repo from Codio.

---

## What’s in the repo (before migration)

| Item | In repo? | Content |
|------|----------|--------|
| **Level-1-1-d3b4** | Yes | Units 0–3 only (unit folders and pages exist). `index.json` order also lists Units 4–6 but those unit folders do **not** exist under this chapter in the repo. |
| **Chapter-1-1---Just-Responses-d3b4** | No | Not in the repo. On Codio it has Units 0–6. |

The root `.guides/content/index.json` lists only **Level-1-1-d3b4** as the first chapter. So when you import from Git, Codio gets that chapter (0–3) and does not get Chapter-1-1 from the repo. If you see **Chapter-1-1---Just-Responses-d3b4** on Codio, it was created there (or by a different import) and is the one with full Units 0–6.

So on Codio you effectively have two Level 1 chapters:

- **Chapter-1-1---Just-Responses-d3b4** – full 0–6 (only on Codio).
- **Level-1-1-d3b4** – 0–3 (from repo). Units 0–3 overlap with the chapter above → **duplication**.

## How to check if Level-1-1 duplicates Chapter-1-1 (Units 0–3)

You need both chapters on disk, then compare overlapping units.

### 1. Get both chapters on disk

- **Level-1-1-d3b4** is already at:  
  `.guides/content/Level-1-1-d3b4/`
- **Chapter-1-1---Just-Responses-d3b4** is only on Codio. To get it:
  - In Codio: right‑click the chapter folder → export/download, or use Codio’s Git integration to push that folder into the repo, then pull locally; or
  - Copy the folder from the Codio workspace (e.g. `guides/content/Chapter-1-1---Just-Responses-d3b4`) into this repo, e.g. under `.guides/content/` for the comparison.

Put the copied chapter next to Level-1-1, e.g.:

- `.guides/content/Level-1-1-d3b4/`
- `.guides/content/Chapter-1-1---Just-Responses-d3b4/`   (temporary copy)

### 2. Compare overlapping units (0–3)

Unit folder names may differ slightly (e.g. `Unit-3--Understanding-Flows-d9bc` vs `Unit-3-Understanding-Flows-6c70`). So compare by **content** for the same logical unit.

From the **repo root** you can:

**List corresponding files (e.g. Unit 0):**

```powershell
# PowerShell
$L = ".guides/content/Level-1-1-d3b4"
$C = ".guides/content/Chapter-1-1---Just-Responses-d3b4"
Get-ChildItem -Path $L -Recurse -File | ForEach-Object { $_.FullName.Replace((Resolve-Path $L).Path + "\", "") }
Get-ChildItem -Path $C -Recurse -File | ForEach-Object { $_.FullName.Replace((Resolve-Path $C).Path + "\", "") }
```

**Diff one file that exists in both (example):**

```powershell
# Example: compare a page that exists in both (adjust paths to real unit/page names)
$f = "Unit-0--Prerequisites-and-Setup-1039/0-1-What-You-Need-Before-Starting-1234.md"
diff (Get-Content ".guides/content/Level-1-1-d3b4/$f") (Get-Content ".guides/content/Chapter-1-1---Just-Responses-d3b4/$f")
```

Or use the comparison script below.

### 3. Run the comparison script (optional)

From the repo root, run:

```powershell
.\.guides\content\compare_level1_chapters.ps1
```

That script will list and diff matching `.md` files under Units 0–3 between the two chapters (see script for exact paths and naming).

## Recommendation: use one chapter and remove the other

- **Keep** the chapter that has the full course (Units 0–6): **Chapter-1-1---Just-Responses-d3b4** on Codio.
- **Remove the duplicate**:
  - In the **repo**: remove `Level-1-1-d3b4` from `.guides/content/index.json` and delete the folder `.guides/content/Level-1-1-d3b4` if you no longer want it in Git; **or**
  - On **Codio**: remove or hide the **Level-1-1-d3b4** chapter from the course so only Chapter-1-1 appears.

Then either:

- **Option A – Codio as source of truth for Level 1:** Keep Chapter-1-1 only on Codio; repo no longer has a Level 1 chapter (or has a copy for reference only). Root `index.json` would list only Chapter-1-2, or you add Chapter-1-1 to the repo by copying it from Codio and add it to `index.json`.  
- **Option B – Repo as source of truth:** Copy the full **Chapter-1-1---Just-Responses-d3b4** (0–6) from Codio into the repo as the single Level 1 chapter, update root `index.json` to point to it, then remove **Level-1-1-d3b4** so there is no duplication.

After that, re-import from Git (or refresh content) so the TOC shows only one Level 1 chapter with Units 0–6.
