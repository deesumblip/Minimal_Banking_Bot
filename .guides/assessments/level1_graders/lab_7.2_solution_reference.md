# Lab 7.2 – Reference solution for LLM Rubric Autograde

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde so the LLM has a model answer to compare against student submissions.

**Grading flexibility:** The example below uses "hours" only as one valid solution. Accept any student submission that adds a different but valid feature (e.g. branch locations, FAQ, feedback)—any new `utter_*` response and any new flow file in `data/basics/` that meets the rubric structure and links the flow to that response.

---

## 1. New response in domain/basics.yml

One new response, following the same pattern as existing responses (e.g. utter_greet, utter_help). Example (students may use a different topic, e.g. utter_locations, utter_faq):

```yaml
responses:
  # ... existing responses (utter_greet, utter_help, utter_contact) ...
  utter_hours:
    - text: "We're open Monday–Friday 9am–5pm and Saturday 10am–2pm."
      metadata:
        rephrase: True
```

- Valid structure: response name (e.g. `utter_hours`), `- text:` with at least one message, optional `metadata: rephrase: True`.
- Must be distinct from the original set (greet, help, contact, goodbye).

---

## 2. New flow in data/basics/

One new flow file (e.g. `hours.yml`, `locations.yml`, `faq.yml`—filename may vary) that uses the new response. Example:

```yaml
flows:
  hours:
    name: bank hours
    description: "User asks for branch or bank opening hours, or when we are open."
    steps:
      - respond: utter_hours
```

- Valid structure: `flows:`, one flow with `name`, `description`, and `steps`.
- At least one step must reference the new response (e.g. `respond: utter_hours`).
- Description should be clear and descriptive so the LLM can match user questions to this flow.

---

## Rubric summary for autograde

- **New response in domain:** Present, valid YAML, not one of greet/help/contact/goodbye.
- **New flow file:** Present in `data/basics/`, valid YAML, has name, description, steps.
- **Flow uses new response:** At least one step references the new response name.
- **Best practices:** Descriptive flow description; rephrase metadata where appropriate.
