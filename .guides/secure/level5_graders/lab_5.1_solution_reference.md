# Lab 5.1 – Reference solution for Code Test

Use this file as reference for the Lab 5.1 code-output-compare grader (Training the Level 5 Bot).

---

## What the grader checks

1. **Virtual environment** – `.venv` exists at project root; venv Python exists (bin/python or Scripts/python.exe).
2. **level5 structure** – level5/ contains required files: domain/basics.yml, config.yml, endpoints.yml, data/basics/, actions/, tools/, etc.
3. **Trained model** – level5/models/ contains at least one model file (e.g. .tar.gz), or the grader runs `rasa train` from level5 and then verifies models/ is populated.

---

## Student steps

- Activate the project-root venv.
- `cd level5`
- Run `rasa train`.
- Ensure level5/models/ contains the trained model.

---

## Rubric summary

- Venv at project root is present and usable.
- level5 has the expected config, domain, data, actions, tools.
- Training completes and produces a model in level5/models/.
