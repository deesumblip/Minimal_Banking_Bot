# Level 1: Just Responses - Implementation Overview for Codio Team

## Executive Summary

This document provides implementation guidance for **Level 1: Just Responses** on the Codio platform. Content is split into separate unit, lab, and assessment files (mirroring Level 2) so you can copy/paste into Codio and configure assessments per lab.

**Key goals**:
- Preserve the complete student tutorial content (in separate content and lab files)
- Use the same file naming and structure as Level 2 for consistency
- Support auto-grading for key labs (e.g. Lab 0.1, Lab 6.1) via grader scripts
- Use Codio AI Coach for hints and troubleshooting

### Content Integration Strategy

- **Unit content**: One markdown file per numbered subsection (e.g. `Level1_Unit1_Content_1.1_What-is-a-Conversational-Bot.md`). Copy into Codio Guide Editor as one page per section.
- **Lab content**: One file per lab (e.g. `Level1_Lab6.1_Content.md`) – student-facing instructions. Copy into Codio as the lab’s guide content.
- **Assessment setup**: One file per graded lab (e.g. `Level1_Lab6.1_Assessment_Setup.md`) – implementer instructions, grader script location, and Codio assessment config. Use for Lab-Implementation or internal docs.
- **Source**: The single-document reference remains `CODIO_IMPLEMENTATION_GUIDE_OPTIMISED.md`; the split files are the canonical source for copying into Codio.

---

## File Layout (Level 1)

### Content Files (Copy into Codio)
- `Level1_Unit0_Content_0.1_*.md` … `Level1_Unit0_Content_0.4_*.md`
- `Level1_Unit1_Content_1.1_*.md` … `Level1_Unit1_Content_1.4_*.md`
- … (Units 2–8 same pattern: `Level1_UnitN_Content_N.M_Section-Name.md`)

### Lab Content (Student-facing)
- `Level1_Lab0.1_Content.md` – Virtual environment and Rasa install
- `Level1_Lab2.1_Content.md`, `Level1_Lab2.2_Content.md`, `Level1_Lab2.3_Content.md`
- `Level1_Lab3.1_Content.md` … `Level1_Lab3.4_Content.md`
- `Level1_Lab4.1_Content.md`, `Level1_Lab4.2_Content.md`
- `Level1_Lab5.1_Content.md`
- `Level1_Lab6.1_Content.md`, `Level1_Lab6.2_Content.md`, `Level1_Lab6.3_Content.md`
- `Level1_Lab7.1_Content.md`, `Level1_Lab7.2_Content.md`

### Assessment Setup (Implementers)
- `Level1_Lab0.1_Assessment_Setup.md` – Lab 0.1 grader and config
- `Level1_Lab6.1_Assessment_Setup.md` – Lab 6.1 (training) grader and config
- `Level1_Lab7.2_Assessment_Setup.md` – Lab 7.2 (Build Your Own Feature) – file manipulation: new response + flow
- (Add others per course design: e.g. Lab 2.1, 2.2, 2.3, 3.1–3.4, 4.1, 4.2, 5.1, 6.2, 6.3, 7.1)

---

## Technical Specifications

### Lab Environment
- **Base**: Linux (Ubuntu 22.04 or similar), Python 3.11
- **Rasa**: Rasa Pro (latest stable)
- **Port**: 5005 for Rasa Inspector (port forwarding required on Codio for Unit 6)

### Project Structure (Level 1)
```
level1/
├── domain/
│   └── basics.yml
├── data/
│   ├── basics/
│   │   ├── greet.yml, help.yml, contact.yml
│   │   └── ...
│   └── system/
│       └── patterns/
│           └── patterns.yml
├── config.yml
├── credentials.yml
├── endpoints.yml
├── .env
└── (optional) run_inspector.ps1, load_env.ps1
```

### Grader Scripts
- Store in `.guides/assessments/level1_graders/` (e.g. `lab_0.1_grader.sh`, `lab_6.1_grader.sh`)
- Run from `/home/codio/workspace/level1` (or project root as appropriate)
- Use absolute paths in Codio COMMAND field: `/home/codio/workspace/.guides/assessments/level1_graders/lab_X.X_grader.sh`

---

## Alignment with Level 2 Format

| Level 2 | Level 1 |
|--------|--------|
| `Level2_Course_Outline.md` | `Level1_Course_Outline.md` |
| `Level2_Implementation_Overview.md` | `Level1_Implementation_Overview.md` |
| `Level2_UnitN_Content_N.M_*.md` | `Level1_UnitN_Content_N.M_*.md` |
| `Level2_LabX.Y_Content.md` | `Level1_LabX.Y_Content.md` |
| `Level2_LabX.Y_Assessment_Setup.md` | `Level1_LabX.Y_Assessment_Setup.md` |
| `.guides/assessments/level2_graders/` | `.guides/assessments/level1_graders/` |

Use the same workflow: copy unit content into guide pages, copy lab content into lab pages, then configure assessments using the Assessment_Setup files and grader scripts.
