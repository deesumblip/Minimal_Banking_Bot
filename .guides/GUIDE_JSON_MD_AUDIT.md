# Guide JSON/MD Audit (Chapters 1.1–1.5)

**Date:** Audit run for JSON/MD conflicts and issues that could cause `t.content is not a function` on Codio.

## Summary

- **Order vs files:** Every page id listed in a unit's `order` array has both `<id>.json` and `<id>.md` present. No MISSING MD or MISSING JSON.
- **Orphan (fixed):** Chapter 1.2, Unit 2 had `Lab-2-1--Exploring-the-Actions-Folder-45a5` as an orphan (files present but id not in `order`). **Fixed** by adding that id to Unit 2's `order`.
- **Malformed `path` in `files` (fixed):** Three page JSONs had `"path": "#terminal: "` (trailing space and colon). Codio may treat this as a special target and call `.content()` on the result, causing the error. **Fixed** by changing to `"path": "#terminal"` in:
  - `Chapter-1-1---Just-Responses-d3b4/Unit-0--Prerequisites-and-Setup-1039/0-2-Project-Structure-c2ed.json`
  - `Chapter-1-1---Just-Responses-d3b4/Unit-0--Prerequisites-and-Setup-1039/Lab-0-1--Create-Virtual-Environment-and-Install-Rasa-Pro-4434.json`
  - `Chapter-1-1---Just-Responses-d3b4/Unit-6--Training-and-Testing-9f4e/Lab-6-1-Training-Your-Agent-c3d4.json`

## Notes

- Some Chapter 1.1 pages have `"path": ""` in a `files` entry with `"action": "open"`. If the error persists, consider changing those to a valid path or removing the open action.
- Assessment JSONs: terminal entries in `metadata.opened` had `"content": ""` removed in a previous fix (to avoid `t.content is not a function` in assessments).
