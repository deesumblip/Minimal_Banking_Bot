# Codio Guide Navigation Bug Report

**Date:** March 2025  
**Environment:** Codio guide preview / published assignment (Guides)  
**Reporter:** [Your name/team]  
**Impact:** Left/right navigation is unreliable; users frequently land on random pages instead of prev/next in sequence.

---

## Summary

**Left (<) and right (>) guide navigation often land on wrong or random pages** instead of the actual previous/next page in sequence. Users cannot reliably step through the guide in order.

- From many pages, pressing **<** or **>** jumps to a different chapter or an unrelated page.
- One reproducible example: from **Level 2, Unit 8, page 8.5**, pressing **<** goes to **Level 1, Unit 0, page 0.1** instead of **Level 2, Unit 8, page 8.4**.
- The problem is not limited to Unit 7/8; navigation is unreliable across the guide.

---

## Steps to Reproduce

1. Open a Codio assignment that uses a **Guides** structure with multiple chapters, each containing multiple units and pages (e.g. Level 1, 1.2, 1.3, …).
2. Navigate to **Level 2 (Custom Actions), Unit 8 (Assessment and Next Steps), last page (8.5 Course Completion Checklist)**.
3. Press the **previous (<)** navigation button.
4. **Observed:** The view jumps to **Level 1, Unit 0, page 0.1** (first page of the guide).
5. **Expected:** The view should go to **Level 2, Unit 8, page 8.4** (previous page in the same unit).

In general, **both < and >** can land on random or wrong pages anywhere in the guide, not just in Unit 7/8.

---

## Likely Cause

We believe the guide viewer identifies the **current page** using a value that is **not unique** across the whole guide, for example:

- **Page title** (e.g. `"8.5 Course Completion Checklist"`), which is the same in Level 1, 1.2, 1.3, etc., or  
- A **path or URL** that does not include the chapter (e.g. only unit + page).

When the user is on a given page, the app may resolve “current page” using a **non-unique** key (e.g. title or a path without chapter). It then picks the wrong index in the flattened page list (e.g. the first match), so prev/next are computed from the wrong position and land on random pages. For example, on **Level 2, 8.5**, the viewer may treat the current page as **Level 1, 8.5**, so “previous” goes 1.1 → 8.4 → … → 0.1.

---

## Content Structure (for reference)

- **Root:** `.guides/content/index.json` has an `order` array listing chapters (e.g. `Chapter-1-1---...`, `Chapter-1-2---...`, …).
- **Per chapter:** Each chapter has an `index.json` with an `order` array of unit folder names (e.g. `Unit-0--...`, …, `Unit-8--...`).
- **Per unit:** Each unit has an `index.json` with an `order` array of **page slugs** (filenames without extension), e.g. `8-1-Knowledge-Check-9fc3`, `8-2-...`, …, `8-5-Course-Completion-Checklist-5f74`.

Page slugs and unit names are **unique across the guide** (different suffixes per chapter). Each page also has a unique `id` in its JSON (e.g. `"id": "bdf7ee5c-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` for Ch1.2 8.5 vs `"id": "8a05d7ec-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` for Ch1.1 8.5).

---

## Request

Please ensure that **prev/next navigation** uses a **unique** identifier for the current page, for example:

1. **Page `id`** from the page JSON, or  
2. **Full path** through the hierarchy (e.g. chapter folder + unit folder + page slug),

so that the “current page” is always the one the user is actually viewing, and prev/next move within the correct linear sequence (chapter order → unit order → page order) without jumping to another chapter.

---

## Workaround we applied (content-side)

We made Level 2 Unit 7 and Unit 8 **page titles** unique by appending `" (Level 2)"` where they would otherwise match other chapters. This may help if the viewer matches by title; if it matches by path/URL only, the fix needs to be in the Codio guide viewer.

---

## Contact

[Your email or support channel]

Thank you for looking into this.
