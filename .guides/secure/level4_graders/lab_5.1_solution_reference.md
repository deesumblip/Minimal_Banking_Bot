# Lab 4.4 – Reference solution for Training the Level 4 Bot

Use this file as the **Instructor Provided Solution File** for Lab 4.4 if you use an LLM Rubric; otherwise the Standard Code Test (Python grader) is the primary assessment.

---

## Required student deliverable

1. **Virtual environment** – The project has a `.venv` in the workspace root (from Lab 0.1 or equivalent), and the student activates it.

2. **Training** – From the project root, the student runs:
   ```bash
   cd level4
   python -m rasa train
   ```
   (with the venv activated).

3. **Outcome** – Training completes without critical errors, and a model file (`.tar.gz`) is created in `level4/models/`.

---

## Rubric summary (if using LLM Rubric)

- **Environment:** Venv exists in project root and was used (or equivalent).
- **Training:** Student ran `python -m rasa train` from the `level4` folder.
- **Model:** A `.tar.gz` model file exists in `level4/models/` and is recent (e.g. created within the session).
- **Logs:** No critical errors in training logs (optional check).

The Python grader (lab_4.4_grader.py) verifies venv, model file existence, model recency, and optional log checks and prints PASS on success.
