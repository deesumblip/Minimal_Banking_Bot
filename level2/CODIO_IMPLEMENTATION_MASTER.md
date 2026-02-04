# Level 2 – Codio Delivery Manual (Simple Actions)

Integrates the complete Level 2 student curriculum with platform execution steps so a Codio newcomer can deliver the “Simple Actions” experience without bouncing between documents. Keep the original references (`CODIO_IMPLEMENTATION_GUIDE.md`, `CODIO_IMPLEMENTATION_PLAYBOOK.md`) for deep dives, but this is your single build script.

---

## 0. Orientation

### Prerequisites Checklist

- Completed Level 1 Codio rollout (or access to a working Level 1 Codio project for reference).
- Codio account with permissions to create projects, edit Guides, and configure assessments/Virtual Coach.
- Valid Rasa Pro licence key and OpenAI API key for `.env` templates.
- Ability to edit Python and YAML (Git optional but useful for resets).
- Two full workdays available (Week 1 Days 3–4 in the master timeline).

### Overview

- **Objective**: Extend the Level 1 banking bot with its first custom Python action (`action_bank_hours`). Students learn why/when to use actions, how to register them, and how flows call custom logic.
- **Audience**: Codio implementers, instructors, and content reviewers.
- **Sprint allocation**: **Week 1 – Days 3 & 4**.
- **Source workspace**: Copy `level2/` folder (includes prebuilt action scaffold).

---

## 1. Course Content Snapshot

| Module | Focus | Student Outcomes |
| --- | --- | --- |
| Module 0 | Recap of Level 1 | Verify prior responses/flows remain intact |
| Module 1 | Intro to actions | Understand what `action_*` can do |
| Module 2 | Action class anatomy | Read & annotate `Action` subclass |
| Module 3 | First action (`action_bank_hours`) | Write Python logic returning bank hours |
| Module 4 | Domain registration | Add actions to `domain/basics.yml` |
| Module 5 | Using actions in flows | Update `data/basics/hours.yml` |
| Module 6 | Training/testing with actions | Run action server + inspector |
| Module 7 | Putting it together | Greet/help/contact/hours scenario |
| Module 8 | Assessment & preview | Review + Level 3 teaser |

Student narrative lives in `CODIO_IMPLEMENTATION_GUIDE.md`; copy text/graphics into Guides as needed.

---

## 2. Codio Workspace Setup

1. **Project copy**: Create new Codio project (e.g., `BankingBot-Level2`), import the repo or zip containing `level2/`.
2. **Stack**: Confirm Python 3.11 + `rasa-pro` installed (same commands as Level 1). Reuse `.env.template` pattern.
3. **Folder focus**: Ensure only the `level2/` folder is exposed to students. Remove other levels from the Codio workspace.
   - **Codio OS reminder**: Codio boxes run Ubuntu Linux. Windows-only commands shown in the curriculum (e.g., PowerShell activation) are for learner context and should not be executed inside Codio.
4. **Virtual environment sanity check**:
   ```bash
   cd level2
   python3.11 -m venv .venv && source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m rasa --version
   ```
5. **Action server script (optional)**: Create `scripts/run_action_server.sh`:
   ```bash
   #!/bin/bash
   cd /home/codio/workspace/level2
   source .venv/bin/activate
   rasa run actions
   ```
   Give execute permission: `chmod +x scripts/run_action_server.sh`.

---

## 3. Guides Authoring Blueprint

1. **Duplicate Level 1 Guides**: Copy `.guides/` from Level 1 project to Level 2 to preserve layout, then update titles.
2. **Update metadata**:
   ```markdown
   title: Level 2 – Simple Actions
   description: Extend the banking bot with custom Python actions.
   ```
3. **Section mapping** (simplified template):
   ```markdown
   ## Welcome Back
   <Recap why actions matter — see `CODIO_IMPLEMENTATION_GUIDE.md` → “Course Introduction”>

   ## Module 0 – Level 1 Recap
   <Checklist verifying responses still work — “Module 0: Recap - What You Built in Level 1”>

   ## Module 1 – Introduction to Actions
   @open{"path":"/home/codio/workspace/level2/actions/action_bank_hours.py"}
   <Explain `Action` class basics from “Module 1: Introduction to Actions”>

   ## Module 2 – Action Anatomy
   <Line-by-line walkthrough of `ActionBankHours` (“Module 2”)>

   ## Module 3 – Writing `action_bank_hours`
   <Coding exercise + Run button (“Module 3: Creating Your First Action”)>

   ## Module 4 – Registering the Action
   @open{"path":"/home/codio/workspace/level2/domain/basics.yml"}
   <Add actions block (“Module 4: Registering Actions in the Domain”)>

   ## Module 5 – Using the Action in a Flow
   @open{"path":"/home/codio/workspace/level2/data/basics/hours.yml"}
   <Explain replacing `utter_hours` (“Module 5: Using Actions in Flows”)>

   ## Module 6 – Training & Testing with Actions
   @term{"command":"python -m rasa train"}
   @term{"command":"python -m rasa run actions"}
   <Guide students through running inspector (“Module 6”)>

   ## Module 7 – Putting It Together
   <Scripted conversation instructions (“Module 7”)>

   ## Module 8 – Assessment & Next Steps
   <Quiz + project reflection (“Module 8”)>

   ## Troubleshooting & Glossary
   <Level 2-specific issues — copy from “Troubleshooting Guide” and “Glossary”>
   ```
