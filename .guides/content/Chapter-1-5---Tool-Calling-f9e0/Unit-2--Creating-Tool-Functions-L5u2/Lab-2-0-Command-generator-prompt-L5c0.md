**Starting point:** Work in **`level5/`** with the **Chapter 1.4 completion** baseline described in **Unit 0.1**. At the **start** of Chapter 1.5, your **`level5/config.yml`** should **not** yet set **`prompt_template`**, and there should be **no** **`level5/data/prompts/`** folder. This lab is the **first** build step in Unit 2: you add the **command-generator prompt** before you define Python tools in **Lab 2.1**.

**Why this lab exists.** Rasa’s **`SearchReadyLLMCommandGenerator`** learns from the **examples in its prompt**. The stock template can bias the model toward **non-domain slot names** (for example `transfer_money_amount` instead of **`amount`**). That produces commands Rasa **skips** (`skip_command_slot_not_in_domain` in debug logs). This chapter ships a **custom Jinja2 prompt** that tells the model to use **exact domain slot names** (`amount`, `recipient`, `account_from`, `account`). You **add** that file and wire it in **`config.yml`** here so slot filling stays reliable for **Labs 2.1–5.2**.

You do **not** need the virtual environment for copying files; you need it when you run **`rasa train`** later.

---

## Part A — Add the prompt file

1. In **`level5/`**, create a folder named **`data/prompts/`** if it does not exist.

2. Copy the template into place **with the exact filename** **`command_prompt_v3_slot_names.jinja2`**:
   - **From the course repository:** copy **`.guides/content/Chapter-1-5---Tool-Calling-f9e0/resources/command_prompt_v3_slot_names.jinja2`** to **`level5/data/prompts/command_prompt_v3_slot_names.jinja2`** (same folder layout in your clone: project root → `.guides/...` → `resources/...`).
   - If your environment only shows the **`level5/`** tree, use the **full repository** view or ask your instructor for this file; it must match the **`resources`** copy byte-for-byte.

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

From **project root**, activate the venv, **`cd level5`**, and run **`python -m rasa train`**. Training should complete; if the prompt path is wrong, training or the next step will error.

---

**Success criteria.** **`level5/data/prompts/command_prompt_v3_slot_names.jinja2`** exists and **`config.yml`** references **`prompt_template: data/prompts/command_prompt_v3_slot_names.jinja2`**. Then continue to **Unit 2.1** (concept) and **Lab 2.1** ( **`tools/banking_tools.py`** ).

There is **no** separate Check It! for this page; **`config.yml`** and **`data/prompts/`** are verified indirectly when you run **Lab 5.1** and train the full agent.
