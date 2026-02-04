# Level 1 – Codio Delivery Manual (Just Responses)

This document stitches together the full Level 1 course content and all Codio platform tasks so a first‑time Codio implementer can build and launch the lab without consulting separate references. Keep the original files nearby (`CODIO_IMPLEMENTATION_GUIDE.md` for student content, `CODIO_IMPLEMENTATION_PLAYBOOK.md` for the standalone plan), but everything you need is summarized or repeated here.

---

## 0. Orientation

### Prerequisites Checklist

- Codio account with permissions to create projects and enable Guides/assessments.
- Rasa Pro Developer Edition licence key and OpenAI API key (for `.env` template).
- Familiarity with basic Git commands (optional but recommended for resets).
- Estimated time available: two full workdays (Week 1 Day 1–2 on the master timeline).
- Disk quota of at least 2 GB per Codio box (Rasa models + logs).

### Overview

- **Course goal**: teach students to build the “Just Responses” banking bot—responses only, no custom code yet.
- **Audience**: students, instructors, and Codio platform implementers.
- **Output**: a Codio project with Guides, auto-graded labs, Virtual Coach, Code Playback, analytics dashboards, and LMS passback, ready in **2 days** (Week 1 Day 1–2 of the sprint).
- **Repository source**: copy the `level1/` workspace from this repo into a new Codio project.

---

## 1. Course Content Snapshot (Student Experience)

| Unit | Focus | Student Outcomes |
| --- | --- | --- |
| Unit 0 | Prerequisites & environment verification | Confirm Python 3.11, Rasa Pro install, `.env` variables |
| Unit 1 | Intro to Rasa bots | Understand bot vs. traditional app |
| Unit 2 | Domain file (responses) | Create and edit `utter_*` responses |
| Unit 3 | Flows basics | Wire flows that call responses |
| Unit 4 | System patterns | Configure `pattern_session_start` & `pattern_completed` |
| Unit 5 | Config files | Review pipeline, policies, credentials |
| Unit 6 | Training/testing | Run `rasa train`, `rasa inspect` |
| Unit 7 | Putting it together | End-to-end checks |
| Unit 8 | Assessment & next steps | Knowledge check + preview of Level 2 |

> **Tip**: The full student narrative, walkthroughs, screenshots, troubleshooting, glossary, and appendices live in `CODIO_IMPLEMENTATION_GUIDE.md`. When copying text into Codio Guides, lift the relevant sections verbatim.

---

## 2. Codio Workspace Setup (Do This First)

1. **Create Codio project**
   - From Codio dashboard: *Projects → New Project → Import from Git* using this repo URL or upload a zip containing `level1/`.
   - Name it `BankingBot-Level1`.
2. **Select stack**
   - Choose the standard Ubuntu 22.04 stack. After provisioning, run:
     ```bash
     python3.11 -V
     pip --version
     python3.11 -m pip install --no-cache-dir rasa-pro
     ```
   - If `python3.11` is missing, install with `sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update && sudo apt install python3.11 python3.11-venv`.
3. **Copy project files**
   - Ensure the Codio file tree matches:
     ```
     /home/codio/workspace/
       └── level1/
           ├── domain/
           ├── data/
           ├── config.yml
           ├── credentials.yml
           ├── endpoints.yml
           ├── load_env.ps1 (reference only)
           └── ...
     ```
   - Delete extra folders if needed so students only see Level 1 files.
   - **Codio OS reminder**: Codio workspaces run Ubuntu Linux. Any Windows-specific commands in the course (e.g., `Activate.ps1`) are included for reference only—do not document or run them inside Codio.
4. **Initialize Git (optional but recommended)**
   ```bash
   cd level1
   git init
   git add .
   git commit -m "Codio baseline for Level 1"
   ```
5. **Create `.env` template**
   - In `level1/`, create `.env.template` with placeholder keys:
     ```text
     RASA_LICENSE=YOUR_LICENSE_KEY
     OPENAI_API_KEY=YOUR_OPENAI_KEY
     ```
   - Students copy to `.env` during Unit 0.
6. **Sanity check**
   - Run `python3.11 -m venv .venv && source .venv/bin/activate` (Linux) or `py -3.11 -m venv .venv` (Windows note for documentation) and then `python -m rasa --version` to confirm dependencies resolve.

---

## 3. Codio Guides Authoring (Step-by-Step)