4. **Embed comparisons**: Use Codio tabs for “Response vs. Action” examples. Example:
   ```markdown
   @tabs
   @tab("Response")
   ```yaml
   utter_hours:
     - text: "We are open 9am-5pm."
   ```
   @tab("Action")
   ```python
   class ActionBankHours(Action):
       ...
   ```
   @end
   ```

---

## 4. Assessments & Auto-Grading

| Module | Assessment | Implementation Notes |
| --- | --- | --- |
| Module 0 | Concept quiz | Confirm students remember Level 1 artifacts. |
| Module 3 | Code test | Run Python unit test to ensure `ActionBankHours` returns expected message. |
| Module 4 | YAML validator | Parse `domain/basics.yml` to verify `actions:` block contains `action_bank_hours`. |
| Module 5 | Flow validator | Ensure `data/basics/hours.yml` calls the action rather than `utter_hours`. |
| Module 6 | Dual script | 1) Start action server in background, 2) run `rasa inspect` with canned query, 3) confirm AI response includes dynamic hours. |
| Module 8 | Rubric | Criteria: action file authored, registered, flow updated, tests pass. |

**Sample unit test snippet** (`.guides/graders/test_action_bank_hours.py`):
```python
import importlib
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet

module = importlib.import_module("actions.action_bank_hours")
action = module.ActionBankHours()
dispatcher = CollectingDispatcher()
tracker = Tracker("sender", {}, {}, [], False, None, {}, "action_listen")

action.run(dispatcher, tracker, {})
messages = [m["text"] for m in dispatcher.messages]
assert any("bank hours" in m.lower() for m in messages), "Action did not mention bank hours."
```
Invoke via Code Test command:
```bash
cd /home/codio/workspace/level2
python -m pytest .guides/graders/test_action_bank_hours.py
```

---

## 5. Virtual Coach Guidance

Focus the Coach on action-centric troubleshooting:

- **Summarize Prompt**: remind learners to edit both the Python file and `domain/basics.yml`, then run `rasa data validate`.
- **Error Augmentation** examples:
  - *Error*: `ActionException: No registered action found`. *Coach response*: “Add `action_bank_hours` under the `actions:` list in `domain/basics.yml` and rerun `rasa data validate`.”
  - *Error*: `ModuleNotFoundError: No module named 'actions'`. *Response*: “Ensure `actions/__init__.py` exists and you’re running commands from `/home/codio/workspace/level2`.”
- **Next Steps**: suggest running the provided test script or restarting the action server.

---

## 6. Code Playback & Analytics

Track `actions/`, `domain/basics.yml`, `data/basics/hours.yml`, and `endpoints.yml`. Review sample playback to confirm students typed logic incrementally. Update Behavior Insight thresholds slightly higher than Level 1 (expect more time spent debugging).

Analytics focus points:
- Time to first passing grader for Module 3.
- Number of attempts on the action server script.
- Frequency of Coach interactions mentioning “register action” (helps refine hints).

---

## 7. Optional: LMS & Support Artifacts

- Map Level 2 assessments to LMS grade items worth roughly **20%** of the total course (adjust to syllabus). 
- Update instructor notes with troubleshooting tips (e.g., checking action server logs at `.rasa/logs/actions.log`).

---

## 8. Two-Day Timeline Slice

| Day | Morning | Afternoon |
| --- | --- | --- |
| Week 1 – Day 3 | Guides migration for Modules 0–4, embed comparisons, set auto-open panes | Build Module 3 & 4 graders, run local tests, draft Coach summaries |
| Week 1 – Day 4 | Finish Guides Modules 5–8, add troubleshooting | Wire remaining graders, enable Coach/Playback/analytics, test LMS sync, run QA walkthrough |

Daily sign-off checklist:
- [ ] Action code compiles; tests pass.
- [ ] Guide preview walks through building the action step-by-step.
- [ ] Graders clearly explain missing registration or code errors.
- [ ] Coach and analytics capture action-related issues.

---

## 9. Final QA Pass

1. Reset repo and virtualenv to simulate a fresh student session.
2. Follow the Guide from Module 0 to 8, completing assessments.
3. Start `rasa run actions` and confirm inspector conversation matches expected transcript.
4. Review Code Playback to ensure the action file creation is visible.
5. Capture any issues in instructor notes before handing off.

### Acceptance Test Commands

- `cd /home/codio/workspace/level2 && python3.11 -m venv .venv && source .venv/bin/activate`
- `python -m rasa train`
- `python -m rasa run actions` (separate terminal)
- `python -m rasa inspect --script scripts/level2_action_story.json --debug`
- `python -m pytest .guides/graders/test_action_bank_hours.py`
- Review Code Playback for `actions/action_bank_hours.py` edits

Level 2 is now Codio-ready. Move on to Level 3 using its integrated manual.
