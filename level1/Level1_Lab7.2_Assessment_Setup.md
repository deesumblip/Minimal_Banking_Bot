# Lab 7.2: Build Your Own Feature (Project) - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Unit 7: Putting It All Together (after 7.2 Summary and 7.3 Best Practices).

---

### Your Task

Add a new feature to your banking bot (new response + new flow):

1. **Create a new response** in `domain/basics.yml` (e.g. bank hours, branch locations, FAQ). Follow the same pattern as existing responses; include `metadata: rephrase: True` where appropriate.
2. **Create a new flow** in `data/basics/` (e.g. `hours.yml`). Give it a clear name and description; reference your new response in the steps.
3. **Train**: Run `python -m rasa train` from `level1` (venv active).
4. **Test**: Start Inspector and test the new flow with several phrasings.

---

### Verification

- New response exists in `domain/basics.yml` and is used by a flow.
- New flow file exists in `data/basics/` with valid structure (name, description, steps).
- Training completes successfully; the new flow triggers correctly in Inspector.

Run the assessment when you're done.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student added a complete new feature: one new response in `domain/basics.yml` and one new flow in `data/basics/` that uses it, with valid YAML and structure. The new feature must be distinct from existing ones (greet, help, contact, goodbye).

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Bash/YAML checks).

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 7.2 section in the Codio Guide Editor.

2. **Add LLM Rubric Assessment** – Add assessment → **LLM Rubric** / **Autograde**.

3. **Configure** (see detailed **Grading** tab below).

4. **Code Playback** (optional): Enable for `domain/basics.yml` and `data/basics/*.yml` for instructor review.

5. **Test**: Run with a complete feature (pass), with only a new response (fail with feedback), with only a new flow (fail with feedback).

---

#### LLM Rubric Autograde – Grading tab (exact settings and copy-paste rubric)

**Grading flexibility:** Students may implement any valid new feature (e.g. bank hours, branch locations, FAQ, feedback). Accept any new response name (e.g. `utter_hours`, `utter_locations`, `utter_faq`) and any new flow file in `data/basics/` that meets the rubric criteria. Do not require a specific topic or filename—only correct structure and that the flow uses the student’s chosen new response.

Use these **exact options** and **copy-paste rubric text** when configuring the assessment.

| Option | Set to |
|--------|--------|
| **Total Points** | **20** |
| **Instructor Provided Solution File** | `level1/.guides/lab_7.2_solution_reference.md` (or `/home/codio/workspace/level1/.guides/lab_7.2_solution_reference.md` if Codio requires absolute path) |
| **Defined Number of Attempts** | **Off** (leave toggle off) |
| **Show Rationale to Student** | **After [1] attempts** (select that radio, leave the number as 1) |

---

**Add Rubric** – Click **ADD RUBRIC** and add the following four criteria. For each criterion, paste the text below into the rubric description field and set the points as indicated. Enable **partial credit** for the assessment.

**Rubric 1** — Points: **5**  
Copy and paste this into the criterion description:

```
The student added at least one new response (e.g. utter_*) in domain/basics.yml. The response has valid structure: under responses: a key like utter_hours with at least one "- text:" message, and optionally "metadata: rephrase: True". The new response must NOT be one of the original set (utter_greet, utter_help, utter_contact, utter_goodbye). Award full points if a valid new response exists; partial credit if structure is wrong or it's a duplicate of an original; zero if no new response.
```

**Rubric 2** — Points: **5**  
Copy and paste this into the criterion description:

```
A new .yml flow file exists in data/basics/ (e.g. hours.yml or similar). The file has valid YAML with a top-level "flows:" key, and at least one flow that has "name", "description", and "steps". Award full points if a new flow file exists with correct structure; partial if file exists but structure is wrong; zero if no new flow file.
```

**Rubric 3** — Points: **5**  
Copy and paste this into the criterion description:

```
The new flow's steps reference the new response. That is, at least one step uses "respond: <new_response_name>" or equivalent where <new_response_name> matches the new response added in domain/basics.yml (e.g. utter_hours). Award full points if the flow clearly uses the new response; zero if the flow does not reference it or references only original responses.
```

**Rubric 4** — Points: **5**  
Copy and paste this into the criterion description:

```
Best practices: The flow has a clear, descriptive "description" (not empty or trivial). The new response in domain uses "metadata: rephrase: True" where appropriate for user-facing text. Award full points if both are present; partial if one is missing; zero if neither.
```

---

**Files tab**  
Configure the assessment so the LLM can read these paths (exact paths to set, if Codio asks for file paths):

- `/home/codio/workspace/level1/domain/basics.yml`
- `/home/codio/workspace/level1/data/basics/` (or list each `.yml` in that folder, e.g. `help.yml`, `hours.yml`, etc., depending on Codio's UI)

### Option B: Standard Code Test (Bash)

**Grader script location**:
```
.guides/assessments/level1_graders/lab_7.2_grader.sh
```

**Checks** (run from `/home/codio/workspace/level1`):

1. **New flow file** – At least one `.yml` in `data/basics/` that is not one of the original set (e.g. count files; or require a minimum number of flow files). Alternatively, check for a known new file (e.g. `hours.yml`) if the lab specifies a single suggested name.
2. **Domain has extra response** – Parse `domain/basics.yml` (e.g. with `grep` or a small script) to ensure there are more response names than the baseline (utter_greet, utter_help, utter_contact, utter_goodbye).
3. **Valid YAML** – Optional: run a YAML lint or `python -c "import yaml; yaml.safe_load(open('domain/basics.yml'))"` (and same for new flow file).

**Total suggested points**: 8–10. Output clear PASS/FAIL and hints.

**Codio config**: Add Code Test → Standard Code Test. COMMAND: `bash /home/codio/workspace/.guides/assessments/level1_graders/lab_7.2_grader.sh`. Working Directory: `/home/codio/workspace/level1`. Timeout: 60.

### Example student deliverable

- New response in `domain/basics.yml` (e.g. `utter_hours`).
- New file `data/basics/hours.yml` with a flow that has name, description, and steps including `action: utter_hours`.
- Successful `rasa train` and working flow in Inspector.
