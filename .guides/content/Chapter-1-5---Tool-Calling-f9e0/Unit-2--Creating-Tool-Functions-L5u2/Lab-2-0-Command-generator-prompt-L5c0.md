**Starting point:** Work in **`level5/`** with the **Chapter 1.4 completion** baseline from **Unit 0.1**. Before this lab, **`level5/config.yml`** should **not** yet define **`prompt_template`**, and there should be **no** **`level5/data/prompts/`** folder. This is Unit 2’s **first** build step: add the **command-generator prompt** before **Lab 2.1** (Python tools).

**Why this lab exists.** **`SearchReadyLLMCommandGenerator`** follows **examples in its prompt**. The default template can steer the model toward **slot names that are not in your domain** (for example `transfer_money_amount` instead of **`amount`**). Rasa then **skips** those commands (`skip_command_slot_not_in_domain` in debug logs). This course provides a **custom Jinja2 prompt** that anchors **`set slot`** on real domain names (`amount`, `recipient`, `account_from`, `account`). You copy that file here and point **`config.yml`** at it so slot filling stays reliable through **Labs 2.1–5.2**.

You do **not** need the virtual environment to copy files; you need it when you run **`rasa train`**.

---

## Part A — Add the prompt file

1. In **`level5/`**, create a folder named **`data/prompts/`** if it does not exist.

2. Copy the template **using the exact filename** **`command_prompt_v3_slot_names.jinja2`**:
   - **From the course repo:** **`.guides/content/Chapter-1-5---Tool-Calling-f9e0/resources/command_prompt_v3_slot_names.jinja2`** → **`level5/data/prompts/command_prompt_v3_slot_names.jinja2`** (project root → `.guides/...` → `resources/...`).
   - If your IDE only shows **`level5/`**, open the full repo tree or ask your instructor; the file must match the **`resources`** copy.

3. Save. You should have **`level5/data/prompts/command_prompt_v3_slot_names.jinja2`**.

---

## Part B — Point `config.yml` at the template

1. Open **`level5/config.yml`**.

2. Under **`pipeline`** → **`SearchReadyLLMCommandGenerator`**, add a **`prompt_template`** entry **and** a short comment so future-you remembers why it is there. The block should look like this (keep your existing **`llm:`** and **`model_group:`** lines as they are):

```yaml
pipeline:
  - name: SearchReadyLLMCommandGenerator
    # Custom prompt: use domain slot names (amount, recipient, …) in SetSlot commands.
    prompt_template: data/prompts/command_prompt_v3_slot_names.jinja2
    llm:
      model_group: gpt-4o-mini
```

3. **Do not** change **`assistant_id`**, **`policy`**, or **`recipe`** unless you know what you are doing.

4. Save **`config.yml`**.

---

## Part C — Quick check (optional)

From **project root**, activate the venv, **`cd level5`**, and run **`python -m rasa train`**. Training should finish; a bad **`prompt_template`** path usually surfaces here or on the next train.

---

**Success criteria.** **`level5/data/prompts/command_prompt_v3_slot_names.jinja2`** exists and **`config.yml`** sets **`prompt_template: data/prompts/command_prompt_v3_slot_names.jinja2`**. Then continue to **Unit 2.1** (concept) and **Lab 2.1** (**`tools/banking_tools.py`**).

There is **no** separate Check It! on this page; **Labs 5.1 and 5.2** include a grader check (**Check 3**) for this file and **`prompt_template`** after you train.
