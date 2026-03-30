# Lab 5.2 – Reference solution for Code Test (Completion Check)

Use this file as reference for the Lab 5.2 code-output-compare grader (Testing Tool Calling / Completion Check).

---

## What the grader checks

1. **tools/ and banking_tools.py** – `level5/tools/` exists; `banking_tools.py` has `__all__` and tool functions (`check_balance`, `process_transfer`).
2. **endpoints.yml** – `tools` section with `tools_module: "tools"`.
3. **Lab 2.0 (command-generator prompt)** – `level5/data/prompts/command_prompt_v3_slot_names.jinja2` exists and `config.yml` sets `prompt_template` on `SearchReadyLLMCommandGenerator` accordingly.
4. **transfer_money_tools.yml** – Flow file exists with collect steps and `action_process_transfer_with_tools`.
5. **action_process_transfer_with_tools** – Action file exists with `name()` / `def name`.
6. **domain/basics.yml** – Lists `action_process_transfer_with_tools`.
7. **Model** – `level5/models/` contains a trained `.tar.gz` model (partial credit if domain OK but no model).

---

## Student steps

- Complete **Labs 2.0–5.1** (prompt, tools, endpoints, flow, action, domain, train).
- Run the Lab 5.2 assessment (completion check) from workspace root. The grader verifies all Level 5 artifacts including the Lab 2.0 prompt wiring and the trained model.

---

## Rubric summary

- All deliverables are in place: Lab 2.0 prompt, tools module, endpoints tools, flow, action, domain, trained model.
- Grader prints PASS when all checks succeed.