### 3.1 Create Guides framework
1. In Codio menu: **Tools → Guides → Edit**. The IDE creates `.guides/guide.md`.
2. Click the gear icon in the Guide editor → **Layout**. Choose **Split (Guide + Code + Terminal)** so instructions, files, and terminal show side by side.
3. In `.guides/guide.md`, set metadata:
   ```markdown
   title: Level 1 – Just Responses
   description: Build the Level 1 Rasa banking bot with responses only.
   ```

### 3.2 Build the table of contents
Copy the template below and paste into `guide.md`. Replace `<CONTENT>` with text from the Level 1 guide. Each section automatically creates a sidebar entry.

```markdown
## Welcome
<CONTENT: overview + objectives from the guide — source at `CODIO_IMPLEMENTATION_GUIDE.md` → “Course Introduction”>

## Unit 0 – Prerequisites & Setup
@open{"path":"/home/codio/workspace/level1/README.md"}
<CONTENT: environment checks, .env instructions, verifying Python — see “Unit 0” section in the implementation guide>

## Unit 1 – Introduction to Rasa Bots
<CONTENT drawn from guide “Unit 1: Introduction to Rasa Bots”>

## Unit 2 – Working with Responses
@open{"path":"/home/codio/workspace/level1/domain/basics.yml"}
<CONTENT + step-by-step edits — copy from “Unit 2: Understanding the Domain File”>

## Unit 3 – Creating Flows
@open{"path":"/home/codio/workspace/level1/data/basics/greet.yml"}
<CONTENT from “Unit 3: Understanding Flows”>

## Unit 4 – System Patterns
@open{"path":"/home/codio/workspace/level1/data/system/patterns/patterns.yml"}
<CONTENT from “Unit 4: System Patterns”>

## Unit 5 – Configuration Files
@open{"path":"/home/codio/workspace/level1/config.yml"}
<CONTENT from “Unit 5: Configuration Files”>

## Unit 6 – Train & Inspect
@open{"path":"/home/codio/workspace/level1"} 
@term{"command":"python -m rasa train"}
<CONTENT from “Unit 6: Training and Testing”>

## Unit 7 – End-to-End Validation
<CONTENT from “Unit 7: Putting It All Together”>

## Unit 8 – Assessment & Next Steps
<CONTENT + assessment instructions from “Unit 8: Assessment and Next Steps”>

## Troubleshooting & Glossary
<Copy relevant sections verbatim from “Troubleshooting Guide” and “Glossary”>
```

> **Guide authoring tips**  
> - Use `{Run Train}(python -m rasa train)` buttons for repeatable commands.  
> - Convert note blocks from the guide into Codio callouts: `:::note ... :::`.  
> - Embed media by uploading to `.guides/img/` and referencing `![alt text](.guides/img/<file>.png)`.

---

## 4. Auto-Graded Labs & Assessments

Create Codio assessments at the bottom of relevant Guide sections. Suggested mapping:

| Guide Section | Assessment Type | Implementation Notes |
| --- | --- | --- |
| Unit 0 | Code Test | Run `python -m rasa --version`, `ls` for `.env`, fail with actionable hint if missing. |
| Unit 2 | Code Test + MCQ | Validate `domain/basics.yml` contains `utter_greet/help/contact`; MCQ about response best practices. |
| Unit 3 | Code Test | Parse `data/basics/greet.yml` for correct steps; confirm `rasa data validate` passes. |
| Unit 4 | Code Test | Ensure `pattern_session_start` & `pattern_completed` exist and include expected events. |
| Unit 6 | Scripted Test | Run `python -m rasa train` (timeout 120s); fail gracefully on error. |
| Unit 7 | Scripted Conversation | Use `python -m rasa inspect --script scripts/level1_happy_path.json` to ensure greet/help/contact responses fire. |
| Unit 8 | Rubric Assessment | Criteria: guide comprehension, correct bot behavior, reflection question. |

**Implementation recipe (Code Test example)**  
1. In the Guide editor, click **Add Assessment → Code Test**.  
2. Use the following shell snippet as starter:
   ```bash
   #!/bin/bash
   cd /home/codio/workspace/level1
   python -m rasa --version >/tmp/rasa_version.txt 2>&1
   if ! grep -q "Rasa" /tmp/rasa_version.txt; then
     echo "Rasa not installed or virtualenv not activated."
     exit 1
   fi
   ```
3. Add custom failure messages (Assessment Settings → **Fail Message**).  
4. Save and test using the **Preview** button.

> **Debug tip**: Place reusable graders under `.guides/graders/`. Use Python for YAML parsing (see `yaml.safe_load`).

