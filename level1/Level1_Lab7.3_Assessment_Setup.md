# Lab 7.3: Best Practices Application - Assessment Setup

## Guide Content (For Students)

**Placement**: This lab follows Lab 7.2 in Unit 7: Putting It All Together.

---

### Your Task

Apply best practices to your bot:

1. **Review one flow** – Improve its description if it's vague (clear, specific, action verbs, context).
2. **Review one response** – Add a response variation if appropriate (multiple options, rephrase metadata).
3. **Test** – Run the flow with several phrasings and confirm the correct flow triggers.

---

### Verification

- At least one flow in `data/basics/` has a clear, non-empty description (e.g. more than a few words).
- At least one response in `domain/basics.yml` has more than one variation (or you documented why no change was needed).
- You tested and confirmed behavior in Inspector.

Run the assessment when you're done.

---

## Assessment Setup (For Implementers)

### Overview

This assessment verifies that the student applied best practices: improved at least one flow description and/or added at least one response variation. Because the lab is open-ended (which flow/response they choose), grading can be rubric-based or structural (e.g. "at least one flow has a description of length ≥ N characters"; "at least one response has ≥ 2 text items").

### Assessment Type

**LLM Rubric Autograde** (recommended) or **Standard Code Test** (Bash).

### Option A: LLM Rubric Autograde (Recommended)

1. **Navigate** to the Lab 7.3 section in the Codio Guide Editor.

2. **Add LLM Rubric Assessment** – Add assessment → **LLM Rubric** / **Autograde**.

3. **Configure**:
   - **Instructions**: Ask the student to (1) improve at least one flow description in `data/basics/` (clear, specific, action verbs), and (2) add at least one response variation in `domain/basics.yml` where appropriate; then test in Inspector.
   - **Rubric/Requirements**: Require (1) at least one flow file has a non-empty `description` field that is descriptive (e.g. > 20 characters, not generic); (2) at least one response in `domain/basics.yml` has multiple text entries (variations) or a single well-written response with a brief justification; (3) YAML remains valid. Award full points when requirements are met; partial credit for only one of the two (flow description vs response variation).
   - **Files to check**: `/home/codio/workspace/level1/domain/basics.yml`, `/home/codio/workspace/level1/data/basics/*.yml`
   - **Points**: e.g. 6–8
   - **Timeout**: 60 seconds

4. **Test**: Run with improved description + variation (pass); with no changes (fail with feedback).

### Option B: Standard Code Test (Bash)

**Grader script location**:
```
.guides/assessments/level1_graders/lab_7.3_grader.sh
```

**Checks** (run from `/home/codio/workspace/level1`):

1. **Flow description** – At least one file in `data/basics/*.yml` contains a `description:` field with a value longer than a threshold (e.g. 25 characters). Use `grep`/`awk` or a small script.
2. **Response variation** – In `domain/basics.yml`, at least one response key has a list of multiple text items (e.g. two or more `- "..."` under the same response). Parsing YAML in bash is limited; optional: use `python -c "import yaml; d=yaml.safe_load(open('domain/basics.yml')); r=d.get('responses',{}); print(any(len(v)>=2 for v in r.values() if isinstance(v,list)))"` to check for at least one response with ≥ 2 variations.

**Total suggested points**: 6. Output clear PASS/FAIL and hints.

**Codio config**: Add Code Test → Standard Code Test. COMMAND: `bash /home/codio/workspace/.guides/assessments/level1_graders/lab_7.3_grader.sh`. Working Directory: `/home/codio/workspace/level1`. Timeout: 30.

### Example student deliverable

- One flow (e.g. `help.yml`) has an updated `description` that is specific and uses action verbs.
- One response (e.g. `utter_help`) in `domain/basics.yml` has two or more text variations.
- Student ran Inspector and confirmed the flow still triggers correctly.
