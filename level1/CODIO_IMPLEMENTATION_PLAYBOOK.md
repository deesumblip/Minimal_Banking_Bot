# Level 1 Codio Implementation Playbook

**Purpose**: Translate `level1/CODIO_IMPLEMENTATION_GUIDE.md` into a Codio-native learning experience without modifying the source guide. This document is scoped to Level&nbsp;1 (“Just Responses”) and addresses the Codio-specific tasks the content team, platform team, and instructors need to complete.

---

## 1. Reference Materials

Use the sources below when implementing or auditing the Codio course. Each section in this playbook cites the relevant documentation.

- Level 1 full curriculum & reference: `level1/CODIO_IMPLEMENTATION_GUIDE.md`
- Codio Guides editor & markdown features: [Codio Guides documentation](https://www.codio.com/docs/guides)
- Auto-grading options (code tests, MCQ, Parsons, etc.): [Codio Auto-Grading overview](https://www.codio.com/features/auto-grading) and [Global Assessments Library announcement](https://www.codio.com/blog/codio-launches-global-assessments-library)
- AI-powered Virtual Coach: [Virtual Coach settings](https://docs.codio.com/instructors/setupcourses/assignment-settings/virtual-coach.html)
- Code Playback tooling: [Code Playback docs](https://docs.codio.com/common/tools/code-playback.html)
- Analytics & Behavior Insights: [Learning Insights](https://www.codio.com/features/learning-insights) and [Behavior Insights configuration](https://docs.codio.com/instructors/teaching/behaviorinsights.html)

---

## 2. Authoring the Codio Guide

1. **Create the `.guides` workspace** via **Tools → Guides → Edit**. Codio will scaffold the folder and `guide.md`. (See [Guides docs](https://www.codio.com/docs/guides)).  
2. **Mirror the Level 1 table of contents** by creating a top-level section for each unit (0–8). Inside each section:
   - Copy the corresponding student-facing markdown from the existing guide.
   - Use layout directives so the correct files/terminals open automatically (e.g., open `domain/basics.yml` in Unit 2).
   - Embed screenshots or GIFs in `.guides/img/` for visual references.
3. **Add interactive controls**:
   - `{Run Train}(python -m rasa train)` buttons for CLI steps.
   - Embedded quizzes (multiple choice, checkbox) for concept checks.
   - Tabs/snippets for Windows vs. Mac/Linux commands.
4. **Preview frequently** using the Guides preview icon to confirm navigation, automatic file opens, and command buttons work.

**Outcome**: Every instruction from the reference guide lives in Codio Guides with contextual tooling so students never leave the IDE.

---

## 3. Designing Assessments & Auto-Graders

| Goal | Action Items | Reference |
| --- | --- | --- |
| Convert walkthroughs into labs | For each hands-on subsection (Units 2–7), append an “Exercise” page with clear success criteria and a “Check my work” button. | [Auto-grading overview](https://www.codio.com/features/auto-grading) |
| Validate YAML + flows | Write Python-based graders that parse `domain/basics.yml`, `data/basics/*.yml`, and ensure required keys exist. Use deterministic error messages (e.g., “Missing `utter_contact` response”). | same as above |
| Scripted bot tests | Drive `rasa inspect` or `rasa run actions` via headless scripts. Compare JSON outputs against expected utterances. Timeout after 60s with actionable hints. | same |
| Concept checks | Pull templates from the Global Assessments Library, disconnect as needed, and localize to banking-bot vocabulary. | [Assessments library](https://www.codio.com/blog/codio-launches-global-assessments-library) |
| Rubrics | For Unit 8 assessment, use Codio’s rubric widget so partial credit matches the “Assessment Specifications” section from the source guide. | same |

> **Tip**: Keep graders language-agnostic (pure Python) so they run inside Codio’s Ubuntu 22.04 stack without extra dependencies.

---

## 4. Configuring Codio Coach (Virtual Coach)

1. Enable Virtual Coach per assignment (Units 0–8). ([Virtual Coach docs](https://docs.codio.com/instructors/setupcourses/assignment-settings/virtual-coach.html))
2. Populate the three coach modes:  
   - **Summarize Prompt** – bullet the key tasks (“1. Open `domain/basics.yml`; 2. Add `utter_help` ...”).  
   - **Error Augmentation** – instruct students to paste CLI tracebacks to receive plain-English explanations.  
   - **Next Steps** – provide gentle hints (“Have you run `rasa data validate` after editing?”).
3. Calibrate tone so hints reference files/commands but never paste final answers.
4. Export Coach logs weekly; convert high-frequency questions into new FAQ blocks inside the Guides.

---

## 5. Instrumenting Code Playback

1. Turn on Code Playback for every unit that edits files (Units 2–7 plus the final assessment). ([Code Playback docs](https://docs.codio.com/common/tools/code-playback.html))  
2. Target files: `domain/basics.yml`, `data/basics/*.yml`, `config.yml`, and any helper scripts students touch.  
3. During QA, scrub through recordings to verify:  
   - Keystrokes are captured (play/pause, speed control).  
   - Copy/paste segments appear in green (useful for academic integrity).  
   - Multi-file navigation is retained.  
4. Document procedures for recovering deleted files using Playback (helpful for student support).

---

## 6. Analytics, Behavior Insights, and LMS Integration

### Analytics & Behavior Insights
- Enable the Learner Insights dashboards for the course to monitor time-on-task, attempt counts, and grade deltas. ([Learning Insights](https://www.codio.com/features/learning-insights))  
- Configure Behavior Insights thresholds ([docs](https://docs.codio.com/instructors/teaching/behaviorinsights.html)):  
  - Time spent per assignment (flag <5 min or >90 min).  
  - Edit rate (flag >4 chars/sec for potential plagiarism).  
  - Debugging ratio (flag <4% debug time).  
- Schedule weekly exports for instructors; share flagged students for early intervention.

### LMS / Grade Passback
- Align each Codio assignment with the institutional LMS via LTI or grade sync.  
- Mirror the Level 1 rubric inside the LMS to keep grading transparent.  
- Run an end-to-end test: enroll a dummy student, complete Units 0–2, confirm grades/time sync correctly.

---

## 7. Recommended Timeline Slice (Two-Week Program)

Level 1 should be completed during the opening sprint so the remaining levels can reuse its assets.

| Day | Focus | Deliverables |
| --- | --- | --- |
| Week 1, Day 1 | Environment freeze + Guides skeleton | Codio project cloned from `level1/`, stack verified (Ubuntu 22.04 + Python 3.11 + `rasa-pro`), `.guides` structure created, Units 0–2 content migrated, layouts validated. |
| Week 1, Day 2 | Assessments + instrumentation | Auto-graders wired to Unit 0–2 exercises, Virtual Coach enabled with prompt summaries, Code Playback & Behavior Insights toggled on, quick LMS smoke test performed. |

Hand off to the next level only after the Quality Assurance Checklist items are satisfied and analytics confirm the sample walkthrough passes.

---

## 8. Handoff Checklist

- [ ] `.guides` content mirrors every Unit/subsection.  
- [ ] All exercises have an attached auto-grader with helpful failure messages.  
- [ ] Virtual Coach prompt summaries exist per unit; logs reviewed weekly.  
- [ ] Code Playback enabled and verified for target files.  
- [ ] Behavior Insights/analytics dashboards monitored; alerts configured.  
- [ ] LMS grade sync tested end-to-end.  
- [ ] Documentation for instructors includes: resetting the stack, reviewing Playback, accessing Coach logs, and interpreting analytics.

Once all boxes are checked, the Codio course is ready for launch without touching the source guide. Future enhancements (e.g., new assessments, localized content) can build on this playbook while keeping `CODIO_IMPLEMENTATION_GUIDE.md` as the canonical reference.