---

## 5. Virtual Coach (AI Assistant) Setup

1. Open **Education → Settings → Features** for the assignment. Toggle **Virtual Coach** on.  
2. Configure each mode:
   - **Summarize Prompt**: provide 3–5 bullet instructions per unit (copy from Unit intros). Example for Unit 2: “Open `domain/basics.yml`; add `utter_help`; save and run `rasa data validate`.”
   - **Error Augmentation**: paste common stack traces from the guide’s Troubleshooting section and map to friendly explanations.
   - **Next Steps**: suggest running `python -m rasa train` or checking YAML indentation when errors appear.
3. Test by opening the student preview, triggering a failure, and confirming Coach responds with the guidance you expect.
4. Plan to export Coach logs weekly (Education → Monitoring) and add new FAQs to the Guides if patterns emerge.

---

## 6. Code Playback & Analytics

### 6.1 Enable Code Playback
1. Open **Education → Monitoring → Code Playback** and ensure it’s enabled for the assignment.  
2. Specify tracked files:  
   - `domain/basics.yml`  
   - `data/basics/*.yml`  
   - `data/system/patterns/patterns.yml`  
   - `config.yml`, `credentials.yml`, `endpoints.yml`
3. Record a sample session by editing a file in preview mode, then verify playback shows keystrokes and paste events (green bars).

### 6.2 Configure Analytics & Behavior Insights
1. In **Education → Monitoring → Behavior Insights**, set thresholds:  
   - Time spent min/max: 10 minutes / 90 minutes  
   - Edit speed alert: >4 characters per second  
   - Debugging ratio alert: <5%
2. Enable **Learning Insights dashboards** for instructors to view time-on-task and grades per unit.
3. Document how to access dashboards in the instructor handoff notes.

---

## 7. Optional: LMS Integration

1. If using LTI/grade sync, open **Education → Settings → Integrations** and connect your LMS.  
2. Map each Codio assessment to an LMS grade item. Weight Level 1 at 20% of the multi-level course (adjust to your syllabus).  
3. Run a smoke test: complete Unit 0 in preview mode, trigger the grader, and confirm the LMS gradebook updates.

---

## 8. Two-Day Implementation Timeline

| Day | Morning (4 hrs) | Afternoon (4 hrs) |
| --- | --- | --- |
| Week 1 – Day 1 | Workspace setup, `.env` template, Guides skeleton (Welcome + Units 0–2) | Complete Guides Units 3–5, embed media, create first wave of assessments |
| Week 1 – Day 2 | Finish Guides Units 6–8, add troubleshooting & glossary, wire remaining assessments | Enable Virtual Coach, Code Playback, analytics, LMS sync; execute QA run and document instructor notes |

> **Daily standup checklist**  
> - [ ] Guides preview works without errors  
> - [ ] All assessments run and report meaningful failures  
> - [ ] Virtual Coach responds to a simulated question  
> - [ ] Playback shows keystrokes for a sample session  
> - [ ] LMS test entry received

---

## 9. Final QA Walkthrough

1. **Reset environment**: `git reset --hard`, remove `.venv`, reinstall dependencies.  
2. **Follow the Guide as a student**: complete each unit, run assessments, note any confusing steps.  
3. **Inspect analytics**: confirm your session appears with reasonable time-on-task metrics.  
4. **Download Code Playback**: verify the recorded timeline includes your edits.  
5. **Sign-off**: complete the checklist below and hand off to instructors.

### Acceptance Test Commands

- `cd /home/codio/workspace/level1 && python3.11 -m venv .venv && source .venv/bin/activate`
- `python -m rasa train`
- `python -m rasa inspect --script scripts/level1_happy_path.json`
- Review `.guides/graders/` outputs for Units 0–8 (run each Code Test manually if needed).
- Open Code Playback for `domain/basics.yml` and ensure keystrokes are captured.

### Handoff Checklist
- [ ] Guides mirror Units 0–8 with working layout and media.  
- [ ] Assessments cover setup, responses, flows, patterns, training, and final verification.  
- [ ] Virtual Coach responses tuned for common failure modes.  
- [ ] Code Playback + Behavior Insights enabled and tested.  
- [ ] LMS integration confirmed (or documented if not applicable).  
- [ ] Instructor quick-start doc stored in `.guides/instructor-notes.md` (optional but recommended).

Level 1 is now production-ready in Codio. Proceed to Level 2 using its own integrated manual.
