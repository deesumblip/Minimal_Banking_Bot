# Level 2: Content vs Lab Audit (After Lab 5.1)

**Rule:** Any page that requires students to make **manual manipulations to files or folders** (create, edit, move, delete) must be a **lab with corresponding assessment setup**. Content-only pages (read, run a single command already covered by a lab, or conceptual) do not need to be converted.

This audit covers all content and labs that come **after** Level 2 Lab 5.1.

---

## Summary

| Unit | Section / Page | File/folder manipulations? | Action taken |
|------|----------------|----------------------------|--------------|
| Unit 5 | Lab 5.1 | Yes — create `hours.yml`, create `holiday_hours.yml` | Full step-by-step in lab; single assessment. |
| Unit 5 | 5.1 (includes mixing responses and actions) | No — example YAML only, conceptual | None |
| Unit 6 | *(former 6.1 page merged into Lab 6.1)* | — | **Lab 6.1** covers training overview + `rasa train` + assessment. |
| Unit 6 | 6.2 Common Training Errors | No — reference / how to fix | None |
| Unit 6 | **Lab 6.1** | Run commands (train); no direct file creation by student | Lab with assessment ✓ |
| Unit 6 | *(testing/debugging merged into Lab 6.2)* | No — Inspector, debug panel, common issues | None |
| Unit 6 | **6.4** Level 2 wrap-up (walkthrough, summary, best practices, knowledge check, limitations, L3 preview, checklist; former **8.x** merged) | MCs embedded on 6.4 | None |

---

## Optional manipulation (not converted)

- **Lab 5.1 optional:** “Edit `utter_help` in the domain to include ‘Holiday hours’.” Left as optional; not assessed. If you want it assessed, add a check to the Lab 5.1 grader and mention it in the lab.

---

## Files updated in this audit

- **Lab 5.1** (`level2/Level2_Lab5.1_Content.md`, `.guides/.../Lab-5-1--Using-Actions-in-Flows-e512.md`) — full step-by-step (navigate to data/basics, create hours.yml and holiday_hours.yml with full YAML, verify, optional Inspector). Former 5.2 (Creating a Flow) removed; its instructions were already integrated here.
- **5.1** (`.guides/.../5-1-Actions-vs-Responses-in-Flows-77a8.md`, `Level2_Unit5_Content_5.1_*.md`) — Actions vs responses **and** mixing both in one flow (conceptual; former **5.2** merged here).

Students now have one place for instructions and one assessment (Lab 5.1); no repeated steps across pages.
