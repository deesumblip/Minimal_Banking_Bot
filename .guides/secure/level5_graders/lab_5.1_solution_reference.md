# Lab 5.1 – Reference solution for Code Test

Use this file as reference for the Lab 5.1 code-output-compare grader (Training the Level 5 Agent).

---

## What the grader checks

1. **Virtual environment** – `.venv` exists at project root; venv Python exists (bin/python or Scripts/python.exe).
2. **level5 structure** – `level5/` contains `domain/basics.yml`, `config.yml`, `endpoints.yml`, and `tools/banking_tools.py`.
3. **Lab 2.0 (command-generator prompt)** – `level5/data/prompts/command_prompt_v3_slot_names.jinja2` exists and `config.yml` sets `prompt_template` on `SearchReadyLLMCommandGenerator` to a path containing `data/prompts/command_prompt_v3_slot_names.jinja2`.
4. **Trained model** – `level5/models/` contains at least one `.tar.gz` model file.

---

## Student steps

- Complete **Lab 2.0** (copy the Jinja2 prompt and wire `prompt_template` in `config.yml`) and **Labs 2.1–4.1** before training.
- Activate the project-root venv.
- `cd level5`
- Run `python -m rasa train`.
- Ensure `level5/models/` contains the trained model.

---

## Rubric summary

- Venv at project root is present and usable.
- level5 has the expected config, domain, endpoints, tools, and Lab 2.0 prompt files.
- Training completes and produces a model in `level5/models/`.
