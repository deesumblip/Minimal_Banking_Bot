**Starting point:** Work in **`level5/`** from the Level 4 completion baseline (**Unit 0.1**).

Rasa’s **`SearchReadyLLMCommandGenerator`** turns model output into commands, including **`set slot`**. It follows **examples in its prompt**.

If those examples don’t match your **domain slot names**—for example the model emits `transfer_money_amount` instead of **`amount`**—Rasa **ignores** the command. Debug logs may show **`skip_command_slot_not_in_domain`**, and slot collection stops working as expected.

**This lab** aligns prompt examples with your slots. The repo ships **`level5/resources/command_prompt_v3_slot_names.jinja2`**, which teaches the model to use real slot names (`amount`, `recipient`, `account_from`, `account`). You copy it under **`data/prompts/`** and set **`prompt_template`** on **`SearchReadyLLMCommandGenerator`** in **`config.yml`** so **`set slot`** stays reliable through Labs **2.1–5.2**.

Do this lab **before Lab 2.1** (the **`tools/`** module). Copying files does not need the venv; activate it when you run **`rasa train`** (Part C).

---

## Part A — Add the prompt file

1. **Create the folder** (if needed): under `level5/`, ensure `data/prompts/` exists.

2. **Copy the template** using the exact filename `command_prompt_v3_slot_names.jinja2`:
   - From: `level5/resources/command_prompt_v3_slot_names.jinja2`
   - To: `level5/data/prompts/command_prompt_v3_slot_names.jinja2`

3. **Confirm:** `level5/data/prompts/command_prompt_v3_slot_names.jinja2` exists. Rasa reads the prompt from `data/prompts/` at runtime; `level5/resources/` holds the copy that ships with the repo.

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
      model_group: openai-gpt-5-1
```

3. Do not change `assistant_id`, the **`policies:`** list (keep **`FlowPolicy`**), `recipe`, or the rest of the **`pipeline`** step unless you intend to.

4. Save `config.yml`.

---

## Part C

- Open a terminal at **project root** (the folder that contains `level5/` and `.venv/`).
- Activate the virtual environment:
  - Codio / Linux / macOS: `source .venv/bin/activate`
  - Windows (PowerShell): `.\.venv\Scripts\Activate.ps1`
- Change into the agent folder: `cd level5`
- Run: `python -m rasa train`

Training should finish; a bad `prompt_template` path usually shows up here or on the next train.

---

**Success criteria.** `level5/data/prompts/command_prompt_v3_slot_names.jinja2` exists and `config.yml` sets `prompt_template: data/prompts/command_prompt_v3_slot_names.jinja2`. Then continue to Unit 2.1 and Lab 2.1 (`tools/banking_tools.py`).

---

## Check It!

{Check It!|assessment}(code-output-compare-501020000)

Labs 5.1 and 5.2 still run a Lab 2.0 check (prompt file and `prompt_template`) inside their larger graders. Passing this Lab 2.0 assessment confirms the same wiring before you move on to Lab 2.1.
