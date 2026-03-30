**Starting point:** Work in `level5/` from the Chapter 1.4 completion baseline (Unit 0.1). The course template already lives in the repo at `level5/resources/command_prompt_v3_slot_names.jinja2`.

**Before you change anything for this lab**, your tree should still match the usual “pre–Lab 2.0” state:

- `config.yml` does **not** set `prompt_template` yet.
- You do **not** have `data/prompts/command_prompt_v3_slot_names.jinja2` yet (and you may not have a `data/prompts/` folder at all).

This is Unit 2’s first build step: install the command-generator prompt, then continue to Lab 2.1 (Python tools).

---

**Why this lab exists**

`SearchReadyLLMCommandGenerator` follows examples in its prompt. The stock behavior can favor slot names that are **not** in your domain—for example `transfer_money_amount` instead of `amount`. Rasa then skips those commands; in debug logs you may see `skip_command_slot_not_in_domain`.

We ship a custom Jinja2 prompt under `level5/resources/` so `set slot` lines up with real domain slots (`amount`, `recipient`, `account_from`, `account`). You will copy that file into `data/prompts/` and point `config.yml` at it so slot filling stays reliable through Labs 2.1–5.2.

Copying files does **not** require the virtual environment. Activate the venv when you run `rasa train` (for example in Part C).

---

## Part A — Add the prompt file

1. **Create the folder** (if needed): under `level5/`, ensure `data/prompts/` exists.

2. **Copy the template** using the exact filename `command_prompt_v3_slot_names.jinja2`:
   - From: `level5/resources/command_prompt_v3_slot_names.jinja2`
   - To: `level5/data/prompts/command_prompt_v3_slot_names.jinja2`

3. **Run the copy from `level5/`**, for example:
   - Linux / macOS: `cp resources/command_prompt_v3_slot_names.jinja2 data/prompts/`
   - Windows (PowerShell): `Copy-Item resources\command_prompt_v3_slot_names.jinja2 data\prompts\`

4. **Confirm:** `level5/data/prompts/command_prompt_v3_slot_names.jinja2` exists. Rasa reads the prompt from `data/prompts/` at runtime; `level5/resources/` holds the copy that ships with the repo.

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
