# Level 2: Content vs Lab Audit (After Lab 5.1)

**Rule:** Any page that requires students to make **manual manipulations to files or folders** (create, edit, move, delete) must be a **lab with corresponding assessment setup**. Content-only pages (read, run a single command already covered by a lab, or conceptual) do not need to be converted.

This audit covers all content and labs that come **after** Level 2 Lab 5.1.

---

## Summary

| Unit | Section / Page | File/folder manipulations? | Action taken |
|------|----------------|----------------------------|--------------|
| Unit 5 | Lab 5.1 | Yes — create `hours.yml`, create `holiday_hours.yml` | Full step-by-step in lab; single assessment. |
| Unit 5 | 5.2 Mixing Responses and Actions | No — example YAML only, conceptual | None |
| Unit 6 | 6.1 Training with Actions | No — run `rasa train`; model file is created by command | **Lab 6.1** already exists and assesses training / model file. |
| Unit 6 | 6.2 Common Training Errors | No — reference / how to fix | None |
| Unit 6 | **Lab 6.1** | Run commands (train); no direct file creation by student | Lab with assessment ✓ |
| Unit 6 | 6.3 Testing Your Action | No — run Inspector, use GUI | None |
| Unit 6 | 6.4 Debugging Actions | No — read debug output, check files | None |
| Unit 7 | 7.1, 7.2, 7.3 | No — walkthrough, summary, best practices | None |
| Unit 8 | 8.1–8.5 | No — knowledge check, review, checklist | None |

---

## Optional manipulation (not converted)

- **Lab 5.1 optional:** “Edit `utter_help` in the domain to include ‘Holiday hours’.” Left as optional; not assessed. If you want it assessed, add a check to the Lab 5.1 grader and mention it in the lab.

---

## Files updated in this audit

- **Lab 5.1** (`level2/Level2_Lab5.1_Content.md`, `.guides/.../Lab-5-1-e512.md`) — full step-by-step (navigate to data/basics, create hours.yml and holiday_hours.yml with full YAML, verify, optional Inspector). Former 5.2 (Creating a Flow) removed; its instructions were already integrated here.
- **5.2** (`level2/Level2_Unit5_Content_5.2_Mixing-Responses-and-Actions.md`, `.guides/.../5-2-Mixing-Responses-and-Actions-bdb7.md`) — Mixing Responses and Actions (conceptual only).

Students now have one place for instructions and one assessment (Lab 5.1); no repeated steps across pages.
