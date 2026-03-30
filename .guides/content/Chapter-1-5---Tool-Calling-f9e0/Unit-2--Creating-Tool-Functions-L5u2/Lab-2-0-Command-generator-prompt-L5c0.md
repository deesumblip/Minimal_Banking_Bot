**Starting point:** Work in `level5/` from the Chapter 1.4 completion baseline (Unit 0.1). The template `level5/resources/command_prompt_v3_slot_names.jinja2` is already in the repo. For this lab, `config.yml` should not yet set `prompt_template`, and you should not yet have `data/prompts/command_prompt_v3_slot_names.jinja2` (or a `data/prompts/` folder). This is Unit 2’s first build step—install the command-generator prompt before Lab 2.1 (Python tools).

**Why this lab exists.** `SearchReadyLLMCommandGenerator` follows examples in its prompt. The default can push slot names that are not in your domain (for example `transfer_money_amount` instead of `amount`). Rasa then skips those commands—see `skip_command_slot_not_in_domain` in debug logs. The course ships a custom Jinja2 prompt under `level5/resources/` that keeps `set slot` aligned with real domain slots (`amount`, `recipient`, `account_from`, `account`). Copy it into `data/prompts/` and wire `config.yml` so slot filling stays reliable through Labs 2.1–5.2.

You do not need the virtual environment to copy files; use it when you run `rasa train`.

---

## Part A — Add the prompt file

1. Under `level5/`, create `data/prompts/` if it does not exist.

2. Copy the file using the exact name `command_prompt_v3_slot_names.jinja2`:
   - **Source:** `level5/resources/command_prompt_v3_slot_names.jinja2`
   - **Destination:** `level5/data/prompts/command_prompt_v3_slot_names.jinja2`
   - From `level5/`, for example: `cp resources/command_prompt_v3_slot_names.jinja2 data/prompts/` (Linux/macOS) or `Copy-Item resources\command_prompt_v3_slot_names.jinja2 data\prompts\` (Windows PowerShell).

3. Confirm: `level5/data/prompts/command_prompt_v3_slot_names.jinja2` exists. Rasa reads the copy under `data/prompts/` at runtime; `resources/` stays the repo template you copied from.

---

## Part B — Point `config.yml` at the template

1. Open `level5/config.yml`.

2. Under `pipeline` → `SearchReadyLLMCommandGenerator`, add `prompt_template` plus a short comment so you remember why it is there. The block should resemble the following (keep your existing `llm:` and `model_group:` lines as they are):

```yaml
pipeline:
  - name: SearchReadyLLMCommandGenerator
    # Custom prompt: use domain slot names (amount, recipient, …) in SetSlot commands.
    prompt_template: data/prompts/command_prompt_v3_slot_names.jinja2
    llm:
      model_group: gpt-4o-mini
```

3. Do not change `assistant_id`, `policy`, or `recipe` unless you intend to.

4. Save `config.yml`.

---

## Part C — Quick check (optional)

From project root, activate the venv, `cd level5`, and run `python -m rasa train`. Training should finish; a bad `prompt_template` path usually shows up here or on the next train.

---

**Success criteria.** `level5/data/prompts/command_prompt_v3_slot_names.jinja2` exists and `config.yml` sets `prompt_template: data/prompts/command_prompt_v3_slot_names.jinja2`. Then continue to Unit 2.1 and Lab 2.1 (`tools/banking_tools.py`).

---

## Check It!

{Check It!|assessment}(code-output-compare-501020000)

Labs 5.1 and 5.2 still run a Lab 2.0 check (prompt file and `prompt_template`) inside their larger graders. Passing this Lab 2.0 assessment confirms the same wiring before you move on to Lab 2.1.
