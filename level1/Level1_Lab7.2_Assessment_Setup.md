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

3. **Configure**:
   - **Instructions**: Ask the student to create a new response in `domain/basics.yml`, a new flow in `data/basics/` that uses it, and to follow best practices (descriptive flow description, rephrase metadata). The feature must differ from greet, help, contact, goodbye.
   - **Rubric/Requirements**: Require (1) new response in `domain/basics.yml` with valid structure and naming; (2) new flow file in `data/basics/` with valid YAML, `flows:`, name, description, steps; (3) flow steps reference the new response; (4) best practices (descriptive description, rephrase where appropriate). Award full points when all are met; allow partial credit for incomplete work.
   - **Files to check**: `/home/codio/workspace/level1/domain/basics.yml`, `/home/codio/workspace/level1/data/basics/*.yml`
   - **Points**: e.g. 14
   - **Timeout**: 90 seconds

4. **Code Playback** (optional): Enable for `domain/basics.yml` and `data/basics/*.yml` for instructor review.

5. **Test**: Run with a complete feature (pass), with only a new response (fail with feedback), with only a new flow (fail with feedback).

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
