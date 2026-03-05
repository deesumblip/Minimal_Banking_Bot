# Lab 5.2 – Reference solution for Code Test (Completion Check)

Use this file as reference for the Lab 5.2 code-output-compare grader (Testing Tool Calling / Completion Check).

---

## What the grader checks

1. **tools/ and banking_tools.py** – level5/tools/ exists; banking_tools.py has __all__ and tool functions (check_balance, process_transfer).
2. **endpoints.yml** – tools section with tools_module: "tools".
3. **transfer_money_tools.yml** – Flow file exists with collect and action step.
4. **action_process_transfer_with_tools** – Action file exists; domain lists the action.
5. **domain/basics.yml** – Valid; includes required slots and actions.
6. **Model** – level5/models/ contains a trained model.

---

## Student steps

- Complete Labs 2.1, 3.1, 4.1, and 5.1.
- Run the Lab 5.2 assessment (completion check) from workspace root. The grader verifies all Level 5 artifacts and the trained model.

---

## Rubric summary

- All Lab 2.1–5.1 deliverables are in place: tools module, endpoints tools, flow, action, domain, trained model.
- Grader prints PASS when all checks succeed.
